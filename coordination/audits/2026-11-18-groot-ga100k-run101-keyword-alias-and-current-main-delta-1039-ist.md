# Groot Academy 100K Factory — Run 101 coordination delta

**Observed:** 2026-11-18 10:39 IST  
**Central Main:** `21af139cc32a7b67aab6908c61edeb5998bd4544` (unchanged)

## Source repository and current-Main delta

The user-supplied `satnamkhowal/gta` alias resolves to the same private GitHub repository ID `1375760757`, currently named `satnamkhowal/grootacademy.com`. Groot Academy remains the source implementation owner; this repository stores coordination evidence only.

Source Main advanced from `388e4a7058ce02897110b3ed114ccd441e2a5875` to `254affd91a55524d438260f4fc1816f10d43a0a1` (1 ahead / 0 behind). The one new commit adds six alumni-only paths: one profile PHP route, two image assets and three alumni include/data files. No blog-factory, article, shared blog-head, registry, blog-sitemap, canonical queue or release-QA path changed.

## New source QA finding

Existing source PR [#855](https://github.com/satnamkhowal/grootacademy.com/pull/855) has a reproduced false-negative in its exactly-one-BlogPosting guard. Exact helper functions from blob `014158285509a0c4ca1347f2dbd8ffaa3c2e38eb` were executed under Python 3.13.5:

- A valid `type` → `@type` keyword alias returns two root objects but only one counted BlogPosting.
- A valid `graph` → `@graph` keyword alias likewise returns two wrapper/root objects but only one counted BlogPosting.

The W3C JSON-LD 1.1 API permits keyword aliases generally and rejects aliasing `@context`; it does not prohibit `@type` or `@graph`: https://www.w3.org/TR/json-ld11-api/#create-term-definitions

A non-approval finding with exact reproductions and requested regressions was posted on PR #855: https://github.com/satnamkhowal/grootacademy.com/pull/855#issuecomment-6969783201

PR #855 remains OPEN/DRAFT with 0 reviews and 0 review threads. PR #840 and the prerequisite date-less/noindex PR #755 each have 0 review submissions. Full committed suite NOT RUN; PHP 8.0 UNAVAILABLE. Exact-head Actions run 44233324394/job 134563389629 failed before steps with Azure BlobNotFound HTTP 404 and zero hosted assertions; no retry.

## Queue and production state

Planning PR #62, original controller queue, active canonical queue and Main queue have the same 29 IDs in identical order. The active writable queue remains on `content/groot-100k-controller-20261116-run61-main-delta`, blob `0b0685b89c8833f9f8b49d7e223c166145082956`; no queue write occurred.

Research PR #68's 14 proceed proposals and GA-B00014 refresh remain research/refresh decisions, not completed new articles.

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

No new article, image or PHP candidate was created. No publication state changed.

## Central Main and ownership

- Current Central Main README blob: `b93187c353f8112a57fffab4b383e64236976394`; Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`.
- PR #1/#2/#3 are closed/merged; existing AEO/GEO baseline from PR #2 is reused, not recreated.
- Central PR #30 remains OPEN/DRAFT with 0 independent reviews. Its branch head before this report was `da1994e29b8b6460c566535b284da704c10ea7c0`.
- Central PRs #27/#28/#29 remain open draft coordination work. PR #28 removes the unsafe merge-all workflow, but the workflow remains on Main until independently reviewed/merged; it was not triggered or modified.
- README lists eight brands but only three active owner/status rows. Groot Academy's 100K/P0 owner row is still missing.
- Jaipur Engineers `je2` social versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved; no assumption or ownership change was made.

## Required next owners/actions

1. Groot source owner: add aliased `@type` and `@graph` regression cases and repair or fail closed in the existing #855 chain.
2. Independent reviewer: review #855 and the #755 date-less/noindex prerequisite; no self-approval.
3. GitHub Actions administrator/storage owner: diagnose Azure BlobNotFound before any retry.
4. Central owner: record one accountable Groot 100K/P0 owner, one canonical queue writer and one independent release approver.
5. Central/Jaipur owners: reconcile the `je2` social and candidate website/deployed-origin mappings explicitly.

No Central Main write, ownership reassignment, source implementation, merge, deployment, publication or indexing occurred.
