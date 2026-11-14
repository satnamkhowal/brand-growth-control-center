# Groot Academy 100K Factory — exact Git-blob SVG/CSS regression rerun

**Observed:** 12 November 2026, 13:38 IST  
**Source:** `satnamkhowal/grootacademy.com` (requested alias `satnamkhowal/gta` resolves to this repository)  
**Source PR:** [#664](https://github.com/satnamkhowal/grootacademy.com/pull/664)  
**Source head:** `df467e92b3e595b6f6b771b92b1d17234f90a652`

## New executable evidence

Fetched the two exact committed Git blobs from PR #664 and materialized them in an isolated `/tmp/groot-qa/tests` fixture:

| File | GitHub blob SHA | Local `git hash-object` | Parity |
|---|---|---|---|
| `tests/groot-recovery-five-diagram-check.py` | `f0e471d75f24230cd2dc312c08c49faf79371c83` | `f0e471d75f24230cd2dc312c08c49faf79371c83` | PASS |
| `tests/test-groot-recovery-svg-css-safety.py` | `4c8a0f9c18b29faf71666f4d4812f1d33de13d71` | `4c8a0f9c18b29faf71666f4d4812f1d33de13d71` | PASS |

- Python 3.13.5 `py_compile`: PASS.
- Exact committed regression module: **28/28 PASS** in normal mode.
- Exact committed regression module: **28/28 PASS** with `-O`.
- Exact committed regression module: **28/28 PASS** with `-OO`.
- Total: **84 test executions, all PASS**.

This closes the previous coordinator-equivalent-helper-only gap for this 28-case CSS/SVG href test module. It is still an isolated two-file fixture, not a complete repository checkout or complete recovery workflow.

## Current source-stack comparison

Current Groot main is `b011929add5297a9e0295af385ec8a1331aec512`, confirmed by the 13:26 IST owner checkpoint in [issue #401](https://github.com/satnamkhowal/grootacademy.com/issues/401).

- PR #507 head `68db39f9862ff66d36fc114032ec5b6e1f0f4dad`: **3 ahead / 4 behind**, diverged from current main; merge base `f048dedf22da86e93b5b505cc1ebc84884f3a5c8`. The recovery owner must reconcile before independent stack review.
- PR #664 head `df467e92b3e595b6f6b771b92b1d17234f90a652`: **12 ahead / 0 behind** immediate parent #660; OPEN/DRAFT with zero independent reviews.
- Recovery sequence remains #507 → #654 → #660 → #664. No branch was rebased or merged in this audit.

## Queue and governance

- Canonical queue blob: `4e087f8cda5479ff9d1124f24ff427a0dbf2b4ad`.
- **29/29 IDs preserved in original PR #62 order**; no missing or extra IDs.
- Current status counts: MERGE 3, REFRESH 2, IDEA 1, PUBLISH_PR 5, TECH_QA 17, CONTENT_QA 1.
- Research PR #68 remains merged with 14 proceed proposals and GA-B00014 as an in-place refresh; none of these proposals is counted as a finished article.
- Main Master Plan remains **10,000 possible IDs** and HAO-008 **P3/REVIEW**. The user-authorized controller target is **100,000/P0**; issue #401 identifies 100,000 as M4 and 1,000,000 as conditional M5. The latest 13:26 owner checkpoint does not explicitly reconcile capacity/priority or name one canonical queue/release owner. New batches remain HOLD; existing repairs continue.
- Central main README still lists eight brands but only three active control-board rows; Groot's active row is missing. Central PRs #1/#2/#3 are closed/merged; reuse the existing AEO/GEO PR #2 baseline. Jaipur Engineers `je2` social versus `jaipur-engieneers` candidate website mapping remains unresolved.

## Remaining release gates and limitations

- GitHub Actions/Azure `BlobNotFound` pre-step failures remain unresolved; no CI PASS is inferred.
- The two exact blobs were executed locally, but no complete Git checkout was available because `github.com` DNS resolution failed.
- Full five-page SVG/article integration, PHP 8.0, full-root rendering, schema/canonical/noindex, registry/sitemap transition, browser/CLS/keyboard/AT, HTTP/MIME and independent review remain pending.
- No article, image, registry entry, sitemap URL, source main, queue, deployment or publication was changed.
- No self-approval, self-merge, deployment, publication or mass indexing occurred.

## Exact next action

Restore authorized GitHub checkout/DNS access and obtain Actions/storage administrator diagnosis. Then execute the exact-head #664 workflow and the remaining full-root/browser/HTTP gates. Have the #507 owner reconcile its 3-ahead/4-behind divergence against current main before independent review of the complete stack. Preserve the 29-ID queue and keep new article batches on hold until the Master owner resolves 10K/P3 versus 100K/P0 and names one canonical queue/release owner.
