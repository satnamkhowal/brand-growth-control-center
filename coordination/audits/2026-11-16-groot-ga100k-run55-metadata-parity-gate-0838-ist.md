# Central coordination delta — Groot Academy 100K Run 55

Observed: 2026-11-16 08:38 IST

## Verified source ownership

- Brand: Groot Academy; domain: https://grootacademy.com/.
- User alias satnamkhowal/gta resolves to satnamkhowal/grootacademy.com, repository ID 1375760757.
- Source implementation and QA tooling remain in the Groot repository. This central report is coordination-only; no other brand repository or owner files were changed.
- Source checkpoint branch: content/groot-100k-controller-20261116-run55-metadata-parity-gate, successor of Run 54. Latest source checkpoint commit: eab6927566a2fd3288e59bef70eef38aa4f5e4ec.
- Source Main remains 21059089fb17d10200a386c7ef648d478bf700d7. Latest commit is limited to course-finder CSS and courses/index.php; no blog-factory overlap.

## New bounded evidence — GA-B00006 metadata parity

- The owner-controlled GA-B00006 source pair was read from branch fix/ga-b00006-defaults-source-20261115-run44, exactly two commits above its PR #782 parent.
- PHP source blob e9528d68cfb4909b60a9432f81acd6b141c6c815 declares robots=index,follow, display_date=November 1, 2026, and 2026-11-01 published/modified dates.
- Paired metadata blob 5946e27f2283f8af4d3c7506719e4776faae32af declares noindex,follow and null schema dates, with no display_date counterpart. This conflicts with the existing PR #755 date-less/noindex draft contract.
- Source owner was not bypassed; no source branch was edited. The article remains blocked from merge/registry/sitemap/publication pending reconciliation and rendered shared-schema/canonical recheck.
- New QA-only checker and tests were committed in the Groot source successor. Python 3.13.5: 8/8 unit tests PASS; py_compile PASS. The exact-value negative reproduction exits 1 with four expected robots/date/display-date mismatches. The checker is a restricted static generated-config guard, not a PHP runtime or release approval.

## Queue and measured state

- Planning PR #62 immutable sequence remains 29 IDs; active successor queue blob 0b0685b89c8833f9f8b49d7e223c166145082956 is unchanged.
- Complete drafts / technical visuals / PHP candidates: 23 / 23 / 23.
- Independent editorial/code/visual component PASS: 22 / 18 / 23.
- Fully approved / published / live verified: 0 / 0 / 0.
- New articles/images: 0 / 0. Research PR #68's 14 proposals and GA-B00014 refresh are not counted as completed articles.

## Central coordination and governance delta

- Central Main remains 21af139cc32a7b67aab6908c61edeb5998bd4544; current README blob b93187c353f8112a57fffab4b383e64236976394.
- README lists eight brands but only three active owner/status rows; Groot Academy's dedicated row remains missing. No owner inferred or reassigned.
- Jaipur Engineers je2 social versus jaipur-engieneers candidate website/deployed-origin mapping remains unresolved; preserve both workstream owners until explicit reconciliation.
- Central PR #1/#2/#3 remain merged; reuse existing AEO/GEO PR #2 baseline rather than recreate it.
- Existing coordination-only PR #22 branch audit/groot-ga22-browser-delta-20261112-0350 was 147 commits ahead / 0 behind Central Main before this report, with zero independent reviews. This report adds one audit file only; Central Main and other worker files remain unchanged.

## Exact next action

1. Groot source owner reconciles the GA-B00006 PHP robots/date/display-date values with the noindex/date-less metadata and PR #755 contract.
2. Rerun the new parity gate on the exact source pair; only after PASS, recheck rendered shared BlogPosting/BreadcrumbList/canonical.
3. Source owner refreshes PR #713 onto current source Main and obtains independent review.
4. Azure administrator diagnoses BlobNotFound before hosted CI retries.
5. Keep new IDs HOLD until Master-owner 100K/P0 alignment, one canonical queue owner and one independent release approver are explicit.

No Central Main write, source Main write, ownership reassignment, self-approval, self-merge, deployment, publication or indexing.
