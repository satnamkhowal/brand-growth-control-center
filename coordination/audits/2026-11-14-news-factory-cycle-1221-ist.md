# News Factory cycle — 14 November 2026, 12:21 IST

## Executive status

Four non-overlapping research lanes were checked: official student/developer opportunities; React/frontend releases and security; Node.js/backend releases and security; AI/cloud/developer announcements. One new, unowned, time-sensitive developer topic was selected for Mango Engineers. Existing story owners were retained. This is a draft-production checkpoint, not a publication or deployment report.

## 1. Official student/developer programmes

### NASA Space Apps Challenge 2026 — existing Forsk owner

- Official programme announcement: 26 August 2026; hackathon event: 14–15 November 2026.
- The official 2026 page says registration, event selection and team changes remain open until the hackathon closes on 15 November.
- Project submission opened 14 November at 09:00 and closes 15 November at 23:59 local time.
- Teams may contain no more than six participants. A project submission is required for a participant certificate and Global Judging eligibility.
- India local-event pages are listed, but local event pages are participant/organizer content and can add their own conditions. The global page does not publish a universal participation fee, stipend or cash-award amount.
- Existing owner: [Forsk issue #230 / Draft PR #231](https://github.com/satnamkhowal/forsk-coding-school/pull/231). Its original NASA Space Apps registration video ID `LhYn_hPfr34` remains the existing verified embed; no duplicate article or new video was created.

Primary source: https://www.spaceappschallenge.org/2026/

### Google Student Researcher, 2027 — existing Forsk owner

- Direct Google Careers listing is live and displays **India — Remote eligible**.
- Application deadline: **4 December 2026**; Google says applications are reviewed on a rolling basis.
- Minimum qualification: current enrolment in a Bachelor's, Master's or PhD programme in one of the listed disciplines (including Computer Science, Linguistics, Statistics, Biostatistics, Applied Mathematics, Operations Research, Economics or Natural Sciences) and experience in one computer-science research area.
- Preferred: full-time enrolment and returning to the programme after the engagement; prior research experience and general-purpose programming experience.
- The listing requires the candidate to be located in one of the specified country locations for the full engagement. It does not state a stipend or fixed engagement duration; do not invent either.
- Existing owner: [Forsk PR #146](https://github.com/satnamkhowal/forsk-coding-school/pull/146). No duplicate article created.

Primary source: https://www.google.com/about/careers/applications/jobs/results/125423735539671750

### INSPIRE-SHE 2025 — existing Forsk owner; live portal recheck incomplete

- Existing [Forsk PR #167](https://github.com/satnamkhowal/forsk-coding-school/pull/167) records a 7 November 2026 call notice and 7 December 2026, 23:59 IST deadline. The live portal homepage timed out in this pass, so the current window is **not independently revalidated here**.
- The official SHE FAQ PDF currently linked by the portal is labelled 2024. It describes ₹80,000/year as ₹60,000 scholarship plus ₹20,000 summer-research mentorship, up to five years, with same-year Class XII and same-year enrolment in listed Basic/Natural Science degrees.
- The FAQ explicitly excludes Engineering, Computer Science, Computer Applications and Information Technology. It must not be promoted as an IT scholarship.
- No new draft was created; recheck the live portal and current cohort guidance before publication.

Primary FAQ: https://online-inspire.gov.in/Content/SHEFAQs2024.pdf

Other current opportunity owners (NMMSS, Sage IT, VSSC, NeGD, AICTE, UGC and related schemes) were preserved in their existing Forsk/Mango PRs. No old programme was presented as newly launched.

## 2. React / frontend releases and security

- React's latest feature announcement in the reviewed release stream is React 19.3 (9 September 2026); the October 14 security patch line is not a new November feature launch.
- On 14 October 2026, React published a **Critical** unauthenticated RCE advisory for React Server Components (CVSS 9.5) and a **High** Server Functions DoS advisory (CVSS 8.2).
- The advisories list patched RSC package versions **19.0.9, 19.1.10, 19.2.9 and 19.3.1** for `react-server-dom-webpack`, `react-server-dom-parcel` and `react-server-dom-turbopack`. Apps without a server or without an RSC-capable framework/bundler/plugin are outside the stated affected deployment conditions.
- Existing owners: [Forsk PR #145](https://github.com/satnamkhowal/forsk-coding-school/pull/145) (RSC security) and [Mango PR #202](https://github.com/satnamkhowal/mangoengineers.com/pull/202) (React 19.3 features/patch guide). No duplicate article created.

Primary advisories:
- https://github.com/react/react/security/advisories/GHSA-xqc2-xf4c-x3h3
- https://github.com/react/react/security/advisories/GHSA-h3gv-c5rc-p453

## 3. Node.js / backend releases and security

- Node.js published security releases on 11 November 2026 for **22.23.5, 24.22.3 and 26.13.1**.
- The official security post lists 16 CVEs in total (7 high, 6 medium, 3 low) across the 22.x, 24.x and 26.x lines, with differing affected-line ranges. Not every CVE affects every line.
- The post includes high-severity HTTP/2 remote abort, HTTP/2 memory/file-descriptor leak, TLS/HTTPS memory-disclosure and TLS-server process-termination issues. Operators should follow the per-CVE affected-range table, not assume identical impact across all release lines.
- Node.js 27.0.0-alpha.0.1.0 (12 November) is an Alpha prerelease, not stable or LTS.
- Existing owner: [Mango PR #143](https://github.com/satnamkhowal/mangoengineers.com/pull/143) already includes the 11 November security release and patched versions. No duplicate article created.

Primary source: https://nodejs.org/en/blog/vulnerability/november-2026-security-releases

## 4. AI / cloud / developer news

### New unowned topic selected: Cloudflare Workers module registry default

- Technical explainer publication date: **9 September 2026**.
- Compatibility changelog publication date: **2 November 2026**.
- Effective default date: **17 November 2026** for JavaScript Workers whose compatibility date is `2026-11-17` or later.
- Earlier JavaScript Worker compatibility dates remain on the legacy registry unless `new_module_registry` is enabled. `legacy_module_registry` retains legacy behaviour after the default date. Existing Workers do not switch merely because the calendar date arrives. Python Workers remain on the legacy registry.
- New guide covers URL-based module identity, `import.meta`, import-attribute validation, CommonJS-to-ESM `require()`, top-level-await restrictions, opt-in/opt-out flags and a staged migration checklist.
- Deduplication: no matching module-registry PR/issue owner found in Mango, Groot, Forsk, Jaipur or central repositories. Existing Cloudflare Spend Management (Groot #745), Kitesurf (Groot #743) and QuePaxa (Mango #216) are distinct stories.

Deliverables: [Mango Draft PR #238](https://github.com/satnamkhowal/mangoengineers.com/pull/238), task ID `NF-MANGO-CLOUDFLARE-MODULE-REGISTRY-20261114-1208`.
- Article: 2,382 words, original English developer migration guide.
- Metadata: SEO/source/claim dates, pricing/geography caveats, video status, media provenance, alt text, dimensions, local paths, sizes and SHA-256.
- Original SVG: 1200×675, committed. Local PNG and WebP derivatives: 1200×675, rendered and visually inspected.
- No third-party graphic, Cloudflare logo or screenshot used. No relevant verified original YouTube video ID/date/embedding evidence found; no iframe was added and no video was downloaded.
- PR remains OPEN / DRAFT. No route, sitemap, schema, PHP, shared UI or production asset changed.

Primary sources:
- https://developers.cloudflare.com/changelog/post/2026-11-02-module-registry-default/
- https://blog.cloudflare.com/workers-module-registry-nodejs/
- https://developers.cloudflare.com/workers/configuration/compatibility-flags/
- https://developers.cloudflare.com/workers/runtime-apis/nodejs/
- https://developers.cloudflare.com/workers/wrangler/bundling/

### Google Cloud follow-up candidates — no draft this cycle

- Google Cloud release notes dated 13 November list Gemini Enterprise 3-legged OAuth with Agent Identity auth manager for A2A agents as GA, Cloud Quotas as GA, and BigQuery federated connections to MySQL/Oracle/PostgreSQL as Preview.
- The current Gemini Enterprise “Register and manage A2A agents” documentation page labels the overall A2A registration feature Preview while describing the 3LO workflow. This status mismatch needs clarification before an article labels the overall workflow GA.
- No new article or video embed was created for these candidates in this cycle.

Primary source: https://docs.cloud.google.com/release-notes

## Repository and coordination review

- **Central:** read README, pending-task queue, latest 11:11 audit and PR #19. Existing branch `ops/news-factory-cycle-20261109-2209` was **201 ahead / 5 behind main (diverged)** at the pre-update comparison. No rebase, force-push or merge.
- **Mango Engineers:** read README, AGENTS, agent start guide, task board, work log and integration queue; reviewed current open PRs and deduped against #143, #202, #204, #216, #218, #229, #230 and other owners. New PR #238 changes only three new News Factory paths. Shared task board/work log/integration queue were not modified because active PRs own those coordination paths.
- **Groot Academy:** reviewed accessible `grootacademy.com` instructions and open PR inventory; existing Cloudflare owners #743 and #745 retained. No new Groot write.
- **Forsk Coding School:** reviewed README, AI task board/session handoff and open PR inventory; #145, #146, #167, #231 and other opportunity/security owners retained. No new Forsk write.
- **Jaipur Engineers:** reviewed Content Radar/open PR inventory; Auto Publish remains OFF. No new Jaipur write.
- **Other verified candidates:** Clever Ape Academy, CadMate India and Forsk Technologies inventories reviewed; no new write. Groot Software canonical production mapping remains unresolved.

## Validation and release state

| Check | Result |
|---|---|
| Article GitHub read-back | 2,382 words; matches metadata |
| Metadata JSON parse | PASS |
| SVG render | PASS; CairoSVG |
| PNG/WebP decode and dimensions | PASS; both 1200×675 |
| PNG visual inspection | PASS |
| Primary source/date separation | Authored; independent editorial review pending |
| Code examples | Authored from official docs; not executed |
| Video | No verified story-specific video; omitted |
| GitHub branch comparison | 7 commits ahead / 0 behind main; 3 new paths |
| PR state | OPEN / DRAFT; GitHub mergeability field reports false/dirty; do not merge |
| Commit status checks | Empty; no CI pass claimed |
| Independent QA | PENDING |
| Live / merged / deployed | 0 / 0 / 0 |

## Production ledger — this cycle

| Stage | Count |
|---|---:|
| Research lanes | 4 |
| New verified unowned stories selected | 1 |
| Original article drafts | 1 |
| Original SVG graphics committed | 1 |
| Local PNG/WebP derivatives | 2 |
| New verified YouTube embeds | 0 |
| Independent QA-ready | 0 |
| Live / published | 0 |
| Merged / deployed | 0 |

**Next:** independent editorial/technical/responsive QA for Mango PR #238; investigate the reported PR mergeability state; recheck Cloudflare's 17 November default before the date; verify Google A2A GA/Preview status; recheck the live INSPIRE portal and approaching student deadlines. No merge, deploy, publication, application submission or indexing claim.
