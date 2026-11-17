# Central coordination delta — Groot Academy 100K, Run 94

Observed: 2026-11-18 04:41 IST. Coordination-only; no Central Main or brand source implementation change.

## Evidence

- Central Main is still `21af139cc32a7b67aab6908c61edeb5998bd4544`.
- Main README lists eight brands and only three active control-board rows; Groot Academy's dedicated 100K/P0 owner row is absent.
- Central PRs #1/#2/#3 are merged. Reuse the existing AEO/GEO baseline and queue from PR #2; do not recreate it.
- Current open coordination PRs #27/#28/#29/#30 are Draft. PR #30 is the existing Groot Run 93 audit lane; this report is appended on its branch.
- PR #28 proposes deleting `.github/workflows/merge-all-open-prs.yml`; the unsafe workflow remains on Main. It was not triggered or changed by this audit.
- Jaipur Engineers `je2` social workstream versus `jaipur-engieneers` candidate website/deployed origin remains unresolved. Preserve both workstream records; the 2026-10-19 report explicitly says this is not proof either repository is wrong.

## Groot source delta

- Source Main `388e4a7058ce02897110b3ed114ccd441e2a5875` compares identical to current Main (0 ahead/0 behind, no changed paths).
- New QA-only child [Groot PR #853](https://github.com/satnamkhowal/grootacademy.com/pull/853) adds bounded JSON-LD 1.1 `@vocab` term/compact-IRI expansion and five regression tests. Focused coordinator differential 9/9 and inserted-test AST parse 5/5; full suite/PHP 8.0/independent review remain pending.
- Actions run [#44198095261](https://github.com/satnamkhowal/grootacademy.com/actions/runs/44198095261), job `134444744539`, failed before steps with `steps=null`, `logs_url=null`; log retrieval returned Azure `BlobNotFound` HTTP 404, hosted assertions 0. Administrator diagnosis required; no blind retry.
- Planning/active/Main queue copies retain all 29 IDs and identical order. Active queue SHA `0b0685b8...` remains canonical; Main SHA `a4210712...` has stale statuses and must not overwrite it.
- Ledger remains 23 complete drafts / 23 visuals / 23 PHP candidates; editorial/code/visual PASS 22/18/23; fully approved/published/live 0/0/0.
- GA-B00006 four metadata differences and PR #755's independent date-less/noindex prerequisite remain open.

## Ownership and boundaries

Central owner must record Groot's accountable 100K/P0 owner, one canonical queue writer and one independent release approver. The source owner retains GA-B00006 metadata and release integration. The Actions administrator/storage owner retains the infrastructure diagnosis. Jaipur repository-role reconciliation remains with the existing central mapping owner.

No owner reassignment, other-brand file change, central-main write, merge, deployment, publishing or indexing.
