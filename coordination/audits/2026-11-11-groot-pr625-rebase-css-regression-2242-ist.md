# Groot Academy 100K — PR #625 rebase and shared-head regression delta

Date: 11 November 2026, 22:42 IST  
Central repository: `satnamkhowal/brand-growth-control-center`  
Source owner/repository: Groot Academy / `satnamkhowal/grootacademy.com` (historical `satnamkhowal/gta` alias)

## New source-repository evidence

The existing Groot source PR [#625](https://github.com/satnamkhowal/grootacademy.com/pull/625) was reconciled onto current Groot main `071ab8a5ed38864fc2c60828d01d6dcf328f0941` with merge commit [`dcf8792`](https://github.com/satnamkhowal/grootacademy.com/commit/dcf8792751771daa8b985aa274168c9e58970554). The previous PR head is the first parent and current main is the second parent. GitHub compare now reports 6 ahead / 0 behind, merge base exactly current main, and four changed files.

The branch removes the duplicate base element from the shared blog partial, retains root `head.php` as the only base owner, and preserves the merged PR #639 dynamic stylesheet path `ga_url('blogs/_shared/assets/blog.css')`. The local-preview and production regression cases now assert the exact CSS URL as well as a single expected base, canonical, `noindex,follow`, BlogPosting and BreadcrumbList.

Local validation on PHP 8.4.24 / Python 3.13.5:
- PHP lint 2/2 PASS (shared partial and PHP harness).
- Python compilation PASS.
- Render regression 2/2 PASS (local subdirectory preview and production-host fixture).
- Workflow YAML parse PASS (19 path filters, 7 steps).
- Git blob hashes match GitHub for all four changed files.

Scope limitation: this run used the exact blob-matched partial, harness, Python test and workflow plus a minimal root-head base-line/site-path fixture. It is not a full repository checkout, PHP 8.0 CI, browser or production HTTP/MIME test. The merge commit uses `[skip ci]` because earlier Actions jobs exposed `steps: null` and Azure Storage `BlobNotFound`; no rerun was triggered. PR #625 remains OPEN/DRAFT, with zero submitted reviews and zero review threads. Independent review and administrator diagnosis remain required. Groot main and production were not changed.

## 100K controller status — no count change

The canonical Groot controller queue remains 29 unique IDs in exact GA-B00001–GA-B00029 order, matching planning PR #62. Counts remain 23 complete original drafts, 23 technical visuals, 23 PHP candidates, 22 current-version independent editorial passes, 18 independent code passes, 0 independent approvals, 0 published and 0 live verified. GA-B00006–GA-B00010 recovery remains a separate stacked owner-led task; no missing route is counted restored. No new article, image, ID or status was added.

New source checkpoint:
- [Detailed Groot QA report](https://github.com/satnamkhowal/grootacademy.com/blob/content/groot-100k-controller-20261016/marketing/blog-factory/work/B0002/qa/shared-blog-head-base-path-rebase-20261111-2242-ist.md)
- Controller branch README/CONTROLLER checkpoint commits: [`c16fd34`](https://github.com/satnamkhowal/grootacademy.com/commit/c16fd3472ba10ac8c3395adfe8866a1b2f2f384b), [`aa20c31`](https://github.com/satnamkhowal/grootacademy.com/commit/aa20c31c313f34ddb9216d4b6513d2d5e9033b4f)

## Central coordination delta

Central main remains `80c75e28734ce22831e93d9f431f4c15ccad0f6c`; this report is added only to the existing audit branch for PR #20. PR #1/#2/#3 remain merged and the existing AEO/GEO baseline from #2 is reused. The central README still lists eight brands but only three active control-board owner/status rows; Groot's active row is missing. Jaipur Engineers `je2` social versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved; neither is assumed incorrect. No central-main write, source ownership transfer or other brand source change occurred.

## Exact next actions

1. Obtain independent review of Groot PR #625; do not self-approve or self-merge.
2. Actions/storage administrator diagnoses Azure `BlobNotFound`; then run exact-head CI.
3. Recovery owner reconciles #507 → #531 → #533 and revalidates GA-B00006–10.
4. Run network-enabled full-root PHP/schema/route and authorized-origin HTTP/MIME gates for GA-B00029.
5. Master owner records the 10K/P3 versus 100K/P0 alignment and one canonical queue/release owner before any new article batch.
6. Continue independent GA-B00016 and GA-B00022 runtime/accessibility review.

Central PR #20 remains a draft coordination review. No central merge, source deployment, publication, indexing or live-ranking claim is made.


## 23:41 IST — complete historical recovery dependency-chain delta

A fresh PR metadata/patch review found that the previous shorthand `#507 → #531 → #533` omitted four required stacked dependencies. The verified chain is **#507 → #511 → #513 → #517 → #520 → #531 → #533**; all seven remain OPEN/DRAFT:

- #507 restores 22 exact historical article/asset/lab files for GA-B00006–GA-B00010.
- #511 adds opt-in intrinsic featured-image dimensions in shared layout/CSS.
- #513 adds PHP/HTTP/asset/code release checks.
- #517 adds responsive 320/390/1440 browser/CLS checks.
- #520 adds effective registry/sitemap draft-vs-release inventory and negative tests.
- #531 fixes the SQL lesson's mobile table readability and extends browser assertions.
- #533 changes the five unreleased articles to `noindex,follow` and adds negative robots-state tests.

Current Groot main is `071ab8a5ed38864fc2c60828d01d6dcf328f0941`. GitHub compare shows root #507 is **1 ahead / 56 behind** current main from merge base `d9eba9445ac5d58652d9b36f026e3b6efb5e2bea`; cumulative #533 is **31 ahead / 56 behind**, with 31 changed paths including shared `blogs/_shared/blog-layout.php` and `blogs/_shared/assets/blog.css`. #533's direct eight-file patch is not the whole stack. Owner-led recovery must rebase root #507 onto current main and replay each child in dependency order, resolving shared files without dropping intrinsic-image or SQL mobile-table fixes. No child merge is safe independently.

No article, image, PHP route, registry, sitemap, redirect, production file, queue ID/status, approval or publication changed. The five historical routes remain absent from current-main source at the pinned 071ab8a5 check; live HTTP/indexation remains unverified. The 100K controller remains at 23 complete drafts, 23 visuals, 23 PHP candidates, 22 independent editorial passes, 18 independent code passes, 0 independent approvals, 0 published and 0 live verified. Master HAO-008 P3/REVIEW versus authorized 100K/P0 is still unresolved; no new batch.

Central coordination remains unchanged on main: README lists eight brands but three active owner/status rows, with Groot missing; PR #1/#2/#3 merged and AEO/GEO #2 reused; Jaipur Engineers `je2` social vs `jaipur-engieneers` candidate website/deployed-origin mapping unresolved. This is a coordination-only delta on the existing Draft PR #20 branch; source implementation remains in the Groot repository.
