# Groot Academy GA-B00006 current-main render revalidation — 2026-11-14 08:43 IST

**Coordination-only evidence.** Source implementation remains in `satnamkhowal/grootacademy.com`; this report does not change any brand source repository.

## Source identity and checkpoint

- User-requested alias `satnamkhowal/gta` resolves to canonical `satnamkhowal/grootacademy.com`, repository ID `1375760757`.
- Source controller branch: `content/groot-100k-controller-20261016`.
- Source main advanced from `9c90902f` to `3beaff8df5a9f5d523acc21bd7c5e8ea3ae8fea7` at 08:39 IST; the only changed path is `assets/css/groot-learning-paths-home.css`. No blog, shared-renderer, registry, sitemap or controller path changed.
- Source checkpoint artifacts:
  - [GA-B00006 revalidation report](https://github.com/satnamkhowal/grootacademy.com/blob/content/groot-100k-controller-20261016/marketing/blog-factory/work/B0002/qa/2026-11-14-ga-b00006-current-main-render-revalidation-0843-ist.md) — commit `a367625d`.
  - [README checkpoint](https://github.com/satnamkhowal/grootacademy.com/commit/5e6ac205519c5f49c657f9c5247a96c713bb1648).
  - [Controller checkpoint](https://github.com/satnamkhowal/grootacademy.com/commit/7fcdcc44221b70216a066eabccf0cbcd83656122).

## GA-B00006 local evidence

- Original article PHP blob `9da774dbb34b7994a1dc0a8efd8f75aa0f300b3b` and `examples.py` blob `84706ec6d80b0458acd915c61943e2e477feafbe` were fetched from recovery PR #507 and their local Git blob hashes matched.
- PHP 8.4.24 article lint PASS. Python 3.13.5 fresh-process execution and `py_compile` PASS; the script printed the expected PASS line for shared default, fresh calls, caller-owned list, copy and shallow-copy boundary.
- A source-derived local PHP fixture reproduced two base elements on current-main behavior in local-preview and production-host modes. Applying the existing PR #713 one-line partial-level base removal to the fixture passed 2/2 regression cases.
- The rendered article fixture checked one H1, eight H2s, 8/8 TOC anchor matches, one canonical, `index,follow`, exactly BlogPosting + BreadcrumbList, and the executable companion plus two related internal-guide links.
- Fixture limits: root header/footer and registry were stubbed; shared includes were source-derived copies rather than a full repository checkout. This is coordinator-run evidence, not independent approval, PHP 8.0 hosted CI, full-root production render, browser/AT/CLS, image decode, HTTP/MIME or release proof.

## Current recovery stack and duplicate ownership

| PR | Current comparison | Net paths | State / reviews |
|---|---:|---:|---|
| #507 | main → recovery: 4 ahead / 28 behind | 22 | OPEN/DRAFT; 0 reviews |
| #654 | #507 → image sizing: 5 / 0 | 2 | OPEN/DRAFT; 0 reviews |
| #660 | #654 → diagram integration: 10 / 0 | 7 | OPEN/DRAFT; 0 reviews |
| #664 | #660 → release QA: 13 / 0 | 6 | OPEN/DRAFT; 0 reviews |
| #625 | main → shared-head / Spoken English: 7 / 28 | 4 | OPEN/DRAFT; 0 reviews |
| #713 | main → shared-head base-path: 12 / 2 | 4 | OPEN/DRAFT; 0 reviews |

Main has 29 commits / 37 paths since recovery merge base `813a66fa`; the 22 PR #507 recovery additions have zero path overlap. #507 metadata still references base SHA `9c90902f`, so the source owner must refresh it against `3beaff8` before exact-head review.

PR #625 and #713 share three byte-identical blobs: partial `5d6b335c`, PHP render harness `94e3b855`, and Python regression `935a48a1`. Preserve #625's unique `groot-spoken-english-qa.yml` workflow and #713's unique `blog-head-base-path-qa.yml` workflow; deduplicate shared files once under owner review. No owner PR branch was edited.

## Hosted CI blocker

The latest #507/#713 jobs still have zero steps. #507 parity job `132275095535` and #713 jobs `132109327188`, `132109327726`, `132109328316`, `132109328179` return Azure Storage `BlobNotFound` HTTP 404 on log retrieval. No hosted assertions are established. Administrator-level Actions runner/log-artifact diagnosis is required before retries; no blind rerun.

## Controller accounting

- Canonical queue remains 29/29 original PR #62 IDs, same queue blob `c12a915e`.
- Controller branch remains 23 complete original drafts, 23 technical visuals, 23 PHP candidates; independent component passes editorial/code/visual 22/18/23.
- Full independent approvals: 0. Published: 0. Live verified: 0.
- GA-B00006 remains `PUBLISH_PR`; it is not approved/live and remains outside current-main registry/sitemap pending the release gate.
- Research PR #68's 14 proceed proposals and GA-B00014's in-place refresh are not completed new articles.

## Central governance delta

- Central main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; README still lists eight brands and three active owner/status rows, with Groot Academy's dedicated row missing.
- Central PRs #1/#2/#3 are merged; existing AEO/GEO baseline #2 is reused.
- Jaipur Engineers `je2` social versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved; neither repository is assumed wrong.
- Master-owner 100K/P0 vs 10K/P3 alignment, one canonical queue owner and one independent release approver remain pending.
- Before this report, PR #22 head was `0cf7aa9bf06091214931080434e01beb7f6a80e9`, 89 ahead / 0 behind, 45 coordination report files, OPEN/DRAFT, zero independent reviews. This report is a coordination-only addition on the existing PR #22 branch.

## Exact next actions

1. Administrator diagnoses Azure Actions storage; only then rerun exact-head checks with retrievable logs.
2. Source owners refresh #507 against `3beaff8`, then sequentially review #654 → #660 → #664.
3. Source owners reconcile #625/#713's three duplicate shared blobs while preserving both unique workflows.
4. Obtain independent full GA-B00006 editorial/code/visual release review.
5. Keep new IDs HOLD until Master-owner priority/queue/release ownership decisions are recorded.

No central-main write, source-main write, cross-brand implementation, owner reassignment, self-approval, merge, deployment, publication or indexing occurred.
