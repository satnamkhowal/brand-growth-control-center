# Forsk Coding School — GSC recovery checkpoint
Updated: 24 October 2026, 23:07 IST
Property: https://forskcodingschool.com/ (URL-prefix)
Source repository: satnamkhowal/forsk-coding-school
Central repository: satnamkhowal/brand-growth-control-center

## Search Console evidence

Latest dated audit is 24 October 2026; it is not a fresh export. Its equal 28-day windows recorded 173 vs 236 clicks (-26.69%) and 21,473 vs 24,910 impressions (-13.80%). Homepage and /final-year-project-ideas/ were the largest observed losses. The same audit counted 19 server errors and 10 redirect errors but does not provide reproducible sample URLs in the checkpoint. Do not infer current failures or change routes from counts alone.

No authenticated GSC property view is available in the current browser. No current page/query exports, URL inspection, AMP validation submission, or indexing status was obtained. No new metrics or causal explanation is claimed.

## FCS-GSC-03 — AMP stories

- Source repair PR #56 merged as `c5634c68a4d0eac01cff565a60c8294925904416`; current source main is `da2fc2f0599c185309cf681aaa20e31bb1798297`.
- Claude live URL: https://forskcodingschool.com/web-stories/claude-fable-5-1-coding-students-september-2026/
- Central handoff records fresh HTTP 200 at the same URL, corrected live boilerplate matching the repaired source, and complete live HTML PASS with `amphtml-validator@1.0.38` plus official `validator_wasm.js`. Recorded live HTML SHA-256: `40a9d882f4629d7a96c8e112cd4a928e1c949e8f9ebf28d3b69765145e01d13b`.
- States: source merged; deployment verified; AMP validation PASS; GSC validation/indexing and recovery NOT verified. No GSC Validate Fix submitted.
- AWS and Android live AMP passes are recorded in the preceding checkpoint; no changes needed this run.

## FCS-GSC-04 — final-year guide

- Draft source PR [#57](https://github.com/satnamkhowal/forsk-coding-school/pull/57), branch `seo/final-year-project-guide-20261024`, owns the guide and shared renderer.
- Commits: renderer `63aaf40da727cc655f31f73a98c99c4cc7b0521b`; guide `5658bda53a93039436316e8e70fc105a74135e15`.
- PR adds three project briefs, test/demo guidance, two FAQs and page-specific freshness metadata. It is not merged or deployed; indexing not checked.
- Current main advanced to `da2fc2f0599c185309cf681aaa20e31bb1798297`; PR #57 is one commit behind main and two commits ahead, with no conflicting paths reported by compare.
- PHP lint/runtime and browser/schema/mobile/link QA remain pending. No PHP executable is installed in this workspace; owner-paused workflows were not triggered.
- Open PR #54 remains a separate editorial pilot owner. Do not duplicate its work.

## Current next action

FCS-GSC-02 is blocked on current error examples: reproduce the exact 5xx/redirect/403/soft-404 URLs from an authenticated GSC export, then test those URLs against the public host before any route change. If GSC remains unavailable, do not substitute old exports or guess URLs. Keep noindex gates; do not merge, deploy, or submit GSC validation.

## Central coordination

This checkpoint is recorded on draft central PR [#9](https://github.com/satnamkhowal/brand-growth-control-center/pull/9), not merged. Source PR #57 and central PR #9 remain separate drafts.
