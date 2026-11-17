# Central coordination delta — Groot Academy 100K Run 73
**Observed:** 2026-11-17 08:41 IST  
**Scope:** coordination-only evidence. Groot source implementation remains in satnamkhowal/grootacademy.com; no Central Main or other-brand implementation changed.

## Verified source and queue mapping
- User alias satnamkhowal/gta resolves to Groot Academy source repository satnamkhowal/grootacademy.com, repository ID 1375760757; domain grootacademy.com. Not Mango Engineers.
- Original controller branch, active successor branch and current Main queue each contain 29 unique IDs in identical GA-B00001–GA-B00029 order.
- Original planning queue status counts: MERGE 3 / REFRESH 2 / IDEA 1 / PUBLISH_PR 5 / TECH_QA 17 / CONTENT_QA 1.
- Active successor queue has the same status counts and is the **single canonical writable queue for this controller**. Original planning queue is the immutable 29-ID baseline.
- Main's queue copy has MERGE 3 / REFRESH 2 / IDEA 13 / TECH_QA 10 / CONTENT_QA 1 and differs from the active queue in 18 rows. GA-B00006–10 are PUBLISH_PR in the active controller but TECH_QA in Main; GA-B00017–18 and GA-B00020–29 are TECH_QA in the active controller but IDEA in Main. Additional duplicate-check, owner, parent-topic and notes fields differ. Same IDs/order does not mean same state. Do not sync Main's stale status snapshot into the active controller.
- Current source Main remains 78edc3af373cdbaf634c7111fa349864dd55be8a; its latest commit touches only two batch-calendar files.

## New central safety finding — merge-all-open-prs workflow
Current Central Main file:
- .github/workflows/merge-all-open-prs.yml
- Exact blob: e21d1b84f37f3459b5fe09bd2c132081561275e7

The workflow has workflow_dispatch and a Main push trigger. The job runs on every manual dispatch or a push whose commit message contains [merge-sweep]. Its shell script:
1. enumerates all open PRs;
2. marks every draft PR ready;
3. attempts to merge every PR at its current head SHA.

It does not first require an independent APPROVED review, required passing checks, a current base, or an explicit per-PR allowlist. This can bypass the user's explicit no-self-merge/no-self-approval and independent release-gate requirements across the central repository. The workflow was not triggered by this run and was not changed. **Central owner action:** disable or replace it with per-PR independent-review, required-check, current-base and allowlist gates before any sweep. Do not use workflow_dispatch or a [merge-sweep] push.

## Priority, branch protection and owner mapping
- Current Groot Main task board docs/ai-ops/MASTER_TASK_BOARD.md lists HAO-008 Blog factory as P3/REVIEW. The user-authorized controller is 100,000/P0. Issue #401 defines 100,000 as evidence-gated M4 and 1,000,000 as conditional M5. Master-owner priority alignment, a named canonical queue owner and an independent release approver remain pending.
- Issue #401's current body says Main is protected by ordinary review/QA gates. Issue #570's latest direct observation (06:44 IST, same unchanged Main SHA 78edc3af) reports protected:false, classic protection disabled and required checks off; ruleset coverage remains unverified due integration permissions. The stale Issue #401 statement needs owner reconciliation; no branch settings were changed.
- Central Main remains 21af139cc32a7b67aab6908c61edeb5998bd4544. README blob b93187c353f8112a57fffab4b383e64236976394 lists eight brands and three active owner/status rows; Groot's dedicated row is missing. PR #1/#2/#3 are merged; reuse the existing AEO/GEO PR #2 baseline. Jaipur Engineers je2 social vs jaipur-engieneers candidate website/deployed-origin mapping remains unresolved.
- Original coordination baseline coordination/audits/2026-10-19-groot-lane-review.md was re-read; the Run 72 report on the current successor branch was also re-read. No owner was inferred, no workstream was reassigned and no other brand's files were edited.

## Groot release state
- GA-B00006 still has four PHP/metadata differences (robots, date_published, date_modified, display_date); PR #755 has zero independent review submissions.
- PR #788 remains OPEN/DRAFT with zero independent reviews; full committed suite is not executed in this run. Run 71's 16/16 PHP 8.4 differential is scratch evidence only.
- Controller ledger remains 23 complete drafts / 23 visuals / 23 PHP candidates; approved/published/live 0/0/0. Latest Issue #401 ledger labels live useful articles UNVERIFIED. No new article/image/queue row was created.

## Next actions
1. Central owner disables/replaces the merge-sweep workflow with per-PR safe gates and reconciles Issue #401's stale branch-protection statement against Issue #570.
2. Master owner resolves 100K/P0 vs HAO-008 P3/REVIEW, names one canonical queue owner and one independent release approver.
3. Source owner and authorized independent reviewer complete #755 → GA-B00006 four-field reconciliation → exact parity/shared-head → full-root PHP/schema/route/browser/accessibility/HTTP/MIME QA.
4. Preserve the active successor queue as canonical; do not copy Main's older status fields.
5. Keep Jaipur repository-role mapping unresolved until explicit central-owner evidence is recorded.

No Central Main write, source merge, other-brand implementation, ownership reassignment, workflow dispatch, self-approval, merge, deployment, publication or indexing.
