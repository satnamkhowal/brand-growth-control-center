# News Factory cycle — 15 November 2026, 06:03 IST

## Run outcome

Four non-overlapping research lanes were rechecked against official sources and current repository ownership. **No new, previously unowned story with a sufficiently fresh primary-source announcement was verified in this cycle.** Existing draft owners were preserved; no duplicate article or new media asset was created.

This is a status-revalidation cycle, not a new production batch. The 05:04 Mango Gemini 4 Hydrogen article and its original SVG remain in Mango PR #253; they are not counted again here.

No article was merged, published, deployed or claimed live.

## 1. Student / developer programmes and opportunities

### Status checked on 15 November 2026

- **Google Student Researcher, 2027:** Google Careers currently shows Apply, **India — Remote eligible**, rolling review and a **4 December 2026** deadline. Minimum qualification: currently enrolled in a Bachelor's, Master's or PhD programme in listed disciplines including Computer Science, Linguistics, Statistics, Biostatistics, Applied Mathematics, Operations Research, Economics or Natural Sciences, plus experience in a computer-science area. The listing does not show a publication date, stipend amount or fixed duration. Existing owner: [Forsk PR #146](https://github.com/satnamkhowal/forsk-coding-school/pull/146). Source: https://www.google.com/about/careers/applications/jobs/results/125423735539671750-student-researcher-2027
- **VSSC BE/BTech/BSc/Diploma academic project work:** the official HRDD portal lists the next project slot as **1 January–31 March 2027** and the last date as **15 November 2026**. This is a downloaded-form/email route, not the online internship intake. The page does not state a closing hour. Its wording also distinguishes the already-closed October–December 2026 slot from the next January–March slot; do not call this an internship. Existing owner: [Forsk PR #172](https://github.com/satnamkhowal/forsk-coding-school/pull/172). Source: https://vsscinternship.vssc.gov.in/HRDD_LOGIN/beforelogincontroller
- **VSSC PG academic project work:** the portal shows an online window through **16 November 2026, 23:59 IST**, for the January–June 2027 slot. Official instructions require Indian citizenship, minimum 60% or CGPA 6.32, and the specified completed semesters for M.E./M.Tech./Integrated M.Tech./M.Sc./Integrated M.Sc./BS-MS candidates. Duration is 120–180 days for M.Sc./Integrated M.Sc./BS-MS and 120–365 days for M.E./M.Tech./integrated engineering degrees. **No stipend, remuneration or financial assistance is provided; VSSC charges no fee.** This is academic project work, not a paid internship. Existing owner: Forsk #172. Sources: https://vsscinternship.vssc.gov.in/HRDD_LOGIN/beforelogincontroller and https://vsscinternship.vssc.gov.in/HRDD_LOGIN/instructionBeforLogin.jsp
- **Sage IT India Scholarship 2026:** sponsor page publication timestamp is **19 October 2026**; submission deadline is **15 November 2026**, winner announcement 30 November. Award: **₹50,000 one-time**. Eligibility: enrolled in a recognised Indian college/university, age 17–30, any major; an individual unpublished 1,000–1,500-word article. **No entry fee.** The page gives no closing hour, so the deadline is today but an exact cutoff/form state is not confirmed. Existing owner: [Forsk PR #184](https://github.com/satnamkhowal/forsk-coding-school/pull/184). Source: https://sageitinc.com/scholarship/india
- **NeGD Technical Internship — Winter 2026:** announcement publication date **12 November 2026**; the current NeGD careers index lists **20 November 2026** and **Delhi-NCR**. The linked technical-internship PDF returned HTTP 403 in this pass; stipend, duration, detailed eligibility and fee are therefore not independently verified. Do not fill these gaps from secondary summaries. Existing owner: [Forsk PR #225](https://github.com/satnamkhowal/forsk-coding-school/pull/225). Sources: https://negd.gov.in/jobs/technical-internship-winter-programme-2026/ and https://negd.gov.in/careers/

No new opportunity article was opened because all five subjects above already have Forsk owners. The DRDO/TBRL amended 2027 notice remains on its existing Forsk PR #236; direct DRDO-hosted PDF verification was still not established, so its secondary-hosted copy must not be treated as fully primary-source verified.

## 2. React / frontend

- Official React blog's latest feature announcement remains **React 19.3**, published **9 September 2026**. The current GitHub release inventory lists patch tags **19.3.1, 19.2.9, 19.1.10 and 19.0.9**, all dated **14 October 2026**. No newer November stable release was found.
- GitHub Advisory Database record **CVE-2026-126187 / GHSA-xqc2-xf4c-x3h3** is Critical (CVSS 9.5); the React project release was published 14 October, while the GitHub advisory database publication/review and last update are 10 November. It affects React Server Components packages in the ranges below 19.0.9, 19.1.10, 19.2.9 and 19.3.1. Upgrade to the matching patched line where those packages are used; non-server React apps and projects without RSC-supporting framework/bundler/plugin are outside the stated impact.
- Existing owners retained: Forsk #145 and Mango #202. No duplicate React article or security advisory draft was created.

Sources: https://react.dev/blog, https://github.com/react/react/releases, https://github.com/advisories/GHSA-xqc2-xf4c-x3h3

## 3. Node.js / backend

- Latest LTS security releases remain **22.23.5**, **24.22.3** and **26.13.1**, all published **11 November 2026**.
- Latest official prerelease is **27.0.0-alpha.0.1.0**, published **12 November 2026**. It includes experimental changes such as subprocess timeout state, X.509 CSR generation and DNS lookup coalescing; it is Alpha, not an LTS/production-stable recommendation.
- The 11 November security bulletin includes high-severity HTTP/2 and TLS fixes. Ubuntu's CVE-2026-123875 record was published 12 November and last updated 13 November; it describes an unauthenticated Node.js HTTP/2 server crash when a client cancels a file response. This is a downstream advisory about the already-published Node security release, not a new Node release.
- Existing Mango Node security owners (#143/#229) and the existing Node 27 Alpha workstream remain in place. No duplicate backend article was opened.

Sources: https://nodejs.org/en/blog, https://nodejs.org/en/blog/vulnerability/november-2026-security-releases, https://nodejs.org/en/blog/release/v26.13.1, https://nodejs.org/en/blog/release/v24.22.3, https://nodejs.org/en/blog/release/v22.23.5, https://nodejs.org/en/blog/release/v27.0.0-alpha.0.1.0, https://ubuntu.com/security/CVE-2026-123875

## 4. AI / cloud / developer news

- The GitHub November changelog currently shows its newest entries dated **13 November 2026**; no 14 or 15 November entry was found in that archive. The 13 November topics include Gemini 4 Hydrogen in Copilot, GHES support in the Copilot app and the public-preview AI Scan REST API.
- These topics already have owners: Mango PR #253 (Gemini 4 Hydrogen in Copilot), Mango PR #230 (GHES support) and Jaipur Engineers issue #52 (AI Scan REST API). The separate Gemini 4 Hydrogen Agent Platform integration has Groot issue #700. Do not combine these distinct surfaces or create near-identical cross-brand copies.
- Google Cloud Gemini release notes' newest visible entry remains 9 October 2026; no fresh November 14–15 announcement was verified there.
- The Copilot 14 December retirement notice is separate from GitHub's 15 October notice for models retiring on 16 November. Forsk PR #185's original 16 November date/model list remains correct.

Sources: https://github.blog/changelog/month/11-2026/, https://docs.cloud.google.com/gemini/docs/release-notes, https://github.blog/changelog/2026-11-13-upcoming-deprecation-of-selected-github-copilot-models-in-december/, https://github.blog/changelog/2026-10-15-upcoming-deprecation-of-selected-github-copilot-models-in-mid-november/

## 5. Repository and queue audit

- **Central coordination:** existing News Factory PR #19 and branch `ops/news-factory-cycle-20261109-2209` reviewed. Before this audit commit, branch compare was **224 ahead / 5 behind main**, diverged; PR remained OPEN/DRAFT and GitHub reported `mergeable=false`. This audit is an append-only file on that existing branch. No rebase, force-push, merge or central-main write.
- **Mango Engineers:** read `AGENTS.md`, `docs/agent-start-here.md`, task board, work log and integration queue; reviewed current open PRs/issues. Existing [PR #253](https://github.com/satnamkhowal/mangoengineers.com/pull/253) is now **4 ahead / 0 behind main**, OPEN/DRAFT and GitHub currently reports `mergeable=true`. Combined status returned no status checks. The PHP Architecture Check workflow failed with `steps: null`; its log download returned Azure `BlobNotFound` 404, so zero hosted assertions ran. This is not a CI pass or a confirmed PHP/code failure. No article files or graphics were changed in this cycle.
- **Forsk Coding School:** read current `README.txt` and `docs/ai-ops/MASTER_TASK_BOARD.md`; reviewed open PR/issue and News Factory drafts/media inventories. Existing opportunity, React, Node-adjacent and Copilot owners remain. No new Forsk task was claimed; no shared task-board or session-handoff file was modified.
- **Groot Academy:** canonical repository is `satnamkhowal/grootacademy.com`. Read controller issue #401 and current PR #750/#755. The canonical queue remains 29 IDs; the current controller snapshot records 23 complete drafts, 23 visuals and 23 PHP candidates, with 0 independent approvals, 0 published and 0 live verified. New IDs remain HOLD pending owner alignment, a named canonical queue owner and independent release approver. PR #755 is a QA-only Draft; exact-head hosted Actions previously failed before steps with Azure BlobNotFound, so no hosted assertions or independent approval are claimed.
- **Jaipur Engineers:** canonical repository is `satnamkhowal/jaipurengineers.com` per central mapping PR #15. Read `README-INSTALL.md`, `docs/content-radar.md` and `data/content-radar/queue.json`; Auto Publish is OFF. Existing issue #52 owns the GitHub AI Scan REST API guide. No duplicate Jaipur article was opened.
- **Other listed brands:** no source write was made to Clever Ape Academy, Groot Software or Forsk Technologies; current canonical News Factory ownership/instructions were not cleared for a new story in this cycle. CadMate's existing AI/cloud owner remains on the prior central ledger; no duplicate task was created.

## 6. Production ledger — this run only

| Stage | New count |
|---|---:|
| Research lanes checked | 4 |
| New verified, unowned stories | 0 |
| Original English article drafts | 0 |
| Existing articles updated | 0 |
| New original graphics | 0 |
| Verified YouTube links / embeds | 0 / 0 |
| Independent QA-ready | 0 |
| Live / published | 0 |
| Merged / deployed | 0 |

No story-specific YouTube video with a verified ID, channel, upload date and embed suitability was established; no iframe was created and no video was downloaded. No new graphic was required because no new article was opened. The original SVG and local PNG/WebP derivatives from Mango PR #253 belong to the prior 05:04 cycle and are not counted again.

## Next action

1. Recheck the VSSC UG and Sage IT deadline-day submission routes only if a new status change is published; VSSC PG closes 16 November at 23:59 IST.
2. Keep Google Student Researcher 2027 on the existing Forsk owner until its 4 December deadline.
3. Diagnose Mango PR #253's Actions/Azure log failure and complete independent editorial, billing, security and responsive QA before any release decision.
4. Keep Groot's new content IDs on HOLD until the canonical queue owner and independent release approver are named; continue the existing QA recovery stack.
5. Recheck primary sources for a genuinely new 14–15 November announcement before opening the next article task.

No source-repository code, public routes, sitemap, schema, redirects, deployment settings or production assets were changed.
