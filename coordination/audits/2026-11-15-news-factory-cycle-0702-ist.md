# News Factory cycle — 15 November 2026, 07:02 IST

## Run outcome

Four non-overlapping research lanes were rechecked against official primary sources and the current brand ownership queues. **No new, previously unowned story cleared deduplication.** This is a source/status revalidation cycle; no new article, graphic or video embed was produced. Existing draft owners remain unchanged.

No merge, deployment, publication or live/indexing claim is made.

## 1. Student and developer opportunities

- **Google Student Researcher, 2027:** the live Google Careers listing still shows **India — Remote eligible**, rolling review and a **4 December 2026** application deadline. It accepts currently enrolled Bachelor's, Master's or PhD students in the listed disciplines with experience in a computer-science area. The page does not state a publication date, stipend or fixed engagement duration. Existing owner: [Forsk PR #146](https://github.com/satnamkhowal/forsk-coding-school/pull/146). Source: https://www.google.com/about/careers/applications/jobs/results/125423735539671750-student-researcher
- **VSSC UG academic project work:** the HRDD portal still lists **15 November 2026** as the receipt deadline for BE/BTech/BSc/Diploma applicants for the **1 January–31 March 2027** project slot. This is a prescribed downloaded-form/email route; the portal publishes no closing hour. Existing owner: [Forsk PR #172](https://github.com/satnamkhowal/forsk-coding-school/pull/172).
- **VSSC PG academic project work:** the online window remains **15 October 2026, 10:00 AM to 16 November 2026, 11:59 PM IST** for the **1 January–30 June 2027** slot. Official instructions require Indian citizenship and at least 60% / CGPA 6.32, with course-specific semester conditions. The instructions explicitly say **no stipend/remuneration/financial assistance and no VSSC fee**. Both routes are academic project work, not paid internships. Sources: https://vsscinternship.vssc.gov.in/HRDD_LOGIN/beforelogincontroller and https://vsscinternship.vssc.gov.in/HRDD_LOGIN/instructionBeforLogin.jsp
- **Sage IT India Scholarship 2026:** sponsor page publication timestamp **19 October 2026**; submission deadline **15 November 2026**; winner announcement **30 November 2026**. Award: **₹50,000 one-time**. Eligibility: enrolled in a recognised Indian college/university, age 17–30, all majors; individual unpublished 1,000–1,500-word article; no entry fee. The sponsor publishes no closing hour/timezone. Existing owner: [Forsk PR #184](https://github.com/satnamkhowal/forsk-coding-school/pull/184). Source: https://sageitinc.com/scholarship/india
- **NeGD Technical Internship — Winter 2026:** announcement page published **12 November 2026**; current careers index lists **20 November 2026**, Delhi-NCR. The five-page official MeitY PDF confirms 50 positions (40 six-month regular-term and 10 two-month short-term), 75% in the qualifying engineering degree, 2025/2026 graduates and 2027 final-year students, institution forwarding, daily offline attendance and a conditional **₹20,000/month** token stipend after mentor certification every 30 days. Fee is not stated. The PDF has one inconsistent “technical summer internship” phrase despite the Winter title. Existing owner: [Forsk PR #225](https://github.com/satnamkhowal/forsk-coding-school/pull/225). Sources: https://negd.gov.in/jobs/technical-internship-winter-programme-2026/ and https://www.meity.gov.in/static/uploads/2026/11/032b92c51d45d44365455c98ea37b0eb.pdf
- **NeGD 18 November technical vacancies:** the current careers index lists Frontend Developer, Junior Backend/Mobile Developer, Platform & Security Engineer, DevSecOps Engineer, AppSec Specialist, QA Tester and Full Stack Developer, among other roles, with an **18 November 2026** deadline. The linked role PDFs returned **403 Forbidden** in this check; detailed eligibility, compensation and fees are therefore unverified. No article was created from titles alone. Source: https://negd.gov.in/hi/careers/page/2/

No new opportunity article was opened because the verified programme topics above already have Forsk owners or lack accessible role-level evidence.

## 2. React / frontend

- Official React blog's latest feature announcement remains **React 19.3**, published **9 September 2026**.
- Current release inventory still shows **19.3.1, 19.2.9, 19.1.10 and 19.0.9**, all dated **14 October 2026**; no newer November stable release was found.
- Critical React Server Components advisory **CVE-2026-126187 / GHSA-xqc2-xf4c-x3h3** is rated **CVSS 9.5**; fixed package versions are 19.0.9, 19.1.10, 19.2.9 and 19.3.1. Existing owners: Forsk #145 and Mango #202.

Sources: https://react.dev/blog ; https://github.com/facebook/react/releases ; https://github.com/react/react/security/advisories/GHSA-xqc2-xf4c-x3h3

## 3. Node.js / backend

- The latest official security bulletin remains **11 November 2026**.
- Patched releases: **Node 22.23.5, 24.22.3 and 26.13.1**.
- The bulletin lists **16 CVEs: 7 High, 6 Medium and 3 Low**. Applicability differs by CVE and release line; do not imply every CVE affects every line.
- **27.0.0-alpha.0.1.0** remains Alpha, not LTS.

Existing Mango security/Alpha owners #143 and #229 retained; no duplicate backend article.

Source: https://nodejs.org/en/blog/vulnerability/november-2026-security-releases

## 4. AI, cloud and developer news

Latest official items checked:
- **13 November:** Gemini 4 Hydrogen in GitHub Copilot; GitHub Enterprise Server support in the Copilot app; AI Scan repository management through the REST API.
- **12 November:** GitHub Secret Scanning adds the Cloudflare `cloudflare_access_service_token` detector; GitHub-hosted Actions ends ARM32 Windows/Linux job execution on **8 December 2026**.
- **13 November:** Google Cloud Architecture Center updated its guide to agentic-AI design patterns; this is a documentation update, not a new ADK release or pricing announcement.

All have existing owners: Mango #253 (Gemini 4 Hydrogen), Mango #230 (GHES support), Jaipur #52 (AI Scan API), Forsk #217 (Cloudflare detector), Forsk #204 (ARM32 retirement) and Mango #251 (agentic-AI design patterns). No new cross-brand syndication was created.

Sources: https://github.blog/changelog/month/11-2026/ ; https://github.blog/changelog/2026-11-12-secret-scanning-adds-a-detector-for-cloudflare/ ; https://github.blog/changelog/2026-11-12-actions-for-arm32-linux-windows-retirement/ ; https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system

## 5. Repository and coordination audit

- **Central News Factory:** existing PR #19 / branch `ops/news-factory-cycle-20261109-2209` reviewed. Current compare is **225 ahead / 5 behind main**, diverged. The checkpoint is added as a new append-only audit file on this existing branch; no rebase, force-push, merge or central-main write.
- **Mango Engineers:** read README, AGENTS, agent-start instructions, task board, work log and integration queue. Existing [PR #253](https://github.com/satnamkhowal/mangoengineers.com/pull/253) remains OPEN/DRAFT, **4 ahead / 0 behind**, currently mergeable. No combined status checks were returned. The last reported PHP Architecture Check failed before executable steps (null step list; Azure BlobNotFound 404); no hosted assertion pass is claimed.
- **Forsk Coding School:** read README.txt, master task board, session handoff and worker registry; reviewed the current opportunity and developer-news owners. No branch or shared board/handoff/registry file was changed.
- **Groot Academy:** canonical repository is `satnamkhowal/grootacademy.com`. The latest [issue #401 checkpoint](https://github.com/satnamkhowal/grootacademy.com/issues/401#issuecomment-6887016521) at 06:25 IST reports 77 registry slugs, 50 blog-sitemap URLs (index + 49 article URLs), 68 page-sitemap URLs and a separate 5,000-URL study-guide shard. These are source counts, not live-published counts; live remains UNVERIFIED. The 29-ID controller queue remains gated; no new content ID was opened. The 06:25 owner inventory reports 244 open PRs (8 non-draft + 236 draft) and zero independent approvals among the eight non-draft PRs.
- **Jaipur Engineers:** canonical repository metadata confirmed; no new article was opened because AI Scan REST API already has owner #52 and the current News Factory lane remains read-only.
- **Other listed brands:** current repository mappings were discovered for Clever Ape Academy, CadMate India and Forsk Technologies. Groot Software still has two plausible repository candidates; no source write was made while that mapping/ownership remains unresolved.

## 6. Production ledger — this run only

| Stage | New count |
|---|---:|
| Research lanes checked | 4 |
| New verified, unowned stories | 0 |
| Original English article drafts | 0 |
| Existing articles materially updated | 0 |
| New original graphics | 0 |
| Verified YouTube embeds | 0 |
| Independent QA-ready | 0 |
| Live / published | 0 |
| Merged / deployed | 0 |

No story-specific video with a verified ID, channel, upload date and permitted embedding was established; no iframe or video download was made. No new graphic was needed because no new article cleared deduplication. Previous-cycle Mango graphics are not recounted.

## Next action

1. Keep the VSSC UG and Sage IT deadline-day warnings on their existing Forsk drafts; neither source publishes an exact closing hour.
2. Recheck VSSC PG before its 16 November, 23:59 IST cutoff.
3. Keep NeGD 18 November role listings on hold until the official job-description PDFs can be read.
4. Continue the existing Mango #253 QA/Actions investigation and preserve Groot's queue/release gates.
5. Open the next article only when a fresh primary-source story is both sufficiently verified and unowned.

No brand source route, sitemap, schema, redirect, production asset, merge, deployment or live publication was changed.