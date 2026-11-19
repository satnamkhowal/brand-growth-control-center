# Groot Academy 100K Factory — Run 144 coordination delta

Observed: 2026-11-20 04:39 IST

## Scope and ownership

Coordination-only delta, stacked on Central PR #44's exact Run143 lineage. Source implementation remains in the verified Groot Academy repository `satnamkhowal/grootacademy.com` (user alias `satnamkhowal/gta`; same repository ID 1375760757). This repository records coordination evidence only.

No central Main, source Main, other-brand repository, queue, ownership row, deployment, publication or indexing change is made here.

## New source evidence

- Source PR [#912](https://github.com/satnamkhowal/grootacademy.com/pull/912) is an OPEN/DRAFT child of Run143 PR #911.
- Run144 reproduced a false-positive `same_key_type` result when only one relationship side had non-blank values. The source candidate now compares exact per-side type sets and returns true only when both sides are populated and share one exact type.
- Three regressions were added; the prior empty-one-side test now expects an inconclusive false result. Coordinator-local focused behavioral mirror: 5/5 PASS. This is not exact-blob full-suite evidence or independent approval.
- Article and metadata document the conservative contract. Existing WebP/SVG are unchanged.
- GA-B00005 remains CONTENT_QA. PR #912 is not independently reviewed or approved. No PHP candidate, registry/sitemap entry, route, publication or deployment was created.

## Queue and release state

- Original planning PR #62 contains 29 IDs; the controller preserves all 29 in order.
- PR #908 remains the sole corrected strict-CSV candidate (29 rows × 19 fields, blob `7f0c005fec5cd2ad1e3691864019a97d480632f3`). It has not been owner-integrated; no queue write occurred in Run144.
- Controller ledger remains 24 complete text drafts, 24 technical visuals, 23 PHP candidates; independent editorial/code/visual PASS 22/18/23; fully approved, published and live-verified 0/0/0.
- GA-B00006 release work remains separate: PHP 8.0/8.4, full-root rendering, shared BlogPosting/BreadcrumbList, canonical/robots, registry/sitemap, route, browser/accessibility and HTTP/MIME checks.

## Current-main delta

- Groot source Main is `0aa396859d3af70935280275b524a51dadc48868`.
- The latest Main commits are homepage-responsive styling, alumni showcase/profile work and course FAQ placement. No new blog-factory or queue commit was observed in the latest ten-commit window. PR #867 remains the existing owner-controlled shared-blog-head repair; its refresh must preserve the contextual FAQ stylesheet.
- Central Main is `70d500412703f605bc61354ab2c60188f06e15f9`; its latest commit links the canonical queue review PR. Central README still lists eight brands but only three active control-board rows (Jaipur Engineers, Central coordination and Forsk Coding School); Groot Academy's P0 owner/status row is absent.
- Central PR #44 is OPEN/DRAFT, 11 commits ahead / 0 behind current Main. This Run144 report is a one-file child delta, not a Main update.

## Governance and cross-brand boundaries

- Central PRs #1/#2/#3 remain the established merged baseline; reuse the existing AEO/GEO PR #2 program and do not recreate it.
- Groot's accountable 100K/P0 owner, one canonical queue writer and independent release approver are still not explicitly registered on the central board.
- Jaipur Engineers' `je2` social-workstream history and the `jaipur-engieneers` candidate website/deployed-origin mapping remain an explicit reconciliation item. Do not infer that either repository is invalid; preserve the verified canonical `jaipurengineers.com` identity and confirm which repository owns each workstream.
- Other brand task ownership is unchanged.

## Blockers and next actions

1. Independent editorial/code/visual review of source PR #912 and independent review of the sole corrected queue candidate PR #908; owner-controlled integration only after review.
2. Owner refresh/review of source PR #867 against current Main, preserving contextual FAQ assets.
3. Continue GA-B00006's independent PHP/schema/route/browser/accessibility/HTTP/MIME release gates.
4. Administrator/storage-owner diagnosis of the Azure Actions BlobNotFound HTTP 404 failures before any hosted retry.
5. Central owner records Groot P0 ownership, canonical queue writer and independent release approver, and reconciles Jaipur repository roles.

No self-approval, self-merge, deployment, publication or mass indexing.
