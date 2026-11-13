# Groot Academy — GA-B00029 / PR #713 base-path edge-case delta

**Observed:** 2026-11-13 14:58 IST  
**Source repository:** `satnamkhowal/gta` (current GitHub name `satnamkhowal/grootacademy.com`)  
**Source branch:** `content/groot-100k-controller-20261016`  
**Central PR:** #22, coordination-only; no central main changes.

## New source-repository evidence

The Groot source controller committed report `marketing/blog-factory/work/B0002/qa/2026-11-13-ga29-pr713-base-path-edge-cases-1458-ist.md` at `db49d51e`, then updated its CONTROLLER and README at `7233a6be` and `dbe287ff`.

The supplemental local fixture used Git-blob-verified current-main `head.php` (`89fe435e`), current `includes/site-paths.php` (`edeaf811`), PR #713's proposed shared partial (`5d6b335c`) and PR render harness (`94e3b855`). PHP 8.4.24 lint passed 4/4. Five base-path cases passed in normal Python, `-O` and `-OO`; intentionally reintroducing the partial-level duplicate base caused all five to fail. The added cases cover mixed-case `WWW` with port, a mounted localhost preview with port/query, and an unmounted local request.

This remains coordinator-run fixture evidence only. It is not PHP 8.0, hosted Actions, full-root production rendering, independent review, production HTTP/MIME, deployment or live verification.

## Current PR #713 handoff

- Current Groot main: `986f316b5d291dd357bd1fdb54488fa79db50e51`.
- PR #713 head: `738abaeffac447c8734b9b465c140b6bb71d8f7d`; base snapshot `2b96297`.
- Direct compare: 4 commits ahead / 2 behind, four changed paths.
- OPEN/DRAFT, zero independent reviews and no reported status checks.
- Owner must refresh the branch to current main and obtain independent review plus exact-head hosted checks after administrator diagnosis of the Azure Actions `BlobNotFound` failure.

Source changes stay in the Groot repository; no PR branch refresh, approval, merge, deployment, publishing or indexing was performed by this audit.

## Central coordination delta

Central main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; this report is added only to the existing PR #22 coordination branch. Current central README still lists eight brands but only three active owner/status rows; Groot Academy's dedicated owner row is missing. PRs #1/#2/#3 remain merged; reuse the existing AEO/GEO baseline from #2. Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved and must be reconciled by its owner, not inferred here.

## Queue and release accounting

Groot's canonical 29-ID queue and PR #62 order remain unchanged; queue blob `2766216c3f47982fdba1934c96873a6892968ef1`. Controller totals remain 23 complete drafts, 23 technical visuals, 23 PHP candidates; independent approvals/published/live 0/0/0. Research PR #68's 14 proposals and GA-B00014 refresh do not count as finished articles.

**Next action:** Groot owner refreshes PR #713 and resolves the Actions storage blocker; independent review and hosted PHP 8.0/full-root/schema/route/HTTP/MIME gates follow. Central owner records a dedicated Groot control-board row and resolves the Jaipur repository-role mapping. No central main write, cross-brand source edit or self-approval.
