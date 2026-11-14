# Groot Academy — GA-B00006 current-main PHP/render integration delta

Observed: 2026-11-14 04:43 IST  
Coordination repository: `satnamkhowal/brand-growth-control-center`  
Coordination branch: `audit/groot-ga22-browser-delta-20261112-0350`  
Source repository: `satnamkhowal/grootacademy.com` (owner's legacy alias `satnamkhowal/gta`)

## Central baseline and ownership

- Central `main`: `21af139cc32a7b67aab6908c61edeb5998bd4544`; unchanged.
- Current main README blob: `b93187c353f8112a57fffab4b383e64236976394`.
- Required 2026-10-19 Groot lane-review baseline blob: `47467f0fc1a4c922affdee1d60cff120bff78d31`; read before this delta.
- Central PRs #1/#2/#3 are closed/merged. Reuse the existing AEO/GEO baseline from PR #2; no new cross-brand crawl or duplicate remediation queue.
- Current central PR #22 branch head before this report: `90e28b2fc1a9fe22755f8ca60668767e62c6e207`, 83 ahead / 0 behind central main, 40 coordination-only report files, OPEN/DRAFT, zero independent reviews.
- README still lists eight brands but only three active owner/status rows; Groot Academy's dedicated active row is missing.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. No inference or owner reassignment.

## New source-side evidence

Source main is `9c90902f3964372ff3536e311b0e4a5f356bf167`. The source owner alias `satnamkhowal/gta` resolves to the canonical GitHub repository `satnamkhowal/grootacademy.com`.

GA-B00006 was tested against its exact recovery PHP candidate and current-main shared blog layout/head/site-paths/root-head blobs:

- Python 3.13.5 exact companion execution: PASS, fresh process, exit 0.
- PHP lint: 6/6 PASS for the candidate, current shared layout/head, header/footer partials and site-paths.
- Bounded PHP render fixture: exit 0; one H1, one canonical, one BlogPosting and one BreadcrumbList; canonical/schema match; eight TOC links match eight H2 IDs; both internal guide targets exist and current .htaccess contains route rules.
- The fixture used root header/footer stubs, so it is not a complete production-root render or HTTP test.
- Current shared blog partial plus root head emit two base elements; existing source PR #713 removes the duplicate partial base line.
- Current shared layout omits featured-image width/height; current CSS applies 16:9 cover to the 1200×630 PNG. Existing source PR #654 adds strict dimension validation and an intrinsic-ratio image class. No browser crop/CLS measurement is claimed.
- GA-B00006 remains absent from current-main registry/sitemap and its recovery candidate is still unapproved.

Detailed source report: [GA-B00006 current-main PHP/render integration probe](https://github.com/satnamkhowal/grootacademy.com/blob/content/groot-100k-controller-20261016/marketing/blog-factory/work/B0002/qa/2026-11-14-ga-b00006-current-main-php-render-integration-0443-ist.md), source commit `437cd79d390c26eb73335927a3a103b295c9c7ec`.

## Recovery and release state

- Source PR #507: current main base metadata, 4 ahead / 27 behind, 22 net historical additions, OPEN/DRAFT, zero independent reviews.
- Source PR #713: current base metadata reports four intended files; direct compare is 12 ahead / 1 behind. It remains OPEN/DRAFT with zero independent reviews. Four exact-head Actions jobs failed before steps with Azure `BlobNotFound` HTTP 404; zero hosted assertions.
- Source PR #625 overlaps three shared-head blobs with #713 but retains a unique Spoken English route-QA workflow. Preserve its owner; do not merge duplicate shared-head changes twice.
- Source PR #654 carries the intrinsic-image sizing fix in the recovery stack. No independent approval is recorded.
- No source merge, registry/sitemap/redirect change, production deployment, publication or indexing occurred.

## Accounting and governance

- Canonical queue: 29/29 IDs, exact original order.
- Controller counts: 23 complete drafts, 23 technical visuals, 23 PHP candidates; independent editorial/code/visual passes 22/18/23; independent approvals 0; published 0; live verified 0.
- Research PR #68's 14 proceed proposals and GA-B00014 in-place refresh are not additional finished articles.
- Source issue #401's latest 04:28 IST checkpoint records 77 registry slugs, 50 blog sitemap URLs (1 hub + 49 articles), 68 page-sitemap URLs, with 77/77 source routes represented once across the two sitemaps. Live-published unique total remains UNVERIFIED.
- Master-owner alignment of 100K/P0 versus 10K/P3, one canonical queue owner and one independent release approver remains pending. New controller IDs remain HOLD.

## Next exact action

1. Source owner obtains independent editorial/code/visual review of GA-B00006; coordinator-run tests are not independent approval.
2. Recovery owner refreshes PR #507 and dependent stack to current main without regenerating historical blobs or changing unrelated paths.
3. Reconcile existing PR #654 and #713 fixes while preserving the unique Spoken English workflow from #625.
4. Diagnose Azure Actions storage, then run hosted PHP 8.0/Python 3.12 and full-root/browser/HTTP/MIME gates.
5. Central owner resolves Groot's active owner row and the existing governance decisions through the normal review process. Keep this PR Draft; no central-main write, merge, deployment, publication or indexing.
