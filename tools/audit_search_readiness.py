#!/usr/bin/env python3
"""Read-only, bounded homepage/robots/sitemap baseline. No ranking predictions."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser
import xml.etree.ElementTree as ET

SITES = [
    ('Jaipur Engineers', 'https://jaipurengineers.com'),
    ('Mango Engineers', 'https://mangoengineers.com'),
    ('Forsk Coding School', 'https://forskcodingschool.com'),
    ('Groot Academy', 'https://grootacademy.com'),
    ('Clever Ape Academy', 'https://cleverapeacademy.com'),
    ('CadMate India', 'https://cadmateindia.com'),
    ('Groot Software', 'https://grootsoftware.com'),
    ('Forsk Technologies', 'https://forsktechnologies.com'),
]
LIMIT = 2_000_000


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.titles, self.h1s, self.canonicals = [], [], []
        self.descriptions, self.robots, self.schemas = [], [], []
        self.capture, self.buffer = None, []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'meta':
            name = a.get('name', '').lower()
            if name == 'description':
                self.descriptions.append(a.get('content', ''))
            if name in ('robots', 'googlebot', 'bingbot', 'oai-searchbot'):
                self.robots.append({'agent': name, 'value': a.get('content', '')})
        if tag == 'link' and 'canonical' in a.get('rel', '').lower().split():
            self.canonicals.append(a.get('href', ''))
        if tag in ('title', 'h1') or (tag == 'script' and a.get('type', '').lower() == 'application/ld+json'):
            self.capture, self.buffer = tag, []

    def handle_data(self, data):
        if self.capture:
            self.buffer.append(data)

    def handle_endtag(self, tag):
        if tag != self.capture:
            return
        value = ''.join(self.buffer).strip()
        if tag == 'title':
            self.titles.append(value)
        elif tag == 'h1':
            self.h1s.append(value)
        else:
            try:
                self.schemas.append({'valid_json': True, 'data': json.loads(value)})
            except ValueError as exc:
                self.schemas.append({'valid_json': False, 'error': str(exc)})
        self.capture, self.buffer = None, []


def fetch(url):
    try:
        with urlopen(Request(url, headers={'User-Agent': 'BrandSearchReadinessAudit/1.0'}), timeout=15) as r:
            raw = r.read(LIMIT + 1)
            return {'url': url, 'final_url': r.url, 'status': r.status,
                    'content_type': r.headers.get('Content-Type', ''),
                    'x_robots_tag': r.headers.get_all('X-Robots-Tag', []),
                    'truncated': len(raw) > LIMIT,
                    'body': raw[:LIMIT].decode('utf-8', errors='replace')}
    except HTTPError as exc:
        return {'url': url, 'status': exc.code, 'error': str(exc), 'body': ''}
    except Exception as exc:
        return {'url': url, 'status': None, 'error': str(exc), 'body': ''}


def schema_types(value):
    found = set()
    if isinstance(value, dict):
        types = value.get('@type', [])
        found.update([types] if isinstance(types, str) else [t for t in types if isinstance(t, str)])
        for item in value.values():
            found.update(schema_types(item))
    elif isinstance(value, list):
        for item in value:
            found.update(schema_types(item))
    return found


def audit(site):
    name, base = site
    home, robots, sitemap = [fetch(base + p) for p in ('/', '/robots.txt', '/sitemap.xml')]
    page = Page()
    page.feed(home['body'])
    findings = []
    if home['status'] != 200:
        findings.append('P0: homepage did not return HTTP 200 to this audit client')
    for label, values in [('title', page.titles), ('canonical', page.canonicals), ('H1', page.h1s)]:
        if len(values) != 1 or not values[0].strip():
            findings.append('REVIEW: expected one non-empty ' + label)
    if not page.descriptions:
        findings.append('REVIEW: no meta description observed')
    if any('noindex' in r['value'].lower() or 'none' in r['value'].lower().split(',') for r in page.robots) or any('noindex' in v.lower() for v in home.get('x_robots_tag', [])):
        findings.append('P1: noindex directive observed; review intended homepage eligibility')
    if any(urlparse(url).netloc.lower().removeprefix('www.') != urlparse(base).netloc.lower().removeprefix('www.') for url in page.canonicals):
        findings.append('REVIEW: canonical is relative or points to a different host')
    if any(x in ' '.join(page.titles).lower() for x in ('techco', 'edublink', 'lorem ipsum')):
        findings.append('P0: template branding in title; verify business content before optimization')
    if any(not s['valid_json'] for s in page.schemas):
        findings.append('P1: invalid JSON-LD syntax observed')
    if not page.schemas:
        findings.append('REVIEW: no JSON-LD observed; assess appropriate schema against visible content')
    robots['homepage_crawl_by_agent'] = {}
    if robots['status'] == 200 and not robots.get('truncated') and 'html' not in robots.get('content_type', '').lower():
        parser = RobotFileParser()
        parser.parse(robots['body'].splitlines())
        robots['homepage_crawl_by_agent'] = {agent: parser.can_fetch(agent, base + '/')
            for agent in ('Googlebot', 'Bingbot', 'OAI-SearchBot', 'GPTBot', 'PerplexityBot')}
    else:
        findings.append('REVIEW: robots policy not parsed (missing/error/HTML/truncated); not proof of blocking')
    try:
        root = ET.fromstring(sitemap['body'])
        sitemap['xml_root'] = root.tag.rsplit('}', 1)[-1]
        sitemap['valid_sitemap_root'] = sitemap['xml_root'] in ('sitemapindex', 'urlset')
    except ET.ParseError:
        sitemap['valid_sitemap_root'] = False
    if sitemap['status'] != 200 or not sitemap['valid_sitemap_root']:
        findings.append('P1: /sitemap.xml not confirmed as successful sitemap XML; inspect alternative discovery')
    types = sorted(set().union(*(schema_types(s.get('data')) for s in page.schemas)))
    for response in (home, robots, sitemap):
        response.pop('body', None)
    return {'brand': name, 'base_url': base, 'home': home, 'titles': page.titles,
            'h1s': page.h1s, 'canonicals': page.canonicals, 'descriptions': page.descriptions,
            'meta_robots': page.robots, 'jsonld_blocks': len(page.schemas),
            'jsonld_invalid_blocks': sum(not s['valid_json'] for s in page.schemas),
            'schema_types': types, 'robots': robots, 'sitemap': sitemap, 'findings': findings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    with ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(audit, SITES))
    result = {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
              'scope': '8 homepages, root robots and root sitemap only; not a full crawl',
              'limitations': ['No Google indexing, AI citation, CWV or deployment verification.',
                             'Robots allowance is path-specific and does not prove WAF access.',
                             'JSON-LD syntax/type inventory does not validate schema truth or eligibility.',
                             'Training bots and search bots are reported separately; no policy changes.'],
              'sites': rows}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    for row in rows:
        print(row['brand'], row['home']['status'], '; '.join(row['findings']) or 'No baseline flags')


if __name__ == '__main__':
    main()
