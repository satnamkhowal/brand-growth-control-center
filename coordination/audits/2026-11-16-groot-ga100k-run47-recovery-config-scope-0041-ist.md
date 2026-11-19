# Central coordination audit — Groot Academy 100K Run 47
Date: 2026-11-16 00:41 IST

## Scope and repository identity

Coordination-only delta. Source implementation remains in the Groot Academy repository; this repository receives no source-code changes.

GitHub redirects the user's historical alias `satnamkhowal/gta` to `satnamkhowal/grootacademy.com`, the same repository ID `1375760757`. This is a rename/alias, not a second brand repository and not Mango Engineers.

## New source-side evidence

- Current Groot Main: `21059089fb17d10200a386c7ef648d478bf700d7`. Its latest commit changes course-finder CSS and `courses/index.php`, with no blog-factory/recovery overlap.
- Recovery PR [#507](https://github.com/satnamkhowal/grootacademy.com/pull/507) remains OPEN/DRAFT at 4 ahead / 40 behind Main, 22 historical additions and zero deletions. Current-Main refresh remains with the source owner.
- Recovery chain current-ref comparisons are linear: #507→#654 (5/0), #654→#660 (10/0), #660→#664 (13/0), #664→#755 (17/0), #755→#760 (27/0), #760→#778 (3/0), #778→#788 (4/0). No owner branch was edited or rebased by this audit.
- QA child [PR #788](https://github.com/satnamkhowal/grootacademy.com/pull/788) now includes two bounded false-positive repairs: ignore inline HTML after PHP close tags and scope metadata to the unique top-level `$blog` array. It changes only two QA files, is 4 commits ahead / 0 behind parent #778, remains Draft and has zero independent reviews/threads.
- Coordinator scratch evidence is Python 3.13.5 12/12 and PHP 8.4.24 syntax fixtures 5/5. These are not the full committed suite, PHP 8.0 or independent QA.
- Exact-head hosted CI remains blocked: run [#43751438095](https://github.com/satnamkhowal/grootacademy.com/actions/runs/43751438095), job `132926047804`, failed before steps with zero steps; Azure `BlobNotFound` HTTP 404 on log retrieval. The final PR #788 head has no associated workflow run yet. Administrator diagnosis is required.

## Canonical production accounting

- Canonical queue: 29 original IDs, unchanged; queue blob `0b0685b89c8833f9f8b49d7e223c166145082956`.
- 23 complete drafts, 23 technical visuals and 23 PHP candidates.
- Independent component PASS: editorial 22, code 18, visual 23.
- Fully approved 0; published 0; live verified 0.
- No new article, image or queue row. Research PR #68's 14 proceed proposals and GA-B00014 refresh are not finished-article counts.

## Central-main and ownership delta

- Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; no central-main write.
- Current main README lists eight brands but only three active owner/status rows; Groot Academy's dedicated row remains missing.
- Central PRs #1/#2/#3 are merged. Reuse the existing AEO/GEO PR #2 baseline; no duplicate AEO/GEO or backlink queue was created.
- Existing audit PR #22 is OPEN/DRAFT at `01b7d08ee686bb1d7051e916dd6b9a1bdf0478a3`, 139 commits / 83 files, zero independent reviews. This report is added to that already-owned audit branch only.
- PR #25 is a source-level course-link inventory, not proof of acquired backlinks, published placements, referral traffic or rankings.
- Jaipur Engineers `je2` social vs `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. Preserve both workstream roles; do not infer either repository is wrong or reassign ownership.
- Existing PRs #17/#18/#20 remain draft coordination work; no parallel duplicate report queue is created here.

## Next actions

1. Independent reviewer examines source PR #788 and parent #778, then #760/#755 in exact stack order.
2. Azure Actions administrator diagnoses storage/runner initialization and runs the committed suite plus PHP 8.0 on a healthy runner.
3. Groot source owner integrates accepted GA-B00006 repairs and refreshes #507 against current Main, retaining all worker changes.
4. Central owner reconciles the missing Groot owner/status row and records authoritative Jaipur social/site/deployed-origin mapping.
5. Keep 100K/P0 master-owner alignment, one canonical queue owner, one independent release approver and batch criteria as explicit governance gates.

No ownership transfer, source-main change, central-main change, merge, deployment, publication, backlink-acquisition or indexing claim was made.
