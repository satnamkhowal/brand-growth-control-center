# Groot Academy — 100K run 13 current-main and registry partition delta

**Observed:** 2026-11-14 14:43 IST  
**Source implementation:** `satnamkhowal/grootacademy.com` (requested alias `satnamkhowal/gta`, same repository ID 1375760757)  
**Coordination-only:** this report changes no source implementation, central Main, other-brand files, owner assignments, publication state, or indexing.

## Current source Main

Groot Main is `4057ca4ab5cfc79f13ddfda1c0df2a945460a6ba` (“Normalize homepage course search terms”). Since `7f007cbc`, the commit changes only `assets/js/groot-home-path-finder.js` and the script cache key in `index.php`. No blog article, shared layout/head, registry, sitemap, or 100K controller path changed.

## Exact registry/sitemap partition

Fresh reads from the source Main:

- Registry `blogs/_shared/blog-registry.php`: 77 unique top-level slugs, blob `2ae5446dabb19e84d89ba3b8a41c3a325580e818`.
- Blog sitemap `blogs/sitemap.xml`: 50 URLs = one blog hub + 49 article routes, blob `5f6a6d8f7e2841f53c6dcfc5f62f443ebb9147e6`.
- Page sitemap `sitemap-pages.xml`: 68 URLs, including 28 root-level registry article routes, blob `212b3182276da25f7cdf00ae7f6d814564558095`.
- Root sitemap index: four locations, blob `a0994f29c3f192fda8f855336a43d4734d1bf08b`.

The route partition is **49 + 28 = 77/77**, exactly once, with zero missing and zero overlap. This supersedes the earlier 14:24 estimate of 74 keys, which was not reproduced by the exact top-level source parse. These are source counts only; live deployment, HTTP and Search Console remain unverified.

The separate historical URL-set change remains unresolved. Do not bulk restore, delete, redirect or edit registry/sitemaps from this count alone.

## Recovery and release state

Fresh compare to Main `4057ca4`:

- #507: 1 ahead / 111 behind; 22 original recovery files.
- #625: 7 ahead / 33 behind; four intended files.
- #654: 9 ahead / 33 behind; inherited recovery paths remain.
- #660: 19 ahead / 33 behind; inherited recovery paths remain.
- #664: 32 ahead / 33 behind; inherited recovery paths remain.
- #713: 12 ahead / 7 behind; four intended files.

All six remain OPEN/DRAFT; no independent review was present in the last inspected comments. The recorded base SHAs of #654/#660/#664 still do not equal the immediate parent heads #507/#654/#660. Owners received fresh exact comparisons and scope handoffs on all six PRs. No worker-owned branch was edited.

#625 and #713 still contain three identical shared PHP/Python blobs and distinct unique workflows. Preserve both workflows and integrate the shared implementation once.

The last inspected exact-head Actions jobs still fail before steps with Azure `BlobNotFound` HTTP 404; zero hosted assertions ran. Administrator diagnosis remains necessary; no blind retry.

## Controller ledger

- Canonical queue: 29 original ordered IDs, unchanged at blob `c12a915e06c8100a350b21338311651df0f35094`.
- Research PR #68: 14 proceed proposals plus GA-B00014 refresh; not completed articles.
- Complete draft packages / visuals / PHP candidates: 23 / 23 / 23.
- Independent editorial/code/visual component PASS: 22 / 18 / 23.
- Fully approved / published / live verified: 0 / 0 / 0.
- GA-B00006 still needs independent full release review and hosted PHP 8.0/full-root/schema/route/browser/accessibility/HTTP/MIME gates.
- GA-B00029 remains TECH_QA/noindex.

## Central coordination

Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; the current README blob is `b93187c353f8112a57fffab4b383e64236976394`. PRs #1/#2/#3 remain merged; the AEO/GEO PR #2 baseline is reused. Central PR #22 remains OPEN/DRAFT with no independent review in the last inspected comments.

The central README still lists eight brands but only three active owner/status rows; Groot Academy's dedicated row is missing. Jaipur Engineers `je2` social versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. Master-owner alignment of the user-authorized 100K/P0 target, one canonical queue owner, and one independent release approver remains pending. The existing 100K task stays evidence-gated; no priority or owner was changed here.

## Exact next action

1. Source owners refresh #507/#625/#713 against Main `4057ca4`, preserving the distinct workflows and integrating shared files once.
2. Owners reconcile #654 → #660 → #664 to exact immediate-parent heads and intended-only diffs.
3. Actions/storage administrator diagnoses `BlobNotFound` before any retry.
4. Obtain independent GA-B00006 full release review and hosted PHP 8.0/full-root/schema/route/browser/accessibility/HTTP/MIME evidence.
5. Keep GA-B00029 noindex until release approval; keep new IDs on HOLD until Master-owner governance decisions are recorded.

No self-approval, self-merge, deployment, publication, or mass indexing.
