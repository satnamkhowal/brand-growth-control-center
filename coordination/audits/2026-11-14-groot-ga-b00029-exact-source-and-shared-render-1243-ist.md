# Groot Academy — GA-B00029 exact-source and shared-render delta

**Date:** 14 November 2026, 12:43 IST  
**Scope:** Coordination-only evidence. Source implementation remains in `satnamkhowal/grootacademy.com`; this report changes no other brand source.

## New source evidence

- Canonical alias `satnamkhowal/gta` resolves to the same Groot Academy repository, `satnamkhowal/grootacademy.com`.
- Current source Main is `50c169e760255c74629e0d37c778fa84e00611b1`, confirmed by the 12:21 IST issue #401 checkpoint. Its latest commit changes only the homepage program stylesheet cache key; no blog/shared-layout/registry/sitemap path changed.
- Controller branch remains `content/groot-100k-controller-20261016`. Canonical queue blob `c12a915e06c8100a350b21338311651df0f35094` still contains the same 29 ordered unique IDs. No row/status changed.
- Research PR #68 remains 14 proceed proposals plus GA-B00014 refresh; neither is counted as a finished article.

## GA-B00029 exact-source execution

All seven package files fetched from the controller branch match their exact GitHub blob SHA-1 values: article, metadata, Python lab, six-test suite, draft verifier, four verifier regressions and authored SVG.

Coordinator-run Python 3.13.5 evidence:
- Demo exit 0: Ada and O'Reilly match, injection-shaped value matches no row, all three fictional rows remain.
- Draft verifier: 25/25 checks and 1,354 words in normal Python, `-O` and `-OO`.
- SQLite unit suite: 6/6 PASS.
- Verifier adversarial regression suite: 4/4 PASS.
- Python compilation: 4/4 PASS.

This resolves the earlier local reconstruction mismatch note. It does not replace the existing independent complete-content review or create a new independent approval.

## Current-main PHP/schema render delta

Exact source inspected:
- Candidate: `18962c3f2ad7ad590083f6ec965b02b79ac01b9c`.
- Current-main shared blog layout: `7e19e1b4b87843d65b5aa7f1cb0fb33a5b154178`.
- Current-main shared head partial: `637d161f762d52b5ed4eca8ec01244b0e3a07bc4`.
- Current-main root head: `89fe435eb1402d963fe8be350c7c20f1a29d3ea4`.
- Current-main site paths: `edeaf8117b160c124d9d55fd23cdee52c6f86777`.

PHP 8.4.24 lint: 4/4 PASS for candidate, shared layout, shared head partial and site-paths.

A bounded render fixture used the exact candidate and current-main shared layout/head/site-paths. Root-head base output was source-derived; navigation, footer and registry were stubbed:
- Current Main emits two base tags in production (`//`, `/`) and mounted preview (`/groot-preview//`, `/groot-preview/`).
- Applying the exact one-line partial-base removal from PR #713 yields one correct base in both modes.
- Canonical 1; robots `noindex,follow`; H1 1; H2/TOC 9/9; exactly one BlogPosting and one BreadcrumbList; null publication dates omitted; featured SVG/alt present; both download links present.
- Both internal guide links exist in current-main registry and sitemap. The candidate slug is absent from both, as required while unapproved.

This is a source-derived coordinator fixture, not full-root production rendering, PHP 8.0 hosted CI, browser/AT, HTTP/MIME or release approval.

## Source PR and infrastructure deltas

- PR #713 head `fa4bac8d616db76085a2bdf946499018867a5c34`: current Main `50c169e` compare is 12 ahead / 5 behind, exactly four intended paths, zero independent reviews. Exact-head hosted jobs still fail before steps with Azure `BlobNotFound` HTTP 404; zero hosted assertions. Keep Draft.
- PR #507 current head `ab7d4c13b3ff68b5c8ea760c50425c2ccf302264`: current-main compare is 1 ahead / 109 behind, 22 original historical additions, zero deletions and zero independent reviews. Its body still records base `d9eba944`; owner refresh is required.
- PRs #625 and #713 still share three byte-identical files. Preserve #625's unique Spoken English workflow and #713's unique base-path workflow; integrate shared files once.
- Azure Actions storage administrator diagnosis remains required; no blind retry.

## Ledger and central governance

Groot controller counts remain: 29 queue IDs, 23 complete drafts, 23 visuals, 23 PHP candidates, independent component PASS 22/18/23, fully approved 0, published 0, live verified 0. GA-B00029 remains `TECH_QA`; no count promotion.

Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`. PRs #1/#2/#3 are merged; the existing AEO/GEO PR #2 baseline is reused. Central README still lists eight brands but only three active owner/status rows; Groot Academy's dedicated row is missing. Jaipur Engineers `je2` social versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved.

Master-owner reconciliation is still needed for the user-authorized 100K/P0 target versus the P3/10K planning records, one canonical queue owner, one independent release approver and evidence-based batch-growth criteria. New IDs remain HOLD while existing repairs continue.

## Exact next action

1. Actions/storage administrator diagnoses Azure `BlobNotFound`; do not retry zero-step jobs blindly.
2. Source owners refresh #713 and #507 against current Main; preserve both #625/#713 unique workflows and integrate the three shared files once.
3. Continue #654 → #660 → #664 sequentially with independent review.
4. Complete PHP 8.0/full-root/schema/route/browser/AT/HTTP/MIME gates and independent GA-B00006 release review.
5. Keep GA-B00029 noindex and out of registry/sitemap until release approval.

No source implementation, central Main write, owner reassignment, self-approval, self-merge, deployment, publishing or indexing occurred in this coordination delta.


## Delta — 2026-11-14 13:53 IST: current Main, recovery base lineage and News Factory dedupe

Groot source repository alias `satnamkhowal/gta` and canonical API repository `satnamkhowal/grootacademy.com` resolve to the same repository ID `1375760757`. Current source Main advanced to `7f007cbc5da988bbce401a1a50a4fbf00fa3bb24` (“Keep homepage search reset within reach”), changing only homepage CSS, homepage path-finder JavaScript and root `index.php`. No blog article, shared blog layout, registry, sitemap or canonical queue path changed.

Fresh source comparisons against current Main:
- #507 head `ab7d4c13`: 1 ahead / 111 behind; 22 historical recovery files; 0 independent reviews.
- #625 head `d1c3d394`: 7 ahead / 33 behind; four intended paths; 0 independent reviews.
- #713 head `fa4bac8d`: 12 ahead / 7 behind; four intended paths; 0 independent reviews.
- #625/#713 still share the same three PHP/Python blobs and have distinct Spoken English and base-path workflows. Preserve both unique workflows and integrate shared files once.
- #713's four exact-head Actions runs remain pre-step Azure `BlobNotFound` failures; zero hosted assertions ran. No retry was triggered.

A new dependency-lineage check found that the actual base SHAs recorded by the stacked PR metadata do not equal their immediately preceding PR heads:
- #654 base `68db39f` vs #507 head `ab7d4c13` (26 ahead / 0 behind; 27 changed paths from its recorded base).
- #660 base `fc25231` vs #654 head `5bf6531` (32 ahead / 0 behind; 33 paths).
- #664 base `46dcc21` vs #660 head `df9431c` (36 ahead / 0 behind; 32 paths).
The diffs include inherited homepage/course/assets/registry/sitemap paths. These branches must be reconciled to exact parent heads and intended-only scopes by their source owners before review. No source branch was edited or merged.

Cross-lane review: News Factory PR #745 is a separate Cloudflare Workers/Durable Objects Spend Management draft with three paths under `docs/news-factory`. Its topic does not appear among the 29 canonical 100K queue intents; it has no GA-B ID and is not counted in the controller ledger. Its latest recorded checks cover article/metadata word count, SVG and shell syntax; independent editorial, technical and responsive/browser QA remain pending. Existing PR #602 Google Maps in AI Studio cross-lane evidence remains in the earlier PR #20 audit and was not recreated.

The canonical queue remains 29 ordered IDs; controller ledger remains 23 complete drafts, 23 visuals, 23 PHP candidates, independent component PASS 22/18/23, fully approved 0, published 0, live verified 0. GA-B00006 remains PUBLISH_PR with full article QA approval NOT YET; GA-B00029 remains TECH_QA/noindex.

Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; PRs #1/#2/#3 are merged and AEO/GEO PR #2 is reused. PR #22 remains Draft/open with zero independent reviews. Central README still lists eight brands and three active owner/status rows; Groot's dedicated row is missing. Jaipur Engineers `je2` social vs `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. Master-owner 100K/P0 alignment, canonical queue owner, independent release approver and evidence-based batch criteria remain pending.

Evidence: [Groot source run 12 report](https://github.com/satnamkhowal/grootacademy.com/blob/content/groot-100k-controller-20261016/marketing/blog-factory/work/B0002/qa/2026-11-14-ga100k-run12-main-7f007cbc-stack-lineage-1353-ist.md).

No central Main write, brand ownership change, source implementation, self-approval, merge, deployment, publication or indexing occurred.
