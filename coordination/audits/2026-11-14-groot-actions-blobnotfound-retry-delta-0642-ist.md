# Groot Academy — GitHub Actions BlobNotFound retry delta

Date: 14 November 2026, 06:42 IST  
Scope: coordination-only evidence; implementation remains in Groot Academy's source repository.

## Verified source identity and checkpoint

- The Groot controller README/CONTROLLER record `satnamkhowal/gta` as the previous repository alias and says the permanent redirect to `satnamkhowal/grootacademy.com` was observed on 2026-11-02. This run used the redirect destination; no Mango Engineers repository was accessed.
- Source controller branch: `content/groot-100k-controller-20261016`; checkpoint commits: report `744cc6b7`, CONTROLLER `d2a0925b`, README `ee4b048c`.
- Source main snapshot: `9c90902f`. Canonical queue remains 29/29 IDs, with no queue/status/order changes.
- Full source evidence: [Actions retry report](https://github.com/satnamkhowal/grootacademy.com/blob/content/groot-100k-controller-20261016/marketing/blog-factory/work/B0002/qa/2026-11-14-actions-blobnotfound-retry-evidence-0642-ist.md).

## New CI delta

- PR #507 remains OPEN/DRAFT, head `72f24de4`, 22 changed files, zero independent reviews. Markdown parity run `43207192750` failed; a targeted retry created job `132275095535`, which also failed with zero steps. Log retrieval returns Azure Storage `BlobNotFound` HTTP 404. No content assertion is available; do not rewrite historical article payloads based on this infrastructure failure.
- PR #713 remains OPEN/DRAFT, head `fa4bac8d`, four changed files, zero independent reviews. Four exact-head jobs (route/schema, shared-head base-path, blog-factory validation, Markdown parity) all failed before steps and all four log fetches return the same `BlobNotFound` HTTP 404. Run/job IDs are recorded in the source report.
- PR #625's separate Spoken English route-QA workflow remains protected; its three shared-head files were previously confirmed identical to PR #713. #654→#660→#664 remain the dependent recovery stack. No PR state or owner was changed.

## Central coordination status

- Current central main README blob: `b93187c353f8112a57fffab4b383e64236976394`; the control board still has only three active owner/status rows and no dedicated Groot Academy owner row.
- The 2026-10-19 baseline audit remains the reference; no full crawl was repeated. It preserves CC-AUD-001 (Jaipur Engineers `je2` social vs `jaipur-engieneers` candidate production mapping), CC-AUD-002 (control-board reconciliation), CC-AUD-003 (Groot independent QA/release gates), and CC-AUD-004 (other brand source mapping) with their existing owners.
- PR #1/#2/#3 are CLOSED/MERGED; reuse the PR #2 AEO/GEO baseline.
- Central PR #22 remains OPEN/DRAFT, 85 commits ahead / 0 behind, 42 coordination-only report files, mergeable=true, zero independent reviews. Central main is unchanged.

## Owner and next action

1. Repository administrator diagnoses GitHub Actions runner/log artifact storage; restore retrievable job logs.
2. Re-run only the exact-head owned checks after infrastructure recovery; capture steps and assertions.
3. Obtain independent GA-B00006 editorial/code/visual release review; owner-refresh #507 and its stack.
4. Reconcile shared-head #625/#713 overlap while preserving the separately owned Spoken English route workflow.
5. Master owner records 100K/P0 vs 10K/P3 alignment, one canonical queue owner and one independent release approver; until then new IDs remain HOLD.

Counts remain 23 complete drafts/visuals/PHP candidates, component editorial/code/visual passes 22/18/23, full approvals/published/live 0/0/0. No source implementation, approval, owner reassignment, merge, deployment, publication or indexing was performed by this central audit.


## Additional source-queue verification — 14 November 2026, 06:47 IST

The source controller compared the original queue patch in merged planning PR #62 (head `567b6b27445191d6705624607dfb3cbeb5c72c32`) with the current canonical queue. Exact result: 29 original IDs, 29 current IDs, zero missing, zero extra, order preserved, no duplicate slugs or primary queries. Existing lifecycle status transitions remain on the same IDs. No queue file change or new article occurred. Full evidence is appended to the linked source report.
