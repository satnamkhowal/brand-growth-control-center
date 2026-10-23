# All-brand search and answer visibility program

Started: 2026-10-19. Owner: current central coordinator. Branch: `coord/all-brands-aeo-geo-20261019`.
User scope: start AEO, GEO and related discovery work across all websites. This is a bounded first implementation cycle, not an unattended worker service.

## Scope and actual state

Eight brands are registered in brands.json from the existing central README. This branch implements the audit utility, current baseline and actionable queue. Production code changes remain in each brand source repository. No main merge, deployment, search-console submission, bot-policy change or AI citation improvement is claimed.

AEO: clear answers to real visitor questions on existing relevant pages. GEO: useful, attributable source material that AI search systems can retrieve. SEO foundations, local/entity consistency, user experience and conversion measurement form the same work program.

## Acceptance criteria

1. Verify source repository and deployment mapping before source changes. Read repository AGENTS and coordination files; claim a small unowned task. Keep assigned branches isolated and preserve indexed URLs.
2. Recheck 200 responses, redirects, canonical, noindex/snippet controls, robots and actual WAF access on home, a commercial page, a learning article and contact page per brand. A root robots 404 does not itself mean blocked crawling. The baseline checks only three endpoints per site.
3. Reconcile sitemap URLs with the approved canonical set. XML syntax alone does not establish indexation. Submit through an authorized verified Search Console/Bing property only when available.
4. Improve existing high-intent pages first: concise direct answer, prerequisites, syllabus, verified duration/mode, project deliverables, examples and relevant internal links. Add visible FAQs where helpful; do not duplicate one article across brands. Topic angles in brands.json are proposals, not exclusive restrictions on each brand.
5. Add or repair Organization/EducationalOrganization, Course, Service, Article/TechArticle and BreadcrumbList only where applicable to visible content. Use stable entity IDs. Exclude invented ratings, placements, trainers, prices, addresses and accreditation. Schema syntax checks do not certify eligibility. FAQ rich-result display is not promised.
6. Verify NAP, official profiles, author/mentor identity and sources. Technical tutorials should include runnable examples and genuine learning value. Do not turn demo people, services or statistics into business claims.
7. Improve mobile readability, image alt text, asset weight, accessibility and lead paths. Measure CWV separately using field/lab evidence; this audit does not measure CWV.
8. Track dated evidence: changed URLs/files, commit, tests, merge, deployment and live verification independently. Measure Search Console impressions/clicks and available AI referral conversions. AI answer checks must record question, engine, date, locale and cited source; a missing citation is not proof of ineligibility.

## Initial priorities from repository evidence

- Forsk Technologies: root homepage title is still `Business Consulting – Techco` in repository and public retrieval. Establish verified business copy and identity before distributing template claims through schema or sitemaps. Root robots.txt was not found in the inspected repository; production must be checked independently.
- Mango Engineers: current repository robots permits public crawling. Historical runtime/deployment and NAP conflicts remain recorded in its task board, but are not asserted as current live failures. Preserve existing migration ownership and global schema integration gates.
- Forsk Coding School: reuse the existing September AI discovery work and IndexNow utility; verify production and gaps before regenerating files. Search discovery and model-training policies are separate; do not change training preferences as a side effect.
- Jaipur Engineers: root robots.txt fetch returned repository 404. A directory listing was capped at 1000 entries, so it is not a complete file inventory. Check the current deployed stack before proposing a replacement.
- Groot Academy: `gta` robots declares grootacademy.com; validate that deployment relationship before edits. Existing other Groot repositories must not be mixed in.
- CadMate India: `CadMateIndia` has PHP brand foundation and robots. `cadmateindia.com` also exists; resolve source mapping rather than editing both.
- Groot Software: existing robots and sitemap foundation; prioritize visible service answers and trustworthy project evidence after source/deploy mapping.
- Clever Ape Academy: live site is discoverable but no source repository was verified. Audit evidence can proceed; code changes remain blocked on source mapping.

## Run

`python tools/audit_search_readiness.py --output aeo-geo/reports/YYYY-MM-DD-baseline.json`

The utility performs bounded read-only HTTP GETs for 8 homepages, robots.txt and sitemap.xml, with 4 workers and 15-second request timeouts. It records the client used. It never submits URLs, sends leads, changes bot policy or rewrites website content. Failed network requests are recorded as audit-client observations, not universal outages. Reports must be dated; do not interpret a stale baseline as current availability.

## Primary references

- https://developers.google.com/search/docs/appearance/ai-features
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- https://developers.openai.com/api/docs/bots

Google's guidance retains SEO fundamentals for AI search and does not require special AI markup or llms.txt. AI inclusion and ranking are not guaranteed. Optional discovery files are lower priority than correct public content, crawl access and internal links.
