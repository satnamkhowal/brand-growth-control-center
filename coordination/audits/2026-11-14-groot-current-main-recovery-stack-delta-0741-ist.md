# Groot Academy — current-main and recovery-stack coordination delta

Observed: 14 November 2026, 07:41 IST  
Scope: coordination-only; source implementation remains in the Groot Academy repository.

## Verified source identity and current main

- User's canonical alias `satnamkhowal/gta` resolves to the same GitHub repository ID as `satnamkhowal/grootacademy.com`; no Mango Engineers repository was accessed.
- Groot source main: `9c90902f3964372ff3536e311b0e4a5f356bf167`.
- Since the prior 00:41 source snapshot, PR #733 changed only `includes/faculty-data.php` and its dated log. No 100K controller queue, registry, sitemap or shared blog-head path changed.
- Latest source inventory checkpoint remains 77 registry slugs, 50 blog-sitemap URLs (1 hub + 49 articles), and 68 page-sitemap URLs. These are source counts, not live publication or indexing proof.
- Source evidence: [Groot current-main/recovery-stack report](https://github.com/satnamkhowal/grootacademy.com/blob/content/groot-100k-controller-20261016/marketing/blog-factory/work/B0002/qa/2026-11-14-current-main-and-recovery-stack-reconciliation-0741-ist.md).

## Canonical 100K queue

- Queue remains 29/29 original IDs in original order, 29 unique slugs and primary queries.
- Statuses: MERGE 3, REFRESH 2, IDEA 1, PUBLISH_PR 5, TECH_QA 17, CONTENT_QA 1.
- Research PR #68's 14 proceed proposals and GA-B00014 in-place refresh remain preserved, not counted as additional finished articles.
- Controller totals remain 23 complete drafts, 23 technical visuals, 23 PHP candidates; independent editorial/code/visual component passes 22/18/23; full approvals/published/live 0/0/0. New articles/images 0/0.

## Recovery and shared-head ownership

- PR #507 remains OPEN/DRAFT, 4 ahead / 27 behind current main, 22 net historical additions, zero independent reviews.
- Stacked PRs #654, #660 and #664 remain OPEN/DRAFT at 5/0 (2 paths), 10/0 (7 paths) and 13/0 (6 paths) against their immediate parents; zero independent reviews.
- #625 and #713 remain OPEN/DRAFT with zero reviews. Three shared files were re-fetched from both heads and their blob SHAs match exactly. #625's unique Spoken English QA workflow remains separately owned; #713 has its own base-path workflow. Preserve the #625 workflow and reconcile shared files only once.
- #713 is 12 ahead / 1 behind current main because of non-overlapping PR #733; its four net repair paths remain unchanged. No source PR branch was modified.

## Infrastructure and release gates

- The last recorded #507 retry and four #713 exact-head jobs failed before steps; Azure Storage `BlobNotFound` HTTP 404 prevented log retrieval. No hosted assertions are evidenced. No blind retry was made; administrator-level Actions storage diagnosis remains required.
- GA-B00006 component QA and coordinator-run PHP fixture do not equal full independent release approval. Full approvals remain zero.
- No merge, self-approval, deployment, publication, registry/sitemap edit or mass indexing.

## Central governance

- Central main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; README blob `b93187c353f8112a57fffab4b383e64236976394`.
- PRs #1/#2/#3 are closed/merged. Existing AEO/GEO baseline from PR #2 is reused.
- Central README still lists eight brands but only three active owner/status rows; Groot Academy's dedicated active row remains missing.
- The 2026-10-19 baseline follow-ups remain in force. Jaipur Engineers `je2` social vs `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved; neither is assumed incorrect.
- Central PR #22 remains OPEN/DRAFT, 87 ahead / 0 behind, 43 coordination report files, zero independent reviews. This report is coordination-only; no central-main write or owner reassignment.
- Master-owner decision remains pending on 100K/P0 vs 10K/P3, canonical queue owner and independent release approver.

## Next action

1. Obtain administrator-level Actions log/artifact-storage diagnosis.
2. After logs become retrievable, rerun only owned exact-head #507/#713 checks and capture actual steps/assertions.
3. Obtain independent GA-B00006 full release review.
4. Have source owners refresh #507 → #654 → #660 → #664 and reconcile #625/#713 without duplicating shared files or taking over the Spoken English workflow.
5. Keep new IDs HOLD until the Master owner records target alignment, queue ownership and independent release approval.

No source implementation, other-brand files, central main, owner assignments, publication or deployment were changed by this report.
