# Central coordination delta — Groot PR #507 current-main recovery reconciliation

**Observed:** 2026-11-12 05:43 IST  
**Central main:** 80c75e28734ce22831e93d9f431f4c15ccad0f6c  
**Source repository:** satnamkhowal/gta (permanent redirect to satnamkhowal/grootacademy.com)  
**Brand/domain:** Groot Academy / https://grootacademy.com/

## Source-lane delta

Groot historical recovery PR #507 was advanced on its existing branch only. Current source main before the operation was 0923feed95358ed967e0d783440fd28ba6d77a54. The old recovery head was ab7d4c13b3ff68b5c8ea760c50425c2ccf302264, based on d9eba9445ac5d58652d9b36f026e3b6efb5e2bea.

- Verified all five target article directories were absent from current main.
- Preserved all 22 exact historical blob objects: five PHP pages, five authored SVG diagrams, five original PNG social cards and seven code/fixture companions.
- Created merge commit 65c50c93733563c2fd55ff9f1b100338623046f0 with parents old recovery head ab7d4c13 and current main 0923feed; updated only recovery/restore-five-historical-articles-20261102 using expected-old-SHA guard.
- Post-update compare against source main: 2 ahead / 0 behind; 22 files; 961 additions; zero deletions. The PR remains OPEN/DRAFT with zero independent reviews and zero inline review threads.
- No source main, registry, sitemap, redirects, deployment, publication or indexing changed.

## Dependent recovery stack

PR #511 remains based on the previous root SHA ab7d4c13 and its head is f19b129a71f5bcd8f237d84848a792a30d4b38e0. It changes shared blogs/_shared/blog-layout.php and blogs/_shared/assets/blog.css; GitHub reports mergeable=false. It has zero inline review threads. Do not apply its shared-layout patch blindly; perform a three-way comparison against current source main and the updated #507 root before replay. PRs #513 -> #517 -> #520 -> #531 -> #533 remain sequential dependent work and must not be rebased independently.

## Canonical controller and queue

The Groot controller branch is now d21087ca768e046c5e366b761b5455c077d99554. README, CONTROLLER.json and the single canonical queue were updated together with the recovery report. The queue parser verified 29 rows and 29 unique IDs; only notes for GA-B00006 through GA-B00010 changed. All five retain PUBLISH_PR.

| Measure | Count |
|---|---:|
| Complete original text drafts | 23 |
| Technical visuals | 23 |
| PHP integration candidates | 23 |
| Independent editorial passes | 22 |
| Independent code passes | 18 |
| Independent approvals | 0 |
| Published | 0 |
| Live verified | 0 |

These are controller-branch artifacts and review states, not live site totals. Queue IDs, research proposals, refreshes and open PRs are not completed/approved/live articles.

## Central current-main and PR delta

- Central main remains 80c75e28734ce22831e93d9f431f4c15ccad0f6c; README SHA b93187c353f8112a57fffab4b383e64236976394.
- Central README registers eight brands but its active control board still has three rows (Jaipur Engineers, Central coordination and Forsk Coding School); Groot Academy's active row remains missing. No owner was invented or assigned.
- Central PR #1/#2/#3 are closed and merged. Existing AEO/GEO baseline from #2 is reused; no replacement audit was created.
- Central PR #20 remains OPEN/DRAFT, 57 ahead / 4 behind, 34 changed files, zero reviews. It was not modified.
- Central PR #22 remains OPEN/DRAFT on this audit branch, 4 ahead / 0 behind, two intended documentation files after this update, zero reviews. Central main was not changed.
- Jaipur Engineers je2 social repository versus jaipur-engieneers candidate website/deployed-origin mapping remains unresolved; no ownership inference or transfer.

## Exact next actions

1. Source owner/recovery lane: three-way review of PR #511's shared PHP/CSS changes against current main and updated #507 root; then replay #513, #517, #520, #531 and #533 in order.
2. Independent source/editorial, PHP/rendered schema, browser/image/download and release reviews remain required before #507 can be approved or merged.
3. Actions/storage administrator diagnoses Azure BlobNotFound on source review-candidate runs before meaningful exact-head CI.
4. Master owner records the 10K/P3 versus user-authorized 100K/P0 alignment and names one canonical queue/release owner.
5. Central owner adds Groot's active row only after confirming the named owner and source mapping; keep je2/website mapping unresolved until explicit reconciliation.

No self-approval, self-merge, deployment, publication, mass indexing, ranking claim or change to another brand's implementation.