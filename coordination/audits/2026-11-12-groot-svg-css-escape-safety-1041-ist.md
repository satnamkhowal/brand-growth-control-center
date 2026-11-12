# Groot Academy 100K factory — SVG CSS escape-safety delta

Checked: 2026-11-12 10:41 IST  
Scope: bounded source/QA and coordination delta only. No full-site crawl, ranking claim, production release or other-brand implementation.

## Source identity and current-main delta

- Historical repository name `satnamkhowal/gta` resolves to the same private repository ID as `satnamkhowal/grootacademy.com`; canonical source is `satnamkhowal/grootacademy.com`.
- Current Groot `main`: `f048dedf22da86e93b5b505cc1ebc84884f3a5c8`. It is one commit ahead of the earlier `0923feed` snapshot and adds the separate Agentic Architect certification article/registry/sitemap update. That article is outside the immutable 29-ID factory queue and is not counted as a finished 100K factory article or as live-verified.
- Controller branch `content/groot-100k-controller-20261016` was updated with the exact current-main observation and this continuation checkpoint (README commit `93fab3a`, CONTROLLER commit `f0c235a`).

## New source QA finding and repair

- Source implementation remains in [Groot PR #664](https://github.com/satnamkhowal/grootacademy.com/pull/664), stacked after #507 → #654 → #660.
- Review found that the SVG diagram checker scanned raw `url(...)` strings but did not decode CSS escapes first. CSS identifier `u\\72l(https://example.invalid/shape.svg#x)` is tokenized by tinycss2 1.5.1 as an external CSS URL token, so a raw regex could miss it.
- PR #664 now removes CSS comments, decodes CSS hexadecimal/simple escapes and escaped line continuations before checking `url()` and `@import`. Only resolved local fragment URLs remain allowed.
- Added ten regression cases: plain external URL, escaped function name, individually escaped identifier characters, escaped scheme/slashes, escaped import keyword, escaped line continuation, valid local fragment, unresolved fragment, data URI and ordinary text.
- Local isolated helper suite: **10/10 PASS**. tinycss2 tokenizer confirmation: escaped `u\\72l(...)` is an external URL token. This is focused regression evidence, not a full exact-repository checkout or independent review.
- PR #664 commits: checker fix `2054ac6`, regression tests `f49e0d1`, workflow integration `162e0cf`. The exact-head workflow auto-started as run [43160487425](https://github.com/satnamkhowal/grootacademy.com/actions/runs/43160487425); job returned `steps: null`, no logs and zero executed assertions. This matches the previously recorded Azure Actions/BlobNotFound infrastructure blocker. No blind retry.
- PR #507, #654, #660 and #664 remain OPEN/DRAFT with zero independent reviews. Do not merge the overlapping stale #533 article-page edits; retain its release-transition/inventory test intent through #664.

## Canonical queue and quality accounting

- Current queue file SHA: `4e087f8cda5479ff9d1124f24ff427a0dbf2b4ad`; all 29 original IDs and order from planning PR #62 remain present.
- Queue status counts: MERGE 3, REFRESH 2, IDEA 1, PUBLISH_PR 5, TECH_QA 17, CONTENT_QA 1. No queue write occurred.
- Controller counts remain 23 complete original text drafts, 23 technical visuals, 23 PHP candidates, 22 independent editorial passes, 18 independent code passes, 23 independent visual passes, 0 independent approvals and 0 published.
- Verified live factory article count: **UNVERIFIED**. Drafts, PRs, source registry/sitemap entries and CI do not establish production deployment or indexation.
- No new article, bitmap artwork, SVG asset, registry entry, sitemap URL or production file was created. Existing assets were not regenerated.

## Central coordination delta

- Current central `main`: `21af139cc32a7b67aab6908c61edeb5998bd4544`; PR #22's owned audit branch was 19 ahead / 0 behind before this report and remains coordination-only.
- Previously requested central PRs #1, #2 and #3 are now all CLOSED/MERGED (2026-10-29). PR #1 records Jaipur Engineers social campaign ownership in `satnamkhowal/je2`, with browser publishing still pending in its source record. PR #2 contains the existing eight-brand AEO/GEO baseline and 16-task board; reuse it rather than recreate the baseline.
- PR #3 merged the original four coordination findings. They remain evidence/ownership follow-ups, not permission to rewrite other brands' repositories:
  - JE social repository `je2` versus `jaipur-engieneers` candidate website/deployment mapping remains unresolved.
  - The central README still lists eight brands but only three active control-board rows; Groot's active row remains missing.
  - Groot's 100K source implementation remains in the Groot repository; central is audit evidence only.
  - Other candidate repository mappings remain unknown until owner evidence resolves them.
- Central PR #22 remains OPEN/DRAFT with zero independent reviews. No central-main write, owner reassignment, other-brand source edit, merge, deployment or publication occurred.

## Exact next action

1. Repository Actions/storage administrator diagnoses the Azure `BlobNotFound` failure; then obtain a successful exact-head #664 workflow run and execute the committed CSS regression file on a full authorized checkout.
2. Obtain independent review of #507 → #654 → #660 → #664. Keep all five recovered pages `noindex,follow` and outside registry/sitemap until an owner-approved all-five transition.
3. Complete GA-B00029 full-root PHP/schema/route/HTTP/MIME checks; finish GA-B00016 independent editorial/AT review, GA-B00022 production/AT review and PR #625 independent review.
4. Preserve all 29 queue IDs and PR #68 research decisions. Do not expand article production until the Master owner reconciles 10K/P3 capacity against the user's 100K quality target and records one canonical queue/release owner.
5. Central owner reconciles Groot's control-board row and the JE repository/workstream mapping without moving implementation into the coordination repository.

No self-approval, self-merge, deployment, publication, mass indexing or ranking/live claim was made.


## Supplemental delta — 2026-11-12 11:39 IST (Groot CSS escape + current-main reconciliation)

- Groot current main advanced from `f048dedf22da86e93b5b505cc1ebc84884f3a5c8` to `dc2d76ec4e81600fceaf36066715f6b7b0418cee` via the homepage Python course-link fix. Its only changed path is root `index.php`; current PR #664's 21-ahead/1-behind comparison has no path overlap with that main delta. The recovery stack remains separate and open/draft; no rebase, merge or main write was made.
- New source repair on Groot PR [#664](https://github.com/satnamkhowal/grootacademy.com/pull/664): CSS hexadecimal escape terminators must consume CRLF as one unit. The prior normalizer consumed CR only, left LF, and could miss a URL function even though tinycss2 tokenized it as an external URL. Regex now handles CRLF atomically; the regression fixture contains an actual CRLF.
- Coordinator-equivalent local unit suite: **11/11 PASS**. Differential fuzzing against tinycss2: **10,000 generated CSS variants, 0 external-URL bypasses after repair**; the pre-repair bypass was reproduced. These are focused local checks, not full repository CI or independent approval.
- Exact-head Actions run [43166872184](https://github.com/satnamkhowal/grootacademy.com/actions/runs/43166872184), job `131010669501`, returned `steps: null`; log retrieval returned Azure `BlobNotFound` 404. Zero assertions ran. Administrator diagnosis remains required; no blind retry.
- PR #664 head `4662082997dba40dfab6d847d609b2bb6cf8fa5c`; #507/#654/#660/#664 all remain OPEN/DRAFT with zero independent reviews. Five recovered pages remain noindex and outside registry/sitemap pending owner-approved all-five transition.
- Factory queue remains 29 IDs in the exact PR #62 order; status counts unchanged. Factory accounting remains 23 complete text drafts, 0 independently approved, 0 published; live verification remains unverified. No article, asset, queue, registry, sitemap or deployment change.
- Latest owner-scope evidence in issue #401 (11:22 IST) records 399 open PRs (365 drafts, 34 non-drafts) across the owner's listed scope; the 28 non-draft candidates checked had zero independent approvals. This is a dated snapshot, not a current complete re-audit. Central main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; PR #22 remains OPEN/DRAFT with zero independent reviews. Existing AEO/GEO PR #2 baseline is reused; Groot's active control-board row and Jaipur Engineers `je2` vs `jaipur-engieneers` mapping remain owner-reconciliation items.

No source ownership, central main, other-brand files, deployment, publication or indexing changed.
