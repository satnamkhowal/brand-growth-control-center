# News Factory checkpoint — 2026-11-09 13:30 IST

## Window

Differential scan from the verified 2026-11-09 08:09 IST checkpoint through 13:30 IST. This checkpoint also reconciles the completed NestJS GraphQL batch whose central checkpoint write was interrupted.

## Produced and independently QA-ready

### NestJS GraphQL 14.2.0 security release — Forsk Coding School

- Official release published 2026-11-04 12:39:08 UTC / 18:09:08 IST.
- Fixes 10 advisories: 3 High and 7 Medium across `@nestjs/graphql`, `@nestjs/apollo` and `@nestjs/mercurius`.
- Draft: `docs/news-factory/drafts/nestjs-graphql-14-2-0-security-release.md`.
- Original media: `docs/news-factory/media/nestjs-graphql-14-2-0-security.svg`, 1200×675.
- Independent QA: PASS.
- Status: QA-ready, not live.

### NestJS 11.2.9 / Multer CVE-2026-113872 — Forsk Coding School

- Exact-window release published 2026-11-09 07:53:24 UTC / 13:23:24 IST.
- `@nestjs/platform-express` updates Multer to 2.5.0, resolving GHSA-q7qp-rjg7-q26m / CVE-2026-113872.
- Affected Multer: `>=2.0.0 <2.5.0`; High, CVSS 7.5.
- Exposure requires an asynchronous `fileFilter` and request teardown while another callback remains pending. A single unauthenticated request can crash the Node.js process. Synchronous `fileFilter` is the documented workaround.
- Draft: `docs/news-factory/drafts/nestjs-11-2-9-multer-cve-2026-113872.md`.
- Original media: `docs/news-factory/media/nestjs-11-2-9-multer-security.svg`, 1200×675.
- Independent QA: PASS.
- Status: QA-ready, not live.

## Research updates

- NIC Winter 2026 portal is reachable and last updated 9 Nov. Registration UI remains visible; no official final deadline is displayed.
- Google Student Researcher 2027 India unchanged and already covered.
- MSME–Samsung remains announcement-only without programme-specific application URL or deadline.
- Frontend and AI/cloud: no exact-window qualifying release.
- NestJS 12.4.1 published at 13:31:22 IST, after this run's 13:30:32 cutoff; defer to next cycle.
- Django 6.1.3/6.0.10/5.2.19 security release is source-complete and remains the next distinct backend draft candidate.

## Media and delivery

- Video embeds: 0; no verified item-specific official/reputable original YouTube ID found.
- Licensed downloads: 0.
- Original graphics produced since previous checkpoint: 2.
- Merge/deploy/publish: 0.

## Counts

| State | Cumulative |
|---|---:|
| Researched | 58 |
| Drafted | 48 |
| Original graphics | 48 |
| Independent QA-ready | 33 |
| Live | 0 |

## Repository notes

- Forsk content branch: `content/news-factory-20261019-1410`.
- Central coordination branch: `ops/news-factory-20261019`.
- No Mango Engineers, Groot Academy or Jaipur Engineers write: no additional distinct accepted story plus verified repository mapping justified a write.

## Next action

Inspect NestJS 12.4.1 in the next window and avoid duplicating the 11.2.9 story. Produce the verified Django multi-line security guide as the next queue item. Continue Node.js 11 November security-release watch.
