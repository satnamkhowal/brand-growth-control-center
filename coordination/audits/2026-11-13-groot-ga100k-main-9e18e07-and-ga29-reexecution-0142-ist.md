# Groot Academy 100K — current-main 9e18e07 and GA-B00029 exact execution delta

**Observed:** 2026-11-13 01:42 IST  
**Source implementation repository:** `satnamkhowal/grootacademy.com` (requested alias `satnamkhowal/gta` redirects here)  
**Brand/domain:** Groot Academy / grootacademy.com  
**Source controller branch:** `content/groot-100k-controller-20261016`  
**Central repository:** `satnamkhowal/brand-growth-control-center`  
**Central main:** `21af139cc32a7b67aab6908c61edeb5998bd4544`  
**Central audit PR #22 branch before this append:** `4a3b172e1747b6d0b410e9df0eee43873ea32c21`

## Source-side implementation evidence (kept in Groot repository)

- Re-executed GA-B00029 from exact GitHub source blobs; all seven files matched their Git blob SHA-1 values.
- Python parameter-binding suite: 6/6 PASS in normal, `-O`, and `-OO` modes.
- Example script exit 0: Ada and O'Reilly matched; injection-shaped value returned no row; three fixture rows remained.
- Draft verifier: 25/25 PASS in normal, `-O`, and `-OO`; article length 1,354 words.
- Verifier regression suite: 4/4 PASS.
- This is coordinator-run exact-source execution, not a new independent QA approval or production database/security certification.
- Source evidence and checkpoint: [Groot report](https://github.com/satnamkhowal/grootacademy.com/blob/content/groot-100k-controller-20261016/marketing/blog-factory/work/B0002/qa/2026-11-13-ga29-exact-package-reexecution-main-9e18e07-0142-ist.md), [source report commit](https://github.com/satnamkhowal/grootacademy.com/commit/1418d5ce913877bd1554970861c18ceb504f8b8a), [controller commit](https://github.com/satnamkhowal/grootacademy.com/commit/b20084a4ce784855c04f3f84d70fa3e7fc25666b).

## New current-main evidence

Owner-merged Groot PR [#693](https://github.com/satnamkhowal/grootacademy.com/pull/693) advanced source main to `9e18e07f29e61f9c2e36f5d39dbc663d72d3e5e9`. It adds the Spring Boot testing roadmap, registry and sitemap entries, a contextual link from the existing booking API guide, and a work log.

Exact current-main counts:

- `blogs/_shared/blog-registry.php`: 68 unique top-level slug entries (blob `a07129fa3ef4587d23d06530bc3166ad8f00c562`).
- `blogs/sitemap.xml`: 41 unique URLs = 1 blog index + 40 article URLs (blob `60662a5a556da00b1c9b7ac44dd5703a7400314c`); no duplicate URLs.
- New article slug is present in both. Its source has no runnable `<pre>`/`<code>` block and no featured image. Issue #401's latest checkpoint asks for a small reproducible JUnit example or clearer conceptual-roadmap positioning.
- PR #693 has zero review submissions and its merge commit has zero combined status contexts; issue #401 records no PR-triggered workflow run. Deployment/live status is not verified. Do not count this owner-lane article as a 100K controller draft or a live publication.

## Recovery stack: newly verified stale shared blobs

All five recovery PRs remain OPEN/DRAFT with zero independent reviews. Fresh comparisons against main `9e18e07`:

| PR | Ahead | Behind |
|---|---:|---:|
| #507 | 4 | 5 |
| #625 | 7 | 5 |
| #654 | 9 | 5 |
| #660 | 19 | 5 |
| #664 | 32 | 5 |

All five branch heads currently carry the same stale blobs for the three paths changed by PR #693:

| Path | Recovery-head blob | Main 9e18e07 blob |
|---|---|---|
| `blogs/_shared/blog-registry.php` | `3b8f34e14cefbfdab070d79b7b9067744b8462bc` | `a07129fa3ef4587d23d06530bc3166ad8f00c562` |
| `blogs/sitemap.xml` | `b7e8b48c9364903154eab1d82fb6e06f28b55218` | `60662a5a556da00b1c9b7ac44dd5703a7400314c` |
| `blogs/spring-boot-rest-api-project-roadmap-2026-jaipur/index.php` | `3a954f1ba36c65e1473c8796f5249ac3fcb21991` | `7ed76c887b260c6d7208b02a717e06703675814b` |

Owners/integrator must reconcile these exact current-main changes into the recovery stack before independent review. No source branch was edited or merged by this audit.

## Governance delta

- Current main `docs/ai-ops/MASTER_TASK_BOARD.md` blob `a1bc5aab018f72675e58e09e1e6cbfec421ddcc7`: HAO-008 remains **P3 / REVIEW** and instructs the blog factory to reconcile competing framework/B0001 PRs before new content.
- Current main `marketing/blog-factory/MASTER-PLAN.md` blob `e1ce95a0a926b5371abff735bd672d8aeb3f1a9c`: 10,000 possible IDs is a capacity envelope, not a publication quota.
- Issue #401 describes the 100K user target as M4 and one million as an aspirational ceiling, but no explicit Master-owner resolution aligns HAO-008/P3 and the authorized 100K/P0 controller or names one canonical queue owner and one independent release approver.
- Canonical controller queue remains 29 IDs in exact PR #62 order; PR #68's 14 research proposals and GA-B00014 refresh are not finished articles.
- Controller-scope totals remain 23 complete drafts, 23 visuals and 23 PHP candidates; independent editorial/code/visual PASS 22/18/23; approved 0, published 0, live verified 0.
- Controller branch still has no common ancestor with current source main; it remains isolated.

## Central ownership and mapping

- Central main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; this report is on the existing isolated PR #22 branch only.
- Central README blob `b93187c353f8112a57fffab4b383e64236976394` lists eight brands but only three active owner/status rows; Groot Academy's active row is missing.
- Central PRs #1/#2/#3 are merged. Reuse the existing AEO/GEO PR #2 baseline; do not recreate it.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved; no ownership or correctness inference is made.
- Central PR #22 remains OPEN/DRAFT with zero independent review submissions. No central-main write, other-brand source change, owner reassignment, source merge, deployment, publication or indexing occurred.

## Exact next action

1. Groot owners/integrator reconcile #507/#625/#654/#660/#664 to main `9e18e07`, preserving PR #693's registry, sitemap and booking-guide updates; then obtain independent reviews.
2. Continue GA-B00029 PHP 8.0/full-root/shared-schema/route/HTTP/MIME and independent review gates; keep noindex and publication hold.
3. Continue GA-B00016 independent corrected-copy/browser/zoom/assistive-technology review and GA-B00022 production browser/AT review.
4. Obtain Azure Actions `BlobNotFound` administrator diagnosis before retrying workflows.
5. Master owner records the 100K/P0 alignment, one canonical queue owner and independent release approver before any new batch.

No new article/image, source PR, approval, deployment or publication was created by this central audit.


## Supplemental correction — recovery net-diff vs inherited tree blobs (13 November 2026, 02:39 IST)

Source-side evidence is recorded in Groot controller commit https://github.com/satnamkhowal/grootacademy.com/commit/4b175db880aae0bd7e0cb90e71bcefd552551cad on the isolated content/groot-100k-controller-20261016 branch. The repository alias satnamkhowal/gta resolves to the same GitHub repository ID as satnamkhowal/grootacademy.com.

A fresh three-way comparison used current main 9e18e07f29e61f9c2e36f5d39dbc663d72d3e5e9, shared merge base 813a66fa986a0725c594ecd3780a2be03f5114b9, and the exact current heads of #507/#625/#654/#660/#664.

| PR | Ahead / behind | Net paths | Main changed-path overlap | Review submissions |
|---|---:|---:|---:|---:|
| #507 | 4 / 5 | 22 | 0 | 0 |
| #625 | 7 / 5 | 4 | 0 | 0 |
| #654 | 9 / 5 | 23 | 0 | 0 |
| #660 | 19 / 5 | 25 | 0 | 0 |
| #664 | 32 / 5 | 30 | 0 | 0 |

Main changed eight paths since the shared merge base, including the registry, blog sitemap, Spring Boot REST roadmap, new Spring Boot Testing roadmap, Spring Security roadmap, courses catalogue and two work logs. None appears in any of the five PR net diffs.

**Correction to the preceding report section:** the older registry/sitemap/REST-roadmap blob SHAs visible in the #507 inherited branch tree are not PR-authored changes. Those paths are absent from #507's 22-path net diff and from every other recovery PR net diff. Do not require manual porting solely because inherited tree blob IDs differ. Owner-controlled branch refresh may still be useful for exact-head CI/review freshness; no source branch was changed by this audit.

Current main source inventory remains 68 unique registry slugs and 41 blog-sitemap URLs (one index + 40 articles, zero duplicates). PR #693 is owner-merged; its deployment/live status is unverified. This source count is not a verified live-published count.

Governance delta remains unchanged: central main 21af139cc32a7b67aab6908c61edeb5998bd4544; eight brands listed, three active owner/status rows, Groot row missing; PRs #1/#2/#3 merged with the existing AEO/GEO PR #2 baseline reused; Jaipur Engineers je2 social vs jaipur-engieneers candidate website mapping unresolved. Latest issue #401 checkpoint at 02:21 IST adds no explicit 10K/P3 vs 100K/P0 alignment, canonical queue owner or independent release approver. PR #22 remains OPEN/DRAFT for independent review.

No source merge, approval, deployment, publication, indexing, owner reassignment or central-main write occurred.


## Supplemental delta — current-main registry route reconciliation (13 November 2026, 03:35 IST)

Groot source-side evidence is committed on the isolated controller branch in [report](https://github.com/satnamkhowal/grootacademy.com/blob/content/groot-100k-controller-20261016/marketing/blog-factory/work/B0002/qa/2026-11-13-main-registry-route-reconciliation-0335-ist.md).

- The requested `satnamkhowal/gta` alias resolves to the canonical `satnamkhowal/grootacademy.com` repository; no Mango Engineers source was used.
- Current main remains `9e18e07`. Exact source blobs: registry `a07129fa`, blog sitemap `60662a5a`, pages sitemap `212b3182`, blog index `bcb93b31`.
- Correct top-level registry count is **68**, not 65 as stated in issue #401's 02:21 IST checkpoint. Route mapping is **40 blog routes** (13 explicit + 27 fallback) and **28 root-level routes**. All 40 blog routes match the 40 article sitemap URLs; all 28 root routes match `sitemap-pages.xml`. Duplicate keys/URLs and route mismatches: 0.
- The discrepancy is source-count interpretation only; it does not establish HTTP status, canonical/robots on the deployed origin, live publication or indexation.
- Planning/current controller queue blobs were compared directly: all 29 IDs remain unique and in exact order. Controller totals remain 23 complete drafts/visuals/PHP candidates; independent approvals, published and live-verified counts remain 0.
- Central main remains `21af139`; PRs #1/#2/#3 remain merged and existing AEO/GEO PR #2 is reused. PR #22 remains OPEN/DRAFT with zero independent reviews. Central README still lists eight brands but only three active owner/status rows; Groot's row is missing. Jaipur Engineers `je2` social vs `jaipur-engieneers` candidate website mapping remains unresolved.

No central-main write, other-brand source change, merge, approval, deployment, publication or indexing occurred. Exact next action remains independent GA-B00029/runtime release gates and Master-owner 100K/P0 + queue/release ownership alignment.
