# Groot Academy coordination delta — 14 November 2026, 01:47 IST

## Verified source identity and current main
- The requested alias satnamkhowal/gta permanently redirects to satnamkhowal/grootacademy.com (repository ID 1375760757). Brand/domain: Groot Academy / grootacademy.com.
- Current source main: 9c90902f3964372ff3536e311b0e4a5f356bf167, PR #733. Its two paths add a profile resource link to the existing Java-roadmap history and a coordination note; no overlap with the controller repair/recovery diffs.
- Current controller queue remains 29/29 IDs in original order; queue SHA 2766216c3f47982fdba1934c96873a6892968ef1. Counts remain 23 complete drafts/visuals/PHP candidates, independent editorial/code/visual PASS 22/18/23, approvals/published/live 0/0/0. PR #62 IDs and PR #68 proposals/GA-B00014 refresh remain preserved.

## Shared blog-head repair: #625/#713 overlap
- PR #713 metadata was refreshed to main@9c90902f; four changed files, direct compare 12 ahead/1 behind, mergeable=true, zero independent reviews. The single main commit not yet in the branch has two non-overlapping paths. Four exact-head Actions jobs fail before steps with Azure BlobNotFound HTTP 404; zero hosted assertions.
- PR #625 remains OPEN/DRAFT with stale base metadata (071ab8a5, 34 listed files); current-main compare is 7 ahead/27 behind and four net paths, zero reviews.
- Three PR #625 blobs are byte-identical to PR #713: shared blog head partial (5d6b335c), PHP fixture (94e3b855), Python test (935a48a1). PR #625's separate fourth net path is .github/workflows/groot-spoken-english-qa.yml; PR #713 instead adds .github/workflows/blog-head-base-path-qa.yml.
- Do not merge both duplicates. Preserve the separate Spoken English route-QA workflow and have its owner split/reconcile the overlapping shared-head portion. No PR was closed or approved.

## GA-B00006–GA-B00010 historical recovery stack
- PR #507 metadata was refreshed to main@9c90902f; it now lists 22 net files and mergeable=true. Direct compare: 4 ahead/27 behind, merge base 813a66fa986a0725c594ecd3780a2be03f5114b9, zero deletions, zero independent reviews.
- Exact historical payload: five article PHP pages, five original SVGs, five original PNG cards and seven code/fixture companions.
- Current main changed 37 paths since the merge base. Path intersection with the net recovery diffs is zero:
  - #507: 4/27, 22 paths.
  - #654: 9/27, 24 paths.
  - #660: 19/27, 25 paths.
  - #664: 32/27, 30 paths.
- #507→#654→#660→#664 remain OPEN/DRAFT with zero independent reviews. Owner-controlled refresh and independent editorial/code/PHP/schema/browser/AT/HTTP/MIME/release gates remain. Separate QA PR #533 is 31 ahead/105 behind, 31 net paths, zero reviews; do not conflate it with the recovery stack.
- No recovery article has been approved, published, deployed or counted as live.

## Source URL-history delta
Compared old main d9eba9445ac5d58652d9b36f026e3b6efb5e2bea with current main 9c90902f:
- Registry: 87 unique slugs → 77; 61 old slugs absent, 51 different slugs added.
- blogs/sitemap.xml: 91 unique URLs → 50 (hub + 49 article URLs); 63 old URLs absent, 22 new URLs added; the hub is common.
- sitemap-pages.xml: 68 unique URLs; 28 root-level article routes match the registry. The 49 blog-sitemap articles plus 28 root-level routes account for all 77 registry slugs at source level.
- Five sampled old PHP files remain with self-canonical/index,follow but are absent from current registry/blog sitemap: Django/Python, Deep Learning, Linux Administration, Git/GitHub and AI Agents. Current .htaccess has no explicit rule naming those five.
- Live HTTP, redirect chains, backlinks and Search Console indexing are unverified. No bulk restore, redirect, deletion or indexation action is authorized by this source comparison; decide per URL after authorized HTTP and editorial review.

## Central coordination baseline
- Central main remains 21af139cc32a7b67aab6908c61edeb5998bd4544. PR #22 is coordination-only Draft, 79 ahead/0 behind, 37 files, zero independent reviews.
- PR #1/#2/#3 are merged. Existing AEO/GEO PR #2 baseline is reused.
- Main README lists eight brands but only three active owner/status rows; Groot Academy's dedicated row remains missing.
- Jaipur Engineers je2 social repository versus jaipur-engieneers candidate website/deployed-origin mapping remains unresolved. No other brand implementation or owner was changed.

## Next actions
1. Azure Storage administrator diagnosis, then exact-head PHP 8.0/Python 3.12 hosted checks and independent #713 review.
2. Reconcile #625/#713 overlap without losing the separate Spoken English workflow.
3. Owner-refresh the #507→#654→#660→#664 stack while preserving exact historical blobs; then independent release review.
4. Investigate retired URLs one by one; do not bulk restore/delete.
5. Continue GA-B00016/GA-B00022 accessibility and production-page QA.
6. Master owner to record 100K/P0 versus 10K/P3 alignment, one canonical queue owner and one independent release approver. New IDs remain HOLD.

This is coordination evidence only. Central main and other-brand source repositories were not changed. No approval, merge, deployment, publication or mass indexing occurred.


## GA-B00006 exact-source execution addendum — 14 November 2026, 01:47 IST
- Controller-branch examples.py blob `84706ec6d80b0458acd915c61943e2e477feafbe` is byte-identical to the GA-B00006 recovery PR #507 companion. Fresh Python 3.13.5 process: exit 0, output PASS for shared mutable default, fresh None-based lists, caller-owned list and shallow-copy boundary.
- Authored SVG blob `c140a0723c290c33cc615656803794925abe9cca` matches the controller branch; XML parse PASS, 1200×630, title/description present.
- PR #507 PHP candidate blob `9da774dbb34b7994a1dc0a8efd8f75aa0f300b3b` statically contains self-canonical, index,follow, featured-image URL and descriptive alt. No PHP lint/render/schema test was run.
- Coordinator-run evidence only; independent QA, PHP/shared-layout/schema/route/registry/sitemap/browser/AT/HTTP/MIME and release gates remain pending. Queue/counts unchanged; no draft or asset regeneration.
