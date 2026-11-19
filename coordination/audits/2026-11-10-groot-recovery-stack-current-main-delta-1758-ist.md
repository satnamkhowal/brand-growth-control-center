# Groot Academy 100K — recovery stack/current-main compatibility delta

**Observed:** 10 November 2026, 17:58 IST  
**Coordination repository:** `satnamkhowal/brand-growth-control-center`  
**Source implementation repository:** `satnamkhowal/grootacademy.com`  
**Verified legacy alias:** `satnamkhowal/gta` resolves to the same repository ID `1375760757`; no separate Mango Engineers repository is involved.

## New source-repository evidence

Current Groot main is `99336e8d0b412f6e0f0bdc0464e0aec4b8fea2b5`. The latest main commit is merged PR #601, a planning-only student-publishing proposal under `docs/student-platform/`; it does not activate a webhook, production route or publishing automation and does not modify the 100K queue or shared blog layout. The preceding `a97dc074` commit only deduplicates Forsk communication-image planning rows.

### GA-B00006–GA-B00010 recovery stack

Recovery PR #533 is a stacked Draft at head `56a11b94e573f3885c415ec64fa5b9a221bc66b3`, 31 commits ahead / 28 behind current main. It must not be merged independently.

Fresh current-main checks:
- Five exact article PHP paths are absent from main.
- The five slugs have 0/5 current registry entries and 0/5 current blog-sitemap URLs.
- All five article pages exist on recovery head and remain `noindex,follow`.
- Current main and recovery head both modify `blogs/_shared/blog-layout.php` and `blogs/_shared/assets/blog.css`.

Exact shared-file blob pairs:
- Layout: main `7e19e1b4b87843d65b5aa7f1cb0fb33a5b154178`; recovery `7628f1038487fd5065a4307a89173716a13b207f`.
- CSS: main `eb19cab931b18bd2decf53ca637e0df2eea3f329`; recovery `394b75d4b445a79a258f120042ecffb6daebf4f9`.

Manual reconciliation is required. Preserve main's canonical-path TOC anchors, registry-aware related-link paths and `.ga-blog-page` CSS scoping. Port recovery's optional 1200×630 intrinsic-image handling deliberately; do not replace the modern scoped CSS with recovery's broad global selectors. Full evidence is in the Groot source repository's [recovery compatibility report](https://github.com/satnamkhowal/grootacademy.com/blob/qa/groot-100k-current-main-20261109/marketing/blog-factory/work/B0001/qa/recovery-stack-current-main-layout-css-overlap-20261110-1758-ist.md).

### GA-B00029 include closure and runtime boundary

The exact candidate's current-main include dependency closure resolves statically across 18/18 fetched source/data files: candidate, shared layout/partials, root head/header/footer, site-paths, mobile-app shell, Diwali offer, batch-calendar embed/catalog, course catalog/data, optional legacy aliases and both course-data JSON files.

PHP 8.4.24 and Chromium are installed in the execution container, but GitHub/Groot DNS and outbound TCP 443 are unavailable. Thus this run did not execute the exact full-root include chain or production HTTP/MIME checks. The 18/18 result is static dependency-closure evidence only; existing isolated 9/9 render and exact-candidate lint are not upgraded to a full-root runtime PASS.

## Current ownership and review state

- Groot implementation PR #569: Draft, head `e2ef553f818bef7c7e45a5f581a8b9680d2b8449`, 146 commits, 210 changed files, 0 submitted reviews and 0 review threads. Source changes remain in the Groot repository.
- Central audit PR #20: Draft on `audit/groot-100k-crosslane-20261110-1443`; coordination-only.
- Central main remains `f76c20abf6c1ea6c45de073c5acbcd936333098c`. Compare from pre-run `31af61b9` is 2 commits ahead and 0 changed files; the transient add/delete audit-file history remains net-zero in the current tree.
- Central PR #1/#2/#3 are merged. The existing all-brand AEO/GEO baseline from PR #2 is reused, not recreated.
- Central README lists eight brands, but its active board still has no Groot Academy row. HAO-008 remains P3/REVIEW on Groot current main; the user controller remains P0. No priority override was made.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website mapping remains unresolved. No assumption was made that either repository is wrong.

## Ownership and next actions

1. Groot recovery owner rebases the full #533 stack and manually reconciles the two shared files, then reruns exact-head PHP/render/browser/inventory and independent editorial/release review.
2. Groot owner obtains an authorized PHP/network runner for GA-B00029 full-root rendering and four endpoint HTTP/MIME checks.
3. Repository Actions administrator diagnoses the repeated PR #569 pre-step failures; no blind retry is recommended.
4. Master owner resolves HAO-008 P3 versus controller P0 and the GA-B00005/next-batch disposition before new 100K production.
5. Central owner may add Groot's active control-board row through the existing reviewed process; this audit does not edit central main.

No worker-owned recovery files, other-brand source files, canonical queue, priority, deployment or publication were changed. No merge, approval, release or indexing is claimed.
