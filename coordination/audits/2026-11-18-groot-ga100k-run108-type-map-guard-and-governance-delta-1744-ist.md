# Groot Academy 100K — Run 108 coordination delta

**Date:** 18 November 2026, 17:44 IST  
**Source repository:** [satnamkhowal/gta](https://github.com/satnamkhowal/gta) — GitHub permanent redirect resolves to [satnamkhowal/grootacademy.com](https://github.com/satnamkhowal/grootacademy.com), repository ID `1375760757`. Brand: Groot Academy. Domain: `grootacademy.com`.

## Source QA delta

Existing [source PR #855](https://github.com/satnamkhowal/grootacademy.com/pull/855) remains OPEN/DRAFT on `qa/recovery-five-jsonld-propagation-guard-20261118-run95`, base `qa/recovery-five-jsonld-vocab-term-guard-20261118-run94`, exact head `16ef59949b4de4c149fad023ebf4742246e29335`, 21 commits / 2 files, zero independent reviews and zero review threads.

A further JSON-LD 1.1 false-negative was identified in the exactly-one BlogPosting guard: type-map keys contribute the type to each map value. The previous collector traversed values but did not apply the map key, so a duplicate BlogPosting could be hidden as an untyped node. JSON-LD 1.1 also permits type-map string values that expand to node objects and the special `@none` key (see [W3C JSON-LD 1.1 §4.6.3 and §9.12](https://www.w3.org/TR/json-ld11/#type-maps)).

Bounded repair on the existing PR #855 branch:
- [`e8536315`](https://github.com/satnamkhowal/grootacademy.com/commit/e853631562a71e7577d674e5ad09dfc96352961f): apply type-map keys to node-object and IRI-string values, preserve existing types, and recognize `@none`.
- [`76bcf268`](https://github.com/satnamkhowal/grootacademy.com/commit/76bcf26816795f19113152513c1f6321b54add98): five regression methods for hidden BlogPosting, existing other type, string values, Organization positive control and `@none`.
- [`8c7dd134`](https://github.com/satnamkhowal/grootacademy.com/commit/8c7dd134cf66832babb6f18a26e48a2d1e02f7d3): reject invalid/unresolved keyword type-map keys other than `@none`.
- [`16ef5994`](https://github.com/satnamkhowal/grootacademy.com/commit/16ef59949b4de4c149fad023ebf4742246e29335): sixth regression method for invalid keyword map keys.

The source test file now contains 111 test methods (six added in this run). An isolated coordinator logic mirror of the new type-map transformation passed 6/6 cases. This is not execution of the committed test suite, a conforming JSON-LD processor, or independent approval.

Exact-head Actions run [44303621580](https://github.com/satnamkhowal/grootacademy.com/actions/runs/44303621580), job `134799389748`, failed before steps (`steps: null`); log retrieval returned Azure `BlobNotFound` HTTP 404 at 12:25:19 UTC. Hosted assertions: 0. No retry; administrator/storage-owner diagnosis remains required. PR #855 remains Draft/unreviewed.

## Production queue and release ledger

The original controller branch `content/groot-100k-controller-20261016` was reread with README, CONTROLLER.json and queue. Active successor queue SHA remains `0b0685b89c8833f9f8b49d7e223c166145082956`; all 29 IDs GA-B00001–GA-B00029 remain in the same order. Planning PR #62 and research PR #68 decisions are preserved. No queue write.

Counts are unchanged:
- 23 complete original drafts, 23 technical visuals, 23 PHP candidates.
- Independent editorial/code/visual PASS: 22 / 18 / 23.
- Fully approved: 0; published: 0; live verified: 0.

GA-B00006 remains `PUBLISH_PR`: recovery PR #507 and dependent #654 → #660 → #664 remain OPEN/DRAFT; content repairs #782/#785 and date-contract prerequisite #755 remain unreviewed. Four PHP/metadata differences and exact-current-Main PHP/shared-schema/route/browser/accessibility/HTTP/MIME gates remain. No new article, image, PHP candidate, registry/sitemap change, publication or indexing.

## Current source Main

Latest source Main remains `f9c900e64baa3979e50c04e7293e246369e8f4b5` (18 Nov 2026, 08:52:54 UTC). Its four changed paths are alumni-only:
- `assets/css/groot-alumni.css`
- `includes/alumni-cards.php`
- `includes/alumni-profile.php`
- `index.php`

No blog-factory, queue, registry or blog-sitemap overlap. No Main write.

## Central control-plane delta

- Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; current Main README blob `b93187c353f8112a57fffab4b383e64236976394`.
- PR #1/#2/#3 are CLOSED/MERGED; existing AEO/GEO PR #2 baseline is reused.
- README registers eight brands, but the active control board has three owner/status rows. Groot Academy's 100K/P0 accountable owner, canonical queue writer and independent release approver are still not recorded.
- Jaipur Engineers `je2` social vs `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved; preserve both workstreams and owners.
- Existing PR #30 remains OPEN/DRAFT; this report is a coordination-only addition to its existing audit branch. No Central Main write, ownership reassignment, other-brand source change, merge, deployment, publication or indexing.

## Exact next actions

1. Independent reviewer evaluates the new type-map changes on source PR #855 and the existing #840/#755 date-contract chain; no self-approval.
2. Actions/storage administrator diagnoses Azure BlobNotFound. Only after diagnosis, run the full committed suite, conforming JSON-LD processor and PHP 8.0 on a healthy checkout.
3. Source owner refreshes GA-B00006 recovery #507 against current Main; preserve #507 → #654 → #660 → #664 and #782/#785. Reconcile the four PHP/metadata differences and complete exact-Main shared PHP/schema/H1/canonical/robots/route/registry/sitemap/browser/accessibility/HTTP/MIME gates.
4. Central owner records one accountable Groot 100K/P0 owner, one canonical queue writer and one independent release approver.
5. Keep new IDs/batches HOLD until release and governance gates are met.

No self-approval, self-merge, deployment, publication or mass indexing.
