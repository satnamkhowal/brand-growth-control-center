# Central coordination delta — Groot Academy Run 41

**Observed:** 2026-11-15 18:41 IST  
**Scope:** coordination-only; source implementation remains in `satnamkhowal/grootacademy.com` (user-facing alias `satnamkhowal/gta`).

## New source evidence

- Current source Main is `e1f629ecd0bffb9d3eafaaadbd6f5bf226950e6f`. Compared with the previous controller snapshot `50c169e`, Main is four commits ahead / zero behind; changed paths are homepage CSS/JS, `courses/index.php` and root `index.php`. No blog article, shared blog layout, registry, sitemap or queue path changed.
- The existing five-article recovery inventory parser had a static false-positive: it returned the first duplicate PHP metadata key, while PHP runtime retains the last. PHP 8.4.24 reproduced the mismatch (static reader: expected slug; runtime: later `spoofed-slug`).
- QA-only child [PR #778](https://github.com/satnamkhowal/grootacademy.com/pull/778) now rejects duplicate literal/inline/nested metadata keys and expression overrides. It is 2 commits ahead / 0 behind exact PR #760 parent, with two intended QA files and zero independent reviews/threads.
- Python 3.13.5 coordinator scratch matrix: 32/32 PASS. PHP 8.4.24 duplicate fixture lint and runtime reproduction PASS. Five recovered article files each have exactly one occurrence of each of nine targeted metadata keys. This is not the complete committed suite, PHP 8.0, hosted CI, full-root, browser/AT, HTTP/MIME or release approval.
- Exact recovery stack compares: #507→#654 5/0; #654→#660 10/0; #660→#664 13/0; #664→#755 17/0; #755→#760 27/0; #760→#778 2/0. #507 versus current Main is diverged 4 ahead / 35 behind, with 22 additions and no modifications/deletions. Owner refresh/reconciliation remains required; no other source branch was edited.
- Automatic Actions run [#43718463981](https://github.com/satnamkhowal/grootacademy.com/actions/runs/43718463981), job 132825011868, failed before steps. Steps are null and log retrieval returns Azure BlobNotFound HTTP 404. Hosted assertions: 0. Administrator diagnosis required; no retry.

## Factory accounting and ownership

- Canonical queue remains 29/29 original IDs, exact order, SHA `c12a915e06c8100a350b21338311651df0f35094`.
- Factory counts remain 23 complete drafts / 23 technical visuals / 23 PHP candidates; independent editorial/code/visual component passes 22/18/23; fully approved / published / live verified 0/0/0.
- Research PR #68 remains 14 proceed proposals plus GA-B00014 in-place refresh, not finished articles.
- GA-B00006 remains PUBLISH_PR; full independent release review and PHP 8.0/full-root/shared-schema/route/browser/AT/HTTP/MIME gates remain pending.
- No new article, image, ID, queue row, registry entry or sitemap URL.

## Central repository and cross-brand delta

- Current Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; current README was read directly from Main.
- Central PR #22 branch `audit/groot-ga22-browser-delta-20261112-0350` compares 131 commits ahead / 0 behind Main; PR #22 remains OPEN/DRAFT with zero independent reviews and zero review threads.
- PRs #1/#2/#3 are merged. Reuse the existing AEO/GEO PR #2 baseline; no new baseline or duplicate queue created.
- Central README lists eight brands but only three active owner/status rows; Groot's dedicated active row is missing.
- Jaipur Engineers `je2` social versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. Treat these as distinct candidate workstream roles until the existing central mapping owner records deployment evidence; no assumption or reassignment.
- No other brand's source files or ownership changed.

## Exact next action

1. Independent reviewer examines PR #778, then PR #760/#755; no self-approval or merge.
2. Administrator diagnoses Azure Actions BlobNotFound before any retry.
3. Existing source owners refresh #507 against current Main and preserve the exact recovery/date-QA chain; do not modify their branches from this coordination lane.
4. Obtain independent GA-B00006 full release review and required PHP 8.0/full-root/schema/route/browser/AT/HTTP/MIME evidence.
5. Master owner records 100K/P0 alignment, one canonical queue owner, one independent release approver and evidence-based batch criteria before new IDs are opened.

Central Main and all source repositories remain unchanged by this coordination report. No merge, deployment, publication, indexing or owner reassignment.
