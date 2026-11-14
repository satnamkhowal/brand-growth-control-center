# Groot Academy — exact PR #625/#713 shared-head overlap delta

Observed: 2026-11-14 07:57 IST  
Scope: coordination-only evidence; source implementation remains in satnamkhowal/grootacademy.com (historical alias satnamkhowal/gta). No Mango Engineers repository was accessed.

## Central sources re-read

- Current central main README blob: b93187c353f8112a57fffab4b383e64236976394. It still lists eight brands but only three active owner/status rows; Groot Academy's dedicated active row is missing.
- Required baseline coordination/audits/2026-10-19-groot-lane-review.md blob: 47467f0fc1a4c922affdee1d60cff120bff78d31. Its CC-AUD-001 Jaipur mapping remains explicitly unresolved: preserve the je2 social workstream and verify the jaipur-engieneers candidate website/deployed origin rather than assuming either is wrong.
- Central PRs #1/#2/#3 remain the previously merged coordination baseline; reuse PR #2's AEO/GEO evidence and queue, do not recreate it.
- Existing central PR #22 remains the coordination-only evidence lane. Its review submission and inline-thread lists currently return zero; no central-main write or merge was made.

## New source-repository evidence

Current Groot main remains 9c90902f3964372ff3536e311b0e4a5f356bf167; the latest #733 commit changes only faculty profile data and a log, with no blog shared-head overlap.

Exact GitHub blob SHA comparison across main, refs/pull/625/head and refs/pull/713/head confirms three shared files are byte-identical between the two open source PR heads:

| Path | Main | PR #625 | PR #713 |
|---|---|---|---|
| blogs/_shared/partials/head.php | 637d161f762d52b5ed4eca8ec01244b0e3a07bc4 | 5d6b335ce573cb9baefa94a167bbe22f4f226f5f | same |
| marketing/blog-factory/tests/blog-head-base-render.php | absent | 94e3b8556e9ae1087c451720078f33538fe047a6 | same |
| marketing/blog-factory/tests/test_blog_head_base_path.py | absent | 935a48a1455ee600e2fc8b166ab98c533a0ac4b3 | same |

The workflows are distinct and both should retain their intended coverage:
- PR #625 uniquely owns .github/workflows/groot-spoken-english-qa.yml (blob 723b26b5a3ae0a659c74b56328b547556c89f616), named Groot Spoken English route QA.
- PR #713 uniquely owns .github/workflows/blog-head-base-path-qa.yml (blob 64864f20fe711c7e285bfb8f4d7ce6a0fd9bf79f), named Blog shared head base-path QA.

Reviews and inline threads were checked on source PRs #507, #625, #654, #660, #664 and #713: all currently have zero submitted reviews and zero review threads. PR #713's latest four exact-head workflow runs fail before steps; the source controller records Azure Storage BlobNotFound HTTP 404 on log retrieval and zero executed steps. Hosted assertions are therefore unverified, not a source PASS or a demonstrated source-test failure.

Detailed source report and exact continuation are committed on the Groot controller branch:
https://github.com/satnamkhowal/grootacademy.com/blob/content/groot-100k-controller-20261016/marketing/blog-factory/work/B0002/qa/2026-11-14-pr625-pr713-exact-shared-head-overlap-0757-ist.md

## Governance / ownership

- One canonical queue remains in the Groot source repository: 29/29 original planning IDs in order. Controller counts remain 23 complete drafts, 23 technical visuals, 23 PHP candidates; component passes 22 editorial / 18 code / 23 visual; independent full approvals 0, published 0, live verified 0.
- Keep #507 -> #654 -> #660 -> #664 as the source-owned recovery stack. Preserve #625's unique Spoken English route-QA workflow while source owners reconcile the three duplicated shared files with #713; this audit does not edit either owner branch.
- Administrator-level Actions log/artifact storage diagnosis remains necessary before any exact-head retry. Do not repeat blind retries.
- Master owner still needs to reconcile the user-authorized 100K/P0 target against the 10K/P3 Master Plan, name one canonical queue owner and one independent release approver before new controller IDs/batches.
- Jaipur je2 social vs jaipur-engieneers website/deployed-origin mapping remains open. No owner reassignment or website-source selection is made here.

## Exact next action

Source owners deduplicate the three shared blobs while preserving the Spoken English workflow and focused base-path coverage; Actions administrator diagnoses BlobNotFound; then obtain independent GA-B00006 full release review and refresh the historical recovery stack sequentially. Central coordinator reviews this evidence through PR #22; source implementation stays in Groot's repository.

No article, image, queue row, source production file, central main, ownership assignment, deployment, publication, indexing or ranking state changed. No self-approval or self-merge.