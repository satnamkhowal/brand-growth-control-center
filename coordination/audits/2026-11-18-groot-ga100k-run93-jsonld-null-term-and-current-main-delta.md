# Groot Academy 100K — Run 93 central coordination delta

**Date:** 2026-11-18 03:43 IST  
**Scope:** coordination evidence only; source implementation remains in the Groot Academy repository.

## Verified repository and source delta

- Canonical user alias `satnamkhowal/gta` resolves to `satnamkhowal/grootacademy.com`, stable repository ID `1375760757`.
- Groot current Main: `388e4a7058ce02897110b3ed114ccd441e2a5875`. Latest commit is outside `marketing/blog-factory`; no article/shared-head/registry/sitemap/queue overlap.
- Controller successor PR #846 head: `6ce2d57beca61aad6c8aef3d53905afc68ff48eb`; Run 93 checkpoint is proposed in child PR #850.
- QA child PR #849 head: `fb6f952dde4f26ee0dbba962bf517493dea5a9cd`, based on exact #848 head `e97e56eb2d47e4bdb562d3edfb03e703799ddf15`. It closes two reproduced false positives in the JSON-LD BlogPosting predicate: slash-normalized schema.org context lookalikes and explicit null term fallback to `@vocab`.
- Coordinator-side focused Python 3.13.5 helper differential: 18/18 expected outcomes. This is not the committed full suite, PHP 8.0, hosted CI or independent approval. PR #849/#848/#847 have zero submitted reviews.
- Parent #847 Actions run 44166227355/job 134332904835 failed before steps; Azure BlobNotFound HTTP 404, hosted assertions 0. Administrator/storage-owner diagnosis is still required; no retry.
- GA-B00006 remains `PUBLISH_PR` with four PHP/metadata differences; independent #755 date-less/noindex approval is still a prerequisite.

## Canonical queue and ledger

- Active queue SHA: `0b0685b89c8833f9f8b49d7e223c166145082956`.
- 29 original IDs, exact order preserved. Queue status distribution: MERGE 3, REFRESH 2, IDEA 1, PUBLISH_PR 5, TECH_QA 17, CONTENT_QA 1.
- 23 complete drafts / 23 technical visuals / 23 PHP candidates.
- Independent editorial/code/visual PASS: 22/18/23.
- Fully approved / published / live verified: 0/0/0.
- No new article, image, PHP candidate or queue write in Run 93. Research PR #68's 14 proceed proposals and GA-B00014 in-place refresh remain preserved; planning PR #62's 29 IDs remain intact.

## Central Main and open PR delta

- Central Main latest commit remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; no newer Main commit observed.
- PRs #1/#2/#3 are CLOSED/MERGED. Reuse PR #2's existing AEO/GEO baseline; no duplicate baseline created.
- PR #27, #28 and #29 remain OPEN/DRAFT.
- Central README currently lists eight brands but only three active control-board rows. Groot 100K/P0 accountable owner, canonical queue writer and independent release approver remain unrecorded.
- PR #28 proposes deleting `.github/workflows/merge-all-open-prs.yml`; it remains Draft. The unsafe workflow is still on Main and was not triggered.
- Jaipur Engineers `je2` social workstream vs `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. Preserve both workstream owners; do not infer either repository is wrong.

## Ownership, gates and next action

1. Central owner records one accountable Groot 100K/P0 owner, one canonical queue writer and one independent release approver.
2. Independent reviewers review source QA chain #849 → #848 → #847, then existing recovery/date parents in order.
3. Administrator/storage owner diagnoses Azure Actions pre-step/log-storage failure.
4. Source owner resolves GA-B00006's four metadata differences only after independent #755 approval, then completes exact-Main PHP/schema/H1/canonical/robots/route/registry/sitemap/browser/accessibility/HTTP/MIME gates.
5. Central mapping owner reconciles Jaipur repository roles with deployed-origin evidence.

No Central Main write, source implementation in another brand, owner reassignment, merge, deployment, publication or indexing occurred.


### Run 93 follow-up — 2026-11-18 03:43 IST

- Two additional committed tests cover an inherited null term inside `@graph` and a child-context mapping that overrides that inherited null term. Coordinator-side graph differential 3/3; combined focused helper differential 18/18.
- QA PR #849 latest head is `e6ee0c5fce422f336f362ffd8a6cb3c3c56151eb`; it remains OPEN/DRAFT with no independent review. Controller checkpoint PR #850 is OPEN/DRAFT.
- No queue or article changes. The 29-ID queue and 23/23/23 draft/visual/PHP-candidate ledger remain unchanged; approved/published/live remain 0/0/0.


### Run 93 queue reconciliation

The original planning branch, active controller successor and current Main all retain the same 29 IDs/order. Queue SHAs: original `c12a915e06c8100a350b21338311651df0f35094`; active canonical `0b0685b89c8833f9f8b49d7e223c166145082956`; Main `a42107125efd657e21f29face2b3e0392c165376`. Main's status distribution is MERGE 3 / REFRESH 2 / IDEA 13 / TECH_QA 10 / CONTENT_QA 1 and its controller snapshot reports 11 drafts. Active canonical status distribution is MERGE 3 / REFRESH 2 / IDEA 1 / PUBLISH_PR 5 / TECH_QA 17 / CONTENT_QA 1 and its controller reports 23 drafts. Do not overwrite the active queue from Main. No queue write.
