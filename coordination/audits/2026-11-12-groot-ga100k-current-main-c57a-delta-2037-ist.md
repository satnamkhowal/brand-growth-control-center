# Groot Academy 100K — current-main and central coordination delta

**Observed:** 12 November 2026, 20:37 IST  
**Source repository:** `satnamkhowal/gta` → private canonical repository `satnamkhowal/grootacademy.com`  
**Brand/domain:** Groot Academy / `grootacademy.com`  
**Scope:** delta-only; no repeated site crawl and no source implementation outside the Groot repository.

## Groot current-main delta

Current `main` is `c57a7c3b24ca2dfc2c61aca54ae3735a0565f3bb` (commit time 20:20 IST). It is one commit after `b4a4390`; the only changed path is `courses/index.php`, associating catalogue filters with results for assistive technology. No blog recovery/shared-head path overlaps this commit.

Fresh exact GitHub comparisons against current main:

| PR | Head | Ahead | Behind | State |
|---|---|---:|---:|---|
| #507 | `72f24de4` | 4 | 4 | OPEN / DRAFT |
| #625 | `d1c3d394` | 7 | 4 | OPEN / DRAFT |
| #654 | `5bf6531d` | 9 | 4 | OPEN / DRAFT, stacked on #507 |
| #660 | `df9431cf` | 19 | 4 | OPEN / DRAFT, stacked on #654 |
| #664 | `934f6b22` | 32 | 4 | OPEN / DRAFT, stacked on #660 |

All comparisons share merge base `813a66fa986a0725c594ecd3780a2be03f5114b9`. #507 retains 22 additive historical article/asset files; #625 retains four shared-head/test/workflow files. No independent review submissions exist on #507 or #625. The five recovery PRs remain unapproved and unreleased.

New owner handoffs posted:
- #507 comment [6827396258](https://github.com/satnamkhowal/grootacademy.com/pull/507#issuecomment-6827396258)
- #625 comment [6827397078](https://github.com/satnamkhowal/grootacademy.com/pull/625#issuecomment-6827397078)

The #625 owner still needs to confirm whether the Spoken English workflow is intentionally the PHP 8.0 runner or whether blog-head tests should be isolated in a blog-specific workflow. Keep root `head.php` as the sole base-tag owner.

## Canonical controller accounting

- Controller branch: `content/groot-100k-controller-20261016`; latest verified checkpoint before this report: `322e942d4adafb6dd9b523b93f7ae8ff15669542`.
- Current queue SHA: `4e087f8cda5479ff9d1124f24ff427a0dbf2b4ad`.
- Planning PR #62 source queue SHA: `df30f7f4e7de86f41f6b04fb765221d6757bb513`.
- Both retain the same 29 unique IDs in exact order, GA-B00001–GA-B00029. PR #68's 14 proposals are research decisions, and GA-B00014 is an in-place refresh; neither increases completed-article count.
- Controller totals: 23 complete text drafts, 23 technical visuals, 23 PHP candidates; 22 independent editorial passes, 18 independent code passes, 23 visual passes; 0 independent publication approvals, 0 published, 0 live verified.
- New IDs/batches remain HOLD. Do not count separate News Factory PRs as controller articles.

## Current-main governance boundary

The current-main `marketing/blog-factory/MASTER-PLAN.md` still describes 10,000 possible IDs, explicitly not validated opportunities or a publication quota. `docs/ai-ops/MASTER_TASK_BOARD.md` still classifies blog factory as P3/REVIEW and says to hold it behind higher-impact UX/QA. The user-authorized controller branch records the 100,000/P0 target. No explicit Master-owner reconciliation of these records, one canonical queue owner, or one independent release approver was found in the latest issue #401 comments. Continue existing repairs and QA only; no new batch.

## Central Control Center delta

- Central `main` remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; the README blob is unchanged and still lists eight brands but only three active control-board rows. Groot's active row remains missing.
- Central PR #22 remains OPEN / DRAFT on `audit/groot-ga22-browser-delta-20261112-0350`; fresh compare is 35 ahead / 0 behind with 12 audit-only files. No independent reviews.
- Central PRs #1, #2 and #3 remain CLOSED / MERGED. Reuse the existing AEO/GEO baseline and queue from #2; do not recreate them.
- Jaipur Engineers `je2` social repository and `jaipur-engieneers` candidate website mapping remains unresolved; they may represent different workstreams. Keep the current owner responsible for reconciliation.

## Blockers and next actions

1. Owners reconcile #507 and #625 against current `main@c57a7c3`; obtain independent reviews before advancing the stacked #654 → #660 → #664 chain.
2. Resolve Azure Actions `BlobNotFound` at the administrator/storage layer; prior jobs failed before steps, so zero assertions executed in those runs.
3. Complete GA-B00029 PHP 8.0/full-root/rendered schema/canonical/noindex/route/HTTP/MIME checks when the runtime and authorized origin are available.
4. Obtain independent editorial re-review for corrected GA-B00016; browser zoom, assistive technology and production navigation remain separate gates.
5. Master owner records the 10K/P3 vs 100K/P0 relationship, one canonical queue owner, one independent release approver and criteria for opening a small next batch.
6. Central coordinator updates the control board and resolves the Jaipur Engineers mapping without changing another brand's source repository.

No source implementation, queue row, central main file, production page, deployment, publication, indexation setting or PR merge was changed by this audit.
