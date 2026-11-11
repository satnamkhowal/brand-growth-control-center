# Central coordination delta — Groot shared blog base-path repair
Date: 2026-11-11 13:43 IST
Scope: coordination only; no source implementation in this repository.

## New verified Groot work
- Source repository: `satnamkhowal/grootacademy.com` (the requested `satnamkhowal/gta` alias resolves to this repository); domain `https://grootacademy.com`.
- New isolated source PR: [Groot PR #625](https://github.com/satnamkhowal/grootacademy.com/pull/625), OPEN/DRAFT, based on current main `d880da02c51f2cdc62db059aaa49a0f14858feb1`.
- It removes a duplicate hard-coded `<base href="/">` from the shared blog head so the root `head.php` `ga_url()` base remains authoritative for both production and local subdirectory previews.
- Source-side local PHP 8.4.24 fixture tests: 2/2 PASS; PHP syntax and Python compile PASS. Full-checkout CI and independent review remain pending. No deployment, publication or indexing.
- The canonical 100K queue remains 29/29 IDs, exact sequence match to planning PR #62. Complete drafts/visuals/PHP candidates remain 23/23/23; independent approvals 0; published/live 0. PR #624's separate historical article is not a 100K queue item.

## Current source/release ownership
- The Groot controller successor PR #569 is OPEN/DRAFT and compares 218 ahead / 10 behind current main; zero independent reviews and zero review threads. Owner-led base reconciliation is still required; no rebase or merge was performed.
- Master-owned priority alignment remains unresolved: Master Plan 10,000 capacity and HAO-008 P3/REVIEW versus user-authorized controller 100,000/P0 and issue #401 M4=100,000. Do not start a new article batch before the Master owner records the decision.
- GA-B00029 full-root PHP/schema/route and authorized-origin HTTP/MIME remain pending on a network-enabled runner. Azure BlobNotFound diagnosis remains with Actions/storage administrators; PR #533 recovery conflicts remain with the recovery owner.

## Central mapping delta
- Central main observed at `80c75e28734ce22831e93d9f431f4c15ccad0f6c`.
- Current README registers eight brands but lists only three active control-board rows; Groot Academy's active owner/status row is still missing. This report does not add or infer an owner.
- Central PRs #1/#2/#3 remain merged. Reuse the existing AEO/GEO baseline in PR #2; do not recreate it.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved; no ownership transfer.
- Existing central audit PR #20 compares 36 ahead / 4 behind main and has zero independent reviews. It remains OPEN/DRAFT; central owner review/base reconciliation is required.

## Exact next action
Central owner: reconcile the Groot row in the control board and review this coordination delta without moving implementation files. Groot source owner/reviewer: independently review PR #625 and require a full-checkout run; do not merge/deploy from this lane.
