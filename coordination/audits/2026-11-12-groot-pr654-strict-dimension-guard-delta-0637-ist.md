# Groot Academy — PR #654 strict featured-image dimension guard delta

**Observed:** 2026-11-12 06:37 IST  
**Coordination repository:** satnamkhowal/brand-growth-control-center  
**Source owner:** Groot Academy implementation remains in satnamkhowal/gta (GitHub rename/redirect to satnamkhowal/grootacademy.com).  
**Source PR:** [Groot Academy #654](https://github.com/satnamkhowal/grootacademy.com/pull/654)

## New source evidence

- A bounded code review found the initial integer conversion accepted malformed dimension values: PHP converts "1200px" to 1200, "1200.5" and 1200.5 to 1200, and true to 1.
- Existing source branch recovery/featured-image-intrinsic-ratio-main-compatible-20261112 was repaired in one file only: blogs/_shared/blog-layout.php.
- Commit [d18a14e](https://github.com/satnamkhowal/grootacademy.com/commit/d18a14e83f758b2b0e165cd6083ac0ab36586515); updated blob bce9d83be5fa50ddf65ffab063aee2baa756c982.
- New validation accepts only positive PHP integers or digit-only strings passing FILTER_VALIDATE_INT(min_range=1); width and height must both pass. CSS and all article/image/registry/sitemap/route files remain untouched.
- Comparison to the reconciled PR #507 parent: 3 commits ahead / 0 behind; exactly the same two intended shared-template paths remain changed.

## Validation and CI boundary

- PHP CLI 8.4.24 isolated fixture: syntax check PASS and 12/12 input cases PASS, including malformed numeric-prefix, fractional, boolean, overflow and leading-zero values.
- This is coordinator-run helper-fixture evidence only; it is not full-root PHP rendering, PHP 8.0 hosted lint, production browser/CLS/AT testing or independent review.
- Exact-head Actions runs [43132691797](https://github.com/satnamkhowal/grootacademy.com/actions/runs/43132691797) and [43132691768](https://github.com/satnamkhowal/grootacademy.com/actions/runs/43132691768) both failed before steps (steps:null). Log retrieval returned Azure BlobNotFound (404); zero assertions are evidenced as executed. Repository Actions/storage administrator diagnosis is required; no retry was triggered.
- PR #654 remains OPEN/DRAFT with zero independent reviews and zero review threads. Parent PR #507 remains independently gated and unmerged.

## Current coordination context

- Source main remains 0923feed95358ed967e0d783440fd28ba6d77a54; no source-main change occurred.
- Central main remains 80c75e28734ce22831e93d9f431f4c15ccad0f6c; this report is added only to the existing isolated PR #22 audit branch.
- Central README still lists eight brands but only three active control-board rows; Groot Academy's row is missing. Existing AEO/GEO PR #2 baseline is reused; PRs #1/#2/#3 are already closed/merged.
- Jaipur Engineers je2 social versus jaipur-engieneers candidate website mapping remains unresolved; no ownership inference or transfer.
- Canonical Groot queue remains 29 IDs, original order/statuses unchanged. Counts remain 23 complete drafts, 23 visuals, 23 PHP candidates, 22 editorial passes, 18 code passes, 0 independent approvals, 0 published and 0 live verified.

## Next action

1. Obtain independent review for updated source PR #654 and parent #507.
2. Restore Actions job-log availability and diagnose Azure BlobNotFound before meaningful CI rerun.
3. Run PHP 8.0/full-root rendering, then 320/390/1440 image decode, responsive, CLS, keyboard and assistive-technology checks.
4. Keep source implementation in the Groot repository and central work coordination-only.
5. Preserve Master-owner 10K/P3 versus user-authorized 100K/P0 and single queue/release-owner reconciliation. New article batches remain held until the owner decision.

No central main write, source main write, owner reassignment, self-approval, self-merge, deployment, publication, mass indexing or ranking claim.
