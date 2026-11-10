# Groot Academy 100K lane delta — GA-B00022 browser runtime evidence — 2026-11-10 18:43 IST

## Repository identity and ownership
- The requested `satnamkhowal/gta` name resolves to the same private GitHub repository ID now named `satnamkhowal/grootacademy.com`; the current repository name is `grootacademy.com`. This is the Groot Academy source repository, not Mango Engineers.
- Source implementation remains in the Groot repository. This report is coordination-only and is committed on the existing draft PR #18 branch.
- Central PRs #1, #2 and #3 are merged. Reuse PR #2's existing all-brand AEO/GEO baseline and queue; do not recreate them.

## New implementation evidence
- GA-B00022 `quiz-lab.html` exact Git blob `f89635f8c11415dc98d82f902b4769c9c9239877` (SHA-256 `e99aef31f891593350bd8bfaecd409853fe1fd896e5cd11f37c3dd74dc0a3fd1`) was exercised locally with Python 3.13.5, Playwright 1.57.0 and Chromium 144.0.7559.96.
- 34 interactive browser/layout assertions PASS; 18 Chromium accessibility-tree assertions PASS; 16 real headed desktop-zoom assertions PASS at 200%/400%; four forced-colors focus assertions PASS. Total: 72 local runtime assertions.
- Desktop zoom was sent through X11/XTest. At 200%, DPR 2 / innerWidth 640; at 400%, DPR 4 / innerWidth 320; `visualViewport.scale=1` at both and no horizontal overflow was observed.
- The exact lab was loaded with `page.set_content`, not via the production route. No manual screen-reader/AT announcement test, production navigation, independent approval, PHP/schema/HTTP release or publication is claimed.
- Groot canonical queue remains 29/29 IDs. Current counts remain 23 complete original drafts, 23 authored technical visuals, 23 PHP candidates, 0 independent publication approvals and 0 live-verified articles. GA-B00022 stays `TECH_QA`, `noindex,follow`, `publication_approved=false`.
- Full QA report: `marketing/blog-factory/work/B0002/qa/GA-B00022-browser-runtime-20261110-1843-ist.md` on Groot PR #569.

## Current coordination and release gates
- Groot main `99336e8d0b412f6e0f0bdc0464e0aec4b8fea2b5` still lists HAO-008 Blog Factory as P3/REVIEW. Its instruction is to reconcile the competing framework and B0001 PRs before generating new content. The controller's P0 target therefore remains a Master-owner priority conflict; do not bypass the hold or start a new batch/GA-B00005 brief without the Master decision.
- Groot PR #569 remains Draft on `qa/groot-100k-current-main-20261109`, head `38e08cf05d1eefee533481be31052552674dc96b`, 152 commits ahead / 2 behind main, 211 changed files, independent reviews 0. It is not approved or merged.
- Recovery PR #533 remains an owner-held stacked Draft; its shared layout/CSS overlap with current main still requires owner-led rebase and manual reconciliation. Do not edit the recovery owner's files or merge the stack independently.
- Central README lists eight brands but its active board has only three rows and no Groot row. Preserve central ownership; request a Master-owned mapping/board update rather than editing another brand's implementation.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website mapping remains unresolved; do not infer that either repository is wrong.
- Central PR #17, #18 and #20 remain separate Draft audit workstreams. No central main change, source deployment, merge or publishing occurred in this delta.

## Exact next action
- Obtain an independent screen-reader/AT and production-page review for GA-B00022.
- Continue GA-B00029 full-root PHP rendering and four authorized-origin HTTP/MIME checks on a network-enabled runner.
- Recovery owner reconciles PR #533's two shared-file overlaps on the full stack.
- Master owner resolves HAO-008 P3/REVIEW versus the requested P0 controller target and confirms queue disposition before new article work.

