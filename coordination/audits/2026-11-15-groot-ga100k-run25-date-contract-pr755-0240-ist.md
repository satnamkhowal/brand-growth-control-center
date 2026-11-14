# Central coordination delta — Groot Academy 100K Run 25

**Observed:** 2026-11-15 02:40 IST  
**Central repository:** satnamkhowal/brand-growth-control-center  
**Audit branch:** audit/groot-ga22-browser-delta-20261112-0350  
**Central Main:** `21af139cc32a7b67aab6908c61edeb5998bd4544` (unchanged)  
**Current Main README blob:** `b93187c353f8112a57fffab4b383e64236976394`

## Groot source implementation remains in the brand repository

- Requested alias `satnamkhowal/gta` resolves to the verified Groot Academy source repository `satnamkhowal/grootacademy.com`, repository ID 1375760757. Mango Engineers was not used.
- Source Main remains `e1f629ecd0bffb9d3eafaaadbd6f5bf226950e6f`; latest observed commit is course-catalogue-only. No blog-factory or five-article recovery path changed on Main.
- Source controller PR [#750](https://github.com/satnamkhowal/grootacademy.com/pull/750) remains OPEN/DRAFT and carries the Run 25 report/checkpoint.
- New source PR [#755](https://github.com/satnamkhowal/grootacademy.com/pull/755) is a stacked QA-only child of source PR #664. It changes only three existing QA files: recovery inventory, rendered-page QA and synthetic fixtures. It is 4 ahead / 0 behind its #664 branch; no article, asset, queue, registry, sitemap or production file changed. PR #755 is OPEN/DRAFT, currently mergeable, with zero independent reviews/comments.
- The child QA proposal requires draft date keys to be absent (including null/empty placeholders), release ISO dates to be valid and ordered, visible display date to equal publication date, and rendered draft schema/meta/visible blog metadata to omit dates.
- Python 3.13.5 coordinator-run synthetic evidence: 24/24 date/render cases and 3/3 PHP key-presence cases PASS. This is not the full committed PR suite, PHP 8.0, hosted Actions, independent review or release approval.
- All five original GA-B00006–GA-B00010 metadata records still have null publication/modification dates; current #660 candidates still emit unsupported 2026-11-01 dates. The QA child must be independently reviewed/integrated before the #660 owner removes those fields. Keep all five pages noindex,follow and outside registry/sitemap.
- Source canonical queue remains 29/29 original IDs, exact blob `c12a915e06c8100a350b21338311651df0f35094`. Complete drafts/visuals/PHP candidates remain 23/23/23; independent component PASS 22 editorial / 18 code / 23 visual; fully approved/published/live verified 0/0/0. No new article or image was created.

## Current central-main and PR delta

- Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; this update is coordination-only on the existing PR #22 branch.
- Existing central PRs [#1](https://github.com/satnamkhowal/brand-growth-control-center/pull/1), [#2](https://github.com/satnamkhowal/brand-growth-control-center/pull/2) and [#3](https://github.com/satnamkhowal/brand-growth-control-center/pull/3) are merged. Reuse PR #2's existing eight-brand AEO/GEO baseline and remediation queue; do not recreate it.
- Central README still lists eight brands but only three active owner/status rows; Groot Academy's dedicated row remains missing. No owner transfer or repository mapping was inferred.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved; neither is assumed wrong.
- Central PR #22 remains OPEN/DRAFT, currently 111 commits ahead / 0 behind Main across 61 files, with zero independent reviews. Its base Main remains unchanged.
- Existing central PR #23's eight-brand article record remains merged but deployment/live verification is not established. PR #24 remains staff-operations architecture only; private student/staff data is excluded from the public repository.

## Exact next action

1. Independent review of source PR #755; no self-approval or merge.
2. Integrate the date contract into #664, then remove unsupported date fields from the five #660 candidates.
3. Reconcile source recovery parent/base snapshots and preserve #625/#713 workflow ownership.
4. Diagnose Azure Actions `BlobNotFound` before any hosted retry.
5. Add Groot's dedicated central owner/status row only after the central owner verifies the responsible owner and source mapping; record the 100K/P0 versus capacity-priority decision, one canonical queue owner and one independent release approver.
6. Keep all 29 IDs intact and new batches HOLD until those governance decisions are explicit.

No central Main write, other-brand source change, ownership reassignment, merge, deployment, publication, indexing or ranking/live claim.
