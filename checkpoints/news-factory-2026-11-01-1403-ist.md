# News Factory checkpoint — 1 November 2026, 14:03 IST

## Coordination
- Parent checkpoint: `checkpoints/news-factory-2026-10-29-0907-ist.md`
- Coordination branch: `ops/news-factory-20261019`
- Brand branch: `content/news-factory-20261019-1410`
- Central checkpoint and accessible brand draft directories were read before writes.
- Four non-overlapping official-source tracks covered student/developer opportunities, frontend, backend and AI/cloud.
- Existing queues were checked for duplicate Google APM and SvelteKit stories; none was found.
- Bounded production batch: two brand-specific drafts and two original SVGs.
- No merge, deployment or publication.

## Accepted fresh research

### 1. Google APM University Graduate 2027 Start — Bengaluru
- Applications began 30 October 2026.
- Deadline: before end of day 24 November 2026; timezone not stated.
- Target cohort starts: April–August 2027.
- India relevance: advertised work location is Bengaluru. The listing does not state citizenship, work-authorisation, visa or relocation terms.
- Compensation and application fee are not stated.
- Official source: https://www.google.com/about/careers/applications/jobs/results/101007950268506822-associate-product-manager-university-graduate-2027-start

### 2. SvelteKit 3.1.1 security release
- Released 29 October 2026 at 23:47 UTC / 30 October 05:17 IST.
- GHSA-m9j8-jcmv-hp69: server-only imports through `src/params.js` could reach client bundles; affected 3.0.0–3.1.0; fixed 3.1.1; High/CVSS 7.5; no known CVE.
- GHSA-3r8g-jcqq-3p5j: experimental remote-form parsing DoS; affected 2.42.0–3.1.0; fixed 3.1.1; High/CVSS 7.5; no known CVE.
- Release: https://github.com/sveltejs/kit/releases/tag/%40sveltejs%2Fkit%403.1.1
- Advisories:
  - https://github.com/sveltejs/kit/security/advisories/GHSA-m9j8-jcmv-hp69
  - https://github.com/sveltejs/kit/security/advisories/GHSA-3r8g-jcqq-3p5j

### 3. pgAdmin 4 v9.19 — researched, queued
- Released 29 October 2026; PostgreSQL announcement published 31 October.
- Official notes report fixes for 15 vulnerabilities, CVE-2026-116238 through CVE-2026-116252.
- Migration caution: configure `SERVER_PASSEXEC_COMMANDS` before first startup after upgrade.
- Announcement: https://www.postgresql.org/about/news/pgadmin-4-v919-released-3426/
- Release notes: https://www.pgadmin.org/docs/pgadmin4/9.19/release_notes_9_19.html
- Not drafted in this bounded batch.

### 4. Google threat research on agentic offensive frameworks — researched, queued
- Official report published 30 October 2026.
- Underlying malicious activity was observed from late August; the incident activity is not presented as beginning on publication day.
- No India-specific victim claim was made in reviewed evidence.
- Source: https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks
- Not drafted in this bounded batch.

## Produced drafts and media

### Groot Academy
- Draft: https://github.com/satnamkhowal/groot-academy/blob/content/news-factory-20261019-1410/docs/news-factory/drafts/google-apm-university-graduate-2027-bengaluru.md
- Original SVG: https://github.com/satnamkhowal/groot-academy/blob/content/news-factory-20261019-1410/docs/news-factory/media/google-apm-2027-bengaluru-application-roadmap.svg
- Draft commit: `c9632fa527ab6f60574970a88a3f3184f8f429f6`
- Graphic commit: `d2abe02bde0dac44c3cbc2520a65d12d24dc4673`
- QA correction commit: `fc89c951d620046889ecdb530ad8a41c188619de`
- Final draft blob: `054cb3fcf002ece65a5c631a7010432a8834c85a`
- Status: independently QA-ready; not live.

### Forsk Coding School
- Draft: https://github.com/satnamkhowal/forsk-coding-school/blob/content/news-factory-20261019-1410/docs/news-factory/drafts/sveltekit-3-1-1-security-update-guide.md
- Original SVG: https://github.com/satnamkhowal/forsk-coding-school/blob/content/news-factory-20261019-1410/docs/news-factory/media/sveltekit-3-1-1-security-remediation.svg
- Draft commit: `91b54a02ba7825588aa3edd2927540706e869bf3`
- Graphic commit: `389319ab8b3b7bb613f13d05dfe29db0bb3ab572`
- QA status commit: `2548881a0b260abfe5eaf4cee3730e510d6f202a`
- Final draft blob: `de62fd7f7ac2094d8d63523b5e78ae80384f5cc6`
- Status: independently QA-ready; not live.

## Independent QA
- Google draft initially overstated India eligibility from the Bengaluru location. It was corrected to distinguish location from unstated citizenship, work-authorisation, visa and relocation terms.
- Both final drafts and both SVGs passed factual, date/version, SEO/AEO/GEO, accessibility, originality, rights-record and non-live checks.
- SVGs are 1200×675 with viewBox, title, description, role and ARIA; no third-party logos or artwork.

## Media and video
- New original graphics: 2.
- Licensed downloads: 0.
- Video embeds: 0. No story-specific official or reputable original YouTube video with a verified ID and confirmed embedding availability was found; no ID or iframe was invented.

## Differential track results
- Programs/opportunities: Google APM Bengaluru accepted and drafted.
- React/frontend: SvelteKit 3.1.1 accepted and drafted; no in-window React-core stable/security item.
- Node/backend: pgAdmin 4 v9.19 accepted for the queue; no qualifying in-window stable Node.js release/advisory.
- AI/cloud/developer: GTIG/Mandiant research accepted for the queue. Google Cloud spend-caps blog dated 30 October was excluded as a new-GA story because official Billing release notes place GA on 13 October.

## Counts
### Since parent checkpoint
- Accepted researched items: 4
- New drafts: 2
- New original graphics: 2
- Newly independent QA-ready: 2
- Brand commits: 6
- Central checkpoint commits: 1
- Newly live: 0

### Cumulative
- Researched: 38
- Drafted: 34
- Original graphics: 34
- GitHub commits including checkpoints: 145
- Independent QA-ready: 20
- Live: 0

## Next action
1. Editorial/legal review of the two QA-ready drafts; re-check application status and security sources immediately before publication.
2. Draft the queued pgAdmin 4 v9.19 and GTIG items only after a new duplicate/ownership check.
3. Continue official-source differential monitoring; keep release dates separate from event or opening dates.
