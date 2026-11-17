# Groot Academy 100K — Run 87 central coordination delta

Observed: 2026-11-17 21:44 IST  
Scope: coordination-only. No Central Main, Groot production source, other-brand source, owner mapping, deployment or publication changed.

## Verified source and control-plane identity

- User alias `satnamkhowal/gta` resolves to canonical GitHub repository `satnamkhowal/grootacademy.com`, repository ID `1375760757`; brand Groot Academy, domain `grootacademy.com`.
- Groot Main remains `388e4a7058ce02897110b3ed114ccd441e2a5875`. Latest commit `388e4a7` changes roadmap empty-search presentation only; no blog-factory/shared-layout/registry/sitemap/queue path changed.
- Active controller successor `content/groot-100k-controller-20261116-run61-main-delta` is tracked by source PR #817; Run 87 evidence and exact continuation are committed on that branch.
- Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; current README blob `b93187c353f8112a57fffab4b383e64236976394`.
- Central Main's 2026-10-19 audit report and master pending queue were re-read. Main lists eight brands but only three active owner/status rows; Groot's dedicated 100K/P0 owner/status row, canonical queue owner and independent release approver are still missing. No owner was inferred or assigned.
- Central PR #1/#2/#3 are merged; existing AEO/GEO baseline PR #2 is reused. Central PR #27 remains OPEN/DRAFT at `df78ceb0b1c96e7b8203e56f48f8167db278e49a`, zero reviews. Safety PR #28 remains OPEN/DRAFT at `27e597db6828232a40b22a4721f52fb45b2a7154`, zero reviews; its proposed workflow deletion is not merged. Main's merge-all workflow remains present and was not triggered.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. Preserve both workstreams; central mapping owner must record distinct roles and evidence.

## New source QA delta

- Source PR #840's JSON-LD parser appended dictionary roots only; a top-level array was silently discarded. A second script containing an Article with `datePublished` inside an array could evade the recursive date guard.
- Python 3.13.5 coordinator-local reproduction confirmed the false-negative.
- Stacked QA-only [Groot PR #841](https://github.com/satnamkhowal/grootacademy.com/pull/841) was created on exact #840 head `a82b07c47e9049765765944c2d3d088cf619c2d0`. It normalizes object/array roots and adds one dated-array rejection and one clean-array control. Latest head `f9074b2f359707f94001f221c8dd52cd1887e11e`; two QA files only.
- Local focused harness: unsafe top-level Article array rejected; clean BlogPosting array accepted. This is not full committed-suite or hosted CI evidence.
- PR #841 remains OPEN/DRAFT, zero independent reviews/threads. Actions run 44124108011/job 134183063863 failed before steps (empty step list, log URL null, hosted assertions 0); root cause unknown, administrator diagnosis required. No retry or approval.
- PR #840 handoff comment: https://github.com/satnamkhowal/grootacademy.com/pull/840#issuecomment-6953856033

## Queue and article accounting

- Original planning queue blob: `c12a915e06c8100a350b21338311651df0f35094`.
- Active canonical queue blob: `0b0685b89c8833f9f8b49d7e223c166145082956`.
- Both contain all 29 original IDs in identical order; no queue write.
- Ledger remains 23 complete drafts / 23 technical visuals / 23 PHP candidates; independent editorial/code/visual PASS 22/18/23; fully approved/published/live 0/0/0.
- Run 87 new articles/images/PHP candidates/queue writes: 0/0/0/0. No planning ID, refresh, or prompt was counted as a finished article/image.

## Ownership and next actions

1. Independent reviewer assesses PR #841 → #840 → #755; no self-approval or merge.
2. Administrator/storage owner diagnoses repeated pre-step Actions failures before full-suite retry and PHP 8.0 verification.
3. Independently review parser stack #838 → #837 → #836 → #834 → #832 → #831 → #827 → #788.
4. After #755 review, source owner reconciles GA-B00006's four metadata differences and completes exact-Main PHP/schema/H1/canonical/robots/date/registry/sitemap/browser/accessibility/HTTP/MIME release gates.
5. Central owner records Groot 100K/P0 owner, one canonical queue owner and one independent release approver through normal reviewed governance.
6. Jaipur mapping owner reconciles social repository, candidate website and deployed origin without assuming either candidate is wrong.

No Central Main write, other-brand source change, ownership reassignment, merge, deployment, publication or mass indexing.
