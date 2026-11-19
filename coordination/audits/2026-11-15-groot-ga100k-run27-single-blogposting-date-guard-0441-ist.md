# Groot Academy 100K — Run 27 coordination delta

**Observed:** 2026-11-15 04:41 IST  
**Source implementation repository:** `satnamkhowal/grootacademy.com` (requested alias `satnamkhowal/gta`)  
**Source controller:** `content/groot-100k-controller-20261114-run16`  
**Coordination branch:** `audit/groot-ga22-browser-delta-20261112-0350`

## New source evidence

The source lane added one bounded QA guard on the existing draft PR [#755](https://github.com/satnamkhowal/grootacademy.com/pull/755):

- Draft rendering must contain exactly one BlogPosting JSON-LD object.
- The sole BlogPosting must omit `datePublished` and `dateModified`.
- A new fixture with a second date-bearing BlogPosting is rejected.
- Source commits: [52f0d7ad](https://github.com/satnamkhowal/grootacademy.com/commit/52f0d7ad152a55f1a2af1ddc3d1ee0f33516b519), [e92c17be](https://github.com/satnamkhowal/grootacademy.com/commit/e92c17bed5bba530173523ab0db3c3491169ee94).
- Focused coordinator-run regression: 2/2 PASS. Full committed suite and independent review remain pending.
- PR #755 is OPEN/DRAFT, 10 ahead / 0 behind its exact #664 parent, three QA files, zero independent reviews/threads.
- Exact-head Actions run [#43652284084](https://github.com/satnamkhowal/grootacademy.com/actions/runs/43652284084), job 132623190804, failed before steps. Log retrieval returned Azure BlobNotFound HTTP 404; no hosted assertions ran and no retry was initiated.

## Current source Main delta

Source Main is `e1f629ecd0bffb9d3eafaaadbd6f5bf226950e6f`. Compared with `7f007cbc5da988bbce401a1a50a4fbf00fa3bb24`, the latest three-commit delta changes only:
- `assets/js/groot-home-path-finder.js`
- `courses/index.php`
- `index.php`

No blog-factory, five-recovery article, shared blog layout, registry or sitemap path changed in this delta.

## Central coordination state — rechecked, not re-audited

- Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; this report is on the existing PR #22 coordination branch only.
- Current central README lists eight brands but only three active owner/status rows (Jaipur Engineers, Central coordination, Forsk Coding School). Groot's dedicated active row is still missing.
- PR #22 remains OPEN/DRAFT; before this append it was 115 ahead / 0 behind Main. Independent reviews and review threads: 0.
- Central PRs #1/#2/#3 remain merged. Reuse the existing AEO/GEO PR #2 baseline; do not recreate it.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. Do not assume either repository is wrong or reassign ownership without central-owner evidence.
- Source implementation remains in the Groot repository. No central Main, other brand source, owner assignment, deployment, publication, indexing or ranking claim changed.

## 100K ledger and release boundary

The canonical source queue remains 29 ordered IDs with blob `c12a915e06c8100a350b21338311651df0f35094`. Source controller counts remain 23 complete original drafts, 23 technical visuals and 23 PHP candidates; independent editorial/code/visual component PASS 22/18/23; fully approved/published/live 0/0/0. GA-B00029 remains TECH_QA/noindex.

The five GA-B00006–GA-B00010 recovery candidates still contain unsupported 2026-11-01 dates while original metadata dates are null. Keep them noindex,follow and outside registry/sitemap until the QA contract is independently reviewed/integrated into #664 and the #660 owner removes the unsupported fields.

No new article or image was created. Queue, registry, sitemap, source Main and production routes were not changed.

## Exact next action

1. Obtain independent review of source PR #755 and full committed-suite execution.
2. Administrator diagnoses Azure BlobNotFound before any hosted retry.
3. After independent integration into #664, owner removes unsupported dates from all five #660 candidates while retaining noindex,follow.
4. Owners reconcile #507 → #654 → #660 → #664 exact base/parent metadata and intended-only diffs.
5. Central owner verifies Groot's active repository/task owner and records the target/priority, canonical queue owner and independent release approver; only then add the Groot row to the central board.
6. Keep new IDs on HOLD until the master-owner 100K/P0 governance decision is explicit.

No self-approval, self-merge, deployment, publication or mass indexing.
