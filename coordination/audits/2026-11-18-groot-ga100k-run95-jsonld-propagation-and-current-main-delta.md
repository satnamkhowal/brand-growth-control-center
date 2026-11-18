# Central coordination delta — Groot Academy 100K, Run 95

Observed: 2026-11-18 05:41 IST. Coordination-only; no Central Main or other brand source implementation change.

## Verified current coordination state

- Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; no Main write.
- Main README blob `b93187c353f8112a57fffab4b383e64236976394` lists eight brands but only three active control-board rows. Groot Academy's dedicated 100K/P0 accountable owner, canonical queue writer and independent release approver remain absent.
- PR #1/#2/#3 are CLOSED/MERGED. Reuse the existing eight-brand AEO/GEO baseline and queue from PR #2; do not recreate them.
- PR #27/#28/#29/#30 remain OPEN/DRAFT. PR #28 proposes removal of `.github/workflows/merge-all-open-prs.yml`; the unsafe workflow remains on Main and was not triggered.
- The 2026-10-19 Groot coordination audit still records Jaipur Engineers `je2` social vs `jaipur-engieneers` candidate/deployed-origin mapping as unresolved. Preserve both workstream owners; no mapping was inferred or reassigned.

## Groot source delta

- User alias `satnamkhowal/gta` resolves to `satnamkhowal/grootacademy.com`, stable GitHub repository ID `1375760757`.
- Current Groot Main remains `388e4a7058ce02897110b3ed114ccd441e2a5875`, identical to the Run 94 controller snapshot; no new blog-factory/shared-head/registry/sitemap/queue overlap.
- New QA-only [PR #855](https://github.com/satnamkhowal/grootacademy.com/pull/855), child of [PR #853](https://github.com/satnamkhowal/grootacademy.com/pull/853), fixes JSON-LD 1.1 `@propagate:false` handling when flattening `@graph` nodes. Exact parent head `c877a4f6a9fa9f018eb9143b6721c4617ec553ab`; current child head `729510f2fd8c22dff3d79b5a6c18e5304d94d71c`. Only two existing QA files changed; three regression tests added.
- The defect could falsely count a graph child under a suppressed schema.org vocabulary or miss a child that should restore a previous schema.org context. W3C JSON-LD 1.1 §4.1.9 / Example 49 and the API context-processing algorithm support the propagation behavior: https://www.w3.org/TR/json-ld/#context-propagation and https://www.w3.org/TR/json-ld-api/#context-processing-algorithm.
- Coordinator-local Python 3.13.5 evidence: 26/26 context/term cases, 14/14 exact-IRI cases, 3/3 old-vs-fixed graph-propagation cases and AST parsing PASS. This is not the full committed suite, PHP 8.0, hosted CI or independent approval.
- PR #855 Actions run [44207142911](https://github.com/satnamkhowal/grootacademy.com/actions/runs/44207142911), job `134475889535`, failed before steps (`steps=null`, `logs_url=null`). Job-log retrieval returned Azure Storage `BlobNotFound` HTTP 404 at 2026-11-18T00:22:28Z; hosted assertions 0. Administrator diagnosis required; no retry.
- Original/active/Main queue copies preserve all 29 IDs and identical order. Active queue SHA `0b0685b89c8833f9f8b49d7e223c166145082956` remains canonical; Main SHA `a42107125efd657e21f29face2b3e0392c165376` is a stale status snapshot and must not overwrite it.
- Ledger remains 23 complete drafts / 23 technical visuals / 23 PHP candidates; independent editorial/code/visual PASS 22/18/23; fully approved/published/live 0/0/0. No new article, image, PHP candidate or queue write.
- GA-B00006 four PHP/metadata differences and independent PR #755 date-less/noindex prerequisite remain open. New IDs remain HOLD.

## Ownership and boundaries

- Source implementation stays in `satnamkhowal/grootacademy.com`; this report is coordination evidence only.
- No Central Main README, owner row, other brand source, AEO/GEO baseline, queue, workflow, deployment, publication or indexing change.
- Next: central owner records Groot 100K/P0 accountable owner, one canonical queue writer and one independent release approver; existing owners reconcile Jaipur repository/deployed-origin mapping. Groot source owner and independent reviewers retain the QA/release chain.
