# Groot Academy coordination delta — Run 118 (2026-11-19)

## Scope

Coordination-only evidence appended to the existing Groot audit successor. Central Main and every brand implementation repository remain unchanged by this report.

## Verified repository identity

- The requested source alias `satnamkhowal/gta` resolves through GitHub's permanent redirect to `satnamkhowal/grootacademy.com`, repository ID `1375760757`.
- This is one repository identity, not a second Groot/Mango implementation. Source work remains in the resolved Groot Academy repository.

## Queue and release-state reconciliation

- Original planning queue SHA `c12a915e06c8100a350b21338311651df0f35094`, active controller queue SHA `0b0685b89c8833f9f8b49d7e223c166145082956`, and current Main queue SHA `a42107125efd657e21f29face2b3e0392c165376` each contain 29 unique IDs in identical order.
- The active queue and original planning queue have matching status counts: MERGE 3, REFRESH 2, IDEA 1, PUBLISH_PR 5, TECH_QA 17, CONTENT_QA 1.
- Main is stale on 17 status values: five active PUBLISH_PR rows are TECH_QA on Main, and twelve active TECH_QA rows are IDEA on Main. The active successor queue remains canonical; do not copy Main's queue over it.
- Research PR #68 retains 14 proceed proposals and GA-B00014 as an in-place refresh; planning PR #62 retains the 29-ID source set. IDs, research decisions and refreshes are not finished articles.

## QA and approval boundary

- A coordinator-run Python 3.13.5 differential exercised the exact helper functions fetched from source PR #778 (head `56bb1622970951f0c6414d25625b8ab7803151ec`, helper blob `3e96a00d945124402b95f58c9cfc0a0edcd5889c)): 43/43 focused cases PASS.
- PHP 8.4.24 confirms PHP duplicate array keys resolve to the later value; the strict reader rejects ambiguous metadata.
- This does not constitute the committed full suite, PHP 8.0 hosted CI, independent review, or release approval. PRs #755/#760/#778/#867/#868 remain OPEN/DRAFT with zero independent reviews. Azure Actions job-log retrieval returns BlobNotFound HTTP 404; no blind retry.
- Groot factory ledger remains 23 complete drafts, 23 technical visuals, 23 PHP candidates; independent editorial/code/visual PASS 22/18/23; fully approved/published/live 0/0/0.

## Central control-board delta

- Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; current README still lists eight brands but only three active owner/status rows, with no dedicated Groot Academy 100K/P0 owner row.
- Central PRs #1/#2/#3 are merged. Reuse the existing AEO/GEO baseline from PR #2; no duplicate audit or baseline was created.
- Central PR #32 remains OPEN/DRAFT and has no independent review. No Main write or ownership reassignment.
- Jaipur Engineers `je2` social versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. Neither repository is assumed wrong.

## Required owner actions

1. Central owner records Groot Academy's 100K/P0 accountable owner, the single canonical queue writer and the independent release approver.
2. Mapping owner explicitly reconciles Jaipur social and candidate website/deployed-origin roles while preserving existing task owners.
3. Source owner refreshes the exact recovery PR stacks; Actions administrator diagnoses the pre-step BlobNotFound issue before retries.
4. Independent reviewers handle the open source QA/release PRs. No coordinator self-approval, merge, deployment, publication or indexing is implied.
