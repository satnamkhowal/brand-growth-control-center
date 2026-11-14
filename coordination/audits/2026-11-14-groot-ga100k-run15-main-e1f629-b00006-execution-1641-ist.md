# Groot Academy 100K — run 15 coordination delta

**Observed:** 2026-11-14 16:41 IST  
**Source repository:** `satnamkhowal/grootacademy.com` (legacy alias `satnamkhowal/gta`, repository ID 1375760757).  
**Central branch:** `audit/groot-ga22-browser-delta-20261112-0350`. Coordination-only; source implementation remains in the Groot repository.

## New source evidence

- Groot Main advanced from `c2603620fe28f0ff26af5967241d3b62b7c64e69` to `e1f629ecd0bffb9d3eafaaadbd6f5bf226950e6f`.
- The only changed path is `courses/index.php` (27 additions, 1 deletion). No blog/layout/registry/sitemap/controller path changed.
- Exact current-source registry parse: 77 unique top-level records/slugs; blog sitemap has 49 article routes; page sitemap has 28 root-level registry routes. Exact partition 49 + 28 = 77, zero missing/duplicate. This corrects the prior 74/25 estimate in the latest issue #401 checkpoint; it is repository-source accounting, not live publication.
- The separate 5,000-URL study-guide shard remains outside the 77-entry registry and 49-article blog sitemap. Existing bounded sample raised near-duplicate/authorship QA leads; no final verdict or new sample in this run.

## GA-B00006 repair progress

- Exact article, metadata, executable companion and authored SVG blobs were re-fetched from the controller branch.
- Coordinator-run Python 3.13.5 companion execution passed in normal, `-O` and `-OO` modes; `py_compile` exit 0. SVG XML parse passed at 1200×630 with title/description and four arrow markers.
- Existing independent review record marks editorial/code/visual PASS, but explicitly leaves full article/release approval pending. No approval state changed.
- Detailed source evidence: [Groot run 15 report](https://github.com/satnamkhowal/grootacademy.com/blob/content/groot-100k-controller-20261114-run13/work/B0002/qa/2026-11-14-ga100k-run15-main-e1f629-b00006-execution-1641-ist.md).

## Current recovery and CI gates

- #507/#625/#654/#660/#664/#713 remain OPEN/DRAFT with zero independent reviews.
- The #507→#654→#660→#664 parent graph remains linear and scoped; displayed descriptions/base metadata need owner refresh.
- #713 exact-head Actions runs failed before steps with Azure `BlobNotFound` 404; zero hosted assertions. No retry.
- Preserve #625 and #713's separate workflows and integrate their three identical shared files once.
- Queue remains 29/29, blob `c12a915e06c8100a350b21338311651df0f35094`; drafts/visuals/PHP candidates 23/23/23; independent component PASS 22/18/23; fully approved/published/live 0/0/0.

## Central coordination delta

- Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`.
- PRs #1/#2/#3 remain merged; existing AEO/GEO PR #2 baseline reused.
- Central PR #22 remains Draft/unreviewed. Main README lists eight brands but only three active owner/status rows; Groot's dedicated row is missing.
- Jaipur Engineers `je2` social vs `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved.
- Controller target is 100,000/P0 while issue #401's latest master-ledger checkpoint says 1,000,000; one Master-owner decision, one canonical queue owner and one independent release approver remain pending.

No central Main or other-brand source change, owner reassignment, self-approval, merge, deployment, publishing or indexing.
