# Groot Academy current-main and control-board delta — 2026-11-13 08:42 IST

## Scope and source identity

This is a coordination-only delta on the existing Groot audit branch. Brand implementation remains in the Groot source repository.

- Requested source alias: `satnamkhowal/gta`.
- Verified canonical source: `satnamkhowal/grootacademy.com` (same repository ID 1375760757).
- Groot main observed: `a1ee6d51edc05ea65b1441cfee7ab78d1b275c88`.
- Central main observed: `21af139cc32a7b67aab6908c61edeb5998bd4544`.
- Central audit PR: [#22](https://github.com/satnamkhowal/brand-growth-control-center/pull/22), branch `audit/groot-ga22-browser-delta-20261112-0350`, OPEN/DRAFT, 53 commits ahead / 0 behind at the start of this append, zero independent reviews.

No Mango Engineers repository was used.

## New Groot main delta

Groot PR [#702](https://github.com/satnamkhowal/grootacademy.com/pull/702) merged at 2026-11-13 02:41:23 UTC. Main commit `a1ee6d51` adds the Spring Data JPA workshop-booking roadmap and updates its registry/sitemap discovery plus an incoming link from the Spring Boot REST API guide.

Changed paths:

- `blogs/_shared/blog-registry.php`
- `blogs/sitemap.xml`
- `blogs/spring-boot-rest-api-project-roadmap-2026-jaipur/index.php`
- `blogs/spring-data-jpa-project-roadmap-2026-jaipur/index.php`
- `logs/2026-11-13-spring-data-jpa-roadmap.md`

The article is source-merged but deployment, live HTTP and indexation are unverified. It is outside the canonical 29-ID 100K controller queue and must not be added to its completion count.

A bounded comparison against GA-B00021 found distinct reader outcomes: GA-B00021 is a Python/SQLite book-lending constraints project; the new article is a Java/Spring Data JPA workshop-booking persistence roadmap. No forced cross-link or duplicate disposition was added.

## Control-board reconciliation

The current central-main README blob `b93187c353f8112a57fffab4b383e64236976394` lists eight brands. Its current control board has exactly three rows:

1. Jaipur Engineers — P0, Account 1 / Master Supervisor, In review.
2. Central coordination — P0, Account 1 / Master Supervisor, Active.
3. Forsk Coding School — P0, Forsk implementation / Central Controller, In review.

Groot Academy appears in the eight-brand list but has **no active brand-specific control-board row**. This is more precise than describing the three total rows as three brand owners. Do not create an owner assignment or edit central main from this audit.

Central PRs #1/#2/#3 are merged. Reuse the existing all-brand AEO/GEO baseline from PR #2; do not recreate it. PR #22 remains the existing coordination-only review lane; this append adds no source implementation.

## Existing mapping and governance findings

- Jaipur Engineers `je2` social work versus the `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. Issue #401's latest 08:23 IST checkpoint resolves the `je2` alias to `jaipurengineers.com`, but does not provide deployed-origin parity or establish the role of the other candidate. Keep both roles explicit; do not infer either is wrong or transfer ownership.
- Groot current-main `marketing/blog-factory/MASTER-PLAN.md` still defines 10,000 possible IDs; `docs/ai-ops/MASTER_TASK_BOARD.md` still records HAO-008 Blog Factory as P3/REVIEW.
- The user-authorized Groot controller remains 100,000/P0. Issue #401's latest checkpoint does not record a Master-owner decision reconciling 10K/P3 with 100K/P0, naming one canonical queue owner or naming one independent release approver.
- Keep new IDs on HOLD; continue existing repairs only.
- Source queue remains 29 IDs; 23 complete text drafts, 23 technical visuals and 23 PHP candidates; independent approvals 0, published 0, live verified 0. PR #68 proposals and GA-B00014 refresh are not completed articles.

## QA/release delta

- GA-B00029 remains TECH_QA. Its candidate slug is absent from current-main registry/sitemap and it remains noindex/unpublished. PR #625 is OPEN/DRAFT, 7 ahead / 6 behind current main, four net changed paths and zero independent reviews; PHP 8.0/full-root/schema/route/browser/authorized HTTP/MIME and independent review remain pending.
- GA-B00022 exact committed Playwright harness is 43/43 coordinator-run PASS and Chromium CDP accessibility-tree probe is 7/7 PASS. Screen-reader, actual 200%/400% zoom, production route and independent QA remain pending. PR #699 remains OPEN/DRAFT, zero independent reviews.
- Actions run 43344650966 failed before steps with Azure `BlobNotFound` HTTP 404; zero assertions ran. Administrator diagnosis is required before a meaningful retry.
- GA-B00016 remains CONTENT_QA pending independent editorial, browser, zoom and assistive-technology review.

## Exact next action

1. Keep the Groot source work in `satnamkhowal/grootacademy.com`; central repository remains coordination-only.
2. Obtain owner-led independent review and PHP 8.0/full-root/schema/route/HTTP/MIME verification for GA-B00029 / PR #625.
3. Complete independent GA-B00022 and GA-B00016 screen-reader/zoom/editorial gates.
4. Have the Actions/Azure storage administrator diagnose `BlobNotFound` before another exact-head run.
5. Ask the Master owner to record the 10K/P3 versus authorized 100K/P0 decision, one canonical queue owner and one independent release approver.
6. Reconcile Jaipur Engineers' social repository and candidate website/deployed-origin mapping with the existing mapping owner.

No central-main write, source-owner reassignment, other-brand implementation, self-approval, self-merge, deployment, publishing, indexing or ranking/live claim occurred.
