# Groot Academy 100K — Run 56 coordination delta

**Observed:** 2026-11-16 09:54 IST  
**Source repository alias:** satnamkhowal/gta  
**Resolved source repository:** satnamkhowal/grootacademy.com (GitHub repository ID 1375760757)  
**Brand/domain:** Groot Academy / grootacademy.com  
**Coordination PR:** [#22](https://github.com/satnamkhowal/brand-growth-control-center/pull/22)  
**Scope:** coordination-only evidence; all implementation remains in the Groot source repository.

## Source-side delta

Groot Run 56 continues from the Run 55 metadata parity checker. Reviewing its exact implementation found that the original regex could read fake $blog blocks from HTML/comments/strings/heredocs, rejected the actual generated PHP integer/boolean fields, and treated an explicit null date key as absent.

Source-side draft PR [#810](https://github.com/satnamkhowal/grootacademy.com/pull/810) adds a bounded PHP-region reader, typed scalar handling, explicit key-presence checks and regression coverage. Python 3.13.5 coordinator-local equivalent harness: **24/24 PASS**. This is not hosted CI, independent review or a full PHP parser.

Exact GA-B00006 source read-back:
- PHP candidate blob e9528d68cfb4909b60a9432f81acd6b141c6c815
- Paired metadata blob 5946e27f2283f8af4d3c7506719e4776faae32af

The repaired checker finds five mismatches: robots index/follow vs noindex/follow; date_published and date_modified present while metadata dates are null; visible display_date present without metadata counterpart; and featured-image alt mismatch. The earlier four-finding note is superseded. A factual handoff is recorded on source PR #785. Source-owner reconciliation is still pending; no source files were changed by this coordination report.

## Queue and release state

- Planning queue blob c12a915e06c8100a350b21338311651df0f35094 and active queue blob 0b0685b89c8833f9f8b49d7e223c166145082956 both contain 29 unique IDs in identical order.
- Counts remain 23 complete drafts, 23 technical visuals, 23 PHP candidates; component PASS editorial/code/visual 22/18/23; approved/published/live 0/0/0.
- New articles/images this run: 0/0. Queue rows changed: 0.
- PR #713 remains OPEN/DRAFT and source-owner controlled; current shared partial and root head both contain base elements. Current-Main refresh, independent review and full-root/schema/browser/HTTP/MIME gates remain.
- Azure Actions BlobNotFound pre-step failure remains unresolved; no blind retry and no hosted assertions claimed.

## Central governance delta

Read current Central Main README at commit 21af139cc32a7b67aab6908c61edeb5998bd4544 (blob b93187c353f8112a57fffab4b383e64236976394), the original 2026-10-19 Groot lane review and the current Run 48 successor report.

- Main still lists eight brands but only three active owner/status rows; Groot Academy's dedicated row remains missing.
- PR #1 (Jaipur social), #2 (AEO/GEO baseline) and #3 (coordination mapping audit) remain merged. Reuse the existing AEO/GEO PR #2 baseline; do not recreate it.
- Jaipur Engineers je2 social repository versus jaipur-engieneers candidate website/deployed-origin mapping remains unresolved. Preserve both owners and workstream roles until explicit mapping/deployment evidence exists.
- Central PR #22 remains OPEN/DRAFT with zero independent reviews; this report changes only the audit branch. No central Main write or owner reassignment.

## Exact next action

1. Groot source owner reconciles the five GA-B00006 source/metadata mismatches and reruns the parity check.
2. Verify rendered shared BlogPosting/BreadcrumbList/canonical only after the exact source pair is reconciled.
3. Source owner refreshes PR #713 against current Groot Main 21059089.
4. Azure administrator diagnoses BlobNotFound before hosted PHP 8.0/Python 3.12 validation.
5. Preserve independent review order #788 → #778 → #760 → #755 and existing #507 recovery ownership.
6. Keep new article IDs HOLD until Master-owner 100K/P0 alignment, canonical queue ownership and independent release approver are explicit.

No cross-brand source implementation, central Main write, self-approval, merge, deployment, publication, indexing or ranking/live claim.
