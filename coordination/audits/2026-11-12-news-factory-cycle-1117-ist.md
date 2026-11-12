# News Factory cycle — 12 November 2026, 11:17 IST

**Scope:** Four non-overlapping research lanes across verified education/IT brands. Existing central checkpoint and accessible brand repositories were reviewed before writes. One new unowned, time-sensitive GitHub developer-operations change qualified for an original Mango Engineers draft. Existing React, Node.js and opportunity owners were preserved.

## 1. New draft delivery — Mango Engineers

- **Draft PR:** https://github.com/satnamkhowal/mangoengineers.com/pull/195
- **Branch:** `news-factory/github-secret-scanning-audit-log-migration-20261112-1117`
- **Task:** NF-MANGO-GH-SECRET-SCANNING-BUSINESS-SLUG-20261112-1117
- **Article:** 2,077-word original English SEO/AEO/GEO-ready guide for backend developers, DevSecOps learners and engineering students in Jaipur/India.
- **Official source publication date:** 20 October 2026.
- **Announced rollout date:** 12 November 2026. GitHub did not state an exact rollout hour or per-tenant completion; the draft instructs readers to inspect an authorised live payload before removing compatibility logic.
- **Verified change:** for affected `secret_scanning_alert.*` and `secret_scanning_push_protection.bypass` audit events, `business` changes from enterprise display name to enterprise slug; it remains a string. Numeric `business_id` and event names remain unchanged.
- **Editorial boundary:** this is an audit-log identifier/data-contract update, not a new secret-detection engine, CVE, push-protection policy change or change to alert resolution.
- **Practical content:** integration inventory, use of `business_id` as the enterprise key, temporary dual-value compatibility, synthetic JSON fixtures, Node.js normaliser, unit-test checklist and FAQs.
- **Cost/India:** no new fee or India-specific restriction is announced; access depends on the existing GitHub Enterprise Cloud plan/configuration. No universal price is invented.

### Original media and video
- Original self-authored SVG: `docs/news-factory/media/github-secret-scanning-audit-log-migration.svg`, 1200×675.
- Local PNG preview: `/mnt/data/news-factory/2026-11-12/1117/mango-github-secret-scanning/github-secret-scanning-audit-log-migration.png`, 1200×675, 390,381 bytes; rendered and visually inspected.
- Local optimized WebP preview: `/mnt/data/news-factory/2026-11-12/1117/mango-github-secret-scanning/github-secret-scanning-audit-log-migration.webp`, 1200×675, 40,966 bytes; decode passed.
- Only SVG committed. PNG/WebP remain local previews.
- SVG uses no third-party assets, logos, screenshots, stock artwork or external fonts. Metadata records source/rights basis, attribution, alt text, dimensions, local paths and SHA-256 hashes.
- Related video candidate: ID `lf7bltxaTHQ`, “Introduction to GitHub Advanced Security”, Microsoft Reactor, published 10 April 2024. It is general background, not a video about the November 2026 field change. Fallback link included. Embed permission was not independently verified, so no iframe and no video download/re-upload.

### Primary sources
- https://github.blog/changelog/2026-10-20-updates-to-github-secret-scanning/
- https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/audit-log-events-for-your-enterprise
- https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/audit-log-events-for-your-organization
- https://docs.github.com/en/enterprise-cloud@latest/rest/secret-scanning/secret-scanning
- https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/searching-the-audit-log-for-your-enterprise
- https://www.youtube.com/watch?v=lf7bltxaTHQ

## 2. Student programmes, internships and scholarships

No new unowned opportunity met the verification threshold in this cycle. Existing owners remain:

- **Google Student Researcher 2027:** India / Remote role remains listed; deadline 4 December 2026; rolling review. Current enrolment in a listed Bachelor's/Master's/PhD programme and relevant computer-science experience required. Stipend and fee are not published. Existing Forsk #146.
  - https://www.google.com/about/careers/applications/jobs/results/125423735539671750-student-researcher-2027
- **NMMSS 2026–27:** NSP currently shows student application through 15 November 2026. Existing Forsk owner #173. The NSP page footer says last updated June 2026; applicants should confirm the student login before submission.
  - https://scholarships.gov.in/All-Scholarships
- **Ishan Uday / AICTE Pragati, Saksham and Swanath:** current NSP list shows student deadlines through 30 November 2026. Existing Forsk owners include #186 and scholarship PRs #147/#149; no duplicate article.
- **PM YASASVI Top Class Schools:** the current NSP list shows 30 November, but the separate official announcement says fresh applicants from Rajasthan, Keralam and Karnataka must wait. Existing Forsk #156. No reopening date is stated.
  - https://scholarships.gov.in/ViewMoreAnnouncement
- **NeGD Non-Technical Winter Internship:** existing Forsk #180 owns the 12-position notice, 20 November deadline and conditional ₹15,000/month remuneration. The official PDF does not give an exact publication date and the Google Forms response state was not independently confirmed.
  - https://www.meity.gov.in/static/uploads/2026/11/53935d4075991e5c3f211f053b583270.pdf
- **VSSC Academic Project Work 2027:** existing Forsk #172 owns the programme guide. Current VSSC page shows 15 November deadline for the BE/BTech/BSc/Diploma form route and a 16 November online-window close for the M.E/M.Tech/M.Sc/Integrated/BS-MS route. No duplicate article.
  - https://vsscinternship.vssc.gov.in/HRDD_LOGIN/beforeLoginPage.jsp
- **Sage IT India Scholarship:** existing Forsk #184; sponsor page continues to show ₹50,000 and 15 November deadline. No duplicate.
  - https://sageitinc.com/scholarship/india

## 3. React / frontend lane

- React official blog still lists React 19.3 (9 September 2026) as the latest feature announcement; no newer November stable core announcement was found.
- React Server Components advisory GHSA-xqc2-xf4c-x3h3 / CVE-2026-126187 remains Critical (CVSS 9.5), published 14 October and updated 10 November. Existing Forsk #145 remains owner.
- React Native official blog lists 0.88 as the latest stable feature release (19 October); release schedule lists 0.88.x as Active and 0.89.x as Future, with 0.89 stable scheduled 7 December. RC builds are not production releases. Existing Groot #644 remains owner.
- No duplicate React/React Native article created.

Sources:
- https://react.dev/blog
- https://github.com/react/react/security/advisories/GHSA-xqc2-xf4c-x3h3
- https://reactnative.dev/blog
- https://reactnative.dev/releases/overview

## 4. Node.js / backend lane

Official Node.js release page now lists the 11 November security releases at the top:

- Node.js 26.13.1 (LTS), 11 November 2026.
- Node.js 24.22.3 (LTS), 11 November 2026.
- Node.js 22.23.5 (LTS), 11 November 2026.
- Node.js 27.0.0-alpha.0.0.0 remains Alpha, dated 29 October.

Existing Mango #143 owns the 11 November security bulletin; Mango #153 and Groot #650 own Node.js 27 Alpha/V8 15.6. No duplicate backend article created.

Source: https://nodejs.org/en/blog/release

## 5. AI / cloud / developer lane

- GitHub's November changelog lists Issue Types and Fields for personal accounts (11 November), Enterprise Copilot seat-management API (10 November), Gemini 4 Carbon in Copilot (10 November), Dependabot inactivity pause (10 November), and secret-scanning workflow-log detection (9 November).
- Existing owners were preserved: Forsk #182 and related Copilot drafts; Groot #597 for workflow-log secret scanning; Mango #185 for Git security; existing AWS/Google AI drafts including Groot #662 and Forsk #188/#189 were not duplicated.
- The 20 October GitHub secret-scanning changelog item with a 12 November rollout date was not owned by an existing PR/branch and became Mango #195.

Source: https://github.blog/changelog/month/11-2026/

## 6. Repository and coordination audit

Repositories reviewed for current open PR ownership and accessible instructions before writing:

- **Mango Engineers:** current README, AGENTS.md, `docs/agent-start-here.md`, task board, work log, integration queue and open PR inventory. New isolated documentation-only branch; no shared task-board/work-log/integration-queue edits.
- **Groot Academy:** current README and open PR inventory. Existing #662 and other News Factory owners retained.
- **Forsk Coding School:** README.txt and open PR inventory. Existing #188/#189 and opportunity/security owners retained.
- **Jaipur Engineers:** canonical private repository and open PR inventory. Root README/AGENTS instructions were not available through the connector; no write.
- **CadMate India** and **Clever Ape Academy:** accessible metadata/README and open PR inventory reviewed; no new unowned story selected.
- **Groot Software** and **Forsk Technologies:** requested repository names did not resolve to canonical installed repositories; no write.
- **Central Control Center:** README, PR #19 and existing checkpoint branch reviewed.

### Central checkpoint correction
The existing PR #19 branch `ops/news-factory-cycle-20261109-2209` contains the 09:06 IST checkpoint file, and that file also contains a section headed “Cycle 10:07 IST”. The separately claimed path `2026-11-12-news-factory-cycle-1007-ist.md` did not resolve (404) when checked. Do not rely on that separate link as an existing file. This new 11:17 checkpoint is created as a distinct append-only file on the existing branch.

Before this append, central PR #19 branch compared **122 commits ahead / 5 behind main**, status **diverged**, and GitHub reported mergeable=false. No rebase, merge or force-push was attempted.

## 7. Mango PR #195 validation and release gate

- PR: https://github.com/satnamkhowal/mangoengineers.com/pull/195
- Branch comparison: **6 commits ahead / 0 behind main**, exactly three added paths.
- Article GitHub read-back: 2,077 words; video fallback present; no iframe.
- Metadata JSON parse and GitHub read-back: PASS; word count and SHA-256 recorded.
- SVG XML parse and 1200×675 dimensions: PASS.
- Local PNG render and visual inspection: PASS.
- Local WebP decode: PASS.
- GitHub PR read-back reports OPEN / DRAFT / unmerged; latest fetch reports mergeable=true.
- Combined commit status returned no status entries and PR workflow-runs endpoint returned no runs. CI is unverified; no CI pass is claimed.
- Independent editorial/source QA, independent technical QA and responsive/browser review remain PENDING.
- No task-board, work-log, integration-queue, PHP, public route, sitemap, schema, navigation, redirect or production file changed.

## 8. Production ledger — this cycle's delta

| Stage | Count |
|---|---:|
| Non-overlapping research lanes | 4 |
| New verified, unowned stories selected | 1 |
| Original English article drafts | 1 |
| New Draft PRs | 1 |
| Original committed SVG graphics | 1 |
| Local PNG/WebP previews | 2 |
| Verified YouTube video candidates | 1 |
| Verified iframe embeds | 0 |
| Independent QA-ready increment | 0 |
| Live/published increment | 0 |
| Production deployments | 0 |

No merge, deployment, publication, indexing, scholarship submission or video download occurred. Next action: independent editorial/source QA and technical review for Mango #195; continue monitoring current opportunity deadlines and existing React/Node owners without creating duplicate drafts.


### CI status recheck — 12 November 2026, after PR creation
- Mango PR #195 later exposed GitHub Actions run [PHP Architecture Check #43164888964](https://github.com/satnamkhowal/mangoengineers.com/actions/runs/43164888964) on head `ead1d7dfbca07db92ec8e44df902aceb6d86987d`; conclusion: **failure**.
- The only job, `php-architecture` (job ID `131004343759`), returned an empty steps list. The job-log endpoint returned `BlobNotFound`; no runner/test-step output was available.
- This is a workflow/runner/log-availability blocker, not evidence of a PHP or Markdown source-test failure. Do not claim CI passed or infer a source-code failure. Independent editorial, technical and responsive QA remain pending.


### VSSC application-status comment — 12 November 2026
- Rechecked the live VSSC HRDD portal and added a dated status comment to Forsk Coding School PR #172: https://github.com/satnamkhowal/forsk-coding-school/pull/172
- The separate INT 08 internship slot (1 November 2026–31 January 2027) now explicitly says application submission is closed. Next INT 09 is scheduled for 1 May–31 July 2027, with an application window 15 February–15 March 2027.
- This does not change the separate Academic Project Work routes already covered by PR #172: BE/BTech/BSc/Diploma form route due 15 November 2026; M.E/M.Tech/Integrated M.Tech/M.Sc/Integrated M.Sc/BS-MS online route closes 16 November 2026 at 23:59 IST.
- No new article was created; existing Forsk #172 remains the single owner. Official portal: https://vsscinternship.vssc.gov.in/HRDD_LOGIN/beforelogincontroller


## Cycle 11 — 12 November 2026, 12:08 IST

### 1. Research lanes and source verification

Four non-overlapping research lanes were reviewed: (1) student/developer programmes and scholarships, (2) React/frontend releases and security, (3) Node.js/backend releases and security, and (4) AI/cloud/developer announcements. Primary-source checks were prioritised. No YouTube news claim was used without official corroboration.

#### Student programmes and opportunities

- **Google Student Researcher, 2027:** Google Careers still displays an Apply action and a **4 December 2026** deadline, with rolling review. The role is marked **India / Remote eligible**. Applicants must currently be enrolled in a Bachelor's, Master's or PhD programme in a listed field and have experience in a relevant CS/research area. Google says applicants must remain in one of the specified country locations for the full engagement. No stipend or application fee is stated on the posting. Existing owner: Forsk PR #146; no duplicate article.
  - Official: https://www.google.com/about/careers/applications/jobs/results/125423735539671750-student-researcher-2027
- **IIIT Guwahati MeitY Project Intern:** the official vacancy page still lists one full-time CSE/allied-discipline project intern, a **₹15,000/month** fellowship from MeitY until **15 September 2027**, a tentative 10-month period (November 2026–September 2027), application deadline **15 November 2026**, and online selection on **20 November 2026**. On-campus participation is preferred; remote may be considered only exceptionally. No hostel is available; the selected intern must arrange accommodation at their own cost. The official notice is dated **30 October 2026**, distinct from the application deadline. The notice links to a Google Form, but response acceptance could not be independently confirmed.
  - Official: https://www.iiitg.ac.in/vacancy-for-project-intern-position-in-a-1
  - Existing owner: Forsk PR #163. Article and metadata research timestamps were refreshed; comment: https://github.com/satnamkhowal/forsk-coding-school/pull/163#issuecomment-6816863742
- Existing opportunity owners retained without duplicate drafts: Google Student Researcher #146; NMMSS #173 (15 Nov); Ishan Uday #186 (30 Nov); Sage IT Scholarship #184 (15 Nov); PM YASASVI #156 (30 Nov listing with state restrictions); Jaipur Engineers #44 NITI Aayog, #45 Bharti Airtel, #46 Honeywell, and #47 PM Scholarship.
- No new unowned scholarship/internship article qualified in this lane.

#### React / frontend

- React's official community conference list currently includes **React Summit US 2026** for **17 and 20 November 2026**, in-person in New York plus online (hybrid): https://react.dev/community/conferences
- The organiser's event page currently lists a regular remote ticket at **US$260**, in-person Late Bird at **US$1,199**, and a remote combo ticket at **US$330**. The remote schedule's UTC timestamps convert to 19:45 IST on 17 Nov (closing 04:10 IST on 18 Nov) and 20:30 IST on 20 Nov (closing 00:30 IST on 21 Nov). The organiser says remote access is available from anywhere; India payment-method acceptance is not explicitly confirmed.
- The event page lists a free React + Firebase + Google Cloud workshop on 12 Nov, 10:00–13:00 EST (20:30–23:30 IST). Its registration action says “Get Full Ticket”, so standalone free access is not confirmed. The page also advertises a limited free-ticket referral promotion; terms/availability require recheck.
- Event-page original publication date is not stated; the event dates are recorded separately. This is a paid conference, not a scholarship or internship.
- New original Forsk article: PR #190, 1,806 words; original SVG 1200×675 committed. Local WebP (1200×675, 48,324 bytes) and PNG (1200×675, 102,149 bytes) previews were generated; only SVG is committed in the PR. Source/license/attribution/alt text/dimensions/local paths/hashes are recorded in metadata.
  - PR: https://github.com/satnamkhowal/forsk-coding-school/pull/190
  - Official event: https://reactsummit.us/
  - Schedule: https://reactsummit.us/schedule
  - Checkout: https://reactsummit.us/checkout
- No event-specific official YouTube video was verified. A GitNation video for the Amsterdam June 2026 edition was reviewed and rejected as not specific to the US event; no iframe or video download.

- React Server Components advisory GHSA-xqc2-xf4c-x3h3 is **Critical (CVSS 9.5)** and was published 14 October 2026. It affects the RSC packages `react-server-dom-webpack`, `react-server-dom-parcel` and `react-server-dom-turbopack`; fixed tags listed by the official advisory are **19.0.9, 19.1.10, 19.2.9 and 19.3.1**. Applications without a React server or an RSC-supporting framework/bundler are not affected. Existing owner: Forsk PR #145; no duplicate article.
  - Official: https://github.com/react/react/security/advisories/GHSA-xqc2-xf4c-x3h3

#### Node.js / backend

- Official Node.js security releases dated **11 November 2026**:
  - 22.x → **22.23.5**
  - 24.x → **24.22.3**
  - 26.x → **26.13.1**
- The release pages list 16 distinct CVEs across the release set: 7 HIGH, 6 MEDIUM and 3 LOW. Applicability differs by branch; for example CVE-2026-126051 appears on 24.x/26.x but not 22.x. The LOW-severity Permission Model change is **CVE-2026-123873**, “check heap snapshot destination”.
- Existing owner: Mango PR #143. Corrected an incorrect CVE ID/description in the existing article from CVE-2026-106071 to CVE-2026-123873 and refreshed its last-verified timestamp. Correction comment: https://github.com/satnamkhowal/mangoengineers.com/pull/143#issuecomment-6816884410
- Official release pages:
  - https://nodejs.org/en/blog/release/v22.23.5
  - https://nodejs.org/en/blog/release/v24.22.3
  - https://nodejs.org/en/blog/release/v26.13.1
- No duplicate Node.js article was created.

#### AI / cloud / developer news

- No new unowned AI/cloud product announcement qualified after checking official sources.
- Existing owners retained: Mango #192 (Google Antigravity CLI in Agent Platform Workbench), Mango #195 (GitHub Secret Scanning audit-log business slug change), Forsk #188 (AWS UAEF), Forsk #189 (Google Agent Gateway), Groot #662 (AWS AI-PDLC), and existing GitHub/Copilot changelog drafts.
- No duplicate AI/cloud article created.

### 2. Repository and ownership audit

Reviewed current repository metadata, open PR inventory, and available instructions before writes:

- **Forsk Coding School:** README/task-board and image-production workflow reviewed. New topic had no matching open PR or branch. Existing PR #163 remained the IIIT Guwahati owner; new React Summit topic is isolated in PR #190.
- **Mango Engineers:** task board/work log and open PR inventory reviewed. Node.js security remains owned by PR #143; its existing draft received a targeted CVE correction only. Existing PR #195 owns the GitHub audit-log change.
- **Groot Academy:** current open PR inventory reviewed; no new write because current News Factory owners and other concurrent course/graphics work were retained.
- **Jaipur Engineers:** canonical repository `satnamkhowal/jaipurengineers.com` verified. Current open News Factory owners include PRs #44–#47; no duplicate opportunity draft. Root README/AGENTS instructions were not accessible, so no write.
- **Clever Ape Academy, CadMate India and Forsk Technologies:** repository metadata/open PR inventory reviewed; no new unowned story selected. Groot Software's guessed repository name did not resolve, so no write.
- **Central Control Center:** README operating rules and existing PR #19/checkpoint branch reviewed. Central repository remains coordination-only; implementation is in brand repositories.

### 3. GitHub implementation and validation

#### Forsk PR #190 — new React Summit US draft

- URL: https://github.com/satnamkhowal/forsk-coding-school/pull/190
- Branch: `content/news-factory-react-summit-us-2026-20261112-1208`
- 4 commits ahead / 0 behind main; GitHub reports OPEN / DRAFT / mergeable=true.
- 3 files: 1,806-word article, JSON research/asset metadata, original 1200×675 SVG.
- Metadata JSON parses; article/SVG/metadata read-back verified. A fourth commit records the final 1,806-word count and successful repository-readback/XML checks.
- Local SVG rendered to PNG; PNG visual inspection passed; WebP decode passed. WebP/PNG previews are local only, not committed.
- Combined status has no status entries and workflow-runs endpoint returned no runs. CI is **unverified**, not passed.
- Independent editorial/source QA, technical QA and responsive review remain PENDING.

#### Forsk PR #163 — existing IIIT Guwahati draft

- Existing article and metadata updated on its existing branch only; no duplicate story.
- Research timestamp refreshed to 12 November 2026, 12:08 IST.
- Official page still lists the 15 November deadline; Google Form response acceptance remains unverified.
- Branch comparison: 7 commits ahead / 1 behind main; GitHub currently reports OPEN / DRAFT / mergeable=true. No rebase or merge.
- Status comment: https://github.com/satnamkhowal/forsk-coding-school/pull/163#issuecomment-6816863742
- No status entries or workflow runs returned for the latest commit; CI unverified.

#### Mango PR #143 — existing Node.js security draft

- Existing article corrected to use CVE-2026-123873 for the heap-snapshot destination permission check.
- Branch comparison: 54 commits ahead / 2 behind main; status diverged; GitHub reports mergeable=false.
- No rebase, merge or force-push. No status entries or workflow runs returned for the latest commit; CI unverified.
- Status/correction comment: https://github.com/satnamkhowal/mangoengineers.com/pull/143#issuecomment-6816884410

### 4. Production ledger — this cycle's delta

| Stage | Count |
|---|---:|
| Non-overlapping research lanes | 4 |
| New verified unowned stories selected | 1 |
| New original English article drafts | 1 |
| Existing article/source corrections | 2 |
| New Draft PRs | 1 |
| Original committed SVG graphics | 1 |
| Local optimized WebP previews | 1 |
| Local PNG previews | 1 |
| Verified event-specific YouTube videos | 0 |
| Verified iframe embeds | 0 |
| Independent QA-ready increment | 0 |
| Live/published increment | 0 |
| Merges/deployments | 0 |

### 5. Central branch state and next actions

- Existing central PR #19 branch `ops/news-factory-cycle-20261109-2209` compared **diverged from main (ahead/behind count changes as append-only checkpoints are committed)**, status **diverged**, GitHub reports mergeable=false. This checkpoint is appended to the existing 11:17 file on that branch; no rebase, merge or force-push.
- Next: independent QA for Forsk #190; recheck React Summit tickets and workshop conditions before 17/20 Nov; monitor IIITG deadline 15 Nov and Google Student Researcher deadline 4 Dec; continue React RSC and Node.js security owner checks; do not publish or deploy without approval.
- No application was submitted, no video was downloaded, and no article was published live.


## 2026-11-12 — 14:02 IST: four-lane revalidation and Node.js CVE correction

### Research lanes

#### 1. Student, internship and scholarship opportunities

- **Google Student Researcher, 2027:** the current Google Careers listing shows an Apply control, **India — Remote eligible**, and asks applicants to complete the application before **4 December 2026**; review is rolling. Minimum requirements include current enrolment in a Bachelor's, Master's or PhD programme in a listed discipline and experience in a relevant computer-science area. The listing does not state stipend, fixed duration or application fee. Existing single owner: Forsk PR #146.  
  Source: https://www.google.com/about/careers/applications/jobs/results/125423735539671750
- **NMMSS 2026–27:** the current NSP scheme card lists **15 November 2026** as the student-application deadline; 30 November and 15 December are verification milestones, not the student deadline. Existing owner: Forsk PR #173.  
  Source: https://scholarships.gov.in/All-Scholarships
- **NeGD Non-Technical Internship, Winter 2026:** current official Careers listing shows Delhi-NCR and **20 November 2026**. The current MeitY-hosted four-page notice specifies 12 positions, recognised Indian university/student routes with at least 60% in the last-held degree/certificate and 15 years of formal education (or listed pre-final/final-year routes), institutional sponsorship/forwarding, minimum two months extendable by one month, and conditional token remuneration of **₹15,000/month** paid after full tenure and mentor/report acceptance. The PDF does not publish a fixed application fee. Existing owner: Forsk PR #180.  
  Sources: https://negd.gov.in/careers/ ; https://www.meity.gov.in/static/uploads/2026/11/53935d4075991e5c3f211f053b583270.pdf
- **NeGD Technical Internship, Winter 2026:** the same official Careers page separately lists a Delhi-NCR technical internship with **20 November 2026** deadline. The linked official PDF currently returns HTTP 403 from the media host; eligibility, disciplines, seats, stipend, duration, application fee and form state remain unverified. No article was created and no non-technical terms were copied to this programme. Status comment on existing Forsk PR #180: https://github.com/satnamkhowal/forsk-coding-school/pull/180#issuecomment-6818935451  
  Listing: https://negd.gov.in/careers/  
  Linked PDF: https://negd-media.digitalindiacorporation.in/wp-content/uploads/2026/11/Advertisement-Announcement-for-Winter-Technical-Internship.pdf
- **VSSC:** the official portal says INT 08 internship applications are closed; INT 09 is scheduled for 1 May–31 July 2027 with applications 15 February–15 March 2027. Separate academic-project routes remain time-sensitive: BE/BTech/BSc/Diploma application last date **15 November 2026**; M.E/M.Tech/Integrated M.Tech/M.Sc/Integrated M.Sc/BS-MS online window through **16 November 2026**. Eligibility and course-specific restrictions remain in the existing Forsk PR #172; no duplicate was created.  
  Sources: https://vsscinternship.vssc.gov.in/HRDD_LOGIN/beforelogincontroller ; https://www.vssc.gov.in/STUDENTS/
- **Google PhD Fellowship 2026:** official page says the 2026 cycle is closed (applications 5 March–30 April). India is an eligible region and the page lists different early-/late-stage PhD award amounts, but this is not a newly open opportunity.  
  Source: https://research.google/programs-and-events/phd-fellowship/

#### 2. React / frontend

- No new stable React release was found in this cycle. Official React releases remain **19.3.1, 19.2.9, 19.1.10 and 19.0.9**, all dated 14 October 2026; React 19.3.0 was released 9 September.
- The Critical React Server Components RCE advisory GHSA-xqc2-xf4c-x3h3 was published 14 October; fixed package versions are 19.0.9, 19.1.10, 19.2.9 and 19.3.1. Server/RSC support is required for exposure; applications without a server or RSC-supporting framework/bundler/plugin are not affected by this advisory.
- Existing owner remains Forsk PR #145; no duplicate article.  
  Sources: https://react.dev/blog ; https://github.com/react/react/releases ; https://github.com/react/react/security/advisories/GHSA-xqc2-xf4c-x3h3

#### 3. Node.js / backend

- Official Node.js security release published **11 November 2026** and links patched versions **22.23.5**, **24.22.3** and **26.13.1**. The bulletin lists **16 distinct CVEs: 7 HIGH, 6 MEDIUM, 3 LOW**; affected release lines vary by CVE.
- A fresh line-by-line review found that Mango's existing article still had one incorrect low-severity Permission Model row after the earlier applicability-only correction. The official bulletin lists **CVE-2026-106071** for wildcard filesystem over-grant and does **not** list CVE-2026-123873 in this release. The article now replaces the incorrect heap-snapshot row with CVE-2026-106071 and records the exact affected-line matrix for all 16 CVEs.
- Mango PR #143 existing branch `content/news-factory-20261109-1808`: article, task-board row and work log updated sequentially; article is now 2,132 words. The aggregate SVG remains accurate (16 CVEs and severity totals) and contains no incorrect identifier, so no graphic change was needed.
- Commits: article `964c432c63fb2118b1f57159342387587d6b4fc5`; task board `8613083ff2d0e27262142b9f4d57d9c85ea68f63`; work log / current branch head `3d7c73c46d552ef7da9642fc1da7bc4f10db842f`.
- PR #143 remains OPEN / DRAFT / mergeable=false because its branch is diverged from main. No rebase, force-push or merge. Comment: https://github.com/satnamkhowal/mangoengineers.com/pull/143#issuecomment-6818893451
- Combined-status and workflow-run lookups for the updated head returned no status entries and no workflow runs; CI is unverified, not passed.  
  Source: https://nodejs.org/en/blog/vulnerability/november-2026-security-releases

#### 4. AI / cloud / developer news

- **Gemini for healthcare:** Google Cloud's announcement publication date is 10 November 2026. The current product page labels it Preview and says product preview is available in the **United States** for Gemini Enterprise Standard and Plus customers. Global connector locations do not establish India product availability. Product-specific pricing is not published; the page directs organisations to contact Google Cloud. Existing owner: Groot PR #631. Current product-page revalidation comment: https://github.com/satnamkhowal/grootacademy.com/pull/631#issuecomment-6818934248
- The official product page embeds a 1:48 YouTube link with video ID `uqmXoKOs_o0`. The link is visible on Google's page, but YouTube metadata retrieval was throttled, so channel and upload date remain unverified. No iframe was added and no video was downloaded.
- **Gemini 4 Carbon in GitHub Copilot:** GitHub changelog publication date 10 November 2026; generally available to Copilot Pro+, Max, Business and Enterprise, with gradual rollout and provider-list usage-based billing. Existing owner: Forsk PR #168; status comment records this as a separate Copilot distribution channel, not a new duplicate article: https://github.com/satnamkhowal/forsk-coding-school/pull/168#issuecomment-6818934938
- **GitHub Copilot model retirements:** official notice says selected models are deprecated on **16 November 2026**; existing Forsk PR #185 remains owner.  
  Sources: https://github.blog/changelog/2026-11-10-gemini-4-carbon-in-github-copilot/ ; https://github.blog/changelog/2026-10-15-upcoming-deprecation-of-selected-github-copilot-models-in-mid-november/

### Repository, ownership and implementation

- Current central README, PR #19 branch and the existing 11:17 IST checkpoint were reviewed. Central repository remains coordination-only.
- Mango README, AGENTS, agent-start, task board, work log and integration queue were reviewed before the existing Node.js draft correction.
- Current open PR inventories were reviewed for Mango, Groot, Forsk and Jaipur. Existing owners were retained: Mango #143/#195; Groot #631; Forsk #145/#146/#168/#172/#173/#180/#185/#190; Jaipur #44–#47. No duplicate topic or overlapping new article was created.
- Groot root README contains only `# gta`; expected docs agent-start/task-board/work-log/integration-queue files were not found at those paths. Forsk and Jaipur expected docs/AGENTS/task-board paths were not found. No new writes were made to those repositories.
- Other candidate brands remain unmodified where canonical repository/source mapping or instructions were not verified.

### Production ledger — 14:02 IST delta

| Stage | Count |
| --- | ---: |
| Non-overlapping research lanes | 4 |
| New verified unowned stories selected | 0 |
| New original English article drafts | 0 |
| Existing article corrections | 1 |
| Existing PR status/research comments | 4 |
| New Draft PRs | 0 |
| New graphics | 0 |
| New optimized previews | 0 |
| Verified video candidates with complete channel/date metadata | 0 |
| Verified iframe embeds | 0 |
| Independent QA-ready increment | 0 |
| Live/published increment | 0 |
| Merges/deployments | 0 |

No fresh unowned story met the full verification/ownership gate. Existing owners already cover the current Google, NMMSS, NeGD non-technical, VSSC, React RSC, Node.js, Gemini healthcare, Gemini 4 Carbon and Copilot-retirement topics. The only article file change in this cycle was the Node.js CVE correction; no new graphic or embed was produced.

### Next actions

1. Independent technical/editorial QA for Mango PR #143; resolve its main-branch divergence without rebase/force-push shortcuts.
2. Recheck NMMSS and VSSC academic-project deadlines on 15–16 November.
3. Retrieve the current NeGD technical internship PDF from an accessible official endpoint before considering a separate draft.
4. Continue React RSC and Node.js release-owner QA; do not mark either QA-ready until independent review runs.
5. Recheck Gemini for healthcare preview geography and the official YouTube video's channel/date before any iframe is added.
6. Keep every PR draft-only; no merge, deployment or publication without approval.


## Cycle 15 — 12 November 2026, 15:11 IST

### Research lanes

#### 1. Student, developer and scholarship opportunities

- **Google Student Researcher, 2027:** Google Careers still displays Apply. The role explicitly lists India as a remote location, requires current enrolment in a relevant Bachelor's, Master's or PhD programme and experience in a computer-science research area. Apply by **4 December 2026**; applications are reviewed on a rolling basis. Existing owner: Forsk PR #146. Stipend and application fee are not stated in the accessible posting.
- **National Means-cum-Merit Scholarship (NMMSS):** the live NSP 2026–27 list shows the student application deadline as **15 November 2026**. The NSP page footer still says “Last update on June 2026”; students should confirm their state/institute workflow in the portal before submission. Existing owner: Forsk PR #173.
- **VSSC academic project work:** the official portal shows the next BE/BTech/BSc/Diploma project slot as 1 January–31 March 2027 with a **15 November 2026** application cutoff; the ME/MTech/Integrated/MSc/BS-MS next slot is 1 January–30 June 2027 with an online window ending **16 November 2026, 11:59 PM**. The current INT 08 internship slot is closed; INT 09 is 1 May–31 July 2027 with applications 15 February–15 March 2027. Existing owner: Forsk PR #172. Read the course-specific instructions carefully; BE/BTech/BSc/Diploma and PhD use a downloaded form rather than the online PG route.
- **NeGD current openings — new watchlist lead, not an article:** the official Careers page currently lists eight Young Professional roles in Noida (including MLOps, Cloud Technology Engineer, API Developer, ML Engineer and AI Engineer) with a 10 December 2026 deadline, plus four junior/frontend/backend/QA-support roles in Delhi-NCR with an 18 November deadline. The linked role-detail PDFs returned HTTP 403 in both the page fetch and direct download attempt. Qualifications, experience, remuneration, contract terms, fees and application-form details therefore remain unverified. Do not publish an eligibility or salary claim until the official PDFs are accessible. The separate Winter Technical and Non-Technical Internship listings show 20 November; existing non-technical owner is Forsk PR #180, and its PDF also returned 403.
- PM YASASVI and the AICTE/UGC schemes remain in the NSP 2026–27 listing with student deadlines shown as 30 November, but the portal footer's June 2026 update and the earlier state-specific YASASVI restriction remain caveats. No duplicate opportunity draft was created.

Primary links:
- Google Careers: https://www.google.com/about/careers/applications/jobs/results/125423735539671750-student-researcher-2027
- NSP: https://scholarships.gov.in/All-Scholarships
- VSSC portal: https://vsscinternship.vssc.gov.in/HRDD_LOGIN/beforelogincontroller
- NeGD Careers: https://negd.gov.in/careers/

#### 2. React / frontend

- React stable release page still lists 19.3.1, 19.2.9, 19.1.10 and 19.0.9, all released 14 October 2026. No newer stable React core release was found on 12 November.
- The RSC unauthenticated RCE advisory remains Critical; affected react-server-dom packages list fixed versions 19.0.9, 19.1.10, 19.2.9 and 19.3.1. Existing owner: Forsk PR #145.
- React Native 0.89.0-rc.1 was released 10 November and is marked Pre-release; 0.88.1 remains the latest stable release (27 October). Existing owner: Groot PR #644. Do not recommend the RC for production.
- Existing Forsk React Summit US PR #190 was corrected after a fresh check of the dedicated Firebase/Google Cloud workshop page. That page lists 12 November at 15:00 without a timezone label and explicitly requires a Multipass or Full conference ticket for live remote attendance. The article no longer calls this a standalone free workshop or converts the time to IST. Article and metadata were updated; a correction comment and PR-description update were added. The event remains scheduled for 17 November (hybrid) and 20 November (remote). Official event page rechecked at 15:31 IST still lists US$260 remote regular, US$1,199 in-person Late Bird and US$330 remote combo; final checkout/payment acceptance and taxes remain to be confirmed by the purchaser.

Primary links:
- React releases: https://github.com/react/react/releases
- React RSC advisory: https://github.com/react/react/security/advisories/GHSA-xqc2-xf4c-x3h3
- React Native releases: https://github.com/react/react-native/releases
- Workshop access: https://gitnation.com/contents/production-react-apps-with-firebase-and-google-cloud
- React Summit schedule: https://reactsummit.us/schedule

#### 3. Node.js / backend

- The latest official security release set remains 11 November 2026: Node.js 22.23.5, 24.22.3 and 26.13.1.
- The bulletin lists 16 distinct CVEs (7 HIGH, 6 MEDIUM, 3 LOW). The official page confirms CVE-2026-106071 is the Permission Model wildcard filesystem over-grant; it is not the heap-snapshot mapping previously suspected. Existing Mango owner: PR #143; no duplicate Node article was created.
- No newer Node.js security or stable release dated 12 November was found.

Primary link: https://nodejs.org/en/blog/vulnerability/november-2026-security-releases

#### 4. AI / cloud / developer news

- **AWS SageMaker HyperPod silent data corruption guide:** AWS Machine Learning Blog publication date is 11 November 2026. This is a technical how-to, not a new product launch or event. It covers per-step non-finite gradient checks, selected cross-node ring-replay audits, replica weight fingerprints and operator-reviewed recovery. AWS's experiments used synthetic data and software-injected faults; they do not establish a real-hardware failure rate.
- The companion repository is MIT-0. The current README's benchmark estimates differ slightly from the AWS blog table; the new draft flags the revision drift rather than mixing values.
- No relevant official YouTube video with independently verified channel and upload date was found. No iframe or video download was made.
- Existing GitHub/AWS/AI topics in the other open News Factory PRs were left with their current owners; no near-identical article was syndicated.

Primary links:
- AWS announcement (published 11 Nov 2026): https://aws.amazon.com/blogs/machine-learning/detecting-and-recovering-from-silent-data-corruption-on-amazon-sagemaker-hyperpod/
- AWS companion sample (MIT-0): https://github.com/awslabs/awsome-distributed-ai/tree/main/examples/use-cases/pytorch-ddp-sdc-detection
- HyperPod regions: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html
- SageMaker pricing caveats: https://aws.amazon.com/sagemaker/ai/pricing/
- AWS Pricing Calculator: https://calculator.aws/

### New implementation

**Groot Academy — new Draft PR #678**
- https://github.com/satnamkhowal/grootacademy.com/pull/678
- One original 2,519-word English article: `docs/news-factory/drafts/aws-sagemaker-hyperpod-silent-data-corruption-pytorch-ddp-guide.md`.
- One source/SEO/rights/QA metadata JSON sidecar.
- One original 1200×675 SVG diagram: `docs/news-factory/media/aws-hyperpod-sdc-three-checks.svg`.
- No public blog route, PHP template, registry, sitemap, canonical, redirect or production page changed.
- Branch `news-factory/aws-hyperpod-sdc-ddp-guide-20261112-1511-r2`: 3 commits ahead / 0 behind main at comparison. PR is OPEN and DRAFT; latest GitHub snapshot reports mergeable=true. No workflow runs or combined-status entries were returned, so CI is UNVERIFIED.
- SVG XML parse, PNG render, WebP decode and visual inspection PASS. Local derivatives: `/mnt/data/news-factory/2026-11-12/1511/groot-sdc/aws-hyperpod-sdc-three-checks.png` (114,247 bytes) and `.../aws-hyperpod-sdc-three-checks.webp` (56,106 bytes). Only the original SVG is committed.
- Independent editorial, technical and responsive QA remain PENDING. No merge, deployment or publication.

The first attempt branch `news-factory/aws-hyperpod-sdc-ddp-guide-20261112-1511` was not used because main advanced by two commits during creation. The clean `-r2` branch was recreated from current main and is the only branch referenced by PR #678; the abandoned branch has no PR and was not merged.

**Forsk Coding School — existing Draft PR #190 correction**
- https://github.com/satnamkhowal/forsk-coding-school/pull/190
- Article corrected from 1,806 to 1,882 words; metadata updated with the dedicated workshop access source and timezone caveat.
- Branch comparison after the workshop and ticket-source corrections: 8 commits ahead / 0 behind main; PR remains OPEN, DRAFT and mergeable=true. No workflow runs or combined-status entries were returned; CI is UNVERIFIED.
- Independent editorial QA remains PENDING; no publication.

### Repository and deduplication audit

Reviewed current repository/PR ownership for Mango Engineers, Groot Academy, Forsk Coding School, Jaipur Engineers, Clever Ape Academy, CadMate India, and Forsk Technologies, plus the central coordination repository. Groot Software's canonical implementation repository remains ambiguous among similarly named repositories; no write was made there. CadMate's verified repository is `cadmateindia.com`; no matching SDC topic was found. Searches across the reviewed brand PRs found no matching silent-data-corruption draft. Mango PR #172 mentions HyperPod only in a separate AWS APT CVE/image-update context; it is not an SDC article and remains independently owned.

Current relevant owners retained:
- Forsk #146 Google Student Researcher; #145 React RSC; #172 VSSC; #173 NMMSS; #180 NeGD internship; #190 React Summit.
- Mango #143 Node.js security; #172 AWS APT CVE; #195 GitHub audit-log migration.
- Groot #644 React Native RC; #662 AWS AI-PDLC; #678 new SDC guide.

### Production ledger — 15:11 IST

| Stage | New count |
| --- | ---: |
| Non-overlapping research lanes | 4 |
| New verified, unowned story selected | 1 |
| New original English article drafts | 1 |
| Existing article corrections | 1 |
| New Draft PRs | 1 |
| Original committed SVGs | 1 |
| Local optimized PNG/WebP derivatives | 2 |
| Verified relevant YouTube videos | 0 |
| Verified iframe embeds | 0 |
| Independent QA-ready increment | 0 |
| Live/published increment | 0 |
| Merges/deployments | 0 |

### Next actions

1. Independent editorial and technical review of Groot #678; do not mark QA-ready based only on source read-back.
2. Recheck the NeGD role-detail PDFs and application endpoint before drafting the new 18 November / 10 December openings.
3. Recheck VSSC academic-project submission route and NMMSS student deadline before 15–16 November.
4. Keep React #145, React Native #644 and Node.js #143 with their existing owners; do not duplicate.
5. Keep Forsk #190 draft-only and verify checkout/ticket access before event coverage is published.
6. Keep central PR #19 and all brand PRs unmerged until independent QA and explicit release approval.


---

## News Factory cycle — 12 November 2026, 16:08 IST

### Research and deduplication
- Four non-overlapping lanes rechecked: student/developer opportunities; React/frontend releases and security; Node.js/backend releases and security; AI/cloud/developer announcements.
- Google Student Researcher 2027 remains an existing Forsk #146 owner (India/Remote, 4 December 2026 deadline; Apply visible; rolling review; stipend/fee not stated).
- NIC Digital India Internship Winter 2026 remains Mango #147. The official portal is now accessible and shows the Winter 2026 notice, registration start 2 November 2026, registration/login controls, and an offline internship period of 1 December 2026–31 January 2027. The portal's last-updated label is 12 November 2026. It does not show an application closing date; the previously reported 13 November claim remains unverified and must not be presented as an official deadline.
- NMMSS, VSSC academic projects, NeGD Non-Technical Winter Internship and existing scholarship drafts remain assigned to their current Forsk owners; no duplicate opportunity article was created.
- React repository release page still shows 19.3.1 / 19.2.9 / 19.1.10 / 19.0.9 as the latest stable patch tags, all dated 14 October 2026. The two RSC advisories retain their existing Forsk #145 owner; fixed versions remain 19.3.1 / 19.2.9 / 19.1.10 / 19.0.9.
- Node.js official 11 November security release lines remain 22.23.5, 24.22.3 and 26.13.1. The prior CVE mapping discrepancy between the November bulletin and individual release notes remains unresolved; Mango #143 stays blocked for independent security QA and no new Node article was made.
- New unowned AI/cloud story selected: AlloyDB AI ai.classify and ai.extract. Google Cloud Blog publication is 11 November 2026; AlloyDB release notes show the functions in Preview from 27 October 2026. PostgreSQL 18+, google_ml_integration 1.6.1+, AI query/Preview flags, optional smart-batching flag, India region caveat and pricing are documented from official sources.

### New delivery — Groot Academy
- Draft PR: https://github.com/satnamkhowal/grootacademy.com/pull/681
- Branch: news-factory/alloydb-ai-classify-extract-20261112-1608
- One original 2,067-word English developer guide plus JSON metadata and one original 1200×675 SVG workflow diagram.
- Local optimized PNG (128,776 bytes) and WebP (40,330 bytes) previews are present in the run workspace; only the SVG is committed.
- Official Google Cloud Tech video candidate EG9nayN3c88, published 26 July 2024, is background context only. Embed permission was not independently confirmed; fallback link only, no iframe, no download.
- Branch comparison: 1 ahead / 0 behind main; exactly three added files; GitHub PR is OPEN, DRAFT and mergeable=true. Combined status has no entries and no workflow run was returned for this branch; CI is UNVERIFIED.
- Independent editorial, technical and responsive QA remain PENDING. No production route, sitemap, canonical, redirect, live registry, merge, deployment or publication changed.

### Central coordination
- Existing checkpoint file updated append-only; no duplicate checkpoint file created.
- Central PR #19 remains the coordination vehicle. Its branch is diverged from main; no rebase, force-push or merge was attempted.

### Production ledger — this cycle only
| Stage | New count |
| --- | ---: |
| Research lanes | 4 |
| New verified unowned stories selected | 1 |
| New original English article drafts | 1 |
| Existing article status comments | 1 (Mango #147 NIC portal status) |
| New Draft PRs | 1 (Groot #681) |
| Original committed SVGs | 1 |
| Local optimized PNG/WebP derivatives | 2 |
| Verified YouTube candidates | 1 (background only) |
| Verified iframe embeds | 0 |
| Independent QA-ready increment | 0 |
| Live/published increment | 0 |
| Merges/deployments | 0 |

### Next actions
1. Independent editorial and technical QA of Groot #681; keep draft-only until reviewed.
2. Recheck NIC portal and application route before any closing-date claim; no official closing date is currently displayed.
3. Resolve the Node.js November bulletin/release-note CVE mapping before Mango #143 can pass security QA.
4. Recheck VSSC and NMMSS deadlines on 15–16 November.
5. Preserve current React/Node/security ownership; do not duplicate existing Forsk/Mango/Groot drafts.
