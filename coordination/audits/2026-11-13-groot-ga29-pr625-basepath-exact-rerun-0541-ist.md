# Groot Academy coordination delta — GA-B00029 shared-head dependency

Observed: 2026-11-13 05:41 IST. This is a coordination-only delta for central PR #22; source implementation remains in the Groot Academy repository.

## New source evidence

- Groot current main is `9e18e07f29e61f9c2e36f5d39dbc663d72d3e5e9`.
- Current main's `blogs/_shared/partials/head.php` blob is `637d161f762d52b5ed4eca8ec01244b0e3a07bc4`. It emits a base element before including root `head.php`, which emits the authoritative second base.
- Exact-source PHP fixture re-execution against PR #625's proposed partial and exact root head/site-path helper passed both configured contexts on PHP 8.4.24: local `/groot-preview/` and production `/`; one base each, canonical, `noindex,follow`, BlogPosting and BreadcrumbList verified.
- The same harness against the exact current-main partial reproduced two base elements in both contexts: `/groot-preview//` + `/groot-preview/`, and `//` + `/`.
- Source blob identities matched for the proposed PR partial, root head, site-path helper and PHP render harness. The runner was coordinator-authored; the committed Python script was not claimed as exact-byte execution.
- PR #625 is still OPEN/DRAFT, 7 ahead / 5 behind current main, four net changed paths, zero independent reviews. No PR/main write was made.

## Groot 100K impact

This is a shared-renderer dependency for GA-B00029's full-root release review, not an article. GA-B00029 stays TECH_QA until the shared-head fix is owner-reviewed and present on main, then full-root/PHP 8.0/schema/H1/canonical/robots/route/assets/internal-link/download HTTP/MIME checks and independent release approval are completed.

Canonical queue remains 29/29 IDs in planning PR #62 order. Factory counts remain 23 complete text drafts, 23 technical visuals, 23 PHP candidates; independent approvals 0, published 0, live verified 0. PR #68 remains research (14 proposals) and GA-B00014 remains an in-place refresh, not a new article.

## Central coordination deltas

- Central main is `21af139cc32a7b67aab6908c61edeb5998bd4544`; central PR #22 compares 49 ahead / 0 behind and has zero independent reviews. It remains Draft.
- Central PRs #1/#2/#3 remain merged; the existing AEO/GEO PR #2 baseline is reused.
- The current central README still lists eight brands but only three active owner/status rows; Groot's active owner row is missing.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website remains an explicit unresolved mapping; neither side is assumed wrong.
- Main's `marketing/blog-factory/MASTER-PLAN.md` remains a 10,000 possible-ID capacity envelope, while `docs/ai-ops/MASTER_TASK_BOARD.md` still marks the blog factory P3/REVIEW and says to hold behind higher-impact UX/QA. User-authorized controller remains 100,000/P0. Master-owner alignment, one canonical queue owner and an independent release approver remain unresolved.

## Exact next action

1. Keep the five existing recovery PRs and PR #625 with their owners; obtain owner-led current-main refresh and independent review where needed.
2. Continue GA-B00029 only after the shared-head fix is approved and merged by its owner; then complete full-root and release checks.
3. Keep new batches on HOLD until the Master owner resolves the 10K/P3 versus 100K/P0 governance difference and records queue/release ownership.
4. Do not modify main, another brand's files, the canonical queue or publication state from this coordination branch.
