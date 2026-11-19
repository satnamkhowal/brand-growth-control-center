# Coordination delta — Groot recovery image compatibility successor

**Observed:** 2026-11-12 06:11 IST  
**Central main:** `80c75e28734ce22831e93d9f431f4c15ccad0f6c`  
**Central main README blob:** `b93187c353f8112a57fffab4b383e64236976394`  
**Source repository:** `satnamkhowal/gta` (GitHub permanent alias `satnamkhowal/grootacademy.com`)  
**Brand/domain:** Groot Academy / https://grootacademy.com/

## New source-lane implementation evidence

Groot recovery PR [#507](https://github.com/satnamkhowal/grootacademy.com/pull/507) now has reconciled parent branch head `65c50c93733563c2fd55ff9f1b100338623046f0`, 2 commits ahead / 0 behind current main, 22 exact historical file additions and no deletions. It remains OPEN/DRAFT with zero independent reviews.

Original dependent PR [#511](https://github.com/satnamkhowal/grootacademy.com/pull/511) is stale against that updated parent: current parent-to-head comparison is diverged 2 ahead / 58 behind, merge base `ab7d4c13`; 0 reviews and 0 threads. Its old layout omits current-parent TOC canonical-path handling and registry root-path related links, and its old stylesheet lacks current blog-index styles. Do not merge #511 as-is.

A current-parent-compatible two-file successor [#654](https://github.com/satnamkhowal/grootacademy.com/pull/654) is OPEN/DRAFT, 2 ahead / 0 behind its #507 parent, with zero reviews/threads. It preserves the current-parent layout and CSS features while adding guarded intrinsic image dimensions for the five recovered 1200×630 images.

- All five recovered article PHP configs were read from the updated #507 parent; each declares 1200×630 and its original social-card PNG path.
- PHP 8.4.24 isolated render fixture: syntax check PASS; 5/5 dimension-gating cases PASS. This is not full-root or production rendering.
- Exact-head workflow runs [43129940302](https://github.com/satnamkhowal/grootacademy.com/actions/runs/43129940302) and [43129940437](https://github.com/satnamkhowal/grootacademy.com/actions/runs/43129940437) failed before step creation. Jobs returned `steps: null` / zero steps; log retrieval returned Azure `BlobNotFound` (404); zero assertions are evidenced. Administrator diagnosis required; no blind retry.
- Source implementation and detailed QA report remain in the Groot repository; no source main change.

## Canonical ledger and release accounting

The controller branch still matches the immutable planning queue exactly: 29 rows, 29 unique IDs, original sequence preserved. Statuses remain MERGE=3, REFRESH=2, IDEA=1, PUBLISH_PR=5, TECH_QA=17, CONTENT_QA=1.

Controller accounting remains 23 complete original drafts, 23 technical visuals, 23 PHP candidates, 22 independent editorial passes, 18 independent code passes, 0 independent approvals, 0 published and 0 live verified. PR #654 is a shared-template repair, not an article or asset.

Issue #401's latest 05:23 IST owner-scope checkpoint reports the public blog hub displaying 61 practical guides, but explicitly does not establish per-URL HTTP 200, canonical, robots/indexability or Search Console coverage. Do not treat 61 as a verified unique live-published count.

## Central coordination status — delta only

- Central PRs #1, #2 and #3 are CLOSED/MERGED. PR #2's existing AEO/GEO baseline is reused; no duplicate baseline created.
- Central PR #22 remains OPEN/DRAFT, 5 commits ahead / 0 behind main, 2 coordination report files, 0 independent reviews and 0 review threads. This report is coordination-only.
- Central main README still lists eight brands but only three active control-board rows (Jaipur Engineers, Central coordination, Forsk Coding School); Groot Academy has no active row. No owner or priority was invented.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. No ownership transfer or assumption was made.
- Central PR #20 and other owners' files were not changed.

## Governance and next action

Current Groot main `docs/ai-ops/MASTER_TASK_BOARD.md` still marks HAO-008 P3/REVIEW and says avoid 10,000-post quotas. The authorized controller remains 100,000/P0; issue #401 describes 100,000 as M4 and 1,000,000 as an aspirational ceiling. The latest issue comments contain no explicit master-owner alignment decision or named canonical queue/release owner. New article batches remain held.

Next:
1. Independent review of source PR #654 and parent #507.
2. Resolve Azure Actions/storage `BlobNotFound`; then run PHP 8.0 hosted lint, full-root render, image decode and browser/CLS/keyboard/AT checks.
3. Reconcile downstream recovery PRs only after parent/successor review; keep old #511 unmerged.
4. Continue GA-B00029 full-root/HTTP/MIME only on a network-enabled authorized checkout; keep GA-B00016 editorial re-review, GA-B00022 production/AT review and PR #625 independent review open.
5. Master owner records the single authoritative target and queue/release owner before any new article batch.

No central main/source main write, owner reassignment, self-approval, self-merge, deployment, publishing or mass indexing.