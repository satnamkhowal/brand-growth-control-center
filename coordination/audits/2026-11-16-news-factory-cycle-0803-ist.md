# News Factory research and draft cycle — 16 November 2026, 08:03 IST

## Outcome

Four non-overlapping lanes were checked against current primary sources and the existing brand PR/issue inventory. One fresh cloud release was verified: **Google SecOps Publisher Agent 2.7.2**, listed as available in Google Cloud release notes dated **15 November 2026**. The Mango Engineers local draft from the previous production pass was revalidated and updated with its original graphic and a clearly labelled background-video fallback link. The existing IICT Winter Internship 2026 Forsk guide was also revalidated and updated with its original graphic and live-form caveat.

**No new article draft or brand GitHub PR was created in this run.** Other fresh topics already have owners, and the two local drafts are waiting for a safe repository handoff. No article was merged, deployed or published.

## 1. Official programmes and opportunities

- **Google Student Researcher 2027 — Forsk PR #146.** Google Careers still displays Apply, India / Remote eligible, rolling review and a **4 December 2026** completion deadline. Minimum qualification: current Bachelor's, Master's or PhD enrolment in a listed discipline plus experience in a relevant computer-science research area. Stipend, fixed duration and application fee are not stated. Existing owner retained; not described as a new opening.
- **IICT Winter Internship 2026 — local Forsk draft.** The official circular is dated **22 September 2026**; registration is listed through **30 November 2026**; first training day is **10 December 2026**. It is a 45-day online, fee-based and non-stipendiary programme: 15 days of coursework plus 30 days of project work, stated capacity 1,070, training fee **₹970**. The official registration form page is accessible and shows applicant fields plus a Proceed to Pay control, but form submission, payment acceptance and remaining seats were not tested. The official page warns users to register only through IICT's own website. This is not a paid job or scholarship.
- **NeGD Winter 2026 technical and non-technical internships — Forsk PRs #225 and #180.** The current careers page still lists **20 November 2026**. The two role tracks remain separately owned. Form response/acceptance was not tested; no duplicate article created.
- **VSSC academic project work — Forsk PR #172.** The live HRDD portal still has a status contradiction: the PG current project slot is labelled closed, while the same page prints an online window through **16 November 2026, 11:59 PM**. The page does not establish that the form is accepting submissions. Existing owner comment at 07:05 IST already records this uncertainty; no duplicate comment or “open” claim added. The UG 15 November date has passed; INT 08 is closed and INT 09 is a separate 2027 internship intake.

## 2. React / frontend

- React 19.3 remains the latest feature release, dated **9 September 2026**.
- Latest official patch tags remain **19.3.1, 19.2.9, 19.1.10 and 19.0.9**, all dated **14 October 2026**.
- The 14 October React Server Components advisories remain the latest verified security items: Critical RSC remote-code-execution and High Server Functions denial-of-service advisories. No newer stable React release or advisory was found.
- Existing Forsk PR #145 remains the sole owner; its CVE wording correction/independent QA remains pending. No duplicate article created.

## 3. Node.js / backend

- The **11 November 2026** security release remains current for **22.23.5, 24.22.3 and 26.13.1**. The official bulletin lists 16 vulnerability entries (7 High, 6 Medium, 3 Low); highest severity is High.
- **Node.js 27.0.0-alpha.0.1.0**, dated **12 November**, remains Alpha and is not a production/LTS replacement.
- Existing owners retained: Mango PR #143 (November security guide) and #229 (Node 27 Alpha); Groot PR #650. No duplicate article created.

## 4. AI / cloud / developer news

- **Google SecOps Publisher Agent 2.7.2 — fresh, verified, locally drafted.** The 15 November Google Cloud release note lists alert lazy loading for remote actions, a fix for installing integrations with interdependent dependency files, a remote-agent deletion directory-permission fix, and Publisher stability/security updates. The note does not enumerate CVEs or state a price change. Google architecture docs confirm the Publisher/Remote Agent task flow and TLS on TCP 443; onboarding requires an active Standard, Enterprise or Enterprise Plus package registration and a signed contract. The local Mango draft is revalidated; no GitHub owner/PR was found for this exact release. A new Mango PR was held because current PRs #143, #282 and #283 edit shared task-board/work-log files and AGENTS requires a task claim before editing.
- **GitHub AI Scan for repositories REST API** — published **13 November**, public preview. Existing Groot PR #737 and Jaipur issue #52 already own the same story; no duplicate.
- **GitHub Copilot model deprecations effective 14 December** — published **13 November**. Existing Forsk PR #185 owns the update; no duplicate.
- Google Cloud Quotas, Gemini Enterprise/Antigravity and Apigee updates are already represented in active Mango/Groot/Jaipur work. No duplicate article opened.

## Repository and concurrency review

- **Central:** reused existing News Factory PR #19 and branch `ops/news-factory-cycle-20261109-2209`. The branch compares **235 commits ahead / 5 behind main (diverged)**. This checkpoint is append-only; no rebase, force-push or merge.
- **Mango Engineers:** read `AGENTS.md`, `docs/agent-start-here.md`, task board, work log and integration queue. Rules require a task claim before editing. Open PRs #143, #282 and #283 touch shared task-board/work-log paths; no brand commit or shared-file write was made.
- **Forsk Coding School:** read `README.txt`, master task board, worker registry and session handoff. Root `README.md` / `AGENTS.md` were absent at checked paths; the worker registry reserves master board/session-handoff aggregation to the controller. Existing PRs #145, #146, #172, #180, #185, #225, #241 and #250 remain owners. No new branch or PR.
- **Groot Academy:** canonical accessible repository is `satnamkhowal/grootacademy.com`; AI Scan is already owned by PR #737, and other current AI/cloud/Node.js topics have active owners. No new write.
- **Jaipur Engineers:** `docs/content-radar.md` keeps Auto Publish OFF; AI Scan is already owned by issue #52 and other current stories have active owners. No new write.

## Local draft and media handoff

- Mango: existing Google SecOps Publisher Agent 2.7.2 draft revalidated; original infographic embedded. The official Google Cloud YouTube candidate is **“Introducing Google Security Operations”**, video ID `VT4xpfPaD1w`, verified Google Cloud channel, published **20 June 2024**. It is general product background, not a 2.7.2 walkthrough. Embed permission/playback could not be verified; the article includes only a labelled fallback link, no iframe.
- Forsk: existing IICT Winter Internship guide revalidated; original two-phase infographic embedded. No suitable programme-specific original video with verified ID/date/embed permission was found.
- Two original self-authored SVG graphics and their 1200×675 PNG/WebP derivatives were retained and validated. No third-party artwork or video was downloaded/reuploaded.
- Local package contains both Markdown drafts, metadata, SVG/PNG/WebP assets and this cycle report; these files have not been committed to brand repositories.

## Checks and status ledger

| Stage | This run |
|---|---:|
| Research lanes checked | 4 |
| Fresh verified stories | 1 (Google SecOps Publisher Agent 2.7.2) |
| New article drafts created | 0 |
| Existing local drafts revalidated/updated | 2 |
| New graphics created | 0 |
| Existing original graphics validated | 2 SVG + 2 PNG + 2 WebP |
| Verified YouTube embeds | 0 |
| New brand GitHub PRs / commits | 0 |
| Independent QA-ready | 0 |
| Live / merged / deployed | 0 |

Metadata JSON parse, SVG XML parse, PNG/WebP decode and 1200×675 dimensions passed. Both images were visually inspected. Independent editorial, technical and eligibility QA remain pending. No browser embed test, application submission, CI pass, merge, deployment or publication is claimed.

## Next action

After Mango PRs #282/#283 release the shared task-board/work-log paths, claim the Google SecOps 2.7.2 draft as a distinct News Factory task and open an isolated draft PR. Independently QA the two local drafts before any merge or publication decision.


## Additional opportunity status correction — 16 November 2026

**GENESIS EIR Cohort 3 is closed, not a current opening.** The MeitY Startup Hub homepage still carries a stale “call live” description, but the cohort was launched on 4 August 2026 and the published application deadline was **3 September 2026**. A participating GENESIS incubator (AIC ISB) lists financial assistance of up to **₹10 lakh**, subject to approval and tranche conditions, and the same 3 September closing date. The official MSH application route is on the government domain but renders a JavaScript shell in this check, so its current form state could not be read. Do not publish it as open or newly announced; wait for a new official cohort call.

Sources:
- MeitY Startup Hub GENESIS scheme: https://msh.meity.gov.in/schemes/genesis
- MeitY Startup Hub homepage / Cohort 3 announcement: https://msh.meity.gov.in/
- AIC ISB participating incubator page (deadline and conditional up-to-₹10 lakh support): https://aicisb.org/meity-genesis-eir/
- Official MSH application route (JS-rendered; form state not readable): https://mshportal.meity.gov.in/ext/form/23966/1/apply


## NeGD stipend detail — 16 November 2026

The two Winter 2026 internships remain separate:
- Technical: the MeitY-hosted official PDF states **₹20,000/month**, conditional on satisfactory performance and mentor certification after each 30-day period; regular-term duration is six months and short-term duration two months. The application deadline is **20 November 2026**.
- Non-technical: the MeitY-hosted official PDF states **₹15,000/month**, but remuneration is paid only after completion of the full tenure and acceptance of the submitted report. The application deadline is **20 November 2026**.

Publication-date distinction: the individual NeGD job pages display 12 November 2026, while the MeitY vacancy index lists 11 November 2026. Existing Forsk PRs #225 and #180 remain the respective owners; the linked forms were not submitted and live response acceptance was not tested.

Official sources:
- Technical listing: https://negd.gov.in/jobs/technical-internship-winter-programme-2026/
- Non-technical listing: https://negd.gov.in/jobs/non-technical-internship-winter-programme-2026/
- MeitY vacancy index: https://www.meity.gov.in/offerings/vacancies
- Technical notice PDF: https://www.meity.gov.in/static/uploads/2026/11/032b92c51d45d44365455c98ea37b0eb.pdf
- Non-technical notice PDF: https://www.meity.gov.in/static/uploads/2026/11/53935d4075991e5c3f211f053b583270.pdf


## 2026-11-16 09:03 IST — News Factory cycle 11

### Four-lane research result

**1) Official programmes, internships, scholarships and grants**
- Google Careers still lists **Student Researcher, 2027** as India / Remote eligible, with a **4 December 2026** deadline and rolling review. Minimum qualification remains current enrolment in a Bachelor's, Master's or PhD programme in the listed disciplines plus experience in a relevant computer-science research area. Existing owner: Forsk PR #146.
- NeGD still lists the separate Technical and Non-Technical Winter 2026 internships in Delhi-NCR with **20 November 2026** deadlines. Existing owners: Forsk PR #225 and #180. Official pages were rechecked; no form submission or response-acceptance test was performed.
- IIIT Kottayam Network Science Research Lab still lists a **20 November 2026** deadline, **25 November** start, four-week minimum, UG/PG CS/Math/Data Science eligibility and **₹5,000** fee. The live page says Online while the linked official brochure says Hybrid; retain this unresolved discrepancy. No stipend amount is stated. Existing owner: Forsk PR #227.
- CGPDTM's current portal still displays “Batch is LIVE NOW” for the **16 November 2026** batch, but the underlying public notice is dated **27 June 2025** and describes a year-round, non-remunerative programme subject to availability. Do not call it a new November launch. Existing owner: Forsk PR #249.
- VSSC HRDD portal status is route-specific and internally contradictory: UG BE/BTech/BSc/Diploma project-work application cut-off **15 November** has passed; INT 08 internship application is closed; INT 09 is May–July 2027 with a 15 February–15 March 2027 application window. For PG/integrated ME/MTech/MSc/BS-MS project work, the portal labels the current slot “closed” while still printing an application window ending **16 November 2026, 11:59 PM**. Do not advertise the PG route as open without confirmed form acceptance. Existing owner: Forsk PR #172.
- NeGD Careers page 1 and page 2 currently list eight BHASHINI/DIBD Young Professional titles in Noida with a displayed **10 December 2026** deadline, and separate Delhi-NCR roles with **18 November 2026** deadlines (including Frontend Developer, Backend/Mobile, QA/Security, Platform/Security, DevSecOps, AppSec and Full Stack). The official index confirms titles, locations and dates only. Linked JD PDFs returned **403 Forbidden**, so qualifications, experience, salary, fee and application terms for the additional roles remain unverified; no new article was drafted. Existing BHASHINI article owner: Forsk PR #197.
- AWS Education Equity Initiative remains available through an official “Apply now” route with rolling review and no fixed closing date. Its original announcement is **4 December 2024**, not a new November 2026 launch. AWS describes a global organisation-level programme; organisations new to AWS may request up to **US$10,000 in AWS Promotional Credits**, not cash. The official application requires an active AWS Account ID; a Free Tier Free Plan must upgrade to a Paid Plan; only one application can be active at a time; AWS expects to respond within about three weeks. No country-by-country list is published, so India-specific eligibility remains unconfirmed. Existing owner: Mango PR #274; status/form correction comment added.
- NMMSS's published 15 November 2026 deadline has passed; do not present it as open on 16 November. Other existing scholarship owners remain unchanged.

**2) React / frontend**
- React's official versions page still identifies **19.3** as latest stable; GitHub release tags show **19.3.1, 19.2.9, 19.1.10 and 19.0.9**, all dated **14 October 2026**. React 19.3 feature announcement is dated **9 September 2026**. No newer stable release or new November React security advisory was found.
- Existing owners remain Forsk PR #145 (React Server Components security catch-up) and Mango PR #202 (React 19.3 frontend features/upgrade guide). No duplicate draft.

**3) Node.js / backend**
- Latest official Node.js security bulletin remains **11 November 2026**, with patched lines **22.23.5, 24.22.3 and 26.13.1**. The bulletin lists 16 entries (7 High, 6 Medium, 3 Low); release-line applicability must remain CVE-specific.
- **Node 27.0.0-alpha.0.1.0** was published **12 November** and remains Alpha, not LTS or a production replacement.
- No newer official Node.js stable/security release was found. Existing owners remain Mango PR #143/#229 and Groot PR #774; no duplicate draft.

**4) AI / cloud / developer news**
- Google Cloud release notes dated **13 November 2026** include Cloud Quotas GA, Apigee X **1-18-0-apigee-9**, Gemini Enterprise A2A 3-legged OAuth with Agent Identity auth manager GA, and single-user quota limits for AI developer tools GA. Existing owners remain Mango PR #282/#283, Jaipur PR #62 and Groot PR #797.
- GitHub Changelog's latest November entries checked remain dated **13 November** (Gemini 4 Hydrogen in Copilot, GHES support in Copilot app and selected model retirements). Existing Mango/Forsk owners remain in place.
- AWS's 11 November “ICYMI” roundup is a recap of October launches, not a newly announced 16 November feature. No new unowned article was justified.

### Repository and concurrency review
- Central News Factory remains on existing PR #19 / branch `ops/news-factory-cycle-20261109-2209`. Current compare: **238 ahead / 5 behind main**, status diverged; PR remains OPEN/DRAFT and GitHub reports mergeable=false. Main base is `21af139cc32a7b67aab6908c61edeb5998bd4544`. No rebase, force-push or merge.
- Mango: read README, AGENTS, `docs/agent-start-here.md`, task board, work log and integration queue. Existing News Factory owners include #143, #202, #229, #274, #282 and #283. Shared task-board/work-log paths remain occupied by active branches; no brand source write.
- Groot: read `.agent/README.md`, DECISIONS, CURRENT-STATE, BACKLOG, `docs/ai-ops/README.md`, master task board and session handoff. Existing owners include #774 and #797 plus the established blog-factory controller. No new source write.
- Forsk: read `README.txt`, `docs/ai-ops/MASTER_TASK_BOARD.md` and `SESSION_HANDOFF.md`; repository contract reserves board/handoff aggregation to the controller. Existing opportunity and React/Node owners were retained. No new branch or PR.
- Jaipur: read `docs/content-radar.md`, current queue and `docs/IMAGE-PRODUCTION-WORKFLOW.md`; Auto Publish remains OFF and existing owners include #51, #56, #62, #65 and #70. No new source write.
- No verified new story passed all primary-source, eligibility/status and duplicate gates for a fresh article. The NeGD 18 November job PDFs are blocked by official-host 403; details were not inferred from aggregators.

### This-run production ledger
| Stage | This run |
|---|---:|
| Research lanes checked | 4 |
| Existing opportunities/news revalidated | 8+ |
| New verified story suitable for an unowned draft | 0 |
| New article drafts | 0 |
| Existing drafts revalidated | 4 (AWS EEI, IIIT Kottayam, Google Student Researcher, Node/React release owners) |
| New graphics / downloaded media | 0 |
| Verified YouTube embeds | 0 |
| New brand commits / PRs | 0 |
| Status comments added to existing owners | 3 (Mango #274; Forsk #197 and #227) |
| Independent QA-ready | 0 |
| Live / merged / deployed | 0 |

### Checks and blockers
- Official React, Node.js, Google Careers, NeGD, VSSC, IIIT Kottayam and AWS sources opened/rechecked.
- Existing repository instructions and open PR inventories reviewed before any writes.
- No third-party graphic or video downloaded; no iframe added because no story-specific video with independently verified embed suitability was established.
- NeGD's additional November JDs remain blocked by official media-host 403. VSSC PG project-work status remains contradictory. IIIT Kottayam delivery mode remains Online vs Hybrid between page and brochure.
- No independent editorial/technical QA was completed in this run. No merge, deployment, publication or indexing claim.

### Next action
Recheck NeGD JD PDF access and the VSSC/IIIT application routes before any new opportunity article; independently QA the existing high-priority drafts rather than create duplicate stories.


## 2026-11-16 12:06 IST — News Factory cycle 12

### Four-lane research result

**1) Official programmes, internships, scholarships and grants**
- Google Student Researcher 2027 remains listed for India / Remote, with a 4 December 2026 deadline and rolling review. The posting requires current enrolment in a Bachelor's, Master's or PhD programme in the named disciplines plus relevant CS/research experience. Existing owner: Forsk PR #146. No application was submitted.
- NeGD Careers page 2 currently lists the following Delhi-NCR roles with an 18 November 2026 deadline: Frontend Developer; Junior L1/L2 Application Support; Junior QA & Security Support; Junior Backend/Mobile Developer; Manager—Development, Support & Onboarding; Platform & Security Engineer; DevSecOps Engineer; AppSec Specialist; QA Tester; Full Stack Developer; Product Manager. The official linked Frontend and Backend/Mobile PDFs returned 403 Forbidden on this check. Salary, experience, degree criteria, fees and full application conditions remain unverified; no article was drafted from titles alone. Official listing: https://negd.gov.in/hi/careers/page/2/
- NeGD Technical and Non-Technical Winter Internships remain on their respective official pages with a 20 November 2026 deadline; existing Forsk PRs #225 and #180 remain owners. No form submission or acceptance test was performed.
- CRISP Fellowship 2027 remains open through 29 November 2026, 5:00 PM IST: 16 two-year full-time positions across 8 states, standard remuneration ₹9 lakh/year (NISHE-ICPC positions have negotiable remuneration), Indian nationals with bachelor's degree or higher plus project-fit skills. The last valid snapshot before this run's 12:06 IST cutoff was the 11:10 AM IST snapshot recorded in the 11:29 checkpoint: 2,259 overall applications and 300 for Rajasthan GIST's 2 positions. A later page snapshot labelled 12:11 PM is after this run's cutoff and was not used. Existing Jaipur PR #51 remains owner.
- NEC Winter Internship 2026 remains advertised through 30 November. The current page shows a Login/Register link and a 3 November update; the NEC archive lists 2 November publication; the application index shows a 10 November update. The revised notice was digitally signed 27 October. The 2025 policy confirms India-recognised UG/PG/research-scholar routes, category-specific 55% thresholds, a separate recent-graduate consideration route, 50% seats for NER students, 50% for women as far as possible, up to two months with at least one month in person at Shillong, 75% attendance, no promised monthly stipend, and only possible field-visit TA/DA. The direct Invest Meghalaya application route returned no readable page content at 12:06; submission acceptance, remaining seats and any portal-side fee remain unverified.
  - The existing Forsk draft is now tracked by [PR #252](https://github.com/satnamkhowal/forsk-coding-school/pull/252), branch `news-factory/nec-winter-internship-2026-1129`, 3 commits ahead / 0 behind main, 3 added files, OPEN/DRAFT, mergeable=true. This run did not create or modify its files.
  - A coordinator source-check comment was added: [PR #252 comment 6909499460](https://github.com/satnamkhowal/forsk-coding-school/pull/252#issuecomment-6909499460). It records the official-source cross-check, the missing NEC archive link in the article's source list, the article/metadata word-count convention to reconcile (2,990 whitespace-separated body tokens after front-matter removal vs metadata 3,064), and the fact that no CI workflow/status was returned. This is not independent QA or approval.
- React Summit US 2026 takes place 17 and 20 November: the official organiser page describes 17 November as a hybrid day in New York/online and 20 November as a remote day joinable from anywhere. Existing Forsk React Summit guide remains owner; no duplicate article.
- AWS SDK for .NET 4.1 was announced 11 November; an existing Mango draft already owns this topic. No duplicate article.
- No official primary-source notice was found for the circulating “AICTE Industry Fellowship 2026” lead; it remains unverified and was not promoted as an open programme.

**2) React / frontend**
- React's official blog still lists React 19.3 (9 September 2026) as its latest feature-release announcement. Official patch tags last checked remain 19.3.1, 19.2.9, 19.1.10 and 19.0.9 (14 October). No newer stable release or new November React security advisory was found. Existing owners remain Forsk PR #145 and Mango PR #202.
- React Summit US is an event, not a new React release; its 17/20 November dates and online format are recorded above. Existing Forsk event-guide owner retained.

**3) Node.js / backend**
- Latest official security bulletin remains 11 November 2026. Patched versions: 22.23.5, 24.22.3 and 26.13.1. The bulletin lists 16 entries (7 High, 6 Medium, 3 Low); applicability must remain CVE/release-line specific.
- Node 27.0.0-alpha.0.1.0 was published 12 November and remains Alpha, not LTS or a production replacement.
- No newer stable/security release found. Existing owners remain Mango PR #143/#229 and Groot PR #774.

**4) AI / cloud / developer news**
- Google Cloud release notes through 13 November include Cloud Quotas GA, Apigee X 1-18-0-apigee-9, Gemini Enterprise A2A 3-legged OAuth/Agent Identity and related single-user quota controls. Existing owners remain Mango #282/#283, Jaipur #62 and Groot #797.
- GitHub Changelog entries checked through 13 November include Copilot model changes; existing Mango/Forsk owners remain in place.
- AWS SDK for .NET 4.1 (11 November) remains with the existing Mango draft. No duplicate story was created.
- No additional fresh, fully verified, unowned AI/cloud story passed the repository-ownership gate in this run.

### Repository and concurrency review
- Central News Factory remains on PR #19 / branch `ops/news-factory-cycle-20261109-2209`. Before this append, compare was **239 ahead / 5 behind main**, status diverged; PR OPEN/DRAFT and mergeable=false. Only the existing append-only audit file was updated. No rebase, force-push, merge or PR-body rewrite.
- Mango: reread README, AGENTS, `docs/agent-start-here.md`, task board, work log and integration queue. Current queue/open PR review confirms the AWS SDK for .NET 4.1 story already has a Mango owner; React/Node and Google Cloud topics remain assigned. No Mango write.
- Groot: reread `.agent/README.md`, CURRENT-STATE, DECISIONS, MASTER-HANDOFF and BACKLOG. Existing blog-factory gate keeps routine blog production at P3 DEFER behind P1 homepage/UX and runtime/lead QA; existing Node/AI/cloud owners remain. No Groot write.
- Forsk: reread README.txt, `docs/ai-ops/MASTER_TASK_BOARD.md`, `SESSION_HANDOFF.md` and open PR inventory. The master board/session handoff remain controller-owned. Existing PR #252 is active; this run only added the source-check comment and did not alter its branch or shared governance files.
- Jaipur: reread `docs/content-radar.md`, `docs/IMAGE-PRODUCTION-WORKFLOW.md` and current open PR inventory. Auto Publish remains OFF; existing CRISP, React/backend, Apigee and GitHub-security owners remain. No Jaipur write.
- No unverified adjacent brand/repository was added to this cycle.

### This-run production ledger
| Stage | This run |
|---|---:|
| Research lanes checked | 4 |
| New verified stories suitable for an unowned draft | 0 |
| New article drafts | 0 |
| Existing draft PRs source-rechecked | 1 (NEC Winter Internship, Forsk #252) |
| New graphics / downloaded media | 0 |
| Verified YouTube embeds | 0 |
| New brand PRs / commits | 0 |
| Status comments added | 1 (Forsk #252 coordinator source-check) |
| Central checkpoint commits | 1 |
| Independent QA-ready | 0 |
| Live / merged / deployed | 0 |

### Checks and blockers
- Official NEC winter page, signed notice PDF, Internship Policy 2025 and direct application route opened. The application service returned a page with no readable lines; do not claim submission acceptance.
- Official NeGD page 2 opened; linked Frontend and Backend/Mobile job-description PDFs returned 403. No salary/eligibility terms inferred.
- React official blog/conference calendar, Node.js official security bulletin, CRISP portal, Google Careers, Google Cloud release notes and GitHub Changelog were rechecked.
- NEC PR #252 article/metadata/SVG were read from the active branch. Metadata JSON parses; SVG includes title/description, 1200×675 dimensions and no external href. Plain whitespace word-count convention differs from metadata; archive citation link is missing from the article's source list. No commit status or workflow run was returned. Independent editorial, eligibility and responsive QA remain pending.
- No third-party media/video was downloaded; no video embed was inserted because no story-specific video with verified ID and embed permission was established.
- No merge, deployment, publication or indexing claim.

### Next action
Have the NEC draft owner reconcile the article source-list/word-count metadata notes, then obtain independent editorial and eligibility QA plus responsive rendering. Recheck the NeGD 18 November job-description PDFs and current portal acceptance before drafting any role guide. Continue existing React/Node/AI/cloud owners without duplication.


## 16 November 2026 — 17:45 IST cycle

### Four research lanes

1. **Student / developer opportunities**
   - Google Student Researcher 2027 remains an existing Forsk owner (#146): India remote eligibility is listed; current application deadline remains 4 December 2026. No duplicate draft.
   - CRISP Fellowship 2027 remains Jaipur Engineers PR #51: 16 two-year full-time positions across 8 states; standard remuneration ₹9 lakh/year; Indian nationals with bachelor's degree or higher and project-fit criteria; deadline 29 November 2026, 5:00 PM IST. The official portal snapshot at **16 November 2026, 5:27 PM IST** shows **2,405 total submitted applications** and **317 Rajasthan GIST applications for 2 positions**. These are submitted counts, not selection odds. Status comment added to the existing owner PR.
   - NSP PM-USP CSSS 2026–27 fresh applications remain open through 30 November; the NSP Students announcement separately lists 31 October as the renewal student deadline and later verification dates. The scheme is longstanding, not a new launch. Existing Forsk PR #259 owns the fresh-applications guide.
   - NeGD technical/other vacancies and winter internships remain with Forsk owners #180/#197/#225; some linked job-description PDFs still return 403, so salary/eligibility details are not inferred.
   - **AICTE Industry Fellowship Programme 2026–27 Phase 2** is a fresh research lead reported by Indian Express (14 Nov), TOI (15–16 Nov) and India Today (16 Nov): reports describe faculty applications through 15 December, one-year industry immersion, up to 350 faculty, and ₹1 lakh/month (₹75,000 AICTE plus at least ₹25,000 industry), alongside continued parent-institution salary. However, the official ifp.aicte.gov.in portal did not return readable content in this check and no primary circular was accessible. Keep this **research-only / not independently primary-verified**; do not create an article or state the details as official until the portal or an AICTE circular is accessible.

2. **React / frontend**
   - React 19.3.1 (14 Oct) remains the latest official stable tag; no newer stable release found.
   - Next.js November security release: seven advisories dated 3 Nov; patch tags 16.4.5 and 15.5.29; latest stable 16.4.6 (9 Nov); 16.5.0-canary.52 (15 Nov UTC) is pre-release. Existing Forsk PR #260 owns the original guide; no duplicate.

3. **Node.js / backend**
   - The official 11 Nov security bulletin remains current: patched LTS versions 22.23.5, 24.22.3 and 26.13.1; 16 CVEs (7 High, 6 Medium, 3 Low). Node 27.0.0-alpha.0.1.0 (12 Nov) remains Alpha, not production LTS. Existing Mango #143/#229 and Groot #774 ownership retained.

4. **AI / cloud / developer news**
   - Google Cloud release notes remain current through the 15 Nov Publisher Agent 2.7.2 / SOAR 6.3.107 update; Mango PR #286 owns the Publisher Agent guide. Existing Cloud Quotas, Apigee and Gemini owners retained.
   - GitHub Changelog is current through 13 Nov in the checked listing: Gemini 4 Hydrogen GA, GHES support in Copilot app, AI Scan REST API public preview and scheduled Copilot model deprecations. Existing Mango/Forsk/Groot/Jaipur owners retained. Do not state universal Copilot model retirement without reconciling the 15 Oct schedule with current supported-model documentation.

### Existing Forsk draft batch and independent review

Two original draft PRs already created by the current News Factory worker tasks in this same conversation were read back and independently source-checked; this cycle did not create a third article:

- [Forsk PR #259 — PM-USP CSSS 2026–27 fresh applications](https://github.com/satnamkhowal/forsk-coding-school/pull/259): OPEN/DRAFT, 5 commits ahead / 0 behind main, 3 files, mergeable. Article and metadata both contain 2,777 whitespace words; JSON parses; SVG title/description and 1200×675 dimensions present. NSP live status, scheme rates/eligibility, free direct application and ₹30 CSC assisted-service charge checked. Review comment [5919909863](https://github.com/satnamkhowal/forsk-coding-school/pull/259#pullrequestreview-5919909863) flags a PR-description-only word-count typo (2,767 vs actual/metadata 2,777). Applicant login, responsive browser and CI remain untested.
- [Forsk PR #260 — Next.js November 2026 security guide](https://github.com/satnamkhowal/forsk-coding-school/pull/260): OPEN/DRAFT, 3 commits ahead / 0 behind main, 3 files, mergeable. Article and metadata both contain 2,251 words; seven distinct GHSA IDs match the current official GitHub security overview; release tags and support policy checked; metadata JSON parses; SVG title/description and 1200×675 dimensions present with no script or external href. Review comment [5919910227](https://github.com/satnamkhowal/forsk-coding-school/pull/260#pullrequestreview-5919910227) records targeted technical/source QA. Full editorial/security review, responsive browser QA and CI remain pending.

No Actions workflow runs were returned for either PR head SHA. The PR descriptions record local PNG/WebP derivatives, but this cycle did not independently access those recorded local raster paths. No video embed was verified; no third-party media was downloaded or reuploaded.

### Repository and concurrency review

- Central News Factory remains PR #19 / branch ops/news-factory-cycle-20261109-2209. Before this append, compare was **240 ahead / 5 behind main**, status diverged; PR OPEN/DRAFT and mergeable=false. Only this existing append-only audit file is updated. No rebase, force-push, merge or PR-body rewrite.
- Mango: current README, AGENTS, docs/agent-start-here.md, task board, work log and integration queue read. Existing Node.js, React, Google Cloud, AWS and Publisher Agent owners retained; no Mango write.
- Groot: .agent/README.md, MASTER-HANDOFF, CURRENT-STATE, BACKLOG and DECISIONS read. Routine blog factory remains P3 DEFER behind P1 homepage/UX and runtime/lead QA gates; no Groot write.
- Forsk: README.txt, docs/ai-ops/MASTER_TASK_BOARD.md, SESSION_HANDOFF.md and active PR inventory reviewed. Existing PRs #252 (NEC), #253 (BigQuery federated-query Preview), #254 (OpenAI API migration), #259 (PM-USP) and #260 (Next.js) remain distinct. Controller-owned board/session handoff and worker registry untouched.
- Jaipur: README-INSTALL, docs/content-radar.md and current News Factory PR inventory reviewed. Existing #50 (Google APM/Silicon), #51 (CRISP) and #56 (GITAM challenge) retained. Content Radar Auto Publish remains OFF.
- No unverified adjacent brand/repository was added.

### This-run production ledger

| Stage | This run |
|---|---:|
| Research lanes checked | 4 |
| New primary-source opportunities suitable for an unowned draft | 0 |
| New article files created by this run | 0 |
| Existing worker drafts independently reviewed | 2 (Forsk #259 and #260) |
| New original SVGs created by this run | 0 |
| Existing original SVG sources read/checked | 2 |
| Local PNG/WebP derivatives independently verified this run | 0 |
| Verified YouTube embeds | 0 |
| New brand PRs / commits | 0 |
| Independent QA review comments | 2 |
| Existing opportunity status comments | 1 (Jaipur #51 CRISP) |
| Central checkpoint commits | 1 (this append) |
| Fully independent QA-ready | 0 |
| Live / merged / deployed | 0 |

### Next action

Have the Forsk owner correct the PR #259 description word-count typo; complete responsive browser and CI QA for #259/#260; test applicant-login status only with the authorised applicant; recheck AICTE's official portal/circular before drafting the faculty fellowship lead; and continue current owners without duplicate stories. No merge, deployment, publication or indexing is claimed.


---

## 18:40 IST cycle addendum — 16 November 2026

### Research findings

#### Student, developer and career opportunities
- **BHASHINI Young Professional recruitment (existing Forsk owner #197):** revalidated against the MeitY advertisement dated 10 November 2026 and the current NeGD careers listing. Eight positions are listed, one under each designation. The official notice requires at least one year of role-specific professional experience and expressly excludes internship/training experience from that minimum; maximum age is 32 on the last application date; consolidated remuneration is ₹50,000/month inclusive of all; current location is Noida with possible posting elsewhere in India; initial contract is one year or until project end, whichever is earlier. NeGD lists 10 December 2026 as the closing date. The linked Google Form was not accessible in this check; submission acceptance was not tested. Existing draft: https://github.com/satnamkhowal/forsk-coding-school/pull/197.
- **Separate BHASHINI Manager-Admin posting:** MeitY’s 12 November notice is a different single vacancy, with a 22 November deadline, maximum age 58 and 5+ years of relevant procurement/administration experience. It is not one of the eight Young Professional roles and was not added to the Forsk YP article.
- **NeGD technology openings:** current official Careers page lists 12 Delhi-NCR roles with an 18 November 2026 closing date, including Frontend Developer, Junior Backend/Mobile Developer, DevSecOps Engineer, Platform & Security Engineer, AppSec Specialist, QA Tester and Full Stack Developer. Every linked job-description PDF tested in this run returned 403; salary, experience and detailed eligibility therefore remain unverified. No article was drafted from the listing alone.
- **NeGD Winter Internships:** Technical and Non-Technical listings remain open to 20 November 2026 and were posted 12 November. Existing Forsk owners #225 and #180 retained; no duplicate.
- **KSCST 50th Student Project Programme:** official submission window is 21 September–30 November 2026, 5 PM, but proposals are accepted only from eligible final-year students at institutions established in Karnataka. The programme page describes modest financial support without a fixed current award amount. The adjacent Mango PR #265 already covers a student-project opportunity, and this Karnataka-only call has weak geo-fit for the verified Jaipur audience; research retained, no new article.
- **PM-USP CSSS, Google Student Researcher 2027 and CRISP Fellowship 2027:** existing Forsk/Jaipur owners retained; no new article or status claim made without a new portal snapshot.

#### React / frontend
- React GitHub release list still shows 19.3.1 (14 October 2026) as latest stable; 19.3.0 is dated 9 September. No newer stable release or new 16 November security advisory found.
- Next.js November advisories remain covered by existing Forsk PR #260. No duplicate.

#### Node.js / backend
- Node.js official blog still lists 26.13.1, 24.22.3 and 22.23.5 as the 11 November security releases, with 27.0.0-alpha.0.1.0 dated 12 November as Alpha only.
- The 11 November bulletin lists 16 patched vulnerability entries: 7 High, 6 Medium and 3 Low. No newer stable/security release found. Existing Mango/Groot owners retained.

#### AI / Cloud / developer news
- **Microsoft AB-100 exam skills update:** effective 16 November 2026. Current official weights: Plan 35–40%, Design 30–35%, Deploy 20–25%. The study guide says the planning and design shares increased while deployment decreased. Passing score 700; no retirement date listed; Expert certification requires AB-100 plus at least one of 15 listed Associate prerequisites. English is listed; Hindi is not. Price is country/region-based; exact India amount was not visible in the current official page view. A new Forsk draft was created as PR #261.
- **GitHub Copilot model retirement:** the scheduled 16 November date is stated in the existing Forsk PR #185. However, the current supported-models documentation still lists Claude Opus 4.8, Claude Opus 5 and GPT-5.6 Terra as GA. Actual account/client rollout is therefore not confirmed; article language must retain this caveat.
- GitHub Changelog’s latest surfaced November entries are dated 13 November; no newer official AI/developer release found in this run.

### Repository and ownership review
- Central News Factory branch ops/news-factory-cycle-20261109-2209 is 241 commits ahead / 5 behind main and remains diverged. No rebase or merge performed.
- Mango repository task board, AGENTS/start instructions, work log and integration queue reviewed. Existing student-project article PR #265 and other active workers retained; no shared task-board edit.
- Groot .agent README, backlog, current state and master handoff reviewed. Routine blog factory remains P3 deferred behind P1 homepage/UX and runtime/lead QA gates; no Groot write.
- Forsk README.txt, docs/ai-ops/MASTER_TASK_BOARD.md, SESSION_HANDOFF.md, current main and active PR ownership reviewed. Controller-owned board/handoff untouched. Existing BHASHINI #197 and Copilot #185 retained.
- Jaipur README-INSTALL, Content Radar and current PR ownership reviewed. Existing CRISP #51 retained; Auto Publish remains OFF.

### New draft implementation — Forsk Coding School
- Draft PR: https://github.com/satnamkhowal/forsk-coding-school/pull/261
- Branch: news-factory/forsk-ab100-exam-update-20261116-1840
- Base: current Forsk main SHA 521455ae974948db9775102f7d210ad3b7664f7d.
- Two files: one original English article (2,105 words) and one JSON source/QA metadata sidecar.
- Video: Microsoft Learn verified YouTube channel, ID PXrv_8v65hk, published 3 August 2026. This is a course preview, not the 16 November exam update. Embed permission could not be verified, so only a fallback link is recorded; no iframe and no video download.
- Media: no graphic added. Forsk’s current workflow defers P3 blog-image work behind 12 P0 missing course-image references. No third-party asset downloaded or assumed reusable.
- Read-back confirmed both files on the new branch; metadata JSON parses; exactly two changed files; no iframe. Independent editorial, responsive/browser and CI QA remain pending. India-specific exam booking price and live booking were not tested.

### This-run production ledger
| Stage | Count |
|---|---:|
| Research lanes | 4 |
| Fresh primary-source stories suitable for new unowned drafts | 1 (Microsoft AB-100 exam update) |
| New article drafts | 1 |
| New original graphics | 0 |
| Third-party graphics downloaded | 0 |
| Verified YouTube embeds | 0 |
| Verified video fallback links | 1 |
| New brand Draft PRs | 1 (Forsk #261) |
| Existing PR status/research comments | 2 (Forsk #197, #185) |
| Central checkpoint commits | 1 (this append) |
| Independent QA-ready | 0 |
| Live / merged / deployed | 0 |

### Next action
Independent editorial and responsive/browser QA for Forsk #261; confirm India-local AB-100 fee only in the official booking flow; recheck NeGD job-description PDF access before writing a vacancy roundup; continue existing React/Node/AI owners without duplicate drafts. No merge, deployment, publication or indexing is claimed.
