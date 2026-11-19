# Groot Academy 100K — Run 19 coordination delta

**Observed:** 2026-11-14 20:44 IST  
**Scope:** coordination-only evidence delta; source implementation remains in Groot Academy's verified repository.

## Repository and current-main reconciliation

- The legacy `satnamkhowal/gta` alias resolves to the same GitHub repository ID `1375760757`, now named `satnamkhowal/grootacademy.com`. This is Groot Academy, not Mango Engineers.
- Groot Main remains `e1f629ecd0bffb9d3eafaaadbd6f5bf226950e6f`; the latest Main commit changes the course catalogue and does not overlap the blog candidate or controller paths.
- The source controller successor remains `content/groot-100k-controller-20261114-run16`, tracked in source Draft PR #750. Run 19 added a single GA-B00006 candidate metadata repair (intrinsic 1200×630 image dimensions), its QA report, and controller/README checkpoint. Source PR #750 remains OPEN/DRAFT; no source Main write or merge occurred.
- Source Run 19 report: [GA-B00006 PHP render/base-path/intrinsic-image QA](https://github.com/satnamkhowal/grootacademy.com/blob/content/groot-100k-controller-20261114-run16/marketing/blog-factory/work/B0002/qa/2026-11-14-ga100k-run19-b00006-php-render-base-path-intrinsic-image-2044-ist.md).
- Source PR #750: https://github.com/satnamkhowal/grootacademy.com/pull/750

## New source evidence

- Coordinator-run PHP 8.4.24 syntax checks: 8/8 PASS.
- Bounded GA-B00006 render: one H1, eight H2/TOC targets, one root base, exact canonical, `noindex,follow`, BlogPosting and BreadcrumbList exactly once, intrinsic SVG dimensions 1200×630, no invented publication dates. The harness used isolated root header/footer stubs and an empty registry; it is not a full repository-root or hosted PHP 8.0 release run.
- Exact existing Python companion passes normal/`-O`/`-OO` and `py_compile`; existing SVG XML/title/description/dimensions pass.
- #713 candidate base-path fixture passes 2/2 local tests; current-Main negative control fails both expected assertions because both root and partial emit a base tag. #713 remains a separate Draft, not integrated into the recovery stack.
- Local PHP HTTP smoke returns 200 for the article route, SVG and examples path. SVG MIME is `image/svg+xml`; local PHP built-in server emits no `Content-Type` for `.py`. Production download MIME remains unverified.
- Chromium headless screenshot timed out and Playwright is absent; zero browser/keyboard/AT/zoom assertions are claimed. Azure Actions `BlobNotFound` remains a pre-step administrator blocker; no blind retry.
- No independent full release approval, authorized-origin HTTP/MIME, hosted PHP 8.0, full-root render or production-page verification is claimed.

## Counts and gates

- Canonical queue: 29/29 original IDs, unchanged order and SHA `c12a915e06c8100a350b21338311651df0f35094`.
- Complete original drafts / visuals / PHP candidates: 23 / 23 / 23.
- Independent component PASS: editorial 22 / code 18 / visual 23.
- Fully approved / published / live verified: 0 / 0 / 0.
- Research PR #68's 14 proceed proposals and GA-B00014 in-place refresh remain research/refresh decisions, not completed articles.
- Separate 5,000-URL study-guide shard remains pending independent editorial disposition; bounded similarity findings are not a plagiarism verdict or proof all 5,000 pages are duplicates.

## Central coordination delta

- Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; no Main write.
- Central PRs #1/#2/#3 are merged; existing AEO/GEO baseline PR #2 is reused.
- Central PR #22 remains OPEN/DRAFT on `audit/groot-ga22-browser-delta-20261112-0350`, with zero independent reviews/threads at this checkpoint. This report is coordination-only.
- Central README still lists eight brands but only three active owner/status rows; Groot Academy's dedicated row is missing.
- Jaipur Engineers `je2` social repository vs `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. No repository role was inferred or changed.
- Master-owner reconciliation of the 100K/P0 target vs capacity/conditional targets, one canonical queue owner and one independent release approver remains pending.

## Exact next action

1. Independent full GA-B00006 release review of the updated candidate.
2. Source owners refresh #507/#625/#713 against current Main and reconcile #654→#660→#664 exact parent heads, preserving each unique workflow and integrating shared files once.
3. Hosted PHP 8.0/full-root/schema/route, authorized-origin HTTP/production MIME, browser/keyboard/AT/zoom gates.
4. Azure Actions administrator diagnoses BlobNotFound before hosted retries.
5. Independent reviewer decides keep/refresh/consolidate/retire for the sampled study-guide families.
6. Master owner records target/priority, canonical queue owner and independent release approver before new IDs/batch expansion.

No owner reassignment, source Main change, central Main change, self-approval, self-merge, deployment, publication or indexing.
