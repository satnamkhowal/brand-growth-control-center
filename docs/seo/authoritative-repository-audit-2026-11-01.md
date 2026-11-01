# Seven-brand authoritative repository audit — 2026-11-01

Status: **coordination evidence only**. This document does not publish, deploy, index or rank a page.

## Decision summary

| Brand | Website | Repository decision | Evidence and boundary |
| --- | --- | --- | --- |
| Jaipur Engineers | https://jaipurengineers.com/ | `satnamkhowal/je2` — VERIFIED | Existing continuous-growth checkpoint and merged/open SEO history identify this as the owned implementation repository. |
| Groot Academy | https://grootacademy.com/ | `satnamkhowal/gta` — VERIFIED | Existing controller and review-only blog-factory work already own this lane. No duplicate content task was opened. |
| Forsk Coding School | repository canonical requires per-page verification | `satnamkhowal/forsk-coding-school` — VERIFIED | Existing hourly SEO/GSC work and open draft companions own this lane. No duplicate task was opened. |
| Mango Engineers | https://mangoengineers.com/ | `satnamkhowal/mangoengineers.com` — VERIFIED | Repository README and project instructions identify the Mango Engineers training site. |
| Clever Ape Academy | https://cleverapeacademy.com/ | `satnamkhowal/clp` — VERIFIED | Current repository identity uses the academy domain. Never redirect to or reuse unrelated `cleverape.in`. |
| Swiggy Wala | https://swiggywala.com/ | **BLOCKED — do not implement yet** | Both candidate repositories contain plausible current PHP taxi implementations. The live origin could not be fetched in this run, and search did not expose a distinctive current homepage signature. Do not modify or merge either candidate until hosting/deployment authority is evidenced. |
| CadMate India | https://cadmateindia.com/ | `satnamkhowal/CadMateIndia` — **VERIFIED AUTHORITATIVE IMPLEMENTER** | Live homepage and repository source match the same current title, H1, course tracks, central enquiry language, two Jaipur locations, phone and footer positioning. `satnamkhowal/cadmateindia.com` is a legacy static WordPress/HTTrack-style mirror with a different historical Yoast title and is not the current implementation owner. |

## CadMate evidence

Live evidence checked 2026-11-01:

- https://cadmateindia.com/ rendered title: “CadMate India | CAD Training Institute in Jaipur | AutoCAD, Revit, SolidWorks & BIM”.
- Live H1: “CAD Training Institute in Jaipur for CAD, BIM & Engineering Design”.
- Live body contains three current learning tracks, “One centralized enquiry form”, Mansarovar and Shyam Nagar locations, phone `8690047091`, and the 2026 footer.
- `satnamkhowal/CadMateIndia/index.php` at main `423bdad8cb4318b161897301988d6b25da6ea93c` contains the same title, H1, central-form copy and current structure.
- `satnamkhowal/cadmateindia.com/index.html` at main `1c2e35f8a4d386960dae6ec05958c3d8ab206d6e` is a large static capture whose title starts “Cad Mate INDIA - AutoCAD Course Training Classes in Jaipur” and references Yoast/WordPress assets. It does not match the current live homepage.

Decision: future CadMate SEO/content/graphics implementation belongs only in `satnamkhowal/CadMateIndia` unless fresh deployment evidence supersedes this audit.

## Swiggy Wala evidence and blocker

Candidate A, `satnamkhowal/swiggy-wala-new-website` main `79f956943cbf5c35a59b4ead26cf577241d6120b`, has a current PHP homepage titled “Jaipur Taxi Booking & Rajasthan Cabs | Swiggy Wala”.

Candidate B, `satnamkhowal/swiggy-wala-website` main `130fb948b797b8e5b50ffc309ea5a55e3ec3913c`, has a different current PHP homepage titled “Jaipur Taxi & Cab Service | Airport, Local & Outstation | Swiggy Wala”, plus one open airport-guide PR.

The live domain was not retrievable through the available public fetch path, and no search result exposed either exact current signature. Repository recency is not deployment evidence. Required unlock evidence is one of:

1. hosting deployment configuration naming the source repository/ref;
2. a live-only fingerprint that exactly matches one candidate;
3. owner-confirmed deployment repository and branch.

Until then: no new route, redirect, sitemap, image or merge in either candidate.

## Jaipur Engineers continuation state

- Main: `d33aee5d0a5116bc80296dca305421a94f6358f5`.
- Growth checkpoint: `837f4b8e44213e590bb91e98dfd28e96bf7259f8`.
- PRs #2, #3, #24, #26 and #28 are merged.
- PR #15 remains open at `041c2bfadb1729a9647509846d8ab024cd3197b4`, but is 317 commits behind current main and now overlaps shared templates and sitemap work. It is not merge-ready.
- PR #27 is the separate social lane and remains out of this SEO/content implementation scope.
- Image workflow was read. No new image was generated because no audited page-specific need was approved in this batch.

## Measured portfolio ledger for this bounded run

All counts are deltas for this run, not lifetime totals. `UNKNOWN` means no authenticated measurement was available.

| Brand | Main SHA inspected | Topics claimed | Drafted | Fact-checked | QA passed | Brand commits | Brand PRs opened | Merged | HD images | Optimized images | Deployed | Live verified | GSC indexed observed | Blocker / next action |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- | --- |
| Jaipur Engineers | `d33aee5d` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | UNKNOWN | 0 | UNKNOWN | Reconcile PR #15 against current shared-template/sitemap ownership before any merge. |
| Groot Academy | `a09aec2e` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | UNKNOWN | 0 | UNKNOWN | Existing PR #405/review-only ecosystem owns production; no duplicate lane. |
| Forsk Coding School | `134e95dd` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | UNKNOWN | 0 | UNKNOWN | Existing SEO task and 22 open PRs; no duplicate lane. |
| Mango Engineers | `af954f7b` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | UNKNOWN | 0 | UNKNOWN | 44 open PRs; claim only after task-board/route ownership review. |
| Clever Ape Academy | `dd0803bb` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | UNKNOWN | 0 | UNKNOWN | Two open PRs; preserve exact academy domain and existing review gates. |
| Swiggy Wala | both candidates inspected | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | UNKNOWN | 0 | UNKNOWN | Authoritative implementer BLOCKED; obtain deployment evidence. |
| CadMate India | `423bdad8` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | UNKNOWN | 1 homepage | UNKNOWN | Implementer now locked; next batch may inventory current blog/graphics queues before claiming one topic. |

Daily 100-per-brand aspiration progress in this run: **0/100 each**. This is intentionally not padded with thin content. The only completed output is an evidence-backed repository-authority decision and control-plane ledger.

## Quality policy basis

Checked 2026-11-01:

- Google people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Google spam policies / scaled content abuse: https://developers.google.com/search/docs/essentials/spam-policies
- Google image SEO best practices: https://developers.google.com/search/docs/appearance/google-images

Large-volume production must remain subordinate to original value, factual accuracy, independent review and actual indexing/lead evidence. A prompt is not an image; a commit is not deployment; sitemap inclusion is not indexing.

## Bounded continuation checkpoint — 2026-11-01, 15:19 IST

Jaipur Engineers PR #15 was reconciled from 365 commits behind to current main `009658fac7383a73099d5933a1619c96fba061e7` with non-forced merge head `de9d00680c77a32e4cef54f813673253cd9948ca`. Three-way edit inspection found zero overlaps in the shared templates and sitemap. The PR is now open, mergeable and 0 behind main with exactly six intended files.

Exact-head evidence:
- Java chooser PHP lint and four-route contract: PASS, run https://github.com/satnamkhowal/je2/actions/runs/41294895413
- Spring Boot idempotency regression: PASS, run https://github.com/satnamkhowal/je2/actions/runs/41294895417
- Communication rendered-browser job: PASS in run https://github.com/satnamkhowal/je2/actions/runs/41294895469
- Separate communication PHP-render job: BLOCKED by sparse-checkout omission of `batch-calendar/embed.php`
- GSC recovery suite: BLOCKED by an unrelated migrated DSA page linking to legacy `jaipurengineers.in`
- Merge/deployment/live/indexing: not performed / UNKNOWN

| Brand | Planned tasks | Articles drafted | Fact-checked articles | QA-passed batches | Brand commits | Existing PRs updated | New PRs | Merged | HD images | Optimized images | Deployed | Live verified | GSC indexed observed |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |
| Jaipur Engineers | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | NO | 0 | UNKNOWN |
| Groot Academy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | UNKNOWN | 0 | UNKNOWN |
| Forsk Coding School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | UNKNOWN | 0 | UNKNOWN |
| Mango Engineers | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | UNKNOWN | 0 | UNKNOWN |
| Clever Ape Academy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | UNKNOWN | 0 | UNKNOWN |
| Swiggy Wala | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | BLOCKED | 0 | UNKNOWN |
| CadMate India | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | UNKNOWN | 0 | UNKNOWN |

Daily article progress remains 0/100 for each brand. This run completed technical integration/QA rather than creating thin articles or unaudited graphics.

