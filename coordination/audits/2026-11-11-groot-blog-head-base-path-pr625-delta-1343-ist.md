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


## Coordination delta — 11 November 2026, 14:37 IST: PR #625 Actions evidence

- Verified the requested historical repository name `satnamkhowal/gta` is recorded by the Groot controller as a previous alias; its verified successor/source repository is `satnamkhowal/grootacademy.com`. No Mango Engineers source or worker files were touched.
- Groot current main remains `d880da02c51f2cdc62db059aaa49a0f14858feb1`. PR #625 remains OPEN/DRAFT at 4 ahead / 0 behind, three files, zero independent reviews and zero review threads. Local PHP fixture evidence is 2/2 PASS.
- Newly inspected the exact PR-head Actions runs: #42986257135, #42986257152 and #42986257134. All jobs completed as failures with `steps: null`; each log retrieval returned Azure Storage `BlobNotFound`. No workflow assertion ran, so no code failure/pass is inferred. No retry was issued. PR comment [#6791798127](https://github.com/satnamkhowal/grootacademy.com/pull/625#issuecomment-6791798127) asks the Actions/storage administrator to diagnose missing log blobs.
- PR #569 still compares 218 ahead / 10 behind current main, merge base `0648b79ee0775e810251192a61b8ae6d842980f4`, 226 files, zero independent reviews/threads. No rebase or merge.
- Central main remains `80c75e28734ce22831e93d9f431f4c15ccad0f6c`; PR #20 compares 37 ahead / 4 behind, 24 files, zero independent reviews. README still lists eight brands and three active rows, with Groot's row missing. PRs #1/#2/#3 are merged; reuse AEO/GEO PR #2. Jaipur Engineers `je2` social vs `jaipur-engieneers` candidate website mapping remains unresolved.
- The canonical 100K queue remains 29/29 IDs and unchanged; controller counts remain 23 complete drafts, 23 visuals, 23 PHP candidates, 18 independent code passes, approvals 0, published/live 0. No new article/image, queue import, owner transfer, main write, merge, deployment or publication.
- Exact next actions: Actions/storage administrator diagnoses BlobNotFound; independent/full-checkout review of PR #625; network-enabled GA-B00029 full-root PHP/schema/route/HTTP/MIME and independent release review; Master-owner 10K/P3 vs 100K/P0 reconciliation before any new article batch; preserve central ownership and existing AEO/GEO baseline.


## Coordination delta — 11 November 2026, 15:36 IST: PR #625 regression CI wiring

- Groot source PR [#625](https://github.com/satnamkhowal/grootacademy.com/pull/625) remains OPEN/DRAFT; its new head is `3a9a412a6ec192e6d16548a7a735159580d0a986`, based on current Groot main `d880da0`. It has 5 commits / 4 files, zero independent reviews and zero review threads.
- The base-path regression Python test had not been invoked by the existing PHP route workflow. Source owner added a targeted CI step and fixture path filters to `.github/workflows/groot-spoken-english-qa.yml`; the job provisions PHP 8.0 and Python 3.12, lints the shared blog head partial, then runs `marketing/blog-factory/tests/test_blog_head_base_path.py`. Source commit: [3a9a412](https://github.com/satnamkhowal/grootacademy.com/commit/3a9a412a6ec192e6d16548a7a735159580d0a986).
- The new PR-head runs [43001353616](https://github.com/satnamkhowal/grootacademy.com/actions/runs/43001353616), [43001353572](https://github.com/satnamkhowal/grootacademy.com/actions/runs/43001353572) and [43001353591](https://github.com/satnamkhowal/grootacademy.com/actions/runs/43001353591) again returned `steps: null`. All three job-log fetches returned Azure Storage `BlobNotFound` (HTTP 404), so no assertion ran. No retry was triggered. PR comment [#6793063039](https://github.com/satnamkhowal/grootacademy.com/pull/625#issuecomment-6793063039) records the administrator blocker.
- Groot controller queue remains 29/29 IDs in the exact planning order. Counts remain 23 complete drafts / 23 visuals / 23 PHP candidates / 18 independent code passes / 0 independent approvals / 0 published / 0 live verified. No new article, image, queue ID, approval, merge, deployment or publication.
- Groot current main remains `d880da02c51f2cdc62db059aaa49a0f14858feb1`; the Java retrospective in PR #624 remains outside the canonical 100K queue. Master-owner 10K/P3 versus 100K/P0 reconciliation, GA-B00029 network-enabled full-root/HTTP gates, and PR #533/#569 owner-led recovery remain pending.
- Central main was not changed. Its README still registers eight brands but lists only three active control-board rows, with Groot's active row missing. PRs #1/#2/#3 remain merged; reuse AEO/GEO baseline PR #2. Jaipur Engineers `je2` social versus `jaipur-engieneers` candidate website mapping remains unresolved. Central PR #20 remains OPEN/DRAFT with independent review pending.
- Source implementation stays in the Groot repository; this central report is coordination-only. No ownership transfer, central-main write, deployment, publishing or indexing.


## Coordination delta — 11 November 2026, 15:37 IST: exact-source fixture execution

- The Groot source lane materialized the five exact blobs required by PR #625's base-path regression harness. All local Git object hashes match the corresponding GitHub blob SHAs.
- On PHP 8.4.24 / Python 3.13.5, PHP lint passed 4/4, Python compilation passed, and the exact-source isolated regression passed 2/2 (local subdirectory preview and production host). The rendered head had exactly one expected base element and expected canonical, noindex, BlogPosting and BreadcrumbList.
- Scope is limited to the exact-source isolated fixture. It is not a full repository checkout, PHP 8.0 Actions result, browser/AT test, raw production HTTP/MIME verification or independent release approval.
- Source PR [#625](https://github.com/satnamkhowal/grootacademy.com/pull/625) remains OPEN/DRAFT, five commits / four files, zero independent reviews and zero review threads. The PR body and comments now distinguish local exact-source evidence from blocked CI.
- The three new Actions runs remain infrastructure failures: `steps: null` and Azure `BlobNotFound`; no assertion ran and no retry was triggered. Admin diagnosis remains the next action.
- Canonical queue remains 29/29 IDs in exact planning order; counts remain 23 drafts / 23 visuals / 23 PHP candidates / 18 independent code passes / 0 approvals / 0 published / 0 live. No new article, image, queue ID, approval, merge, deployment or publication.
- Central main/README remain unchanged; eight registered brands, three active control-board rows, Groot row missing. PRs #1/#2/#3 remain merged and existing AEO/GEO PR #2 baseline is reused. Jaipur Engineers `je2` social vs `jaipur-engieneers` candidate website mapping remains unresolved. Central PR #20 remains Draft for owner review.
