# News Factory cycle — 15 November 2026, 05:04 IST

## Run outcome

Four non-overlapping research lanes were checked against official primary sources and current brand repository ownership. One newly verified, previously unowned developer story passed deduplication: **Gemini 4 Hydrogen in GitHub Copilot** (GitHub Changelog, 13 November 2026). One original Mango Engineers article, source/pricing/provenance metadata and one original SVG infographic were committed to an isolated draft branch and opened as a draft PR.

No article was merged, published or deployed. This continues the existing News Factory coordination PR #19 and its append-only `coordination/audits/` directory.

## 1. Student / developer programmes and opportunities

### Active or deadline-day items checked 15 November

- **Google Student Researcher, 2027:** Google Careers currently shows Apply, India — Remote eligible, rolling review, and a **4 December 2026** application deadline. Minimum degree levels: Bachelor's, Master's or PhD in listed fields including Computer Science, Linguistics, Statistics, Applied Mathematics, Economics and Natural Sciences; relevant computer-science experience is required. Google says the candidate must remain in one of the listed countries for the engagement. No fixed stipend or project duration is stated on the listing. Existing owner: [Forsk PR #146](https://github.com/satnamkhowal/forsk-coding-school/pull/146). Source: https://www.google.com/about/careers/applications/jobs/results/125423735539671750-student-researcher
- **Google Software Engineering PhD Intern, Summer 2027:** Google Careers shows Apply. India locations include Bengaluru, Hyderabad and Pune. Minimum requirements include pursuing a PhD in software development or a related technical field, programming experience, Unix/Linux, data structures, algorithms and software design. Google describes a **12+ week paid internship**; the listing does not disclose a stipend amount or application deadline. Existing owner: [Forsk PR #160](https://github.com/satnamkhowal/forsk-coding-school/pull/160). Source: https://www.google.com/about/careers/applications/jobs/results/109976286780105414-software-engineering-phd-intern-summer-2027
- **VSSC UG Academic Project Work:** current HRDD portal shows the downloaded-form route for BE/BTech/BSc/Diploma project work for the 1 Jan–31 Mar 2027 slot, with **15 November 2026** as the last date. This is academic project work, not the VSSC internship intake. Existing owner: [Forsk PR #172](https://github.com/satnamkhowal/forsk-coding-school/pull/172). Source: https://vsscinternship.vssc.gov.in/HRDD_LOGIN/beforelogincontroller
- **VSSC PG Academic Project Work:** online window for M.E/M.Tech/Integrated M.Tech/M.Sc/BS-MS applicants runs through **16 November 2026, 23:59 IST**. Official instructions require Indian citizenship, minimum 60% or CGPA 6.32, specified completed semesters, and relevant listed courses. Project duration is 120–180 days for M.Sc/Integrated M.Sc/BS-MS and 120–365 days for M.E/M.Tech/Integrated M.Tech. **No stipend, remuneration or financial assistance is provided; no VSSC fee is charged.** Work is limited to unclassified areas and selection is capacity-dependent. This is project work, not an internship. Existing owner: Forsk #172. Sources: https://vsscinternship.vssc.gov.in/HRDD_LOGIN/beforelogincontroller and https://vsscinternship.vssc.gov.in/HRDD_LOGIN/instructionBeforLogin.jsp
- **Sage IT India Scholarship 2026:** sponsor page dated **19 October 2026** still lists a **15 November 2026** submission deadline. Award: **₹50,000 one-time**, paid directly to the winner's college/university. Eligibility: enrolled in a recognised Indian college/university, age 17–30, any major, individual unpublished 1,000–1,500-word article, no entry fee. No closing hour is published. Existing owner: [Forsk PR #184](https://github.com/satnamkhowal/forsk-coding-school/pull/184). Source: https://sageitinc.com/scholarship/india
- **NeGD Technical Internship — Winter 2026:** official posting dated **12 November 2026**; NeGD careers index lists **20 November 2026** and Delhi-NCR. The linked official PDF returned HTTP 403 in this pass, so detailed eligibility, stipend, duration and any fee are not independently confirmed here. Do not infer those details from the listing. Existing owner: [Forsk PR #225](https://github.com/satnamkhowal/forsk-coding-school/pull/225). Non-technical counterpart already has Forsk PR #180. Sources: https://negd.gov.in/jobs/technical-internship-winter-programme-2026/ and https://negd.gov.in/careers/
- **NSP AY 2026–27:** current scheme listing shows NMMSS student applications through **15 November 2026**; AICTE Pragati, Saksham, Swanath and UGC National Scholarship for PG Studies through **30 November 2026**. The NSP page footer says last updated June 2026, so check the individual live scheme and state/institute rules before telling students a form is open. **PM-USP CSSS explicitly says “NOT YET OPENED”** even though the listing shows a 30 November date; do not describe it as open. Existing Forsk scholarship owners retained. Source: https://scholarships.gov.in/fresh1819/All-Scholarships

No new unowned opportunity article was created: the current Google, VSSC, NeGD, Sage IT and NSP topics already have active Forsk owners.

## 2. React / frontend

- Official React release inventory still lists React **19.3.1, 19.2.9, 19.1.10 and 19.0.9**, all dated **14 October 2026**. React 19.3.0 feature release is dated 9 September. No new November stable React release was found.
- GitHub Advisory Database lists the React Server Components unauthenticated RCE as Critical, published 14 October and updated 10 November; affected ranges are below patched 19.0.9, 19.1.10, 19.2.9 and 19.3.1 for the listed RSC packages. Applicability depends on use of the affected server-component packages.
- Existing owners retained: Forsk #145 and Mango #202.
- Sources: https://github.com/react/react/releases and https://github.com/advisories/GHSA-xqc2-xf4c-x3h3

## 3. Node.js / backend

- Official Node.js security release: **11 November 2026**; patched release lines: **22.23.5 LTS, 24.22.3 LTS and 26.13.1 LTS**.
- Bulletin lists 16 CVEs: 7 High, 6 Medium and 3 Low. High-impact issues include unauthenticated HTTP/2 server termination, HTTPS heap-memory disclosure, TLS authentication-policy bypass and HTTP/2 memory/file-descriptor leaks.
- Latest official Alpha inventory: **Node.js 27.0.0-alpha.0.1.0**, published 12 November. It is Alpha, not LTS or a production-stable recommendation.
- Existing owners retained: Mango #143 / #229 and the existing Node 27 alpha branch. No duplicate security article was opened.
- Sources: https://nodejs.org/en/blog/vulnerability/november-2026-security-releases and https://nodejs.org/en/blog/release

## 4. AI / cloud / developer news

### New verified, previously unowned story — Gemini 4 Hydrogen in GitHub Copilot

- **Official publication date:** 13 November 2026.
- **Separate event date:** none stated; this is a Copilot model-availability announcement.
- GitHub describes Gemini 4 Hydrogen as a fast, efficient model for agentic coding, tool use and multi-step workflows, with improved instruction following over Gemini 3.8 Flash. No benchmark guarantee is published in the announcement.
- Plans named: Copilot Pro, Pro+, Max, Business and Enterprise. Rollout is gradual.
- Clients named: VS Code, Visual Studio, Copilot CLI, coding agent, Copilot app, github.com, GitHub Mobile, JetBrains IDEs, Xcode, Eclipse and Copilot SDK.
- Business/Enterprise administrators can control model access through model policies.
- Copilot pricing documentation checked 15 November: **US$1.50 / 1M input tokens, US$0.075 / 1M cached input tokens, US$7.50 / 1M output tokens**; **1 AI Credit = US$0.01**. Included plan allowances differ. These are USD usage rates, not monthly subscription prices or guaranteed INR charges.
- GitHub's separate 13 November deprecation notice schedules Gemini 3.8 Flash retirement on **14 December 2026**, suggesting Gemini 4 Hydrogen as the replacement. Free/Student direct model-picker access is not promised by the launch notice; current Docs say those users access models through Auto model selection only.
- No India-specific country table, India-only price, stipend or scholarship is published. The article avoids a blanket India guarantee.
- Primary sources:
  - https://github.blog/changelog/2026-11-13-gemini-4-hydrogen-in-github-copilot/
  - https://github.blog/changelog/2026-11-13-upcoming-deprecation-of-selected-github-copilot-models-in-december/
  - https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing
  - https://docs.github.com/en/copilot/reference/ai-models/supported-models
  - https://docs.github.com/en/copilot/reference/ai-models/model-comparison

### Mango Engineers draft delivery

- Task: NF-MANGO-GH-GEMINI4-HYDROGEN-20261115-0504; [Issue #252](https://github.com/satnamkhowal/mangoengineers.com/issues/252).
- [OPEN / DRAFT PR #253](https://github.com/satnamkhowal/mangoengineers.com/pull/253).
- Original English article: **2,347 words**; focused on fast agentic coding and a review-first Node.js/React learner workflow.
- SEO/source/pricing/provenance JSON sidecar.
- Original **1200×675 SVG** workflow graphic committed; local PNG and optimized WebP derivatives rendered and visually inspected.
- No third-party logo, screenshot, photograph or downloaded media used. Rights basis, attribution, alt text, dimensions, local paths and SHA-256 hashes recorded.
- Local package: `/mnt/data/mango-gemini-hydrogen/mango-gemini-4-hydrogen-graphics.zip`.
- GitHub read-back: all 3 files present; metadata JSON parsed; article word count 2,347; SVG title/description/dimensions checked.
- Branch: `news-factory/gemini-4-hydrogen-copilot-fast-agentic-workflows-20261115-0504`; **4 commits ahead / 0 behind main**, exactly 3 files.
- GitHub reports PR mergeable=false. No workflow run or combined status was returned; CI is unverified, not passed.
- Independent editorial, plan/pricing, security and responsive QA pending.
- No story-specific official/reputable YouTube video with verified ID, channel, date and embedding permission was established; no iframe or video download.

### Existing AI/cloud owners preserved

- Google Cloud agentic HPC at SC26: CadMate PR #5 (previous cycle).
- Google Cloud ADK agent workflows: Mango PR #251.
- AWS Emulator local testing: Mango PR #250.
- Gemini 4 Carbon in Copilot: Mango PR #220 and Forsk PR #168.
- GitHub Copilot app GHES support: Mango PR #230.
- GitHub AI Scan API and related Copilot features remain with their existing brand owners.
- No duplicate story was opened for these topics.

## 5. Copilot retirement-date correction — Forsk PR #185

A previous comment #6884026363 incorrectly told the Forsk PR #185 owner to change its 16 November date. The official source review confirms that was wrong:

- GitHub's **15 October** notice schedules Claude Opus 4.8, Claude Opus 5 and GPT-5.6 Terra for **16 November 2026**.
- GitHub's separate **13 November** notice schedules a different model set, including Gemini 3.8 Flash, for **14 December 2026**.
- The incorrect comment #6884026363 has been edited to withdraw the wrong instruction. **Keep Forsk PR #185's original 16 November title and model list.** The separate December addendum comments #6865739827 and #6869517067 remain valid.
- Sources: https://github.blog/changelog/2026-10-15-upcoming-deprecation-of-selected-github-copilot-models-in-mid-november/ and https://github.blog/changelog/2026-11-13-upcoming-deprecation-of-selected-github-copilot-models-in-december/

## 6. Repository and coordination audit

- Central Brand Growth Control Center and existing News Factory branch/PR #19 reviewed; current 04:11 checkpoint was corrected in place for the Copilot retirement-date distinction, and this 05:04 run is appended as a new audit file.
- Mango README, AGENTS.md, agent-start guide, task board, work log and integration queue read. Current open PRs and task ownership checked; no Gemini 4 Hydrogen issue/PR existed before issue #252.
- Forsk current open PR ownership checked: Google Student Researcher #146, Google PhD internships #160, VSSC #172, Sage IT #184, Copilot #185, NeGD #225 and other scholarship/security tasks retained.
- Groot Academy repository alias `satnamkhowal/gta` resolves to canonical `satnamkhowal/grootacademy.com`; current open PRs and controller [issue #401](https://github.com/satnamkhowal/grootacademy.com/issues/401) reviewed. #401 defines a **1,000,000-article aspirational ceiling** with evidence-gated milestones; the user's **100,000-article working target** remains distinct and does not override quality gates. Current graphics/QA owners preserved; no new Groot content ID or article was opened.
- Jaipur Engineers repository/PR inventory reviewed read-only; its current News Factory canonical mapping and instruction set were not sufficiently clear for a safe content write. No Jaipur write was made.
- CadMate India PR #5 (Google Cloud HPC) remains the current AI/cloud owner; no duplicate was opened.
- Clever Ape Academy, Forsk Technologies and Groot Software were checked for accessible repository/PR ownership; no new story was assigned to them in this cycle.
- No branch was merged, rebased, force-pushed or deployed.

Central News Factory branch: `ops/news-factory-cycle-20261109-2209`. Recheck compare after this audit commit; previous checkpoint was **219 ahead / 5 behind main**, diverged. Do not merge or rebase as part of this run.

## 7. Production ledger — this run only

| Stage | New count |
|---|---:|
| Research lanes | 4 |
| New verified unowned stories | 1 |
| Original English article drafts | 1 |
| Existing articles updated | 0 |
| Original SVG graphics committed | 1 |
| Local PNG/WebP derivatives | 2 |
| Verified YouTube links / embeds | 0 / 0 |
| Independent QA-ready | 0 |
| Live / published | 0 |
| Merged / deployed | 0 |

**Next action:** independent QA of Mango PR #253; investigate its mergeable=false state and missing CI result; recheck the 15–16 November VSSC deadlines and current NSP/NeGD/Google listings; preserve the corrected distinction between the two Copilot retirement notices.