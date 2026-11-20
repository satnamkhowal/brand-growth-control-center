# PR integration supervisor — initial checkpoint (2026-11-20 IST)

**Status:** Active scheduled hourly inspection; this is a verified checkpoint, **not** proof of deployment or successful merging.

## Scope and order

1. `satnamkhowal/jaipurengineers.com` — inspect and integrate only safely merge-ready PRs targeting `main`.
2. Other `satnamkhowal` repositories — use each repository's verified default branch; some use `master` or `Main`.
3. `satnamkhowal/brand-growth-control-center` — reconcile P0 tasks and preserve one owner per task.
4. Remaining capacity — work on the highest-priority unclaimed verification or blocker.

## Observed GitHub evidence

| Repository / PR | Observed state | Release gate / next action |
| --- | --- | --- |
| Jaipur Engineers — [#115](https://github.com/satnamkhowal/jaipurengineers.com/pull/115) | Open, non-draft, GitHub reports mergeable; latest checked head `629d1659489c232f48d0299100a21f3b04c47d23` | **HOLD.** Four exact-head Actions runs reported failure (Communication course PHP and browser QA; GSC recovery validation; Java path chooser QA; Internship canonical sitemap contract). Review failing workflows, rerun validated checks and obtain required review before any merge. |
| Jaipur Engineers — [#116](https://github.com/satnamkhowal/jaipurengineers.com/pull/116) | Open, Draft, base `main`; head `010e30ff2d939a861c0b5d90e8d8a4bd33ef8357` | **HOLD.** Exact-head PHP lint and rendered contract pending, with reviewer check explicitly required. |
| Jaipur Engineers — [#117](https://github.com/satnamkhowal/jaipurengineers.com/pull/117) | Open, Draft, base `main`, GitHub reports not mergeable | **HOLD.** Required CI, responsive QA, and performance validation pending. |
| Jaipur Engineers open PR queue | 26 open PRs returned by repo-scoped search | Additional PRs have not yet completed per-head checks; neither green CI nor merge eligibility has been assumed. |
| Central Controller open PR queue | 33 open PRs returned by repo-scoped search | Inspect priorities and dependencies before integrating; do not merge controller documentation updates blindly. |

Repository discovery found 78 repositories accessible in the linked `satnamkhowal` account. This is an inventory count, not a claim that all are approved for automated merging.

## Mandatory merge gates

- Repository belongs to the authorized owner; PR base is the verified default branch.
- PR is non-draft, reviewed as required, and no unresolved release/security restrictions.
- Required CI completes successfully on the **current head SHA**, not just on a previous commit or a textual PR claim.
- Diff, conflicts, overlapping edits and dependencies have been inspected.
- Use `expected_head_sha` on merge, do not bypass GitHub protections, never use a mass-merge-all workflow.
- Mark `DONE` only after merge and independently evidenced deployment/production verification where applicable.

## Work performed in this checkpoint

- Inspected controller operating policy and initial Jaipur/Controller PR queues.
- Verified exact-head workflow failures for Jaipur #115.
- Verified Draft status for Jaipur #116 and #117.
- **No PR was merged. No production deployment was performed.**
- Opened a scoped coordination PR for this evidence so other workers can review the checkpoint.

## Next scheduled iteration

1. Re-check Jaipur's latest PR heads and required workflows.
2. Diagnose or route Jaipur #115 CI failure and identify safe ready PRs.
3. Scan the other authorized brand PR queues after Jaipur's ready queue.
4. Update this checkpoint or the main controller board without overwriting parallel agents' edits, citing PR/test evidence.

## Supervisor checkpoint — 2026-11-20 18:05 IST

- **Jaipur inventory:** 26 open PRs targeting the repository search scope; main tracker read from blob `0db8e2c6755e10ec23f3b6094735fa9c240b5d63`. Latest QA evidence records exact-head Actions failures before job steps and no production verification.
- **Exact current PR metadata:** #115 head `629d1659489c232f48d0299100a21f3b04c47d23`, non-draft, `mergeable=false` at this refresh; #116 head `010e30ff2d939a861c0b5d90e8d8a4bd33ef8357`, Draft and `mergeable=false`; #117 head `cdddaca5aa768dd1fb77f36940e3e1ba09209d41`, Draft; #112 head `6478c15aa4561624335c57f174617573fa2bc9f2`, `mergeable=false`; #72 head `8f5679b1a30cc17c4fb5620afa9d876327479e9f`, `mergeable=false`. The mergeable flag changed from the earlier #115 checkpoint; treat live metadata as authoritative and re-evaluate later.
- **Other owned repositories sampled:** `grootacademy.com` (30 open PRs returned, capped), `forsk-coding-school` (30, capped), `mangoengineers.com` (30, capped), `groot-software-new-website` (7), and this Controller (34). This is not an exhaustive 78-repository PR sweep. Sampled #918 Groot, #264 Forsk and #38 Groot Software are Draft; no merge attempted.
- **Controller safety risk:** [#28](https://github.com/satnamkhowal/brand-growth-control-center/pull/28) proposes removing unsafe `merge-all-open-prs.yml`, but remains Draft and unmerged. It documents an existing manual workflow capable of converting drafts and attempting merges without review/CI gates. **P0 next action:** independently review and safely retire this workflow, without executing it.
- **CI blocker:** [Jaipur #115](https://github.com/satnamkhowal/jaipurengineers.com/pull/115) and [#116](https://github.com/satnamkhowal/jaipurengineers.com/pull/116) have exact-head Actions jobs failing before steps according to the independent QA ledger. Diagnose Actions startup/billing/policy and obtain actual Python/PHP checks plus independent QA before integration. No legacy combined-status result is a substitute.
- **Outcome:** 0 PRs merged; 0 deployments; 0 tasks marked DONE. This update is a coordination-only change on the existing PR #48 branch, not on Controller `main`.
- **Next run:** prioritize #115 exact-head CI recovery and mergeability/conflict inspection, then inspect non-draft Jaipur PRs with passing checks; follow with the owned-brand queue and controller #28 safety review.
