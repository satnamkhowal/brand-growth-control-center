# Groot Academy 100K coordination delta — 2026-11-11 11:40 IST

## Central main and ownership boundary

Current central main advanced to `80c75e28734ce22831e93d9f431f4c15ccad0f6c` with an Anna Walker Cafe business-details/domain-shortlist log. This is unrelated to Groot. The current main README remains blob `b93187c353f8112a57fffab4b383e64236976394` and still lists eight brands but only three active control-board rows; Groot Academy has no active row.

PRs #1, #2 and #3 remain merged. Reuse the existing AEO/GEO baseline from PR #2; no baseline or queue was recreated. Jaipur Engineers `je2` social repository vs `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. Keep both workstream records and their existing owner; no assumption or ownership transfer is made.

## New source-repository evidence

Groot's requested `satnamkhowal/gta` resolves to `satnamkhowal/grootacademy.com`. Implementation and the new route issue remain in that source repository; this central report is coordination-only.

Groot main advanced from `83d20b3` to `7f9380356d6f7f578e064a3a6f0b705137c3fc3f` through PRs #619–#622. Their changes are homepage-only. Shared blog layout/head, registry and sitemap blobs were rechecked; no blog dependency changed in those four commits.

The public blog hub lists 61 guides. Cards 31–35 returned readable content on direct canonical open (5/5). Card 33 had a click-follow fetch error but direct open of the same URL returned the complete article. Five source files use the shared blog layout, all five have exact registry entries, the root-level three are in `sitemap-pages.xml`, the two `/blogs/` pages are in `blogs/sitemap.xml`, and 36/36 TOC anchors match. The five intents remain distinct. Sixteen internal destinations source-resolve: 15 file-backed and one static-page route.

One real public route defect was found: both `/placement-support/` and its slashless form returned 404, even though current-main `.htaccess`, `static-page.php`, `includes/static-pages.php` and `sitemap-pages.xml` define the intended route. The route is linked from the live GitHub Portfolio article. Groot issue [#623](https://github.com/satnamkhowal/grootacademy.com/issues/623) now tracks deployed document-root/SHA, rewrite and server-log checks plus GET/HEAD acceptance. This is route-local, not a site-wide outage. No source route, article link, sitemap or deployment was changed.

Groot evidence report: [cards 31–35 route QA](https://github.com/satnamkhowal/grootacademy.com/blob/qa/groot-100k-current-main-20261109/marketing/blog-factory/work/B0002/qa/2026-11-11-public-hub-route-sample-31-35-placement-support-1140-ist.md).

## Factory and PR boundaries

The canonical queue remains 29/29 original IDs, unchanged. Counts remain 23 complete original drafts, 23 technical visuals, 23 PHP candidates, 18 independent code passes, 0 independent publication approvals, 0 published and 0 live-verified. GA-B00014 remains an in-place refresh, not a new article.

- Groot PR #569 remains the existing factory review lane. Against current main it is 209 ahead / 9 behind, 225 changed files, with zero independent reviews and zero review threads. Its large legacy-artifact/governance diff requires owner-led reconciliation; do not rebase or merge from this coordination lane.
- Groot recovery PR #533 and link-repair PR #614 have no independent reviews in the current observations. Preserve their existing owners and shared-file boundaries.
- Central PR #20 remains the existing coordination lane. Current branch comparison is 33 ahead / 4 behind main, 21 changed files; zero independent reviews. It remains open and unmerged. This delta is appended to the existing branch only; central main is untouched.

## Exact next actions

1. Groot hosting/release owner resolves [issue #623](https://github.com/satnamkhowal/grootacademy.com/issues/623) and verifies deployed route parity; do not deploy from this lane.
2. Groot Master owner reconciles the 100,000/P0 controller, 10,000-capacity Master Plan, HAO-008 P3/REVIEW and issue #401 M4=100,000 before any new queue IDs.
3. Groot source owner obtains a network-enabled runner for GA-B00029 full-root PHP/schema and four authorized-origin HTTP/MIME checks; Actions/storage administrator diagnoses pre-step Azure `BlobNotFound`.
4. Existing owners reconcile PR #533/#569/#614 and obtain independent review; independently review GA-B00016/GA-B00022.
5. Central owner records Groot's active repository/workstream/owner row in the appropriate central control-board process without moving source implementation; keep Jaipur's repository-role question with its existing owner.
6. After repair/release gates, continue bounded public hub cards 36–40. Do not start a new 100K article batch before the Master-owner decision.

No central main write, other-brand source change, queue edit, approval, merge, deployment, publication or indexing occurred.
