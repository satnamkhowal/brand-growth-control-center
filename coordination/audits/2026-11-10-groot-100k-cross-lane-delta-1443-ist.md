# Groot Academy 100K / News Factory cross-lane audit delta

**Checked:** 10 November 2026, 14:43 IST  
**Central main snapshot:** `31af61b9a796472b7eb13d6b254aa6d9dc2ecc34`  
**Scope:** coordination-only; no source implementation or ownership reassignment.

## Repository and workstream mapping

- Canonical brand: Groot Academy, domain `grootacademy.com`.
- GitHub repository alias `satnamkhowal/gta` redirects to `satnamkhowal/grootacademy.com` (same repository identity recorded in PR #17).
- Canonical 100K controller source branch: `content/groot-100k-controller-20261016`.
- Verified successor: `qa/groot-100k-current-main-20261109`.
- Central News Factory remains a separate workstream; its drafts under `docs/news-factory/` are not automatically members of the 100K Blog Factory queue.

## New cross-lane deduplication evidence

Groot Academy News Factory [PR #602](https://github.com/satnamkhowal/grootacademy.com/pull/602) proposes a Google Maps in AI Studio / store-locator prototype guide.

- Compared the proposal with all 29 canonical Blog Factory queue IDs, the current-main blog registry, and repository search for Google Maps / store-locator / Places / Routes terms.
- No overlap with the existing 29 reader intents was identified. This is a queue/registry/source check, not an exhaustive legacy-URL crawl or demand estimate.
- PR #602 contains only three `docs/news-factory/` paths. Its branch is 6 commits ahead / 1 behind current main; the main-only commit is PR #601's planning-only `docs/student-platform/` change. No 100K queue, production PHP, registry, sitemap, route or shared schema path overlap was observed.
- The PR body has an internal word-count conflict: 2,751 words in the summary and 2,659 in the validation section. The committed Markdown count should be reconciled before independent editorial review.
- PR #602 is open/draft/unmerged; independent source/editorial QA, responsive browser QA, live AI Studio execution and CI remain pending. No GA ID is assigned and it is not counted as a 100K article.
- PR #19's News Factory ledger references PR #602 separately; do not fold its cross-brand portfolio totals into the Groot 100K counts.

## 100K controller state

- Original and successor canonical queues: 29 rows, 29 unique IDs, identical ID sequence.
- Current controller counts: 23 complete original drafts, 23 authored technical visuals, 23 PHP candidates, 18 independent code passes, 0 independent publication approvals, 0 published/live-verified.
- GA-B00014 is an in-place refresh, not a new article.
- GA-B00029 remains TECH_QA, `noindex,follow`, `publication_approved=false`. Existing evidence includes 15/15 static cross-artifact checks, 18/18 Python test executions and local Apache 2/2 MIME checks. Production HTTP/MIME and full-root PHP rendering remain unverified.
- [PR #569](https://github.com/satnamkhowal/grootacademy.com/pull/569) is Draft at head `9c9124197058b750adc157574fee42eba25c5d04`, 117 ahead / 2 behind current main, 204 changed files, 0 reviews and 0 review threads. No rebase or merge.
- Current Groot main `99336e8d0b412f6e0f0bdc0464e0aec4b8fea2b5` still marks HAO-008 Blog Factory P3/REVIEW. The user-authorized controller retains its P0 goal; central ownership and Master priority are not overridden here.

## Central coordination delta

- Central main: `31af61b9a796472b7eb13d6b254aa6d9dc2ecc34`.
- PRs #1, #2 and #3 are merged. Reuse the existing AEO/GEO baseline in PR #2.
- PRs #17, #18 and #19 remain open/draft; PR #19 is the separate News Factory ledger.
- Central README lists eight brands; the active control-board currently has three rows and no active Groot row. This remains a visibility gap for the central owner, not an ownership reassignment.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website mapping remains unresolved; neither is presumed wrong.

## Blockers and exact next action

1. Master owner resolves HAO-008 P3 versus controller P0 priority and queue disposition before a new 100K batch or GA-B00005 brief.
2. Repository Actions administrator diagnoses PR #569's repeated pre-step failures (`steps=null` / `BlobNotFound`); no CI result is inferred and no blind retry is requested.
3. Authorized PHP/network runner executes GA-B00029 with full current-main root includes and verifies all four manifest endpoints plus Content-Type.
4. Obtain independent review of PR #569 and the existing GA-B00006–GA-B00010 recovery stack; no self-approval or merge.
5. PR #602 owner reconciles the word count and completes separate editorial/responsive QA.

**No main write, source implementation, queue change, priority change, merge, deployment, publication, indexing or owner reassignment occurred in this audit.**
