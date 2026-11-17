# Central coordination delta — Groot Academy Run 75

Observed: 2026-11-17 10:40 IST  
Scope: coordination-only evidence; source implementation remains in the verified Groot Academy repository.

## Source mapping and current heads

- User-facing repository alias `satnamkhowal/gta` resolves by GitHub permanent redirect to `satnamkhowal/grootacademy.com`, repository ID `1375760757`. The original controller branch remains `content/groot-100k-controller-20261016`; active verified successor is `content/groot-100k-controller-20261116-run61-main-delta`.
- Groot Main: `78edc3af373cdbaf634c7111fa349864dd55be8a`; no blog-factory path changed in its latest two batch-calendar commits.
- Active controller branch latest before this delta: `96f59a30227c584144980f14ca8e0cd206c84790`; source checkpoint Run 74.
- Central Main: `21af139cc32a7b67aab6908c61edeb5998bd4544`; README blob `b93187c353f8112a57fffab4b383e64236976394`.
- Central PR #1/#2/#3 are CLOSED/MERGED. Reuse the existing AEO/GEO PR #2 baseline; no duplicate baseline or queue created. Current Groot coordination PR #27 remains OPEN/DRAFT with zero independent reviews; this report is a new bounded delta on its existing audit branch.

## New source QA finding — owner action required

Groot PR #788 (QA-only child in the existing #755 → #760 → #778 → #788 recovery-date contract stack) has a reproducible false-negative:
- Exact inventory-reader blob: `5cc020476305f1d4a2a0aec4c2e20014ba1597f7`.
- Exact test blob: `3321ad460ed1e0ff50ca75566e1d59850cc5fa91`.
- Its `php_key_present()` and `php_value()` filters ignore double-quoted literal PHP keys/values.
- Coordinator Python 3.13.5 harness: 9/9 double-quoted cases missed across `display_date`, `date_published`, `date_modified` (null, empty and ISO value); 3/3 single-quoted baselines detected.
- PHP 8.4.24 accepts a double-quoted date key (`php -l` PASS) and runtime `array_key_exists()` returns true.
- This can let a valid PHP double-quoted date key evade the draft “omit all date keys” gate. The current five candidate files were not shown to use this form; do not claim an affected production candidate.

A non-approval finding was posted on [Groot PR #788](https://github.com/satnamkhowal/grootacademy.com/pull/788#issuecomment-6939283680). The QA owner's parser/test files were not changed by this coordination lane.

## Ownership and status boundaries

| Workstream | Verified owner / source | State | Next action |
|---|---|---|---|
| Groot 100K factory | Groot Academy; active successor branch above | 23 complete drafts, 23 visuals, 23 PHP candidates; approvals/live 0/0 | QA owner repairs double-quoted parser false-negative; independent #755 and #760→#778→#788 reviews remain mandatory |
| Central AEO/GEO | Existing central PR #2 baseline and follow-up queue | PR #2 merged; no new audit or source implementation | Reuse existing queue; source owners retain each fix |
| Jaipur Engineers social | `satnamkhowal/je2` workstream from merged PR #1 | Social repository evidence retained | Mapping owner records social vs production repository roles and deployed-origin evidence |
| Jaipur Engineers candidate website | `jaipur-engieneers` remains a candidate source in prior AEO registry | Production identity unresolved | Do not infer either repository is wrong; reconcile against deployed origin |
| Other brands | Existing named source owners | No new evidence in this run | No ownership transfer or cross-brand edits |

Central README still lists eight brands but only three active owner/status rows; Groot's dedicated owner row is missing. Main Master Plan still records 10,000 capacity and HAO-008 P3/REVIEW while the authorized Groot controller is 100,000/P0. Master-owner alignment, one canonical queue owner and one independent release approver remain unresolved.

The Central Main all-open merge-sweep workflow finding from Run 73 is unchanged: it can ready Draft PRs and attempt all open PRs on manual dispatch or `[merge-sweep]` without per-PR approval/check gates. It was not triggered or modified.

## Ledger and release boundary

- Planning PR #62 and research PR #68 remain preserved; all 29 canonical IDs/order remain unchanged.
- Active queue is the only writable queue; Main's 18-row status drift is not synchronized back.
- Complete drafts / visuals / PHP candidates: 23 / 23 / 23.
- Independent editorial/code/visual component PASS: 22 / 18 / 23.
- Fully approved / published / live verified: 0 / 0 / 0.
- Run 75 new articles / images / PHP candidates / queue writes: 0 / 0 / 0 / 0.
- No central Main write, other-brand source change, owner reassignment, merge, deployment, publication or mass indexing.

## Exact next action

Groot QA owner fixes double-quoted literal-key handling with regressions and runs the complete committed #788 suite on a healthy checkout. Obtain independent review of the #760 → #778 → #788 stack and separately of #755's date-less/noindex contract. Only then may the existing source owner reconcile GA-B00006's four fields and continue PHP 8.0/full-root/schema/route/browser/accessibility/HTTP/MIME release gates. Central owner/admin handles the unsafe merge-sweep and adds the missing Groot owner/status row; Master owner reconciles P0/P3 and names the queue/release owners. No self-approval or integration is authorized by this delta.
