# News Factory checkpoint — 2026-11-03 05:05 IST

## Window

Differential scan from 2026-11-03 01:02 IST through 05:05 IST, plus catch-up reconciliation of newly indexed official releases and security bulletins.

## Produced and independently QA-ready

### AWS SDK for pandas 3.17.1 / CVE-2026-119301 — Forsk Coding School

- AWS Important bulletin 2026-161-AWS published 2026-11-02 08:30 PST / 22:00 IST.
- This is a catch-up disclosure; fixed version 3.17.1 was released earlier on 2026-08-03.
- Affected: `awswrangler >=3.5.2,<3.17.1`.
- Condition: authenticated actor can modify AWS Glue Data Catalog metadata while a separate, more-privileged principal performs the Iceberg write.
- Impact: crafted column identifier may cross the writer's data permission boundary as described by AWS.
- No complete workaround; upgrade and restrict `glue:UpdateTable`/related permissions.
- Draft: `docs/news-factory/drafts/aws-sdk-pandas-3-17-1-iceberg-cve-2026-119301.md`.
- Original media: `docs/news-factory/media/awswrangler-3-17-1-iceberg-security-checklist.svg`, 1200×675.
- Independent QA: PASS.
- Status: QA-ready, not live.

## Researched and queued

### Other AWS Important bulletins

- 2026-162-AWS / CVE-2026-119085: Virtual Engineering Workbench publishing-template injection; affected all commits before `c146486`; fix requires redeployment/patching forks. No complete workaround.
- 2026-163-AWS / CVE-2026-120497: stored XSS in pre-fix aidlc-traceability HTML reports. Catch-up only; not drafted in this bounded batch.

### Frontend maintenance

- Angular 20.3.35 published 2026-11-03 03:38:33 IST; `upgrade` fix for compiling downgraded component template contents.
- Angular 21.2.26 published 2026-11-03 04:05:58 IST; same maintenance fix.
- Astro 7.4.5 published 2026-11-02 19:51:33 IST; stability/hardening fixes, not an official security advisory.
- Next.js November security release was still unpublished at 05:05 IST. Next.js 16.4.4 remains a bug-fix backport and is not described as the promised security release.

No standalone draft was created for low-priority maintenance patches or unreleased advisories.

## Programs/opportunities

- No new exact-window opening.
- NIC portal timed out during recheck; timeout is not treated as closure. Last verified official state remains registration interface open from 2026-11-02, with no official final deadline.
- URSC date/year conflict remains unresolved; research hold remains correct.
- No newly dated official Google India opportunity.

## Other tracks

- Backend: no new qualifying stable release or advisory.
- AI/cloud exact window: no additional OpenAI, GitHub, Google Cloud, Azure or Anthropic release.
- Video embeds: 0; no verified item-specific official/reputable original YouTube ID found.
- Licensed downloads: 0.
- Merge/deploy/publish: 0.

## Counts

| State | Cumulative |
|---|---:|
| Researched | 50 |
| Drafted | 42 |
| Original graphics | 42 |
| Independent QA-ready | 27 |
| Live | 0 |

## Repository notes

- New article/media work is isolated on Forsk branch `content/news-factory-20261019-1410`.
- Central checkpoint is isolated on `ops/news-factory-20261019`.
- No write to Mango Engineers, Groot Academy or Jaipur Engineers because no distinct accepted story plus verified repository content mapping justified a write in this batch.

## Next action

Recheck the promised Next.js security publication and create a guide only after official advisories expose affected and patched version ranges. Before any NIC publication, reverify the portal and official deadline.
