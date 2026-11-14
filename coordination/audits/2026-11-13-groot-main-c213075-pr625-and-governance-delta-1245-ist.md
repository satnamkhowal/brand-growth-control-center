# Groot Academy — current-main c213075 and governance delta

**Observed:** 2026-11-13 12:45 IST  
**Source repository:** `satnamkhowal/grootacademy.com` (legacy alias `satnamkhowal/gta`)  
**Central repository:** `satnamkhowal/brand-growth-control-center`  
**Central PR:** #22, coordination-only; no source implementation copied here.

## New source-main evidence

Current Groot `main` is `c21307530ec959338b0cdb92fe2f9cc6924a63ab`. Compared with the previously recorded `e5f42a7` snapshot, it advanced 3 commits / 4 paths:

- `c213075`: catalogue search/filter reset in `courses/index.php`
- `bfc17cb`: related learning guides in Satnam faculty data/profile plus work log
- `bfa0f89`: redundant catalogue result announcement correction in `courses/index.php`

No overlap with the four net PR #625 paths or the 22 new article/asset paths in recovery PR #507.

## Source repair status

- [Groot PR #625](https://github.com/satnamkhowal/grootacademy.com/pull/625): 7 ahead / 13 behind main, merge base `813a66fa`, four net paths, zero independent reviews and zero review threads. Main's three commits do not overlap those four paths. Keep OPEN/DRAFT; owner-controlled base refresh and exact-head CI plus PHP 8.0/full-root/schema/route/HTTP/MIME review remain.
- [Groot PR #507](https://github.com/satnamkhowal/grootacademy.com/pull/507): 4 ahead / 13 behind, 22 additions, no modifications/deletions. It remains a draft recovery package, not publication. Keep dependent #654/#660/#664 owner-coordinated; no blind merge.
- The isolated 100K controller branch has no common ancestor with current main. No rebase/merge was attempted.

## Governance and accounting

- Main `marketing/blog-factory/MASTER-PLAN.md` says 10,000 possible IDs, not validated opportunities or a quota.
- Main `docs/ai-ops/MASTER_TASK_BOARD.md` remains HAO-008 / P3 / REVIEW and requires reconciling competing blog-factory/B0001 PRs before new content.
- Main `marketing/blog-factory/CONTROLLER.json` is an old 2026-10-20 snapshot with 11 drafts; it is not the user-authorized 100K controller ledger.
- User-authorized isolated controller remains 100K/P0. Issue #401 defines 100K as M4 and 1M as conditional M5. No explicit Master-owner reconciliation, canonical queue owner or independent release approver is recorded in the latest available comments through 11:32 IST. New batches remain HOLD.
- Canonical queue remains 29/29 in original PR #62 order, SHA `2766216c3f47982fdba1934c96873a6892968ef1`; PR #68 remains 14 proposed proceed decisions plus GA-B00014 refresh. Counts remain 23 complete drafts, 23 technical visuals, 23 PHP candidates; independent approvals/published/live 0/0/0.

## Central coordination state

- Central main: `21af139cc32a7b67aab6908c61edeb5998bd4544`; unchanged.
- [Central PR #22](https://github.com/satnamkhowal/brand-growth-control-center/pull/22): 57 ahead / 0 behind, 23 coordination-report files, zero independent reviews; OPEN/DRAFT.
- PRs #1/#2/#3 are closed; reuse the existing AEO/GEO baseline from #2.
- Central README lists eight brands but only three active owner/status rows; Groot's active row is missing.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. No ownership transfer is inferred.

## Next action

Source owner: refresh/reconcile PR #625 and obtain independent technical review; complete GA-B00016/GA-B00022 manual AT and production-page gates; request Azure Actions storage administrator diagnosis. Master owner: resolve 10K/P3 versus 100K/P0 and name one queue owner plus independent release approver. Source implementation remains in the Groot repository.

No central-main write, source owner reassignment, self-approval, self-merge, deployment, publication or mass indexing occurred.
