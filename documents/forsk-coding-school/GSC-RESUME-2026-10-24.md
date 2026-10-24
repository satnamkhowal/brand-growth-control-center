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
- Live full-document AMP validation: not run in this checkpoint. Do not claim the live document passes AMP validation based only on the rendered style block.
- Search indexing: not checked in GSC. Do not claim reindexing or issue resolution in Google.

Verified public URL: https://forskcodingschool.com/web-stories/claude-fable-5-1-coding-students-september-2026/

### Search Console access

A fresh Search Console navigation in this browser redirected to the public Search Console about/sign-in page. The previous connected account had reported it lacked access to `https://forskcodingschool.com/`. No authenticated property view, fresh export, URL inspection, or Validate Fix submission was available. No new metrics or causes are claimed.

## Current repository ownership

- Forsk main is `f0e8076aa2647e02de5cf682846518aac0c9dbd9`.
- Forsk open PR #54 remains the editorial pilot owner; do not duplicate its Python/Java article work.
- Forsk PR #56 is merged; no open source AMP PR currently owns the Claude repair.
- Central PR #9 is still the scoped draft for this checkpoint. It has not been merged.
- No code change, deployment action, GSC submission, or noindex change occurred in this run.

## Next actions

1. Run the official AMP validator against the exact live Claude URL and record the result separately from source validation.
2. When an authenticated account with property access is available, inspect the AMP issue and URL status; submit GSC Validate Fix only after the live AMP validation passes and deployment is verified.
3. Resume P0 query/date diagnosis and reproduce reported 5xx, redirect, 403 and soft-404 examples only after acquiring current examples; verify each URL against the public host before route changes.
4. Continue the final-year guide task only after reconciling current source and existing recovery work. Preserve all existing noindex gates.

Never merge or deploy from this checkpoint, submit GSC validation without verified evidence and access, remove noindex gates, or redirect unrelated URLs.
