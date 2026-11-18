# Central coordination delta — Groot Academy 100K Run 97

Observed: 2026-11-18 07:40 IST  
Scope: coordination-only evidence. No central Main change, no all-brand crawl, no source implementation outside the Groot repository and no ownership transfer.

## Source evidence

- Groot Academy source: `satnamkhowal/grootacademy.com`; user alias `satnamkhowal/gta`, same GitHub repository ID `1375760757`.
- Controller/report successor: [PR #857](https://github.com/satnamkhowal/grootacademy.com/pull/857), OPEN/DRAFT, stacked on Run 96 controller branch.
- Exact PR #840 date-guard helper blob `16fe83c2eb4f3f7324f93dadd86801c428c1754d` has a reproduced false-negative: a second Article JSON-LD object can use an inline `@context` alias `published -> https://schema.org/datePublished` and pass the current literal-key-only date guard.
- Coordinator Python 3.13.5 reproduction: current helper returns PASS / no date fields for that alias fixture. A local bounded resolver prototype passed 11/11 expected cases, but it is not committed or integrated.
- PR #840 and PR #855 both modify `tests/groot-recovery-five-render-qa.py` and `tests/test-groot-recovery-five-release-inventory.py` on divergent stacks; both have zero independent reviews and zero review threads. PR #855 remains stacked on #853 → #849 → #848 → #847; PR #840 is based on #755.
- No third code branch was opened, to avoid overlapping writes. Source owner should consolidate the alias guard into one linear current-head chain and obtain independent review.

## Current Main / queue / ledger

- Source Main remains `388e4a7058ce02897110b3ed114ccd441e2a5875`; latest commit only changes `career-roadmaps-2027.php`, with no blog/factory/shared-head/registry/sitemap/queue overlap.
- Planning, original and active queues preserve 29 unique IDs GA-B00001–GA-B00029 in identical order. Canonical queue SHA `0b0685b89c8833f9f8b49d7e223c166145082956`; no queue write.
- Statuses: MERGE 3, REFRESH 2, IDEA 1, PUBLISH_PR 5, TECH_QA 17, CONTENT_QA 1.
- Ledger: 23 complete drafts, 23 technical visuals, 23 PHP candidates; independent editorial/code/visual component PASS 22/18/23; fully approved 0, published 0, live verified 0.
- GA-B00029 remains TECH_QA; its existing content and candidate are not a publication approval.

## Central governance delta

- Central Main README blob remains `b93187c353f8112a57fffab4b383e64236976394`; central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`.
- Eight brands remain registered, three active control-board rows remain; Groot 100K/P0 accountable owner, canonical queue writer and independent release approver remain missing.
- Existing AEO/GEO baseline from PR #2 is reused; no duplicate crawl or baseline created.
- Jaipur Engineers `je2` social vs `jaipur-engieneers` candidate/deployed-origin mapping remains unresolved. Preserve both workstreams and owners.
- Unsafe merge-all workflow remains an existing central review item and was not triggered.
- No other brand's source files or task ownership changed.

## Exact next action

1. Groot source owner consolidates PR #840 and PR #855 → #853 → #849 → #848 → #847 into one linear current-head QA chain, incorporating alias/compact-IRI tests.
2. Obtain independent review; diagnose Azure Actions storage before retry; run the full committed suite and PHP 8.0 on a healthy checkout.
3. Independently review PR #755's date-less/noindex contract.
4. Only then continue GA-B00006 source-owner metadata reconciliation and exact-Main release gates.
5. Central owner records Groot 100K/P0 owner, one canonical queue writer and one independent release approver.

No central Main write, owner reassignment, source merge, deployment, publication or mass indexing.
