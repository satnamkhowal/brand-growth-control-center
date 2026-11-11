# Groot Academy cross-lane delta — main 071ab8a shared blog-head base-path reconciliation — 11 November 2026, 21:44 IST

**Scope:** Coordination-only delta on the existing audit branch. Source implementation remains in `satnamkhowal/grootacademy.com`; no central-main or other-brand source files changed.

## Verified repository identity and source state

- Requested `satnamkhowal/gta` and canonical `satnamkhowal/grootacademy.com` resolve to the same GitHub repository ID `1375760757`.
- Groot main is `071ab8a5ed38864fc2c60828d01d6dcf328f0941`.
- Controller branch `content/groot-100k-controller-20261016` is isolated at `b92e44b00d6e676d88a98e9cd17952ec4bbcc9e8`; do not replace it from stale main planning files.
- Latest main commit `071ab8a` changes only `.htaccess` for a Windows Server course image allowlist. Merged PRs #637–#640 precede it.

## New Groot implementation delta

Merged PRs:
- #637 — static contact URL path.
- #638 — blog-index subpath links and responsive styling.
- #639 — shared blog-head dynamic base path and stylesheet URL.
- #640 — Python blog course CTA.

A bounded PHP include-chain reproduction found that current `blogs/_shared/partials/head.php` emits a base element and then includes root `head.php`, which emits another. The blog partial appends a slash to `ga_url()` even though the helper already returns a trailing slash. Exact current-main shared-partial and site-path helper blobs were materialized and hash-matched; PHP lint was 4/4 and six local/production fixture assertions passed. This is a minimal source fixture, not a full checkout, browser test or production release check.

PR #625 is now 5 ahead / 20 behind current main, OPEN/DRAFT, four files, zero reviews. Its removal of the duplicate base is useful, but its old static stylesheet URL conflicts with merged #639's dynamic `ga_url()` URL. The owner should rebase and preserve the dynamic stylesheet while making root `head.php` the sole base owner. The Actions `steps: null` / Azure `BlobNotFound` blocker remains; no blind retry.

Other gates:
- PR #533 is OPEN/DRAFT, stacked 8 commits ahead / 0 behind its immediate base, zero reviews; keep the full #507→#531→#533 stack owner-led.
- PR #569 is OPEN/DRAFT, 218 ahead / 30 behind current main, 226 files, zero reviews; owner-led reconciliation required.
- Master Plan remains 10K capacity, HAO-008 remains P3/REVIEW; issue #401 has no owner decision in latest comments. No new batch is authorized in this lane.
- The canonical 29-ID queue still matches planning PR #62 exactly; 23 drafts, 23 visuals, 23 PHP candidates, 22 current editorial passes, 18 code passes, approvals 0, published/live 0.
- Research PR #68's 14 proceed proposals and GA-B00014 in-place refresh remain preserved; refreshes and research are not new finished articles.

## Central coordination delta

- Control-center main remains `80c75e28734ce22831e93d9f431f4c15ccad0f6c`; its README still lists eight brands but only three active control-board rows. Groot's active row is still missing.
- PRs #1/#2/#3 remain merged. Existing AEO/GEO baseline from PR #2 is reused, not recreated.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. No ownership transfer or source correction is inferred.
- PR #20 remains OPEN/DRAFT on `audit/groot-100k-crosslane-20261110-1443`, 47 commits ahead / 4 behind main, 29 changed files and zero submitted reviews. This report is append-only evidence; no self-merge or approval.

## Exact next action

The Groot owner/release owner resolves the 10K/P3 vs 100K/P0 governance and queue ownership; PR #625 owner reconciles the duplicate-base fix with the dynamic stylesheet path after Actions storage diagnosis; recovery owner handles the stacked #533 recovery; independent QA remains separate. Central coordinator reviews PR #20 normally. No deployment, publication or ranking/live claim is made.


## Post-commit accounting

This report itself adds one coordination file/commit to PR #20. After the append, the verified PR comparison is **48 commits ahead / 4 behind** central main, **30 changed files**, OPEN/DRAFT, with zero submitted reviews. Central main remains `80c75e28734ce22831e93d9f431f4c15ccad0f6c`.
