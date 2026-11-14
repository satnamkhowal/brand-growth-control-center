# Groot Academy 100K — run 14 Main and recovery-lineage coordination delta

**Observed:** 2026-11-14 15:44 IST  
**Source owner/repository:** Groot Academy — `satnamkhowal/grootacademy.com` (requested alias `satnamkhowal/gta`, same repository ID 1375760757).  
**This repository is coordination-only:** no Groot source implementation, central Main, other-brand files, owner assignment, publication or deployment changed.

## New source evidence

Groot source Main advanced from `4057ca4ab5cfc79f13ddfda1c0df2a945460a6ba` to `c2603620fe28f0ff26af5967241d3b62b7c64e69`. The one-commit diff is limited to homepage/course search normalization in:
- `assets/js/groot-home-path-finder.js`
- `courses/index.php`
- `index.php`

No blog article, shared blog layout/head, registry, sitemap, or controller/queue path changed.

Exact current-source inventory remains:
- Registry: 77 unique `slug` entries.
- Blog sitemap: 50 locs (1 hub + 49 article routes).
- Page sitemap: 68 locs, of which 28 match root-level registry article routes.
- Registry partition: 49 + 28 = 77/77, zero missing and zero overlap.
- Root sitemap index: four locs.

These are source counts only, not live deployment/indexation evidence.

## Recovery stack — correction from exact head-to-head compares

All source PRs #507/#625/#654/#660/#664/#713 remain OPEN/DRAFT with zero independent reviews.

Fresh Main comparisons: #507 4/34 (22 original files), #625 7/34 (four intended files), #654 9/34, #660 19/34, #664 32/34, #713 12/8.

Exact commit graph comparisons now show:
- #507 → #654: 5 ahead / 0 behind, exactly two shared layout/CSS paths.
- #654 → #660: 10 ahead / 0 behind, exactly seven intended diagram/article/test paths.
- #660 → #664: 13 ahead / 0 behind, exactly six intended QA workflow/test paths.

This supersedes the prior run-13 concern that the stacked child branches still included inherited unrelated paths. The actual commit graph is linear and scoped. Some PR body/base metadata remains stale; owners should refresh the descriptions before review. No worker-owned branch was rewritten.

#625 and #713 retain three previously verified identical shared files but separate unique workflows. Keep both workflows and integrate shared files once. Last observed Actions jobs still fail before steps with Azure BlobNotFound 404; zero hosted assertions. Administrator diagnosis required; no retry.

## Controller and governance

- Canonical queue remains 29/29 original ordered IDs, blob `c12a915e06c8100a350b21338311651df0f35094`.
- PR #68's 14 proceed proposals and GA-B00014 refresh are not completed articles.
- Draft packages / visuals / PHP candidates: 23 / 23 / 23.
- Independent component PASS: editorial 22, code 18, visual 23.
- Fully approved / published / live verified: 0 / 0 / 0.
- GA-B00006 still requires independent full release review and hosted PHP 8.0/full-root/schema/route/browser/AT/HTTP/MIME checks.
- GA-B00029 remains TECH_QA/noindex.

Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`. PRs #1/#2/#3 remain merged and AEO/GEO PR #2 is reused. Central PR #22 remains Draft and unreviewed. Eight brands/three active owner rows remain on the README; Groot's dedicated row is missing. Jaipur Engineers `je2` social versus `jaipur-engieneers` website/deployed-origin mapping remains unresolved. Master-owner 100K/P0 alignment, one canonical queue owner and one independent release approver remain pending.

## Exact next action

Owner-refresh PR descriptions/base metadata to match the verified #507→#654→#660→#664 commit graph; preserve #625/#713 unique workflows and shared-file single integration; obtain administrator diagnosis of Azure Actions storage; then independent GA-B00006 and hosted release gates. Keep new IDs HOLD. No self-approval, self-merge, deployment, publication or indexing.
