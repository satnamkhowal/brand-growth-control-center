# News Factory checkpoint — 2026-11-03 06:08 IST

## Window

Differential scan from 2026-11-03 05:05 IST through 06:08 IST, plus production from the verified AWS security queue.

## Produced and independently QA-ready

### AWS Virtual Engineering Workbench / CVE-2026-119085 — Forsk Coding School

- AWS Important bulletin 2026-162-AWS published 2026-11-02 09:30 PST / 23:00 IST.
- This is a disclosure catch-up; fixed commit `c146486` was merged earlier on 2026-05-04.
- Affected: all commits before `c146486`.
- Exploit path: remote authenticated actor submits a crafted CloudFormation template with template-engine directives through the product-versioning API.
- Impact: arbitrary code executes with the publishing Lambda IAM role; AWS says this could reach data/resources across all tenant projects.
- No complete workaround. Redeploy latest/fixed code and patch forks; until then restrict users who can create/update product versions.
- Draft: `docs/news-factory/drafts/aws-virtual-engineering-workbench-cve-2026-119085.md`.
- Original media: `docs/news-factory/media/aws-vew-template-injection-remediation.svg`, 1200×675.
- Independent QA: PASS.
- Status: QA-ready, not live.

## Exact-window research

- Programs: no new official opening/status change. NIC timed out but is not treated as closed; last verified state remains open registration from 2 November with no official final deadline. URSC remains on research hold.
- Frontend: no new stable/security release. Next.js promised November security release still unpublished; canary 16.5.0-canary.37 excluded.
- Backend: no new stable release or advisory.
- AI/cloud: no new exact-window OpenAI, Google Cloud, GitHub, AWS, Azure or Anthropic release.
- CVE-2026-120497 aidlc stored-XSS remains on hold because a complete direct AWS bulletin was not consistently available through the official index/search.

## Media and delivery

- Video embeds: 0; no verified item-specific official/reputable original YouTube ID found.
- Licensed downloads: 0.
- Merge/deploy/publish: 0.

## Counts

| State | Cumulative |
|---|---:|
| Researched | 50 |
| Drafted | 43 |
| Original graphics | 43 |
| Independent QA-ready | 28 |
| Live | 0 |

## Repository notes

- Work is isolated on Forsk branch `content/news-factory-20261019-1410`.
- Central checkpoint is isolated on `ops/news-factory-20261019`.
- No write to Mango Engineers, Groot Academy or Jaipur Engineers because no distinct accepted story plus verified repository content mapping justified a write in this batch.

## Next action

Continue the Next.js advisory watch. Create no security article until official affected and patched version ranges are available. Reverify NIC status/deadline before any publication.
