# Groot GA-B00016 zoom evidence and control-board delta — 2026-11-13 11:38 IST

## Scope and repository authority

Coordination-only update on the existing Groot audit branch. Source implementation remains in Groot Academy's repository; this central repository stores coordination evidence only.

- Requested source alias: `satnamkhowal/gta`.
- Verified canonical source: `satnamkhowal/grootacademy.com`, same private repository ID 1375760757.
- Brand/domain: Groot Academy / `grootacademy.com`; no Mango Engineers repository or files used.
- Source controller branch: `content/groot-100k-controller-20261016`.
- Latest source checkpoint: [`fd6b3f9`](https://github.com/satnamkhowal/grootacademy.com/commit/fd6b3f918a4cde830910e761adae65c05a9a971f).
- Central main observed: `21af139cc32a7b67aab6908c61edeb5998bd4544`, unchanged from the previous delta.
- Central PR #22 branch comparison: **56 ahead / 0 behind**, merge base equals current central main; PR remains OPEN/DRAFT with zero independent reviews.

## New source-side QA reconciliation

Existing exact-source GA-B00016 desktop-zoom evidence was found on the QA successor branch `qa/groot-100k-current-main-20261109` and reconciled into the canonical controller branch. The finished test was reused, not regenerated or rerun.

- Exact lab blob: `1e6832c50d3416fabfea7cb90c81c34202e20254`.
- Existing zoom script blob: `4a868d9ceb4fccead89583ee7bdcbc79c9ec2e6c`.
- Existing result report blob: `daab5a7f5e569bd02e9b1180f7512bdd3cce67b5`.
- [Source reconciliation report](https://github.com/satnamkhowal/grootacademy.com/blob/content/groot-100k-controller-20261016/marketing/blog-factory/work/B0001/qa/GA-B00016-zoom-evidence-reconciliation-20261113-1138-ist.md).

Recorded headed Chromium/X11 desktop browser zoom: **12/12 PASS**.
- 200%: DPR 2, innerWidth 640, visualViewport.scale 1; corrected flex row fits and text wraps.
- 400%: DPR 4, innerWidth 320, visualViewport.scale 1; corrected flex row fits and text wraps.
- Keyboard focus reaches the corrected row's link and retains its visible 3px outline.

The canonical controller branch now has the corrected article wording, merged metadata, corrected integration note, CONTROLLER.json evidence and README continuation. Existing 40/40 viewport+keyboard, 18/18 CSS-viewport reflow and 27/27 AX-tree results remain distinct. All are coordinator-run local-lab evidence, not independent production approval.

GA-B00016 remains `CONTENT_QA`. Independent corrected-copy editorial review, manual screen-reader/AT, production-page navigation and release review remain pending. This evidence does not promote its status or publication gate.

## Current source-main / release snapshot

- Groot main observed at `e5f42a7a0bf4a7b21a4a805c6ba09fa00b54f987`; latest commit adds only the GSC verification file. The already merged Spring Boot testing and Spring Data JPA roadmaps remain outside the canonical 29-ID controller queue.
- Controller branch and current main still have no common Git ancestor; it remains isolated, with no rebase/merge.
- GA-B00029 remains `TECH_QA`: exact Python lab 6/6 and demo PASS; PHP 8.4 isolated evidence exists, but PHP 8.0/full-root/shared-schema/H1/canonical/robots/registry/sitemap/route/browser/authorized-origin HTTP/MIME and independent release review remain open.
- PR #625 remains OPEN/DRAFT, 7 ahead / 10 behind current main, four net changed paths, zero independent reviews. Current main still emits the duplicate base from both the shared blog partial and root head; the proposed PR removes the redundant partial base. No merge/deployment.
- Azure Actions `BlobNotFound` is still an administrator diagnosis blocker; no blind retry.

## Central coordination findings retained

- Current central main README lists eight brands but only three active control-board rows. Groot Academy is named in the brand inventory but has no active brand-specific owner/status row.
- PRs #1/#2/#3 are merged; reuse the existing all-brand AEO/GEO baseline from PR #2. No duplicate baseline was created.
- Jaipur Engineers `je2` social work versus the `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. Preserve both workstream roles; do not assume either repository is wrong or reassign ownership.
- Groot current-main Master Plan still defines 10,000 possible-ID capacity; HAO-008 remains P3/REVIEW. User-authorized controller remains 100,000/P0 and issue #401 records 100,000 as M4. No Master-owner decision aligning these scopes, naming one canonical queue owner or naming one independent release approver was found.
- New article IDs remain HOLD.

## Accounting

- Canonical queue: 29 original IDs, unchanged SHA `2766216c3f47982fdba1934c96873a6892968ef1`.
- Complete original drafts: 23; technical visuals: 23; PHP candidates: 23.
- Independent editorial/code/visual PASS: 22/18/23.
- Independent approvals: 0; published: 0; live verified: 0.
- PR #68's 14 proposals and GA-B00014 refresh remain research/refresh work, not completed articles.

No central-main write, source-main write, owner reassignment, self-approval, self-merge, deployment, publication, indexing or ranking claim occurred.
