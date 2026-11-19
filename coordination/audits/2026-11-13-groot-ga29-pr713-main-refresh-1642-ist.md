# Groot Academy — GA-B00029 current-main refresh coordination delta

Observed: 2026-11-13 16:42 IST  
Scope: coordination evidence only. Source implementation remains in the verified private Groot Academy repository (ID 1375760757), currently named `satnamkhowal/grootacademy.com`; legacy alias `satnamkhowal/gta` permanently redirects to it.

## Source repository delta

- Current source main: `b353916bb36732e3b82b85282a59e2a5beb9853f`.
- Since the 15:44 checkpoint `986f316b5d291dd357bd1fdb54488fa79db50e51`, two commits landed: `efaec429` (2024 Java retrospective plus registry/sitemap/related-link changes) and `b353916` (contact WhatsApp prefill).
- Neither touches the four GA-B00029 shared-head repair paths.

## PR #713 refresh

- Existing source PR [#713](https://github.com/satnamkhowal/grootacademy.com/pull/713) was refreshed by a two-parent merge commit `de09fd53050a0269253bbdb1d7fed627b75c4475`: current main as first parent, previous PR head `c14550e` as second parent. The existing branch ref was advanced with expected-head compare-and-swap; main was not modified.
- Direct current-main → PR-branch compare: 5 ahead / 0 behind; four intended net paths:
  1. `.github/workflows/blog-head-base-path-qa.yml`
  2. `blogs/_shared/partials/head.php`
  3. `marketing/blog-factory/tests/blog-head-base-render.php`
  4. `marketing/blog-factory/tests/test_blog_head_base_path.py`
- **Outstanding GitHub PR metadata discrepancy:** PR API still reports base SHA `986f316` and nine changed filenames, while direct compare against current main reports four intended paths. PR remains OPEN/DRAFT; independent reviewer must verify the displayed diff before review. Do not treat the API mismatch as resolved.

## Hosted CI blocker

Four automatic exact-head runs on the refreshed branch failed before any step:
- [Blog shared-head QA 43415453466](https://github.com/satnamkhowal/grootacademy.com/actions/runs/43415453466)
- [Blog factory QA 43415453454](https://github.com/satnamkhowal/grootacademy.com/actions/runs/43415453454)
- [Spoken English route QA 43415453430](https://github.com/satnamkhowal/grootacademy.com/actions/runs/43415453430)
- [Markdown parity 43415453335](https://github.com/satnamkhowal/grootacademy.com/actions/runs/43415453335)

All jobs have `steps=null`; each log retrieval returned Azure Storage `BlobNotFound` HTTP 404. Zero hosted assertions executed. Administrator/storage-owner diagnosis is required; no blind retry. Earlier local Python 5/5 normal/-O/-OO and PHP 8.4.24 lint 4/4 are unchanged prior evidence, not hosted PHP 8.0 proof.

## Controller and release accounting

- Canonical queue SHA remains `2766216c3f47982fdba1934c96873a6892968ef1`: 29 rows, 29 unique IDs, GA-B00001–GA-B00029.
- Counts unchanged: 23 complete drafts, 23 technical visuals, 23 PHP candidates; independent editorial/code/visual PASS 22/18/23; approved/published/live 0/0/0.
- No new article, image, ID, source publication or deployment in this run.
- New IDs remain HOLD pending explicit Master-owner alignment, one canonical queue owner and one independent release approver.

## Central control-plane reconciliation

- Central main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; no central-main write.
- Central README blob `b93187c353f8112a57fffab4b383e64236976394` lists eight brands but only three active owner rows (Jaipur Engineers, Central coordination, Forsk Coding School); Groot Academy's dedicated owner row remains missing.
- Central PRs #1/#2/#3 are closed/merged; reuse the existing AEO/GEO PR #2 baseline.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. Preserve ownership; do not infer either mapping is incorrect.
- Central PR #22 remains OPEN/DRAFT, branch `audit/groot-ga22-browser-delta-20261112-0350`, 65 commits ahead / 0 behind, 28 changed report files, zero independent reviews/threads. This report adds bounded coordination evidence only; source changes stay in Groot's repository.

## Next action

1. Independent reviewer/owner resolves PR #713's stale base/diff metadata and confirms only four intended paths.
2. Repository Actions/storage administrator diagnoses Azure `BlobNotFound`.
3. After infrastructure recovery, exact-head PHP 8.0/Python 3.12 workflow, then full-root/schema/route/browser/authorized-origin HTTP/MIME and independent release gates.
4. Continue GA-B00016/GA-B00022 independent accessibility reviews.
5. Master owner records the 100K/P0 versus 10K/P3/M4 alignment, queue owner and independent release approver before new IDs.

No central-main changes, cross-brand source changes, owner reassignment, self-approval, self-merge, publication, deployment or mass indexing.
