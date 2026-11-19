# Coordination delta — Groot Academy GA-B00029 current-main refresh

**Observed:** 13 November 2026, 19:44 IST  
**Central main:** `21af139cc32a7b67aab6908c61edeb5998bd4544`  
**Source repository:** `satnamkhowal/grootacademy.com` (legacy `satnamkhowal/gta` redirects to the same private repository ID 1375760757)  
**Brand/domain:** Groot Academy / https://grootacademy.com/  
**Scope:** coordination-only evidence. Source implementation remains in the Groot repository.

## Source-main delta and counts

- Groot main advanced from `d864a7e3760bd4352359817c8d223c8ba073fe4f` to `064554c5a792aa0c0114824e0442f8e6d9439cff` through PR #722, which adds the source-checked 2017 Java full-stack retrospective and modifies the 2018 retrospective, registry and blog sitemap.
- The four #722 paths do not overlap the four GA-B00029 repair paths. The 2017 retrospective is a separate Main article outside the controller's 29-ID queue; it is not counted among the controller's 23 complete drafts and is not live-verified here.
- Exact current-Main source counts: registry 74 unique slugs; blog sitemap 47 URLs (1 hub + 46 article URLs); page sitemap 68 URLs with 28 registry article matches. Reconciliation is 46 + 28 = 74, with zero missing registry slugs and zero cross-sitemap overlap. These are repository-source counts, not live-published or Search Console-indexed totals.
- Issue #401's latest owner checkpoint at 18:25 IST recorded 73 registry slugs / 46 blog-sitemap URLs (1 hub + 45 articles) / 68 page-sitemap URLs with 28 registry matches. PR #722 adds one registry and one blog-sitemap article after that checkpoint; its source changes were counted directly. Live verification and Search Console indexation remain unverified.

## GA-B00029 / source PR #713

- Source PR [#713](https://github.com/satnamkhowal/grootacademy.com/pull/713) was refreshed to `main@064554c5` using two-parent merge commit `df061ee082ee071afe17494c3f91cdab90d08b11` (current main first parent, previous repair head `a7b49dfa` second).
- Direct compare is **8 ahead / 0 behind**, exactly four intended net paths: dedicated workflow, shared blog head partial, PHP rendering fixture and Python regression. PR base SHA and paginated changed-file list match the direct compare.
- PR remains OPEN/DRAFT, four changed files, zero independent reviews; GitHub reports mergeable=true. No merge or approval.
- Exact-source local fixture evidence (PHP 8.4.24 / Python 3.13.5): PHP lint 4/4; workflow tests 2/2 in normal/-O/-OO; supplemental edge tests 5/5 in normal/-O/-OO. All five fixture input files were checked against their exact GitHub blob hashes.
- Exact current-Main shared partial blob `637d161f762d52b5ed4eca8ec01244b0e3a07bc4` is the negative control: all five edge tests fail as expected due to the duplicate base; the PR partial passes all five. This is coordinator-run local fixture evidence, not independent approval or hosted PHP 8.0/full-root verification.
- Four workflows triggered on the refreshed head: [43441383301](https://github.com/satnamkhowal/grootacademy.com/actions/runs/43441383301), [43441383114](https://github.com/satnamkhowal/grootacademy.com/actions/runs/43441383114), [43441383139](https://github.com/satnamkhowal/grootacademy.com/actions/runs/43441383139), [43441383130](https://github.com/satnamkhowal/grootacademy.com/actions/runs/43441383130). All failed before steps; step arrays are empty and log downloads return Azure Storage `BlobNotFound` HTTP 404. Zero hosted assertions ran. Administrator/storage-owner diagnosis is required; no blind retry.
- Remaining gates: exact-head PHP 8.0/Python 3.12 hosted run after storage recovery; independent four-path review; full-root PHP/schema/H1/canonical/robots; registry/sitemap/route parity; production browser; authorized-origin HTTP/MIME and asset/link checks.

## Controller ledger

- Controller branch: `content/groot-100k-controller-20261016`.
- Canonical queue blob `2766216c3f47982fdba1934c96873a6892968ef1`: 29 rows, 29 unique IDs in exact GA-B00001–GA-B00029 order. Status counts: MERGE 3, REFRESH 2, IDEA 1, PUBLISH_PR 5, TECH_QA 17, CONTENT_QA 1.
- Planning PR #62's immutable 29 IDs and research PR #68's 14 proceed proposals plus GA-B00014 in-place refresh remain preserved.
- Counts remain 23 complete original drafts, 23 technical visuals, 23 PHP candidates; independent editorial/code/visual PASS 22/18/23; independent approvals/published/live 0/0/0. GA-B00029 remains TECH_QA. No new article, image or queue ID was created.

## Central ownership / PR deltas

- Central main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; current main README blob is `b93187c353f8112a57fffab4b383e64236976394`.
- Central PR [#22](https://github.com/satnamkhowal/brand-growth-control-center/pull/22) remains OPEN/DRAFT on its isolated audit branch, **72 ahead / 0 behind, 32 coordination report files**, zero independent reviews after this report and its read-back correction. This file is a non-overlapping coordination-only artifact; keep PR Draft pending independent review.
- Central PRs #1 (Jaipur Engineers social), #2 (all-brand AEO/GEO) and #3 (coordination audit) are CLOSED/MERGED. Reuse PR #2's existing AEO/GEO baseline and queue; do not recreate them.
- Current README lists eight brands but only three active owner/status rows; Groot Academy's dedicated row is still missing. Do not invent an owner or alter another brand's ownership.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. Preserve both records until the owner explicitly reconciles them.
- No central-main, other-brand source, owner, deployment or publication change.

## Exact next actions

1. Actions/storage administrator diagnoses Azure `BlobNotFound`; no blind retry.
2. After recovery, source PR #713 gets exact-head PHP 8.0/Python 3.12 hosted checks and independent four-path review.
3. Finish full-root/schema/route/browser/HTTP/MIME release gates and independent GA-B00016/GA-B00022 accessibility reviews.
4. Master owner records 100K/P0 vs issue #401 M4 alignment, one canonical queue owner and one independent release approver before new IDs/batches.
5. Central owner adds a verified Groot active control-board row and resolves the Jaipur repository/origin mapping without changing source ownership.

No self-approval, self-merge, deployment, publishing or mass indexing.
