# Forsk Coding School — hourly GSC recovery checkpoint
Date: 24 October 2026 (Asia/Kolkata)
Property: https://forskcodingschool.com/ (URL-prefix)
Source repository: satnamkhowal/forsk-coding-school
Central repository: satnamkhowal/brand-growth-control-center

## Verified baseline

Use the performance and indexing figures in [GSC-AUDIT-2026-10-24.md](GSC-AUDIT-2026-10-24.md) as dated 24 October evidence. They are not a live refresh. The 28-day comparison recorded 173 versus 236 clicks and 21,473 versus 24,910 impressions. Two highest-loss URLs remained indexed with matching user and Google-selected canonicals during that audit. The connected Google account currently lacks access to the property; an authorized account or read-only property access is needed to refresh exports and submit validation.

## Implementation state

- FCS-GSC-03 source repair: PR [#55](https://github.com/satnamkhowal/forsk-coding-school/pull/55) merged to source `main` as `f56881389148382b2fdb2e08dc3581c3116a8f95`; current `main` at checkpoint read: `2362ed63f6f4dc3b379bd246c0c241782191c76f`.
- Change scope: two AMP boilerplate lines in the Android Studio Quail 4 and AWS DVA-C03 Web Stories.
- Existing validator evidence: `amphtml-validator@1.0.38` passed both complete patched source files. Not rerun in this session; the GitHub status endpoint returned no statuses.
- Live state: the Android story rendered in a browser. Live HTML/source parity was not checked, the AWS page was not checked, production deployment is unverified, and GSC Validate Fix is not submitted.
- Current Search Console data: the connected Google account lacks property access. No fresh GSC metrics are claimed.
- Hourly `Forsk GSC Recovery` automation was created on 24 October (Asia/Kolkata). Runs are bounded by platform access and credits; no uninterrupted background work is promised.

## Next actions

1. Restore authenticated Search Console access for the URL-prefix property and export daily, page and query comparisons.
2. Verify both live story responses against merged source, run the live AMP validator, then use GSC Validate Fix only after deployment is verified.
3. Reproduce reported 5xx, redirect, 403 and soft-404 examples before route changes.
4. Resume unowned query/date diagnosis and final-year guide work; preserve noindex gates and existing recovery decisions.

Do not merge, deploy, submit GSC validation, remove noindex gates or redirect unrelated URLs without the required authorization and evidence.
