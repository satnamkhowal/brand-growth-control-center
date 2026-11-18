# Groot Academy 100K — Run 103 coordination delta

**Observed:** 2026-11-18 12:38 IST  
**Central Main:** `21af139cc32a7b67aab6908c61edeb5998bd4544` (unchanged)

## Source implementation delta

Source implementation remains exclusively in Groot Academy's repository. The user-supplied `satnamkhowal/gta` alias resolves to the same private repository ID `1375760757`, current name `satnamkhowal/grootacademy.com`.

Existing source QA PR [#855](https://github.com/satnamkhowal/grootacademy.com/pull/855) was advanced on its existing branch; no third overlapping source branch was created. The exact Run 99 parent comparison is 4 ahead / 0 behind and contains exactly the two existing QA files.

Run 103 found that the BlogPosting collector handled `@graph` but omitted JSON-LD 1.1 `@included` node objects, including aliasable `included` → `@included`. W3C JSON-LD 1.1 defines included blocks as secondary node objects and permits the keyword to be aliased: https://www.w3.org/TR/json-ld11/.

The existing collector now traverses both `@graph` and `@included` through the same context-propagation boundary. Three regression methods cover literal duplicate, aliased duplicate (string and object-`@id`) and a single included BlogPosting positive control.

- Helper commit: [`ae7e9dc`](https://github.com/satnamkhowal/grootacademy.com/commit/ae7e9dc239be97f7037aa26a684d22ae799d581a)
- Tests commit: [`dc81bb78`](https://github.com/satnamkhowal/grootacademy.com/commit/dc81bb78f90d28a058bfaad208104e650c3250c7)
- Coordinator-local structural mirror: **4/4 PASS**; not the committed full suite or JSON-LD processor conformance.
- Non-approval source handoff: [PR #855 comment](https://github.com/satnamkhowal/grootacademy.com/pull/855#issuecomment-6971825543).
- PR #855 reviews/threads: **0/0**; prerequisite #755 and ancestor #840 reviews: **0/0**.

Latest observed Actions run [44249851762](https://github.com/satnamkhowal/grootacademy.com/actions/runs/44249851762) failed before steps with Azure `BlobNotFound` HTTP 404; hosted assertions 0. No retry without administrator/storage-owner diagnosis. Full committed suite NOT RUN; PHP 8.0 UNAVAILABLE.

## Current Main and ownership delta

- Groot source Main remains `254affd91a55524d438260f4fc1816f10d43a0a1`; latest change is alumni-only and has no blog-factory, shared blog-head, registry, blog sitemap or queue overlap.
- Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; current README blob `b93187c353f8112a57fffab4b383e64236976394`.
- Central PRs #1/#2/#3 remain merged. Reuse PR #2's existing AEO/GEO baseline; do not recreate it.
- PR #27/#28/#29/#30 remain OPEN/DRAFT. PR #30 has 0 independent reviews and 0 review threads before this update. PR #28's unsafe merge-all workflow removal remains a draft; the workflow was not triggered.
- Central README lists eight brands but only three active owner/status rows. Groot Academy's 100K/P0 accountable owner, one canonical queue writer and one independent release approver remain missing.
- Jaipur Engineers `je2` social vs `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. Preserve both owners/workstreams; do not infer either mapping.

## Queue and article ledger

- Planning PR #62, original controller branch and active canonical queue retain all **29 IDs in the same order**.
- Active canonical writable queue remains `content/groot-100k-controller-20261116-run61-main-delta`, blob `0b0685b89c8833f9f8b49d7e223c166145082956`.
- Research PR #68's 14 proceed proposals and GA-B00014 refresh remain research/refresh decisions, not completed articles.

| Metric | Verified |
|---|---:|
| Queue IDs | 29 |
| Complete original drafts | 23 |
| Technical visuals | 23 |
| PHP candidates | 23 |
| Independent editorial/code/visual PASS | 22 / 18 / 23 |
| Fully approved | 0 |
| Published | 0 |
| Live verified | 0 |

Run 103 created 0 articles, 0 images and 0 PHP candidates; no queue write, source ownership reassignment, Central Main write, merge, deployment, publication or indexing.

## Exact next owners/actions

1. Groot source owner / independent reviewer: review the consolidated #855 chain including #840 ancestry and prerequisite #755; keep all release gates intact.
2. GitHub Actions administrator/storage owner: diagnose BlobNotFound before any retry; then run the committed suite on a healthy checkout and verify PHP 8.0.
3. Groot source owner: after #755 approval, reconcile GA-B00006's four metadata differences and complete exact-Main PHP/shared-schema/H1/canonical/robots/route/registry/sitemap/browser/accessibility/HTTP/MIME checks.
4. Central owner: record one accountable Groot 100K/P0 owner, one canonical queue writer and one independent release approver.
5. Central/Jaipur owners: reconcile the social-vs-website/deployed-origin mapping explicitly.

No Central Main write, owner reassignment, self-approval, self-merge, deployment, publication or mass indexing.


## Post-commit Actions readback — 12:38 IST

The exact source head `dc81bb78f90d28a058bfaad208104e650c3250c7` triggered Actions run [44257891136](https://github.com/satnamkhowal/grootacademy.com/actions/runs/44257891136), job `134643875587` (`recovered-article-qa`). It completed as failure before any step: `steps: []`, `logs_url: null`; direct log retrieval returned Azure `BlobNotFound` HTTP 404 at `2026-11-18T07:25:57.6157922Z`. Hosted assertions **0**. This is infrastructure/log-artifact evidence, not a source test failure or a passing CI run. No retry without administrator/storage-owner diagnosis.
