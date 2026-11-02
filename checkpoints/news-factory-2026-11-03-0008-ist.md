# News Factory checkpoint — 2026-11-03 00:08 IST

## Window

Differential scan from 2026-11-02 15:04 IST through 2026-11-03 00:08 IST, plus source-status revalidation of the prior URSC item.

## Accepted and produced

### Fastify 5.12.8 security release — Forsk Coding School

- Official release published 2026-11-02 10:51:32 UTC / 16:21:32 IST.
- Security advisory: GHSA-3qgw-9275-xf8w / CVE-2026-120216.
- Severity: Moderate, CVSS 5.9, CWE-248.
- Affected: `>=5.8.0 <5.12.8`; patched: `5.12.8`.
- Exposure requires a nonzero `handlerTimeout` and a streaming response; default `handlerTimeout: 0` is not affected.
- Draft: `docs/news-factory/drafts/fastify-5-12-8-handler-timeout-streaming-dos-fix.md`.
- Original media: `docs/news-factory/media/fastify-5-12-8-security-checklist.svg`, 1200×675.
- Media record includes source, permission, attribution, path, alt text and dimensions.
- Independent QA: PASS after provenance and label corrections.
- Final status: QA-ready, not live.

## Researched, queued, not drafted in this bounded batch

### Google Cloud Apigee EKM health monitoring

- Official release note dated 2026-11-02.
- Adds Cloud EKM health monitoring and alerting through Cloud Logging.
- Rollout began on 2026-11-02 and may take four or more business days across Google Cloud zones.
- Feature applies only to Apigee organizations configured with CMEK + EKM at organization creation; it cannot be enabled for existing organizations.
- India relevance supported by Apigee locations in Mumbai (`asia-south1`) and Delhi (`asia-south2`).
- Exact publication time was not provided, so it is a dated catch-up candidate rather than a proven exact-window launch.

## Source-status correction

### URSC internship draft moved to research hold

The official URSC page no longer displays the January–March 2027 invitation. It now says the portal will reopen on 1 February 2027 for “April–June 2026,” an internally inconsistent year pairing. The registration endpoint timed out. The existing draft was updated:

- status: `research-hold`
- publication: not live; status re-verification required
- prior QA: invalidated because the source status changed
- no silent correction from 2026 to 2027 was made

NIC Digital India Internship could not be verified as open: the official portal timed out, and third-party claims were excluded.

## Other tracks

- React/frontend: no new stable release or upstream advisory in-window.
- Node/backend: Fastify 5.12.8 was the only qualifying stable/security item.
- AI/cloud: Apigee EKM monitoring accepted as a research queue item; no second draft created in this bounded batch.
- YouTube: no current story-specific official or reputable original video with a verified ID was found; embeds 0.
- Licensed downloads: 0.
- Original graphics created: 1.
- Merge/deploy/publish: 0.

## Counts

| State | Cumulative |
|---|---:|
| Researched | 42 |
| Drafted | 39 |
| Original graphics | 39 |
| Independent QA-ready | 24 |
| Live | 0 |

The QA-ready count remains 24 because Fastify passed independent QA while the earlier URSC draft was removed from QA-ready status after the official page changed.

## Repository notes

- Forsk work remains isolated on `content/news-factory-20261019-1410`.
- Central checkpoint remains isolated on `ops/news-factory-20261019`.
- No new write was made to Mango Engineers, Groot Academy or Jaipur Engineers because no accepted story plus verified repository instructions/branch mapping justified a write in this batch.

## Next action

Recheck URSC and NIC official portals for consistent application status. Draft the queued Apigee item only after duplicate/brand ownership review, and reverify rollout availability immediately before publication.
