# Groot GA-B00029 exact-source QA and current-main coordination delta — 12 November 2026, 17:41 IST

## Source repository identity

The requested `satnamkhowal/gta` URL permanently redirects to GitHub repository ID `1375760757`, currently named `satnamkhowal/grootacademy.com` (private). The requested `content/groot-100k-controller-20261016` branch and factory files were read there. No Mango Engineers repository was accessed or changed.

## New bounded QA evidence

GA-B00029's four Python source files were fetched from the controller branch and their Git blob hashes matched exactly:
- `parameterized_queries.py`: `132c9b1337988edd5221b85718b9e7846088eb9b`
- `test_parameterized_queries.py`: `52777ba739587ea89d8e94271fba51f19466b4a7`
- `test_verifier.py`: `0a105a3e8aa1840ab87204fbcc915ed93e835795`
- `verify_draft.py`: `e5320c9750e99570fc82ce92a95a52d3ca3e770d`

Python 3.13.5 results: 6/6 query tests in normal/`-O`/`-OO` (18 executions), 4/4 adversarial verifier regressions, four-file `py_compile`, and the executable SQLite example all pass. Example output matched the expected Ada and O'Reilly rows; the injection-shaped value returned no rows and all three fixture rows remained.

A PHP 8.4.24 syntax check also passed on a local reconstruction of the fetched GA-B00029 candidate. That reconstruction was not byte-hash matched to the GitHub candidate blob; this is supplemental syntax evidence only, not exact-source CI, PHP 8.0 or full-root rendering. The 25-check draft verifier was run in all three Python modes against fetched package text; non-Python article/metadata/SVG copies were not blob-hash matched in this run.

Detailed source-side checkpoint: [GA-B00029 exact Python re-execution and current-main delta](https://github.com/satnamkhowal/grootacademy.com/blob/content/groot-100k-controller-20261016/marketing/blog-factory/work/B0002/qa/2026-11-12-ga29-exact-python-reexecution-and-main-delta-1741-ist.md).

## Current-main and recovery-stack delta

Groot main advanced to `548f8a4ba6a42e1c49d253f773b1ea1aef0349d4`. The only changed path in the new commit is `courses/index.php` (technology spelling normalization in catalogue search); it does not overlap the recovered blog files or shared blog-head files.

Fresh comparisons against current main:
- #507: 4 ahead / 1 behind, merge base `813a66fa`.
- #625: 7 ahead / 1 behind, merge base `813a66fa`.
- #654: 9 ahead / 1 behind, stacked.
- #660: 19 ahead / 1 behind, stacked.
- #664: 32 ahead / 1 behind, stacked.

All five are OPEN/DRAFT with zero independent reviews. GitHub reports mergeable state unknown for #507/#625 and unstable for #654/#660/#664. The stacked child comparisons are cumulative against main, not direct-parent counts. The 16:36 zero-behind checkpoint was accurate against main then; this one-commit course-only delta makes the branches one behind current main.

Source owners received updated handoffs: [#507 comment 6823540998](https://github.com/satnamkhowal/grootacademy.com/pull/507#issuecomment-6823540998) and [#625 comment 6823541785](https://github.com/satnamkhowal/grootacademy.com/pull/625#issuecomment-6823541785). No branch was changed in this coordination report.

Latest exact-head #664 Actions run `43207445829` failed before any step. Azure `BlobNotFound` 404 remains an administrator blocker; zero assertions ran. The current main shared blog partial and root `head.php` both emit a `<base>`; #625's independent review remains necessary.

## Canonical queue and accounting

The 29 IDs remain in exact PR #62 order; queue SHA remains `4e087f8cda5479ff9d1124f24ff427a0dbf2b4ad`. Research PR #68's 14 proceed proposals and GA-B00014 in-place refresh remain preserved.

Unchanged controller counts: 23 complete text drafts, 23 technical visuals, 23 PHP candidates, 22 independent editorial PASS, 18 independent code PASS, 0 independent approvals, 0 published, 0 live verified. GA-B00029 is already included in these 23 drafts; the new run adds QA evidence, not a new article or asset.

## Master and central governance

The latest issue #401 source audit comment (17:28 IST, `6823183149`) reports 66 registry entries, 39 blog-sitemap URLs (38 article URLs), 28 registry-only keys, and all 38 sitemap article slugs matching registry keys. Live publication and Search Console indexation remain UNVERIFIED. It does not record the required Master-owner decision on 10K planning capacity / HAO-008 P3-REVIEW versus the user-authorized 100K/P0 controller, nor one canonical queue owner and release approver. New IDs/batches remain HOLD.

Central main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; current README blob is `b93187c353f8112a57fffab4b383e64236976394`. It lists eight brands but only three active control-board rows; Groot's active row is missing. Central PRs #1/#2/#3 are merged; reuse the existing AEO/GEO baseline from #2. Jaipur Engineers `je2` social versus `jaipur-engieneers` candidate website mapping remains unresolved. Existing central PRs #18/#20 remain Draft; their runtime and News Factory dedupe records were read and reused, not duplicated.

Central PR #22 remains OPEN/DRAFT on `audit/groot-ga22-browser-delta-20261112-0350`, previously 31 ahead / 0 behind with zero independent reviews. This report is coordination-only. No central main write, other-brand source change, ownership reassignment, self-approval, merge, deployment, publication or indexing occurred.
