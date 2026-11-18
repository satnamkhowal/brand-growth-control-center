# Groot Academy 100K — Run 111 central coordination delta

**Observed:** 2026-11-18 20:40 IST  
**Scope:** Coordination-only; no Central Main or other-brand implementation changes.  
**Source:** satnamkhowal/grootacademy.com (user alias satnamkhowal/gta; repository ID 1375760757).

## Verified source delta

- Current source Main is c3c7f6a23e7c4506d3261774ea0949e723fd5821. It is 18 commits ahead / 0 behind Run 110's a36cba9629a3d8a267b0660277967c72c02056a1 snapshot, with 21 changed paths.
- The current Main change to blogs/_shared/partials/head.php adds groot-placement-polish-v2.css while that partial includes root head.php, which independently adds the same stylesheet. Five static checks confirm the nested blog head emits two identical stylesheet references. This is a non-blocking source-owner follow-up; blogs/_shared/blog-layout.php and its BlogPosting/BreadcrumbList generator are unchanged.
- Source PR #855 remains OPEN/DRAFT at 16ef59949b4de4c149fad023ebf4742246e29335, exactly two QA files, 111 test methods, 0 reviews/threads. Its exact-head Actions run 44303621580 failed before steps with Azure BlobNotFound HTTP 404; hosted assertions 0; no retry. Full committed suite, W3C conformance and PHP 8.0 remain pending.
- Recovery PR #507 is 4 ahead / 80 behind current Main, with 22 intended historical additions and no deletions. Owner refresh is required; #654 → #660 → #664 plus #755/#782/#785 remain Draft.

## Queue and production ledger

- Original and active canonical queues retain the same 29 ordered IDs. Active canonical SHA 0b0685b89c8833f9f8b49d7e223c166145082956 remains on the existing queue branch; Main's older queue copy is not authoritative.
- 23 complete drafts / 23 technical visuals / 23 PHP candidates; independent editorial/code/visual PASS 22/18/23; fully approved/published/live 0/0/0.
- GA-B00006 remains PUBLISH_PR with four PHP/metadata differences and independent release gates pending. No new article, image, PHP candidate, queue row, registry or sitemap entry was added.

## Central governance delta

- Central Main remains 21af139cc32a7b67aab6908c61edeb5998bd4544. Its README lists eight brands and three active control-board rows; Groot Academy's 100K/P0 accountable owner, canonical queue writer and independent release approver are still absent.
- PR #1/#2/#3 are merged; reuse the existing AEO/GEO baseline from #2. Existing Central PR #30 remains OPEN/DRAFT with 0 independent reviews and 0 review threads.
- Safety PR #28 remains OPEN/DRAFT, and .github/workflows/merge-all-open-prs.yml is still on Main with workflow_dispatch. It can mark open drafts ready and attempt merges without per-PR approval gates. It was not dispatched or modified.
- Jaipur Engineers je2 social vs jaipur-engieneers candidate website/deployed-origin mapping remains unresolved. Preserve both workstream owners.

## Next actions

1. Central owner records one accountable Groot 100K/P0 owner, one canonical queue writer and one independent release approver.
2. Source owner obtains independent review of #855 and #755/#840 ancestry; Actions/storage administrator diagnoses BlobNotFound before any retry, then a healthy runner executes the full suite, conforming JSON-LD tests and PHP 8.0.
3. Source owner refreshes #507 against current Main, reconciles GA-B00006's four PHP/metadata differences and completes independent release gates.
4. Source owner removes the duplicate placement stylesheet reference from the shared blog head in a separate reviewed change.
5. Central owner disables/replaces the unsafe merge sweep before any dispatch and reconciles the Jaipur repository mapping with both owners.

No Central Main write, ownership reassignment, other-brand source change, self-merge, deployment, publication or mass indexing.
