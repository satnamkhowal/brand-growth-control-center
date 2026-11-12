# Central coordination delta — Groot Academy current main and shared-head regression

**Observed:** 12 November 2026, 14:40 IST  
**Source implementation repository:** `satnamkhowal/grootacademy.com` (requested alias `satnamkhowal/gta` redirects to repository ID `1375760757`)  
**Central repository:** `satnamkhowal/brand-growth-control-center`  
**Central main:** `21af139cc32a7b67aab6908c61edeb5998bd4544`  
**Central review branch:** `audit/groot-ga22-browser-delta-20261112-0350`

## New source-side evidence

Groot current main advanced to `52e2b83f77e7607f411bf8011276c98172ea0216`. Since the prior `6c2597` snapshot, two course-catalogue accessibility/search commits landed and PR #676 merged a separate Spring Boot REST API project roadmap with registry and sitemap entries. PR #676 has zero independent review submissions and no PR-triggered workflow run returned for its merge commit; live/deployment/indexation remain UNVERIFIED. It has no canonical GA-B ID and is outside the 29-ID factory queue.

### PR #625 — duplicate shared `<base>` regression

Current main emits one base in `blogs/_shared/partials/head.php` and another in root `head.php`. PR #625 removes the partial-owned base while preserving the dynamic `ga_url()` stylesheet.

Exact Git-blob local fixture evidence:
- Exact current root `head.php`, `includes/site-paths.php`, PR #625 partial, PHP harness and Python test blobs were materialized and hash-verified.
- Current-main partial reconstructed from the one-line patch matched its exact current-main blob.
- Baseline current-main partial fails both render tests as expected: duplicate base values `/groot-preview//` + `/groot-preview/`, and `//` + `/`.
- Proposed PR #625 partial passes 2/2 tests in normal Python, `-O` and `-OO` (6/6 executions).
- PHP 8.4.24 lint 4/4 and Python `py_compile` PASS.

PR #625 remains OPEN/DRAFT with zero independent reviews, zero review threads and no workflow run returned for its current head. Against current main it is 6 ahead / 9 behind (merge base `071ab8a5`); owner-led rebase/reconciliation is required before independent review. A source PR comment records the evidence; no approval or merge was made.

### Recovery stack

- PR #507 is now 3 ahead / 7 behind current main `52e2b83f` (merge base `f048dedf`); owner-led reconciliation is required.
- PR #654 → #660 → #664 remain sequential stacked drafts; PR #664 has zero independent reviews.
- The source owner received a current-main reconciliation comment on #507. No recovery branch was rebased, approved, merged or deployed in this delta.

## Queue, quality and governance

- Canonical queue blob remains `4e087f8cda5479ff9d1124f24ff427a0dbf2b4ad`; all 29 IDs and PR #62 order preserved, no queue write.
- Current factory accounting remains 23 complete original drafts, 23 technical visuals, 23 PHP candidates, 22 independent editorial passes, 18 independent code passes, 23 independent visual passes, 0 independent approvals, 0 published and 0 live verified.
- Main Master Plan blob `e1ce95a0a926b5371abff735bd672d8aeb3f1a9c` still defines 10,000 possible IDs, not validated opportunities or a quota. HAO-008 remains P3/REVIEW.
- User-authorized target remains 100,000/P0; issue #401 records 100,000 as M4 and 1,000,000 as conditional M5. Latest owner checkpoint/comment available through 14:19 IST does not explicitly reconcile 10K/P3 vs 100K/P0 or name one canonical queue/release owner. New batches remain HOLD; repairs continue.

## Central ownership and prior lanes

- Central main README blob remains `b93187c353f8112a57fffab4b383e64236976394`: eight brands listed, three active owner/status rows, Groot Academy active row missing.
- Central PR #1/#2/#3 remain CLOSED/MERGED; reuse the existing AEO/GEO PR #2 baseline and do not recreate it.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website mapping remains unresolved; neither is assumed wrong.
- Source implementation stays in Groot's repository. This report is coordination-only; central main and other brand repositories/files are untouched.

## Exact next action

1. Master owner to reconcile 10K/P3 and 100K/P0 and name one canonical queue/release owner.
2. Groot source owner to rebase/reconcile #625 and #507 against current main, then obtain independent reviews.
3. Actions/Azure administrator to diagnose `BlobNotFound`; restore authorized exact-checkout/DNS access.
4. Continue existing GA-B00029, GA-B00016 and GA-B00022 release gates. Preserve all 29 IDs.

No self-approval, self-merge, deployment, publication, indexing or cross-brand ownership change occurred.


## Follow-up delta — latest Groot main ref during this audit

Groot main advanced from `52e2b83f77e7607f411bf8011276c98172ea0216` to `73f4cd51a23f4bf2a4978815114d059210325dfc` during this run. The two new commits (`a018050`, `73f4cd5`) touch only `includes/course-layout.php` to improve course-image fallback accessibility. They do not touch the shared blog head or the five recovered article folders.

Current comparisons are now:
- PR #507: 3 ahead / 9 behind current main; merge base `f048dedf`.
- PR #625: 6 ahead / 11 behind current main; merge base `071ab8a5`.

The shared blog-head blobs are unchanged, so the exact-source duplicate-base reproduction and PR #625 fix evidence remains applicable. Both source PRs received updated owner-coordination comments; neither was approved, rebased, merged or deployed. The canonical 29-ID queue and current Master Plan/HAO-008 governance findings remain unchanged.


## Follow-up delta — latest Groot main e6dd951 (12 November 2026, 15:35 IST)

Current Groot main advanced from `73f4cd51a23f4bf2a4978815114d059210325dfc` to `e6dd951a20cef66bb6048292efbde6824e80480c`. The intervening merged commits were reviewed; changes are confined to homepage image delivery/paths, course-data JSON, homepage graphics checks, hero CSS and root homepage asset versioning. None overlaps the 22 historical article/asset paths in #507 or the four shared-head/test/workflow paths in #625. No blog registry, sitemap or canonical 29-ID queue change was found in this delta.

Fresh GitHub comparisons against the actual current main:
- Source [#507](https://github.com/satnamkhowal/grootacademy.com/pull/507): **3 ahead / 15 behind**, merge base `f048dedf22da86e93b5b505cc1ebc84884f3a5c8`, 22 files, OPEN/DRAFT, 0 independent reviews.
- Source [#625](https://github.com/satnamkhowal/grootacademy.com/pull/625): **6 ahead / 17 behind**, merge base `071ab8a5ed38864fc2c60828d01d6dcf328f0941`, 4 files, OPEN/DRAFT, 0 independent reviews. Its diff includes the spoken-English QA workflow for test wiring; source owner should confirm that workflow is the intended PHP 8.0 runner or isolate the blog-head test wiring.
- [#654](https://github.com/satnamkhowal/grootacademy.com/pull/654) remains based on #507; [#660](https://github.com/satnamkhowal/grootacademy.com/pull/660) remains based on #654; [#664](https://github.com/satnamkhowal/grootacademy.com/pull/664) remains based on #660. All are OPEN/DRAFT with no independent reviews.

Fresh owner-coordination comments with these exact comparisons were posted on #507 and #625. No rebase, approval, merge or deployment was made. The previously recorded exact-source tests remain bounded local evidence only; Azure Actions `BlobNotFound` and authorized checkout/DNS blockers remain unresolved.

The canonical controller queue was re-read and compared with the immutable PR #62 planning source: both contain 29 unique IDs in the exact original order (GA-B00001–GA-B00029); current queue SHA `4e087f8cda5479ff9d1124f24ff427a0dbf2b4ad`, planning SHA `df30f7f4e7de86f41f6b04fb765221d6757bb513`. No queue write. Controller accounting remains 23 complete drafts, 23 technical visuals, 23 PHP candidates, 22 editorial passes, 18 code passes, 23 visual passes, 0 independent approvals, 0 published and 0 live verified.

A separate [Groot PR #678](https://github.com/satnamkhowal/grootacademy.com/pull/678) is an OPEN/DRAFT AWS SageMaker HyperPod news article candidate outside the canonical 29-ID queue. It was not imported, assigned a queue ID, counted, approved or published by this lane.

Governance remains unchanged: current-main Master Plan = 10,000 possible IDs; HAO-008 = P3/REVIEW; user-authorized controller = 100,000/P0; issue #401 = M4 100,000 and conditional M5 1,000,000. The latest 15:19 IST issue comment is a PR-inventory snapshot correction, not the required Master-owner reconciliation or canonical queue/release-owner decision. New batches remain HOLD while existing repairs continue.

Central main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; its README still lists eight brands but only three active owner/status rows, with Groot's row missing. Central PRs #1/#2/#3 are CLOSED/MERGED; reuse the existing AEO/GEO baseline from #2. Jaipur Engineers `je2` social versus `jaipur-engieneers` candidate website mapping remains unresolved. This is coordination-only evidence; no central-main or other brand source change.

### Exact next action
1. Source owner reconciles #507 and #625 against Groot `main@e6dd951`; preserve noindex and release-inventory gates, root-owned single `<base>`, and dynamic `ga_url()` stylesheet.
2. Independent review follows the owner reconciliation; then review the dependent #507 → #654 → #660 → #664 stack.
3. Actions/storage administrator diagnoses Azure `BlobNotFound`; restore authorized checkout/DNS, then execute PHP 8.0/full-root/schema/registry/sitemap/browser/HTTP/MIME gates.
4. Continue GA-B00029 full-root, GA-B00016 editorial/AT and GA-B00022 production/AT gates.
5. Master owner reconciles 10K/P3 vs 100K/P0 and names one canonical queue/release owner before new batches.

No self-approval, self-merge, deployment, publication, mass indexing, queue mutation or cross-brand ownership change occurred.
