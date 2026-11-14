# Groot Academy 100K — GA-B00029 PR #713 workflow-isolation delta

Observed: 2026-11-13 15:44 IST  
Scope: coordination evidence only; source implementation remains in `satnamkhowal/gta` / canonical GitHub repository `satnamkhowal/grootacademy.com`.

## Source-repository delta

Current source main: `986f316b5d291dd357bd1fdb54488fa79db50e51`.

Two commits since the prior `c213075` snapshot change six paths: a contact-page directions link/CSS update and a 2022 Java full-stack retrospective with registry/sitemap and 2023 related-link changes. The retrospective is not in the 29-ID controller queue and is not counted in the 23 complete controller drafts. Deployment/live verification is unknown.

### PR #713

- Existing shared-head repair PR [#713](https://github.com/satnamkhowal/grootacademy.com/pull/713) was refreshed onto current main with a force-with-lease against its exact previous head.
- Base `main@986f316`; head `c14550ebed246f29a341ec7df0b5573d452a976f`; compare 4 ahead / 0 behind; exactly four paths.
- The old unrelated Spoken English workflow modification was removed. A dedicated `.github/workflows/blog-head-base-path-qa.yml` now owns the PHP 8.0 / Python 3.12 full-checkout base-path regression.
- Local workflow YAML parse and six path-filter structural checks PASS. Previous exact-source PHP 8.4.24 lint 4/4 and Python base-path edge cases 5/5 in normal/-O/-OO are carried forward; they were not rerun because the tested source blobs are unchanged.
- New hosted workflow run `43408472143` and three path-triggered existing runs failed before steps. Job step/log retrieval returned Azure Storage `BlobNotFound` HTTP 404; zero hosted assertions are evidenced as executed. No retry was issued.
- PR #713 remains OPEN/DRAFT with zero independent reviews/threads. PHP 8.0 hosted execution, full-root/schema/route/browser/HTTP/MIME and independent release review remain pending. No merge, publication or deployment.

## Canonical 100K queue and accounting

- Canonical controller queue SHA: `2766216c3f47982fdba1934c96873a6892968ef1`.
- 29 rows, 29 unique IDs, exact `GA-B00001` through `GA-B00029` order; no queue mutation.
- Counts remain 23 complete text drafts, 23 technical visuals and 23 PHP candidates; independent editorial/code/visual PASS 22/18/23; approved/published/live 0/0/0.
- Research proposals and GA-B00014 refresh are not additional finished articles. Separate News Factory articles are outside this queue.

## Current-main governance delta

- Source `marketing/blog-factory/MASTER-PLAN.md` still supports exactly 10,000 possible IDs, not validated opportunities or a publication quota.
- Source `docs/ai-ops/MASTER_TASK_BOARD.md` keeps HAO-008 at P3/REVIEW and says to reconcile the competing framework/B0001 PRs before generating new content.
- Issue #401 defines 100,000 as conditional M4, subject to demand, expertise, coverage and server-cost evidence.
- The user's authorized controller target is 100,000/P0; master-owner alignment, one canonical queue owner and one independent release approver remain unresolved. New IDs remain HOLD.

## Central-control-plane delta

- Central main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; no central-main write.
- Current central README blob `b93187c353f8112a57fffab4b383e64236976394` lists eight brands and three active owner rows: Jaipur Engineers, Central coordination and Forsk Coding School. Groot Academy has no active owner row.
- Central PRs #1/#2/#3 remain closed/merged; reuse the existing AEO/GEO PR #2 baseline rather than recreating it.
- Jaipur Engineers `je2` social repository vs `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved; do not assume either is wrong.
- Central PR #22 remains OPEN/DRAFT on `audit/groot-ga22-browser-delta-20261112-0350`; before this append it compared 64 ahead / 0 behind, 27 changed files, zero independent reviews and zero review threads. This report is an append-only coordination successor; it does not transfer source ownership.

## Next actions

1. Administrator/storage owner diagnoses Azure Actions `BlobNotFound`; do not blindly rerun failed jobs.
2. After infrastructure recovery, run the dedicated PHP 8.0/Python 3.12 exact-head workflow and obtain independent PR #713 review.
3. Keep production full-root/schema/canonical/robots/registry/sitemap/route/browser/authorized-origin HTTP/MIME gates separate.
4. Continue GA-B00016 and GA-B00022 independent accessibility review.
5. Keep new article IDs on HOLD until Master-owner priority/capacity, queue ownership and independent release approval are explicit.

No cross-brand source changes, central-main changes, self-approval, self-merge, deployment, publishing or mass indexing.
