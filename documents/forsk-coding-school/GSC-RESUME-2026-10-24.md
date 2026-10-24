# Forsk Coding School — hourly GSC recovery checkpoint
Date: 24 October 2026 (Asia/Kolkata)
Property: https://forskcodingschool.com/ (URL-prefix)
Source repository: satnamkhowal/forsk-coding-school
Central repository: satnamkhowal/brand-growth-control-center

## Verified baseline

Use the performance and indexing figures in [GSC-AUDIT-2026-10-24.md](GSC-AUDIT-2026-10-24.md) as dated 24 October evidence, not a live refresh. The 28-day comparison recorded 173 versus 236 clicks and 21,473 versus 24,910 impressions. The two highest-loss URLs were indexed with matching user and Google-selected canonicals in that audit.

## Latest execution — 24 October 2026, 22:00 IST

### AMP source, public deployment and indexing states

- Source fix: Forsk PR [#56](https://github.com/satnamkhowal/forsk-coding-school/pull/56) corrected the Claude Fable 5.1 Web Story AMP boilerplate and merged to main as `c5634c68a4d0eac01cff565a60c8294925904416`.
- Current source main: `f0e8076aa2647e02de5cf682846518aac0c9dbd9` (documentation follow-up; parent is the #56 merge).
- Existing validator evidence from PR #56: `amphtml-validator@1.0.38` failed the previous source document and passed the patched source document. No validator was run during this checkpoint.
- Public deployment: the exact live URL below now renders the story. Its live `style[amp-boilerplate]` contains the full corrected animation block, including the `-o` and standard keyframes. This supersedes the earlier 21:48 note that publication was pending.
- Live full-document AMP validation: no valid result. The official validator UI raised a JavaScript TypeError (`setURLAndValidate is not a function`) before loading the URL; the displayed FAIL was for an empty document, not this story. No local `amphtml-validator` executable is installed in the current workspace. Do not treat this as a target-page failure or pass.
- Search indexing: not checked in GSC. Do not claim reindexing or issue resolution in Google.

Verified public URL: https://forskcodingschool.com/web-stories/claude-fable-5-1-coding-students-september-2026/

### Search Console access

A fresh Search Console navigation in this browser redirected to the public Search Console about/sign-in page. The previous connected account had reported it lacked access to `https://forskcodingschool.com/`. No authenticated property view, fresh export, URL inspection, or Validate Fix submission was available. No new metrics or causes are claimed.

## Current repository ownership

- Forsk main is `f0e8076aa2647e02de5cf682846518aac0c9dbd9`.
- Forsk open PR #54 remains the editorial pilot owner; do not duplicate its Python/Java article work.
- Forsk PR #56 is merged; no open source AMP PR currently owns the Claude repair.
- Central PR #9 is still the scoped draft for this checkpoint. It has not been merged.
- Source PR #57 now holds a scoped final-year guide improvement; no merge/deployment, GSC submission, or noindex change occurred.

## Next actions

1. Run `amphtml-validator` against the exact live Claude HTML from a working local/source environment; the official web validator UI is currently failing to initialize. Record the result separately from source validation.
2. When an authenticated account with property access is available, inspect the AMP issue and URL status; submit GSC Validate Fix only after the live AMP validation passes and deployment is verified.
3. Resume P0 query/date diagnosis and reproduce reported 5xx, redirect, 403 and soft-404 examples only after acquiring current examples; verify each URL against the public host before route changes.
4. Continue the final-year guide task only after reconciling current source and existing recovery work. Preserve all existing noindex gates.

Never merge or deploy from this checkpoint, submit GSC validation without verified evidence and access, remove noindex gates, or redirect unrelated URLs.


## Latest execution — final-year guide

- Verified current live canonical `https://forskcodingschool.com/final-year-project-ideas/` renders the existing guide and its ten idea list. Current main source is `final-year-project-ideas/index.php` using the shared `includes/restored-content-page.php` renderer.
- Open PR #54 does not touch either file. No other open source PR owns this page or renderer.
- Draft PR [#57](https://github.com/satnamkhowal/forsk-coding-school/pull/57) proposes three practical project briefs (attendance tracker, placement application tracker, public dataset dashboard), test/demo guidance, two matching FAQs, and page-specific visible/Article freshness dates.
- Branch: `seo/final-year-project-guide-20261024`. Commits: renderer `63aaf40da727cc655f31f73a98c99c4cc7b0521b`; guide `5658bda53a93039436316e8e70fc105a74135e15`. Compare reports only these two PHP files changed.
- Tests: no PHP syntax/runtime check could run because `php` is not installed in this workspace; owner-paused CI was not triggered. Browser QA, schema/link checks and mobile review remain pending.
- Source fix: draft only, not merged. Deployment: not deployed. Indexing: not checked in GSC. Preserve the current canonical, internal links and all noindex gates.

Next: obtain PHP lint/render QA for PR #57, then verify its host deployment only after ordinary approval/merge; independently restore authenticated GSC access for live indexing checks.