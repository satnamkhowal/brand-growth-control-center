# Groot Academy 100K — Run 109 coordination delta

**Date:** 18 November 2026, 18:43 IST  
**Source repository:** [satnamkhowal/gta](https://github.com/satnamkhowal/gta) — verified redirect to [satnamkhowal/grootacademy.com](https://github.com/satnamkhowal/grootacademy.com), repository ID `1375760757`. Brand: Groot Academy; domain: `grootacademy.com`.

## Source QA delta

- Existing [source PR #855](https://github.com/satnamkhowal/grootacademy.com/pull/855) branch `qa/recovery-five-jsonld-propagation-guard-20261118-run95` compares IDENTICAL to exact head `16ef59949b4de4c149fad023ebf4742246e29335`; two QA files only, 0 independent reviews and 0 review threads.
- Added a bounded independent-parser smoke using RDFLib 7.5.0 with inline JSON-LD contexts: **12/12 expected node-count cases PASS** across type maps, nested property nodes, reverse/list/set/index/id/graph containers, Organization and `@none` controls, `@json` literal exclusion, and `@nest` same-node behavior.
- This is not the W3C JSON-LD test suite, the committed 111-method repository suite, PHP 8.0, hosted CI, or independent approval. Local runtime has Python 3.13.5 and PHP 8.4.24; PHP 8.0 is unavailable.
- Latest recorded exact-head Actions run [44303621580](https://github.com/satnamkhowal/grootacademy.com/actions/runs/44303621580) failed before steps with Azure BlobNotFound HTTP 404; hosted assertions 0. No retry; administrator diagnosis required.
- A non-approval evidence comment was added to PR #855. No QA helper/test source change in this run.

## Current source Main

- Current Main advanced from `f9c900e64baa3979e50c04e7293e246369e8f4b5` to `861ad5028e6341b9ae420c62287a082833bfd79d`.
- The one-commit delta changes only `assets/css/groot-alumni.css` (+2 / -0), aligning alumni-card action placement.
- No blog-factory, article, queue, shared blog layout, registry or sitemap overlap. No Main write.

## Queue and production ledger

- Original controller branch, verified Run 108 successor, and active canonical queue were read. The active writable queue remains on `content/groot-100k-controller-20261116-run61-main-delta`, SHA `0b0685b89c8833f9f8b49d7e223c166145082956`; 29 ordered IDs remain intact. Planning PR #62's 29 IDs and Research PR #68's 14 proposals plus GA-B00014 refresh remain preserved. No queue write.
- 23 complete drafts / 23 technical visuals / 23 PHP candidates.
- Independent editorial/code/visual PASS: 22 / 18 / 23.
- Fully approved / published / live verified: **0 / 0 / 0**.
- GA-B00006 remains PUBLISH_PR; #507 → #654 → #660 → #664 recovery and #782/#785/#755 review/release gates remain open. Four PHP/metadata differences remain. No new article/image/PHP candidate, registry/sitemap update, deployment, publication or indexing.

## Central control-plane delta

- Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; README blob `b93187c353f8112a57fffab4b383e64236976394`.
- PR #1/#2/#3 remain merged; reuse the existing AEO/GEO PR #2 baseline.
- PR #28 remains OPEN/DRAFT; unsafe merge-all workflow is still on Main and was not triggered.
- Eight brands are registered, only three active control-board rows exist. Groot Academy 100K/P0 owner, canonical queue writer and independent release approver remain missing.
- Jaipur Engineers `je2` social vs `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved; no owner or repository reassignment.

## Exact next actions

1. Independent review of PR #855 and the #840/#755 date-contract chain.
2. Actions/storage administrator diagnoses Azure BlobNotFound before any retry; then full committed suite, W3C JSON-LD conformance harness and PHP 8.0.
3. Source owner refreshes GA-B00006 #507 against Main `861ad502`, reconciles #654 → #660 → #664 and #782/#785, and closes the four metadata differences plus exact-Main release gates.
4. Central owner records one Groot 100K/P0 owner, one canonical queue writer and one independent release approver.
5. Keep new IDs/batches HOLD pending independent release and governance gates.

No Central Main write, ownership reassignment, other-brand source change, merge, deployment, publication or mass indexing.
