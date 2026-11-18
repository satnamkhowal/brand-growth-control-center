# Central coordination delta — Groot Academy 100K Run 99

Observed: 2026-11-18 09:09 IST  
Scope: coordination-only delta. No Central Main change, no all-brand crawl, no source implementation outside the Groot repository and no ownership transfer.

## Groot source evidence

- User alias `satnamkhowal/gta` resolves to `satnamkhowal/grootacademy.com`, repository ID `1375760757`; this is the Groot Academy lane.
- Re-read the original controller branch README, CONTROLLER.json and canonical queue, plus the Run 97 successor and latest source Main.
- Source Main remains `388e4a7058ce02897110b3ed114ccd441e2a5875`; latest commit changes only `career-roadmaps-2027.php`, with no blog-factory/shared-head/registry/sitemap/queue overlap.
- Controller checkpoint [PR #858](https://github.com/satnamkhowal/grootacademy.com/pull/858) is OPEN/DRAFT, documentation-only, stacked on Run 97 controller PR #857.

## Run 98 QA chain and Run 99 finding

- Source QA PR #855 is OPEN/DRAFT at `a83b5d542c7e4976ce31a23322ecd4e68013a016`; PR #840 head `a82b07c47e9049765765944c2d3d088cf619c2d0` is now an ancestor (18 ahead / 0 behind, exactly two QA files). The earlier divergent-stack observation is superseded.
- Run 99 fetched the exact helper blob `cae5af215f997e57d8715e399773ccb954fb1611`. Two JSON-LD 1.1 scoped-context fixtures (property-scoped and type-scoped) both returned an empty date-field list on Python 3.13.5, exposing a remaining false-negative in the draft date guard.
- Non-approval finding is recorded at [PR #855 comment 6968382182](https://github.com/satnamkhowal/grootacademy.com/pull/855#issuecomment-6968382182). W3C scoped-context reference: https://www.w3.org/TR/json-ld/#scoped-contexts.
- PR #855 has 0 independent reviews/threads; PR #755 has 0 reviews/threads.
- Exact-head Actions run [44230373414](https://github.com/satnamkhowal/grootacademy.com/actions/runs/44230373414), job `134553634600`, failed before steps; steps/log URL are null and log fetch returns Azure BlobNotFound HTTP 404. Hosted assertions 0. Administrator diagnosis required; no blind retry.

## Queue and article ledger

- Planning, original and active queue preserve 29 unique IDs GA-B00001–GA-B00029 in the same order.
- Active canonical queue remains on `content/groot-100k-controller-20261116-run61-main-delta`, SHA `0b0685b89c8833f9f8b49d7e223c166145082956`. Main's older status copy is not authoritative; do not overwrite the active queue.
- Statuses: MERGE 3, REFRESH 2, IDEA 1, PUBLISH_PR 5, TECH_QA 17, CONTENT_QA 1.
- Ledger: 23 complete original drafts, 23 technical visuals, 23 PHP candidates; independent editorial/code/visual PASS 22/18/23; fully approved/published/live verified 0/0/0.
- GA-B00029 remains TECH_QA. GA-B00006's four metadata differences and PHP/schema/publication integration remain pending. Research PR #68's 14 proceed proposals and GA-B00014 in-place refresh remain preserved and are not counted as extra completed articles.
- No new article, image, PHP candidate or queue write in this run.

## Central Main and PR #1/#2/#3

- Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; current Main README blob `b93187c353f8112a57fffab4b383e64236976394`.
- PR #1 (Jaipur Engineers social), #2 (AEO/GEO baseline) and #3 (coordination audit) are CLOSED/MERGED. Existing PR #2 baseline is reused; no duplicate crawl or AEO/GEO queue was created.
- README lists eight brands, but the active control board still has three owner/status rows. Groot Academy's 100K/P0 accountable owner, canonical queue writer and independent release approver remain missing.
- Jaipur Engineers `je2` social vs `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. Preserve both workstreams and owners; do not infer either is wrong.
- Existing unsafe merge-all workflow was not triggered or modified.
- Central PR #30 remains OPEN/DRAFT; this report extends its existing audit branch. No Central Main write, owner reassignment, merge, deployment, publication or indexing.

## Exact next action

1. Groot source QA owner fixes scoped-context support or fails closed on the existing #855 chain, adds property/type-scoped negative fixtures, then obtains independent review.
2. Administrator/storage owner diagnoses Azure Actions BlobNotFound; run the full committed suite on a healthy complete checkout and verify PHP 8.0 only after diagnosis.
3. Independently review PR #755's date-less/noindex contract.
4. Only after those gates, continue GA-B00006 source-owner metadata correction and exact-Main PHP/shared-schema/H1/canonical/robots/route/registry/sitemap/browser/accessibility/HTTP/MIME release checks.
5. Central owner records Groot 100K/P0 accountability, one canonical queue writer and one independent release approver. Keep new IDs/batches HOLD.

No self-approval, self-merge, deployment, publication or mass indexing.


## Run 99 follow-up — source QA guard repaired conservatively

The scoped-context false-negative reported above was addressed on the existing source PR #855 branch (no third code branch). The helper now fails closed when a term definition carries nested `@context`; two property-scoped/type-scoped regression methods were added. Exact source head `d1b94441a6649b8dd8ebda2513b867f0c3b4dec7`; PR #840 is an ancestor (20 ahead / 0 behind, two QA files).

Coordinator-local Python 3.13.5 focused mirror: **4/4 PASS** (two fail-closed cases and two clean controls); inserted test-method AST parse PASS. Full committed suite remains NOT RUN. New exact-head Actions run [44233324394](https://github.com/satnamkhowal/grootacademy.com/actions/runs/44233324394), job `134563389629`, failed before steps; log fetch returned Azure BlobNotFound HTTP 404, hosted assertions 0. PR #855 remains Draft with 0 reviews/threads.

Next: independent review, healthy-checkout full suite, PHP 8.0, PR #755 date-less/noindex review, then GA-B00006 release integration. No approval, merge, deployment or publication.
