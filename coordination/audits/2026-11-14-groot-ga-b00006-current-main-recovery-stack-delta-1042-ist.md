# Groot Academy — GA-B00006 current-main and recovery-stack coordination delta

**Observed:** 14 November 2026, 10:42 IST  
**Central repository:** `satnamkhowal/brand-growth-control-center`  
**Central base:** `main@21af139cc32a7b67aab6908c61edeb5998bd4544`  
**Coordination PR:** [#22](https://github.com/satnamkhowal/brand-growth-control-center/pull/22), branch `audit/groot-ga22-browser-delta-20261112-0350`  
**Source repository:** `satnamkhowal/grootacademy.com` (requested alias `satnamkhowal/gta` returns 301 Moved Permanently; canonical repo ID `1375760757`)  
**Source controller:** `content/groot-100k-controller-20261016`

## Delta-only review

Read current central Main README, the prior 2026-11-13 GA-B00029 coordination report, central PR #22 metadata/reviews, source Main, controller README/CONTROLLER/queue, source PRs #507/#625/#654/#660/#664/#713, planning PR #62 and research PR #68. No full site crawl, source code re-execution, central Main write or other-brand source write was performed.

## Source Main and recovery dependencies

Groot Main advanced from `3c4c18e78808b600f606be76ccd8ae6498029ef2` to `9dfa886e74b350bcc0e2d58630eba139c4d63f74` through one commit changing only `assets/css/groot-programs-home.css` (homepage mobile course-filter styling). No blog/recovery/shared-head/registry/sitemap overlap.

| PR | Direct Main compare / parent compare | State | Independent reviews |
|---|---|---|---:|
| #507 | 4 ahead / 30 behind; 22 historical additions | OPEN/DRAFT | 0 |
| #654 | 5 ahead / 0 behind #507 | OPEN/DRAFT | 0 |
| #660 | 10 ahead / 0 behind #654 | OPEN/DRAFT | 0 |
| #664 | 13 ahead / 0 behind #660 | OPEN/DRAFT | 0 |
| #625 | 7 ahead / 30 behind; 4 paths | OPEN/DRAFT | 0 |
| #713 | 12 ahead / 4 behind; 4 paths | OPEN/DRAFT | 0 |

Merge-base path intersections are zero for #507 (40 Main-side paths vs 22 recovery paths), #713 (5 vs 4), and #625 (40 vs 4). This is path-level evidence only; it does not replace owner-controlled base refresh, exact-head CI or independent review.

The three #625/#713 shared blobs were re-fetched from both current PR heads and remain byte-identical:
- shared partial `5d6b335ce573cb9baefa94a167bbe22f4f226f5f`;
- PHP fixture `94e3b8556e9ae1087c451720078f33538fe047a6`;
- Python regression `935a48a1455ee600e2fc8b166ab98c533a0ac4b3`.

Keep #625's Spoken English workflow and #713's focused base-path workflow; integrate the three shared files once, under their source owners' decision. No source PR branch was modified. Existing Azure Actions `BlobNotFound` zero-step failures remain a storage/admin blocker; no blind retry was run.

## Controller queue and planning lineage

- Canonical queue blob `c12a915e06c8100a350b21338311651df0f35094`; current queue matches the original planning PR #62 queue **29/29 IDs in identical order**.
- Status distribution: MERGE 3, REFRESH 2, IDEA 1, PUBLISH_PR 5, TECH_QA 17, CONTENT_QA 1.
- Research PR #68 proposal CSV has 15 rows: 14 RESEARCH/proceed proposals and GA-B00014 REFRESH. They are not completed articles or new IDs.
- GA-B00006 remains PUBLISH_PR. Prior exact-source/Python/PHP fixture evidence is preserved; full-root/runtime/browser/HTTP release gates and independent release approval remain pending.
- Controller counts unchanged: 23 complete drafts, 23 technical visuals, 23 PHP candidates; independent component PASS editorial/code/visual 22/18/23; full release approvals 0, published 0, live verified 0.

## Central ownership and governance

- Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; current README still lists eight brands and only three active owner/status rows. Groot Academy's dedicated row is missing.
- Central PRs #1/#2/#3 are CLOSED/MERGED. Existing AEO/GEO baseline #2 remains the source of truth; no replacement queue was created.
- Jaipur Engineers `je2` social vs `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. Preserve both candidate roles pending explicit mapping evidence; no assumption either is wrong.
- Current Groot Main `docs/ai-ops/MASTER_TASK_BOARD.md` still categorizes Blog Factory/Web Stories/routine social as P3/hold. `marketing/blog-factory/MASTER-PLAN.md` supports 10,000 possible IDs, not validated opportunities. Issue #401 defines 100K as evidence-gated M4 and 1M as conditional M5. The user's 100K/P0 mandate remains recorded, but Master-owner alignment, one queue owner, one independent release approver and batch-growth criteria remain unresolved; new IDs stay HOLD while existing repairs continue.
- Central PR #22 remains OPEN/DRAFT, 92 commits / 47 report files, 0 independent reviews. No central Main change or ownership reassignment.

## Exact next actions

1. Source owners refresh #507 and the dependent #654 → #660 → #664 chain against current Main without regenerating historical article/asset payloads.
2. Owners decide one shared implementation for #625/#713, preserve both unique workflows, then obtain exact-head CI and independent review.
3. Actions storage administrator diagnoses Azure `BlobNotFound` before further retries.
4. Obtain independent GA-B00006 full release review and finish full-root PHP/schema, route, browser/AT and authorized-origin HTTP/MIME gates.
5. Master owner reconciles the 100K/P0 target with current task-board/ID governance and records queue owner, independent release approver and evidence-based batch criteria.

No central Main write, other-brand source change, source owner-branch rewrite, approval, merge, deployment, publication or indexing.
