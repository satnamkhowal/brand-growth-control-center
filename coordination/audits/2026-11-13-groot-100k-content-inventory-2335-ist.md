# Groot Academy 100K — coordination inventory delta

**Observed:** 2026-11-13 23:35 IST  
**Coordination branch:** `audit/groot-ga22-browser-delta-20261112-0350`  
**Source repository:** `satnamkhowal/grootacademy.com` (legacy `satnamkhowal/gta` permanently redirects here)  
**Current source main:** `a5706a7f33e389be15e36f1093b4dd953aee1737`.

## What changed since the 22:38 coordination checkpoint

- Source main advanced from `86f5289b` to `a5706a7f` through PR #729, JDK 27 migration checks for the existing Java 27 / Spring Boot 4.1 roadmap.
- The exact latest commit changes three files: the shared blog registry, the Java 27 roadmap page and the 2025 retrospective page. None overlaps the four GA-B00029 repair paths in source PR #713.
- Source PR #713 remains OPEN / DRAFT, head `4eb38b5e`, base `86f5289b`; current compare is 11 ahead / 1 behind, exactly four intended files, zero independent reviews. Eight exact-head Actions jobs previously failed before steps with Azure BlobNotFound HTTP 404; zero hosted assertions. Keep the PR Draft and do not retry until the storage owner diagnoses the runner/log allocation issue.
- Canonical controller queue remains 29/29 IDs, 23 complete drafts, 23 visuals and 23 PHP candidates; independent approvals/published/live remain 0/0/0. Planning PR #62 and merged research PR #68 remain intact; 14 proceed proposals and GA-B00014 refresh are not new articles.

## Bounded source inventory finding

At current source main:
- Registry: 77 unique slugs.
- Blog sitemap: 50 URLs (one index + 49 article URLs).
- Page sitemap: 68 URLs, including 28 root-level article routes that match the registry.
- Ten additional root-level content candidates appear in `sitemap-pages.xml` but not in the blog registry or `/blogs/` directory. Their source configs have self-canonicals and `index,follow`; no exact duplicate paragraph was found among these ten. The highest simple token Jaccard was 0.371 between the Python role-comparison and Python career-options guides. Keep them as separate root-level pages; do not silently add them to the 100K blog count. The 431-word full-stack project guide is the shortest and should receive a bounded depth review; AI-certification facts need fresh issuer verification.

## Separate 5,000-URL study-guide shard

This sitemap is outside the 29-ID controller and the 100K completed count.

Existing source documentation says all 5,000 guides are AI-assisted, records 5,000 PHP syntax/render checks and 43,000 TOC entries, and explicitly does not establish production deployment. The associated HTTP verification used a local `127.0.0.1` server and records `production_deployment_verified=false`.

A stratified source sample at sitemap positions 1, 500, 1,000, 2,500 and 5,000 found:
- Three project guides share five exact paragraphs and 7/8 H2 headings; pairwise token-set Jaccard 0.684–0.728.
- Two debugging guides share ten exact paragraphs and 8/9 H2 headings; token-set Jaccard 0.660.
- All five sampled pages have self-canonicals and `index,follow`.

This is evidence of template-heavy prose in the sample, not proof that all 5,000 pages are duplicates. Existing syntax/render/link checks do not prove independent editorial usefulness or distinct reader intent. Keep the shard outside the 100K count; do not alter sitemaps/robots or submit mass indexing. Before any further scale-up, require independent review of at least 25 pages stratified across task families and assess task-specific explanation, code, expected output and repeated prose.

## Ownership and governance

- Current Control Center main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; this is a coordination-only branch update.
- PRs #1/#2/#3 remain merged; reuse the existing AEO/GEO PR #2 baseline.
- README still lists eight brands but only three active owner/status rows; Groot Academy's dedicated row is missing.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved with the central mapping owner.
- Source implementation remains in the Groot Academy repository. No central-main write, other-brand file edit, owner reassignment, merge, deployment, publication or indexing occurred.

## Exact next action

1. Administrator/storage-owner diagnosis of Azure BlobNotFound; then exact-head PR #713 hosted PHP 8.0/Python 3.12 checks and independent four-path review.
2. Continue GA-B00016 corrected-copy/editorial/manual AT and GA-B00022 production-page/AT reviews.
3. Independently review at least 25 stratified pages from the 5,000 shard before any quality/count decision.
4. Keep the ten root-level pages outside the blog registry and 100K controller count.
5. Master owner reconciles 100,000/P0 with the 10,000 possible-ID/P3 plan, names one canonical queue owner and one independent release approver. New IDs remain HOLD.

No ranking, Search Console indexation, live deployment or production HTTP status is inferred from these source/local checks.
