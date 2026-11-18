# Central coordination delta — Groot Academy Run 106

**Observed:** 2026-11-18 15:38 IST  
**Scope:** coordination-only evidence. Source implementation remains in `satnamkhowal/grootacademy.com`; no Central Main or other-brand source changes.

## Central baseline and governance

- Re-read Central Main README and the existing Run 105 report on PR #30's branch. Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`.
- Main lists eight brands but only three active control-board rows. Groot Academy still has no dedicated 100K/P0 accountable owner row, canonical queue writer or independent release approver.
- PR #1/#2/#3 are CLOSED/MERGED. Reuse the existing AEO/GEO baseline from PR #2; do not recreate it.
- PR #27/#28/#29/#30 remain OPEN/DRAFT. PR #28's proposed unsafe merge-all workflow removal is not merged; the workflow remains on Main and was not triggered.
- Jaipur Engineers `je2` social vs `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. Preserve both workstreams; do not infer either repository is wrong.

## Groot source delta

The user-supplied alias `satnamkhowal/gta` resolves to the same repository ID `1375760757`, currently named `satnamkhowal/grootacademy.com`.

Existing source QA PR [#855](https://github.com/satnamkhowal/grootacademy.com/pull/855) remains OPEN/DRAFT at head `5d7bfcbb07e83f62d8f71791d95c0dbd0324650a`, with zero independent reviews and zero review threads. Run 106 found another bounded false-negative: the current `_json_ld_root_objects()` traverses root objects and `@graph` / `@included`, but not node objects used as ordinary property values. W3C JSON-LD 1.1 §9.2 permits a property value to be a node object: https://www.w3.org/TR/json-ld11/#node-objects.

A coordinator-local Python 3.13.5 transcribed-collector reproduction counted one BlogPosting for a fixture containing a primary and nested secondary BlogPosting (1 collected / 2 present); a nested Organization control remained one BlogPosting. A non-approval finding was posted on [PR #855 comment 6975487384](https://github.com/satnamkhowal/grootacademy.com/pull/855#issuecomment-6975487384). This is not the committed full suite or a conforming processor run. Source-owner action: add nested duplicate-negative and non-BlogPosting positive fixtures, then traverse nested nodes with correct value/list/`@nest`/context semantics or fail closed where unsupported.

Exact-head Actions run [44275236448](https://github.com/satnamkhowal/grootacademy.com/actions/runs/44275236448) failed before steps; hosted assertions 0. No retry; administrator diagnosis of Azure BlobNotFound remains required.

## Current Main, recovery and GA-B00006

- Source Main advanced from `254affd91a55524d438260f4fc1816f10d43a0a1` to `f9c900e64baa3979e50c04e7293e246369e8f4b5` by one commit changing four alumni-only paths. No blog-factory, article, shared blog-head/layout, registry, sitemap or queue path changed.
- The exact GA-B00006 production path remains absent from current Main.
- Recovery PR #507 remains OPEN/DRAFT; current `main...#507-head` compare is 4 ahead / 49 behind with 22 added recovery paths. Owner refresh is required; no child was merged or refreshed.
- GA-B00006 source repairs #782/#785 and date-contract prerequisite #755 remain separate Draft gates. Independent review and exact-Main PHP/schema/H1/canonical/robots/route/registry/sitemap/browser/accessibility/HTTP/MIME evidence remain pending.

## Queue and production ledger

Original controller and active canonical queue were fetched separately; both contain the same 29 ordered IDs, GA-B00001 through GA-B00029. Original queue blob: `c12a915e06c8100a350b21338311651df0f35094`; active queue blob: `0b0685b89c8833f9f8b49d7e223c166145082956`. No queue write.

- Statuses: MERGE 3 / REFRESH 2 / IDEA 1 / PUBLISH_PR 5 / TECH_QA 17 / CONTENT_QA 1.
- Planning PR #62's 29 IDs remain preserved. Research PR #68's 14 proceed proposals and GA-B00014 refresh are not completed articles.
- Ledger: 23 complete drafts / 23 technical visuals / 23 PHP candidates; independent editorial/code/visual PASS 22/18/23; fully approved/published/live verified 0/0/0.
- No new article, image, PHP candidate, queue row, registry entry, sitemap URL, deployment, publication or indexing.

## Exact next owners/actions

1. Groot source owner: address nested node-object counting on existing PR #855; add duplicate-negative and non-BlogPosting positive fixtures.
2. Independent reviewer: review #855 and its #840 ancestry, plus prerequisite #755 date-less/noindex contract; no self-approval.
3. GitHub Actions/storage administrator: diagnose pre-step Azure BlobNotFound before any retry; then full committed suite, JSON-LD processor conformance and PHP 8.0.
4. Source owner: reconcile GA-B00006's four PHP/metadata differences and refresh #507 → #654 → #660 → #664 while preserving #782/#785 content work; complete exact-Main release gates.
5. Central owner: record one accountable Groot 100K/P0 owner, one canonical queue writer and one independent release approver; keep the Jaipur mapping open until repository/deployed-origin evidence is explicit.

No Central Main write, other-brand source change, owner reassignment, self-approval, merge, deployment, publication or mass indexing. Keep new IDs/batches HOLD.
