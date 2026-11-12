# Coordination delta — Groot Academy PR #625 exact shared-head render

**Observed:** 2026-11-12 21:42 IST  
**Central main:** `21af139cc32a7b67aab6908c61edeb5998bd4544`  
**Source repository:** `satnamkhowal/grootacademy.com` (requested alias `satnamkhowal/gta`; same private repository ID `1375760757`)  
**Brand/domain:** Groot Academy / https://grootacademy.com/

## New source-lane evidence

Groot PR [#625](https://github.com/satnamkhowal/grootacademy.com/pull/625) proposes removing a duplicate `<base>` from the shared blog head partial while retaining root `head.php` as the single base owner.

An isolated local reproduction used six exact Git-blob-matched source files: current-main root `head.php`, `includes/site-paths.php`, current-main shared head partial, proposed PR #625 partial, its PHP render harness and its Python test.

- Current-main baseline: both render cases fail as expected in normal, `-O` and `-OO` (6 expected failures), exposing duplicate base values `/groot-preview//` + `/groot-preview/` and `//` + `/`.
- PR #625 proposal: 2/2 tests PASS in each of normal, `-O` and `-OO` (6/6 passes).
- PHP 8.4.24 syntax lint: 4/4 files PASS in each fixture.
- Python test `py_compile`: PASS.
- The test also checks canonical URL, `noindex,follow`, BlogPosting/BreadcrumbList JSON-LD, the single base and dynamic `ga_url()` stylesheet path.

Source evidence: [Groot PR #625 exact shared-head report](https://github.com/satnamkhowal/grootacademy.com/blob/content/groot-100k-controller-20261016/marketing/blog-factory/work/B0002/qa/2026-11-12-pr625-exact-shared-head-render-2142-ist.md). The source owner was notified in [PR #625 comment](https://github.com/satnamkhowal/grootacademy.com/pull/625#issuecomment-6829165424).

This is coordinator-run local exact-source evidence, not independent review, PHP 8.0 CI, full-root production render, authorized-origin HTTP/MIME, deployment or publication. PR #625 remains OPEN/DRAFT with zero independent reviews. It is 7 ahead / 4 behind current main, merge base `813a66fa`, with four changed paths. The owner must reconcile intervening main commits and confirm the workflow scope before independent review.

## Current-main and recovery delta

Current Groot main is `c57a7c3b24ca2dfc2c61aca54ae3735a0565f3bb`; the latest main commit changes only `courses/index.php`, without overlap with the recovery or shared-head paths.

- PR #507: 4 ahead / 4 behind, 22 changed paths, OPEN/DRAFT, zero independent reviews.
- PR #625: 7 ahead / 4 behind, four changed paths, OPEN/DRAFT, zero independent reviews.
- PRs #654 → #660 → #664 remain sequentially stacked Drafts; the previous current-main comparison remains valid because main has not advanced since the 20:37 IST checkpoint.
- Exact-head Actions failures remain blocked by Azure `BlobNotFound`; no blind rerun was made.

## Canonical 100K ledger and source counts

The Groot controller branch still has 29 unique canonical queue IDs, preserving the original planning PR #62 sequence and research PR #68's 14 proceed proposals plus the GA-B00014 in-place refresh.

| Controller measure | Count |
|---|---:|
| Complete original text drafts | 23 |
| Technical visuals | 23 |
| PHP integration candidates | 23 |
| Independent editorial passes | 22 |
| Independent code passes | 18 |
| Independent approvals | 0 |
| Published | 0 |
| Live verified | 0 |

No queue row, article, image, registry entry or sitemap URL was added in this delta. Ideas, research proposals, refreshes and review candidates are not completed/approved/live articles.

## Latest source-only site inventory

The latest issue #401 comment at 21:19 IST records current-main source counts:
- `blogs/_shared/blog-registry.php`: 67 unique top-level entries.
- `blogs/sitemap.xml`: 40 unique URLs (one blog index plus 39 article URLs).
- `sitemap-pages.xml`: 68 unique URLs.
- All 39 registry blog routes match the 39 sitemap article URLs; all 28 explicit root-level registry routes match `sitemap-pages.xml`.

These are source-level route reconciliation results, **not** proof of HTTP 200, production deployment, canonical/indexable status, live publication or Search Console indexation. The latest audit still leaves live publication and GSC counts unverified.

## Central governance and ownership

- Central main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; no central-main write occurred.
- Central PR #22 remains OPEN/DRAFT and has zero independent reviews. This report is a coordination-only addition to its existing isolated branch.
- Central PRs #1/#2/#3 are CLOSED/MERGED; the existing AEO/GEO baseline from PR #2 is reused.
- The central README registers eight brands but has only three active owner/status rows; Groot Academy's active row is still missing. No owner was invented or reassigned.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved; neither is assumed incorrect.

The Groot main task board still places the blog factory at P3/REVIEW. The user-authorized controller target remains 100,000/P0, while the Master-owner alignment and explicit canonical queue owner / independent release approver remain unresolved. Preserve both records; do not expand the queue or change another brand's ownership.

## Exact next actions and boundaries

1. PR #625 owner reconciles current main and confirms workflow scope; independent review required.
2. After shared-head repair is independently accepted, resume GA-B00029 PHP 8.0/full-root/schema/canonical/noindex/route/HTTP/MIME checks.
3. Keep #507 → #654 → #660 → #664 stacked and Draft pending owner-led reconciliation and independent reviews.
4. Diagnose Azure Actions storage failure before another hosted test attempt.
5. Master owner records 10K/P3 versus user-authorized 100K/P0 alignment and names one canonical queue owner plus an independent release approver.

No central-main/source-main write, owner reassignment, self-approval, self-merge, deployment, publishing, mass indexing or ranking claim occurred. This file is coordination-only.
