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
- 3 commits ahead / 0 behind main; GitHub reports OPEN / DRAFT / mergeable=true.
- 3 files: 1,806-word article, JSON research/asset metadata, original 1200×675 SVG.
- Metadata JSON parses; article/SVG/metadata read-back verified.
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

- Existing central PR #19 branch `ops/news-factory-cycle-20261109-2209` compared **125 commits ahead / 5 behind main**, status **diverged**, GitHub reports mergeable=false. This checkpoint is appended to the existing 11:17 file on that branch; no rebase, merge or force-push.
- Next: independent QA for Forsk #190; recheck React Summit tickets and workshop conditions before 17/20 Nov; monitor IIITG deadline 15 Nov and Google Student Researcher deadline 4 Dec; continue React RSC and Node.js security owner checks; do not publish or deploy without approval.
- No application was submitted, no video was downloaded, and no article was published live.
