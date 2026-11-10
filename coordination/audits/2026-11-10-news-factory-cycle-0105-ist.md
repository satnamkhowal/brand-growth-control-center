# News Factory research and draft-production checkpoint

Date: 10 November 2026 (Asia/Kolkata)  
Research/status check: 01:05 IST  
Scope: Mango Engineers, Groot Academy, Forsk Coding School and Jaipur Engineers. Other brands remain read-only because the central source-mapping queue does not verify their repository/catalogue identity for this content lane.

## Coordination baseline

- Central repository main observed at `31af61b9a796472b7eb13d6b254aa6d9dc2ecc34`.
- Reused the existing News Factory coordination PR #19 and its branch `ops/news-factory-cycle-20261109-2209`; this file is appended to that existing checkpoint PR. No new central branch or duplicate controller was created.
- Read the central README, current pending-task queue location, existing PR #19 and its 9 November checkpoint.
- Verified current brand repositories:
  - Mango Engineers: `satnamkhowal/mangoengineers.com`, main `8eeb57fdf05341aa0a5ec31846148a37b0be3ba6`. Read `AGENTS.md`, README, agent start guide, task board, work log and integration queue. No write: no distinct Mango-owned story was needed in this batch; current Mango PR #143 already owns Node.js readiness and other news drafts.
  - Groot Academy: `satnamkhowal/grootacademy.com`, main `a97dc07463a352ea924af3dea22af915a6f9bdb1`. Read `.agent/README.md`, master handoff, current state, backlog, decisions, migration status, dated migration handoff, current News Factory inventory, recent commits and open News Factory PRs.
  - Forsk Coding School: `satnamkhowal/forsk-coding-school`, main `a690ef725029e8c7f96b6148e9012f82a481bd6d`. Read README, `docs/ai-ops/MASTER_TASK_BOARD.md`, `docs/ai-ops/SESSION_HANDOFF.md`, News Factory inventory and open PR ownership. No write: current Forsk PRs already own React RSC, Google Student Researcher, scholarship, AWS and ISI stories.
  - Jaipur Engineers: `satnamkhowal/jaipurengineers.com`, main `677da49970ffd2871514fd1d08a7fc94b3f42004`. Read `MIGRATION-NOTES.md`; it says the `je2` application is canonical and legacy SEO/content folders must not be copied wholesale. No approved News Factory draft lane was identified, so no write was made.
- Clever Ape Academy, CadMate India, Groot Software and Forsk Technologies remain untouched because the central mapping queue still marks their repository/catalogue identity unresolved for this task.

## Research results

### 1. Student, developer and founder opportunities

**Startup Buildathon India 2026 — newly researched and drafted**

- Organiser landing page: https://startupbuildathon.com/
- Hack2skill event/application route: https://hack2skill.com/event/startupbuildathon2026
- Public organiser page does not display a publication date; the current status was checked on 10 November 2026.
- The page shows an application window of 23 October–13 November and an Apply Now control; deadline is **13 November 2026**.
- Participation is listed as free.
- Eligible applicant types listed: early-stage startups with a new product idea, aspiring entrepreneurs, solo founders and teams; no technical co-founder/coding background is required. The page does not state an age, citizenship, domicile or student-enrolment rule.
- Jaipur is listed among the 10 city buildathon locations for 20–21 November 2026. Shortlisted teams are expected to hear by 18 November. Regional showcases are listed for 23, 25 and 27 November; the grand finale is 2 December at Google Bengaluru.
- Top 10 teams are listed for USD 5,000 cash plus USD 5,000 Google AI/Cloud credits each, subject to terms and applicable taxes. This is not a guaranteed award for all applicants.
- The Hack2skill application route is linked from the organiser page, but the dynamic form was not independently inspected. Article explicitly tells applicants to recheck the live form and does not claim successful submission.
- This is a founder/buildathon opportunity, not a scholarship or paid internship.

**Existing opportunity watch items — no duplicate drafts**
- Google Student Researcher 2027: existing Forsk PR #146 remains the owner; prior official listing check shows India remote eligibility and 4 December 2026 deadline. Recheck before publication; no new copy created.
- NMMSS, AICTE and UGC scholarship articles remain in existing Groot/Forsk/Mango PRs. Their application deadlines are tracked separately; no old programme is described as newly opened.
- Google Research Scientist PhD Intern link previously in Mango PR #143 returned “Job not found” in the existing revalidation; it remains on hold and is not described as open.

### 2. React / frontend

- Official React blog and GitHub release history were checked.
- Latest listed stable tags remain 19.3.1, 19.2.9, 19.1.10 and 19.0.9, all dated 14 October 2026.
- No new qualifying stable release or security advisory was found in this cycle.
- Existing Forsk PR #145 owns the October React Server Components security catch-up; no duplicate article or graphic was created.

Sources:
- https://react.dev/blog
- https://github.com/react/react/releases

### 3. Node.js / backend

- The official Node.js notice, published 3 November 2026 and last updated 3 November, still schedules security releases for 26.x, 24.x and 22.x on or shortly after 11 November.
- Highest severity is HIGH in each line.
- As of this 10 November check, the advance notice still does not publish CVE IDs, affected patch ranges or patched versions. It remains a pre-alert, not a completed patch release.
- Existing Mango PR #143 owns the Node.js readiness draft. No duplicate guide was written.

Source: https://nodejs.org/en/blog/vulnerability/november-2026-security-releases

### 4. AI / cloud / developer infrastructure

**Google TPU 8tx and TPU 8i Max**

- Google Cloud Blog and Google Blog both published the announcement on **9 November 2026**.
- TPU 8tx is positioned for confidential inference; Google says it uses TPU 8t silicon with custom AMD CPU hosts and hardware-level protection, and claims up to 2× lower latency than TPU 8t with near-zero performance penalty.
- TPU 8i Max combines two TPU 8i chips in one package; Google lists double compute, SRAM and HBM bandwidth compared with TPU 8i.
- These are system configurations for different workload bottlenecks, not interchangeable general-purpose chips.
- The announcement does not state public SKU pricing, an India launch date, India region/zone availability or a customer availability schedule. The draft does not infer these.
- Existing Groot PR #580 (Cloud Pathways GA) and #582 (TPU Sync model-state layer) were checked. The new article covers the distinct 8tx/8i Max hardware configurations and does not duplicate either guide.

Sources:
- https://cloud.google.com/blog/topics/ai-infrastructure/tpu-8tx-and-tpu-8i-max
- https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/

## New production this cycle

### Groot Academy — two original English drafts

- Repository: `satnamkhowal/grootacademy.com`
- Base main: `a97dc07463a352ea924af3dea22af915a6f9bdb1`
- Branch: `content/news-factory-tpu-8tx-buildathon-20261110`
- Draft PR: https://github.com/satnamkhowal/grootacademy.com/pull/586
- PR is open, draft, 9 commits ahead / 0 behind main, and GitHub currently reports it mergeable.
- Files:
  - `docs/news-factory/drafts/startup-buildathon-india-2026-jaipur.md`
  - `docs/news-factory/media/startup-buildathon-india-2026-jaipur.svg`
  - `docs/news-factory/drafts/startup-buildathon-india-2026-jaipur.metadata.json`
  - `docs/news-factory/drafts/google-tpu-8tx-vs-tpu-8i-max-2026.md`
  - `docs/news-factory/media/google-tpu-8tx-vs-tpu-8i-max-20261110.svg`
  - `docs/news-factory/drafts/google-tpu-8tx-vs-tpu-8i-max-2026.metadata.json`
- Article word counts from GitHub read-back: 1,481 and 1,928.
- Both metadata JSON sidecars parsed successfully after GitHub read-back.

### Original graphics and video

- Two self-authored 1200×675 SVG diagrams. No external graphics, logos, photos or videos were downloaded.
- Buildathon graphic local path: `/mnt/data/news-factory/2026-11-10/media/startup-buildathon-india-2026-jaipur.svg`.
- TPU comparison graphic local path: `/mnt/data/news-factory/2026-11-10/media/google-tpu-8tx-vs-tpu-8i-max-20261110.svg`.
- Both SVGs passed XML parsing, 1200×675 rendering and visual inspection. Metadata records source, original-artwork permission, attribution, local path, alt text and dimensions.
- One official Google Cloud video was verified: ID `3Qw_CZkiQQg`, “Google TPU 8t and TPU 8i: Purpose-built for the Agentic Era”, channel Google Cloud, published 22 April 2026. It is included only as background because it predates and does not cover the 9 November 8tx/8i Max announcement.
- TPU article contains responsive iframe markup using `youtube-nocookie`, a descriptive title, lazy loading, fullscreen support and a fallback watch link. The channel's embed-permission setting and browser playback were not independently confirmed.
- No verified story-specific Buildathon video was found; no iframe was added for that article.

## QA, release gate and limitations

- GitHub read-back confirmed all six PR #586 files.
- PR changed-file list contains exactly the six intended draft/media/provenance files; no shared course, PHP, migration, sitemap, schema or production route files changed.
- Branch comparison: 6 commits ahead, 0 behind main; GitHub reports mergeable.
- SVG XML/dimensions, local render, metadata JSON parsing and article word-count checks passed.
- Combined GitHub commit status returned no status checks; PR workflow-run query returned no runs.
- Independent editorial/technical QA, browser rendering and YouTube embed playback remain **PENDING**. PR #586 is **drafted, not QA-ready**.
- No merge, deployment, publication, indexing or live-site claim is made.

## Cumulative News Factory ledger

Previous carried-forward ledger: 65 researched, 55 drafted, 55 original graphics, 33 independent QA-ready, 0 live.

This cycle adds two distinct researched stories, two article drafts and two original graphics:

| State | Cumulative |
|---|---:|
| Researched | 67 |
| Drafted | 57 |
| Original graphics | 57 |
| Independent QA-ready | 33 |
| Live / published | 0 |

## Next actions

1. Independent editorial and technical QA of PR #586; check the Buildathon deadline/form route and full organiser terms before publication.
2. Recheck the 13 November Buildathon application status before the deadline; do not imply a student-only eligibility rule.
3. Recheck Node.js 26.x/24.x/22.x patched versions and CVEs when the announced 11 November security release is published.
4. Verify official TPU 8tx/8i Max customer access, India availability and pricing only when Google publishes those details.
5. Preserve existing PR ownership. Do not merge, deploy or publish without independent QA and owner approval.


## Additional official opportunity status recheck — 10 November 2026, 01:20 IST

- Google Careers still lists **Student Researcher, 2027** with India as a remote-eligible location and asks applicants to complete the application before **4 December 2026**. Rolling review is stated. Minimum qualifications include current Bachelor's, Master's or PhD enrolment in a listed subject area and experience in a relevant computer-science area. The public listing does not state compensation or a fixed project duration. Existing Forsk PR #146 remains the single owner; no duplicate draft was created.  
  Source: https://www.google.com/about/careers/applications/jobs/results/125423735539671750
- The current NSP 2026–27 All-Scholarships listing still shows NMMSS student applications through **15 November 2026**; AICTE Swanath, AICTE Pragati, UGC National Scholarship for Post Graduate Studies and ISI stipend applications through **30 November 2026**. The NSP footer still says last update June 2026, so the live form and scheme guideline must be checked again before student submission. Existing Groot/Forsk/Mango drafts remain the owners; no duplicate scholarship guide was written.  
  Source: https://scholarships.gov.in/All-Scholarships
- NSP's current student-announcements page says PM YASASVI Top Class Education in Schools for OBC/EBC/DNT students is open for fresh applications, but explicitly says students from **Rajasthan, Keralam and Karnataka must wait**. The announcement does not state a revised Rajasthan opening date. No Rajasthan-facing application article was created; monitor the official announcement rather than implying local eligibility.  
  Source: https://scholarships.gov.in/student-announcements
- These are status rechecks of existing programmes, not newly announced opportunities; cumulative story counts remain unchanged.


## Frontend/backend release list recheck — 10 November 2026

- React's official blog's latest stable release announcement remains **React 19.3**, published 9 September 2026; the official versions page labels 19.3 as the latest version. No newer stable React announcement was found in this cycle. The earlier React Server Components security work remains owned by Forsk PR #145; no duplicate was created.  
  Sources: https://react.dev/blog and https://react.dev/versions
- Node.js official blog currently lists **Node.js 26.13.0 (LTS)** and **24.22.2 (LTS)** dated 28 October 2026; Node.js 27.0.0-alpha.0.0.0 is a prerelease dated 29 October and is not treated as a stable upgrade. The 3 November security advance notice still schedules releases for 26.x, 24.x and 22.x on or shortly after 11 November, with HIGH as the highest severity in each line. No patched security versions/CVE ranges are listed in the advance notice as of this check. Existing Mango PR #143 remains the Node.js readiness owner.  
  Sources: https://nodejs.org/en/blog and https://nodejs.org/en/blog/vulnerability/november-2026-security-releases


## 10 November 2026 — 02:09 IST research and draft-production cycle

### Repository and queue review
- Re-read the central README and the current open News Factory PR #19. The central repository remains coordination-only; brand implementation belongs in the source repository.
- Re-read Mango Engineers AGENTS.md, docs/agent-start-here.md, docs/task-board.csv, docs/work-log.md and docs/integration-queue.md. No existing task-board owner or shared integration item was reassigned. Mango remains read-only in this cycle because its current news and Node.js topics already have owners.
- Verified repository identities and permissions for Mango Engineers (satnamkhowal/mangoengineers.com), Groot Academy (satnamkhowal/grootacademy.com), Forsk Coding School (satnamkhowal/forsk-coding-school) and Jaipur Engineers (satnamkhowal/jaipurengineers.com). No guessed paths or live-site writes were made.
- Forsk has no root AGENTS.md or README.md; the existing News Factory draft/media directory and prior draft PR conventions were inspected. docs/IMAGE-PRODUCTION-WORKFLOW.md was read; this work adds an editorial draft graphic only and does not claim website integration.
- Current open News Factory PRs and branch names were searched across the four brand repositories. No existing Copilot code-review API management story or duplicate media path was found. Existing PRs #145–#151 remain untouched.
- Central PR #19 branch is 13 commits ahead and 0 behind current main; the existing checkpoint file is being appended rather than creating a parallel coordination branch.

### 1. Official programs, internships and scholarships
- No newly opened, fully verified India-eligible student/developer programme with a fresh application window was found in this cycle.
- Google Student Researcher 2027 remains listed for India remote applicants with a 4 December 2026 application deadline and rolling review. Existing Forsk PR #146 remains the single draft owner; no duplicate was created. Source: https://www.google.com/about/careers/applications/jobs/results/125423735539671750
- NSP 2026–27 still lists NMMSS through 15 November and AICTE Swanath/Pragati, UGC PG Studies and ISI stipend applications through 30 November. NSP's footer still reports June 2026 as its last update; check each live form and scheme guideline before advising submission. Existing draft owners remain unchanged. Source: https://scholarships.gov.in/All-Scholarships
- COEP Technological University's scholarship page lists an ONGC Merit Scholarship 2026–27 notice dated 2 November 2026. The linked PDF timed out during retrieval, so eligibility, award value, deadline, fee and live application status could not be verified. It is a research hold, not a new open-opportunity article. Source: https://www.coeptech.ac.in/student-corner/student-services/scholarship/scholarship-notifications/
- The IET India Scholarship Award 2026 page confirms applications closed on 5 July 2026; its current page invites visitors to sign up for the next edition. It is not a newly open opportunity. Source: https://scholarships.theietevents.com/

### 2. React / frontend
- React's official blog still identifies React 19.3, published 9 September 2026, as the latest stable announcement. No new stable release or security update was found in this cycle. Existing Forsk PR #145 remains the owner; no duplicate was created.
- Source: https://react.dev/blog

### 3. Node.js / backend
- The Node.js official blog lists 26.13.0 LTS and 24.22.2 LTS (28 October 2026); 27.0.0-alpha.0.0.0 (29 October) is a prerelease, not a stable production upgrade.
- The official 3 November advance notice still schedules security releases for 26.x, 24.x and 22.x on or shortly after 11 November, with HIGH as the highest severity in each line. It still provides no patched versions or CVE ranges. Existing Mango PR #143 remains the readiness owner.
- Sources: https://nodejs.org/en/blog and https://nodejs.org/en/blog/vulnerability/november-2026-security-releases

### 4. AI / cloud / developer news — new verified item
- GitHub published “Copilot code review: API management and review overview updates” on 6 November 2026.
- Selected code-review settings can now be managed through REST and GraphQL at enterprise, organization and repository scope. Copilot attribution and review-effort metadata are available; comments can report skills, MCP servers and custom instructions identified as sources.
- Important authentication boundary: enterprise and organization settings endpoints, including the organization runner endpoint, do not support GitHub Apps or fine-grained PATs. Repository settings endpoints support GitHub Apps and fine-grained PATs with Administration: read / Administration: write; classic PATs require repository administrator access.
- GitHub lists Copilot Pro, Pro+, Max, Business and Enterprise. The announcement states no separate API fee; AI credits and Actions minutes may still be consumed. Maximum review effort, billing and approval settings remain outside the documented settings API.
- Sources: https://github.blog/changelog/2026-11-06-copilot-code-review-api-management-and-review-overview-updates/ and https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/configure-code-review

### New Forsk Coding School delivery
- Repository: satnamkhowal/forsk-coding-school
- Base main: a690ef725029e8c7f96b6148e9012f82a481bd6d
- Branch: content/news-factory-copilot-code-review-api-20261110
- Draft PR: https://github.com/satnamkhowal/forsk-coding-school/pull/152
- Article: docs/news-factory/drafts/github-copilot-code-review-api-management-nov-2026.md (about 1,980 words).
- Original graphic: docs/news-factory/media/github-copilot-code-review-api-control-layers-20261110.svg (1200×675).
- Provenance: docs/news-factory/drafts/github-copilot-code-review-api-management-nov-2026.metadata.json.
- No official or reputable original YouTube video covering the 6 November API-management changes was verified; no iframe was included.
- Branch comparison: 3 commits ahead, 0 behind main; exactly three intended files added. GitHub read-back confirmed article, SVG and metadata sidecar.
- Local checks: SVG XML parse and 1200×675 raster render passed; graphic visually inspected; metadata JSON parsed; article word count checked. Independent editorial/technical QA and browser rendering remain PENDING. PR #152 is draft-only and unmerged.

### Cycle ledger
Previous carried-forward ledger: 67 researched, 57 drafted, 57 original graphics, 33 independent QA-ready, 0 live.

This cycle adds one verified developer-news item, one article draft and one original graphic:

| State | Cumulative |
|---|---:|
| Researched | 68 |
| Drafted | 58 |
| Original graphics | 58 |
| Independent QA-ready | 33 |
| Live / published | 0 |

### Next actions
1. Independent technical/editorial QA of Forsk PR #152, including API-scope/authentication wording and the SVG at browser breakpoints.
2. Recheck the ONGC scholarship attachment from COEP's official notice; do not draft until deadline, award and eligibility are verifiable.
3. Recheck Node.js 26.x/24.x/22.x patched versions and CVEs when the announced 11 November security release is published.
4. Recheck NMMSS before its 15 November deadline and Google Student Researcher before 4 December.
5. Preserve current owners and draft-only release gates. No merge, deployment, publication or indexing claim is made.


## 10 November 2026 — 03:11 IST research and draft-production cycle

### Repository and ownership review
- Re-read the central README and open central News Factory PR #19. The central repository remains coordination-only; brand implementation belongs in each verified brand repository. Central main is `31af61b9a796472b7eb13d6b254aa6d9dc2ecc34`; the existing checkpoint branch was 14 commits ahead / 0 behind before this append. Existing central PRs #17 and #18 remain untouched.
- Verified current repository identities and main heads: Mango Engineers `8eeb57fdf05341aa0a5ec31846148a37b0be3ba6`; Groot Academy `a97dc07463a352ea924af3dea22af915a6f9bdb1`; Forsk Coding School `a690ef725029e8c7f96b6148e9012f82a481bd6d`; Jaipur Engineers `677da49970ffd2871514fd1d08a7fc94b3f42004`.
- Mango required instructions were read: `AGENTS.md`, `docs/agent-start-here.md`, `docs/task-board.csv`, `docs/work-log.md` and `docs/integration-queue.md`. Existing Mango PR #143 owns the Node.js readiness and current News Factory batch; its Google Research Scientist PhD Intern listing is on hold because the official URL now returns “Job not found”. No Mango write was made.
- Forsk has no root `README.md` or `AGENTS.md`; its existing News Factory draft/media lane, current PR #152, and `docs/IMAGE-PRODUCTION-WORKFLOW.md` were inspected. Existing PR #152 covers GitHub Copilot code-review API management, not the distinct Google Agent Distraction study. No duplicate article/media path or topic was found.
- Groot's current main and active PR inventory were checked. Existing PR #586 owns Startup Buildathon Jaipur and Google TPU 8tx/8i Max; #580/#582/#583/#578/#577 remain separate owners. No Groot write was made.
- Jaipur Engineers current main and `MIGRATION-NOTES.md` were checked. The current application history is canonical in the renamed `jaipurengineers.com` repository; active PR #43 owns readability changes and PR #41 owns batch-planning. No News Factory article lane was changed.
- Central README continues to mark Clever Ape Academy, CadMate India, Groot Software and Forsk Technologies repository/catalogue mappings unresolved. No writes were made to those brands.

### 1. Student, internship and scholarship research
- Google Careers still shows **Student Researcher, 2027** as India remote eligible, with an Apply control and a deadline of **4 December 2026**; review is rolling. Minimum qualifications include current enrolment in a Bachelor's, Master's or PhD programme in the listed relevant fields and experience in a computer-science area. The accessible listing does not state an opening date, fixed duration or stipend amount. Existing Forsk PR #146 remains the single draft owner.
- NSP 2026–27 still lists NMMSS student applications through **15 November 2026**, and AICTE Swanath/Pragati and UGC National Scholarship for Post Graduate Studies through **30 November 2026**. The NSP listing footer still says last update June 2026, so applicants should recheck the individual live form and current scheme circular before submission. Existing drafts remain with their current owners; no duplicate opportunity article was created.
- No new fully verified India-eligible student/developer programme with a fresh application window was added in this cycle.

Sources:
- https://www.google.com/about/careers/applications/jobs/results/125423735539671750
- https://scholarships.gov.in/All-Scholarships

### 2. React / frontend
- React's official blog still lists **React 19.3**, published 9 September 2026, as the latest stable announcement. No newer stable release or fresh security advisory was found. Existing Forsk PR #145 remains the React Server Components security owner; no duplicate was created.
- Source: https://react.dev/blog

### 3. Node.js / backend
- Node.js's official advance notice was published **3 November 2026** and still schedules security releases for the 26.x, 24.x and 22.x lines on or shortly after **11 November 2026**. Highest severity is HIGH in each line.
- As of this check, the notice still lists no patched version numbers, CVE IDs or affected patch ranges. Existing Mango PR #143 remains the single readiness owner; no final patch guide was written before the release.
- Sources: https://nodejs.org/en/blog/vulnerability/november-2026-security-releases and https://nodejs.org/en/blog

### 4. AI / cloud / developer news — new verified item
- Google Developers Blog published **“Agent Distraction”** on **6 November 2026**. The article does not state a separate event date.
- Google reports that 13% of file-reading sessions were exposed to inline `TODO(bug/...)` / `FIXME(bug/...)` references; 6% of those encounters led to a secondary action, and 83% of those actions were unprompted. Google categorises 41% of the unprompted detours as closed dead ends and 57% as scope creep involving open tickets. It reports 70% more steps, 77% more tokens and 105% more wait time per unprompted-detour session.
- The article attributes the findings to Google's own agent-session analysis and explicitly warns that they are not universal benchmarks. The research explains why stale comments should be checked for ticket status and task relevance before an agent expands scope.
- Source: https://developers.googleblog.com/agent-distraction/

### New Forsk Coding School delivery
- Repository: `satnamkhowal/forsk-coding-school`
- Base main: `a690ef725029e8c7f96b6148e9012f82a481bd6d`
- Branch: `content/news-factory-agent-distraction-20261110`
- Draft PR: https://github.com/satnamkhowal/forsk-coding-school/pull/153
- Article: `docs/news-factory/drafts/google-agent-distraction-coding-agent-repository-hygiene.md` (2,122 words).
- Original graphic: `docs/news-factory/media/google-agent-distraction-todo-workflow-20261110.svg` (1200×675).
- Provenance sidecar: `docs/news-factory/drafts/google-agent-distraction-coding-agent-repository-hygiene.metadata.json`.
- The graphic is an original self-authored SVG. Source, permission, attribution, local path, alt text and dimensions are recorded; no third-party image or logo was downloaded.
- No story-specific official/reputable YouTube video was verified; no video ID or iframe was added.
- Branch comparison: 3 commits ahead / 0 behind main; exactly three intended files added. GitHub read-back passed for the article, SVG and metadata.
- Local checks: article word count checked; metadata JSON parsed; SVG XML parsed and rendered at 1200×675; graphic visually inspected. Official source/date and quantitative-claim attribution checks passed.
- Independent editorial/technical QA and browser-responsive rendering remain PENDING. GitHub returned no combined status checks and no PR workflow runs for the latest draft commit. PR #153 is open, draft and unmerged.
- No public route, sitemap, schema, redirect or production content changed. No merge, deployment, publication or indexing claim is made.

### Cycle ledger
Previous carried-forward ledger: 68 researched, 58 drafted, 58 original graphics, 33 independent QA-ready, 0 live.

This cycle adds one verified research item, one article draft and one original graphic:

| State | Cumulative |
| --- | ---: |
| Researched | 70 |
| Drafted | 59 |
| Original graphics | 59 |
| Independent QA-ready | 33 |
| Live / published | 0 |

### Next actions
1. Independent editorial/technical QA and browser-responsive review for Forsk PR #153; do not merge before review.
2. Recheck the Node.js 26.x/24.x/22.x security release on or after 11 November for actual versions, CVEs and affected ranges before updating Mango PR #143.
3. Recheck NMMSS before 15 November and AICTE/UGC scholarship forms before 30 November.
4. Recheck Google Student Researcher 2027 before 4 December.
5. Preserve all existing brand owners and draft-only release gates.


### Additional scholarship status conflict — 10 November 2026
- The current NSP PM-USP Special Scholarship Scheme for Jammu & Kashmir and Ladakh card displays a 22 October 2026 opening and a 30 November student deadline. However, the NSP announcement describes only renewal applications and gives 31 October as the student deadline; an institution notice attributed to the SSSJKL/AICTE cell also gives 31 October 2026 for fresh Phase II student registration and 15 November for institution verification.
- These official/portal surfaces conflict. As of this check, fresh 2026–27 registration is **not safely confirmable as open**. Do not market the scheme as a newly open scholarship or direct students to a fresh application until AICTE/NSP confirms the current status. Existing 2026–27 scheme eligibility/benefit information must be checked against the current AICTE guideline before drafting.
- Sources: https://scholarships.gov.in/All-Scholarships ; https://scholarships.gov.in/ViewMoreAnnouncement ; https://adgips.ac.in/2026/10/28/
- This adds one researched status-hold item, not a new article, graphic or QA-ready item. Cumulative ledger is now 70 researched, 59 drafted, 59 original graphics, 33 independent QA-ready, 0 live.


## 10 November 2026 — 04:08 IST follow-up

### New official opportunity — NIC Digital India Internship Winter 2026

- Official NIC Training Division portal: https://dii.nic.in/
- The official landing page lists **Digital India Internship — Winter 2026**, says registration starts **2 November 2026**, and shows the internship period **1 December 2026 to 31 January 2027**. The page explicitly states **offline only**.
- The portal page's last-updated date is **10 November 2026**; it does not display a separate notice publication date.
- The visible registration form includes a currently pursued degree selector and warns applicants not to register if their degree is not listed.
- The accessible official landing-page text does not state the application deadline, exact degree/branch/year eligibility, stipend, application fee, seat count or posting centres. The official Winter 2026 guideline linked from the portal timed out in the research client. No such details are guessed or copied from third-party summaries.
- Official contact displayed on the portal: internship-nic@nic.in; +91-11-24305869.
- Jaipur/Rajasthan applicants must verify the actual offline reporting location; the official page does not confirm a Jaipur centre or remote option.
- New Mango Engineers delivery: [PR #147](https://github.com/satnamkhowal/mangoengineers.com/pull/147), an original approximately 1,800-word English guide, one self-authored 1200×675 SVG and a provenance sidecar. Article/graphic/metadata are documentation-only; no live route or production content changed.
- Local PNG preview: /mnt/data/news-factory/2026-11-10-nic-internship/nic-digital-india-internship-winter-2026-checklist.png.
- No story-specific original YouTube video was verified; no ID or iframe was added.
- Branch content/news-factory-nic-internship-20261110 is 6 commits ahead / 0 behind Mango main. Five intended files are present (article, SVG, JSON sidecar, task-board row, work-log entry). GitHub read-back passed for the three content/media files.
- Mango PR #147 remains open and draft; PR creation returned mergeable=false. PHP Architecture Check run 42715210065 completed failure with zero steps; job logs were unavailable (BlobNotFound). No code-level PHP failure or pass is inferred. Independent QA remains pending.
- No merge, deployment or publication.

### Node.js / backend release recheck — new research candidate

- Official Node.js blog index lists **Notable V8 changes from Node.js 26 to 27 (Alpha)**, published **5 November 2026**. The separate Node.js 27.0.0-alpha.0.0.0 tag was released **29 October 2026**; the blog publication date and release-tag date are distinct.
- Node.js 27 Alpha upgrades V8 from 14.6 (Node 26) to 15.6. The official technical post covers Math.sumPrecise, Intl.Locale.prototype.variants, iterator methods, PowerSort, changes to Math.random, Date/time-zone offsets, serialization compatibility, heap limits and memory behaviour.
- Node.js warns that Alpha/Current may receive breaking V8 changes; this is a prerelease, not an LTS recommendation for production.
- Latest stable/LTS versions shown on the Node.js blog index remain **26.13.0 LTS** and **24.22.2 LTS**, both dated **28 October 2026**; 27.0.0-alpha.0.0.0 is prerelease. No newer stable patch was found in this check.
- The 3 November security advance notice still schedules 26.x/24.x/22.x security releases on or shortly after **11 November 2026**, with highest severity HIGH in each line. No CVEs or patched versions are in the advance notice yet. Existing Mango PR #143 remains the single owner for that security-readiness article; no duplicate was created.
- V8 Alpha research is logged as a research candidate only; no separate article or graphic was produced.
- Sources: https://nodejs.org/en/blog/ ; https://nodejs.org/en/blog/announcements/notable-v8-changes-from-node-js-26-to-27-alpha ; https://nodejs.org/en/blog/vulnerability/november-2026-security-releases

### React / frontend version correction

- React's official feature blog still has **React 19.3** (9 September 2026) as its latest feature-release announcement.
- The official React GitHub release list shows the latest patch tags dated **14 October 2026**: **19.3.1**, **19.2.9**, **19.1.10** and **19.0.9**. Therefore, “19.3.0 is the latest version” would be incomplete; distinguish the 19.3 feature release from current patch tags.
- No newer stable release or fresh November security advisory was found. Existing Forsk PR #145 owns the 14 October RSC security advisories and patched-version guide; no duplicate article was created.
- Sources: https://react.dev/blog ; https://github.com/react/react/releases

### Student programme and scholarship status recheck

- Google Careers still shows **Student Researcher, 2027** as India remote eligible, with an Apply control and **4 December 2026** deadline; applications are reviewed on a rolling basis. The listing requires current enrolment in a Bachelor's, Master's or PhD degree in one of the listed fields and experience in a computer-science area. No stipend amount or fixed duration is disclosed on the listing. Existing Forsk PR #146 remains the single article owner.
- NSP 2026–27 listing currently shows NMMSS student applications through **15 November 2026** and AICTE Swanath/Pragati plus UGC National Scholarship for Post Graduate Studies through **30 November 2026**. The NSP page footer still says last updated June 2026; students should verify each live form and current guideline before submission.
- PM-USP Special Scholarship Scheme for J&K/Ladakh remains a status conflict: the All-Scholarships card shows a 22 October opening and 30 November deadline, while the student announcement says renewal only and a 31 October student deadline. Fresh applications are not safely confirmable as open.
- PM YASASVI Top Class Education in Schools fresh applications are listed as open, but the NSP announcement says Rajasthan, Keralam and Karnataka students must wait; no revised Rajasthan opening date is stated.
- Sources: https://www.google.com/about/careers/applications/jobs/results/125423735539671750 ; https://scholarships.gov.in/All-Scholarships ; https://scholarships.gov.in/Students ; https://scholarships.gov.in/

### AI / cloud / developer news

- Google Cloud's **TPU 8tx and TPU 8i Max** announcement is dated **9 November 2026** and remains owned by Groot Academy PR #586. No duplicate article was created. The official post distinguishes TPU 8tx confidential inference from TPU 8i Max's larger context/memory configuration; no India region, SKU pricing or customer-access date is inferred.
- Other already-owned AI/cloud stories in Groot PRs #580/#582 and Mango PR #143 were not duplicated.
- Source: https://cloud.google.com/blog/topics/ai-infrastructure/tpu-8tx-and-tpu-8i-max

### Repository/queue coordination and QA

- Mango: new [PR #147](https://github.com/satnamkhowal/mangoengineers.com/pull/147); existing PR #143 remains owner for its current five-story batch.
- Forsk: existing PR #145 (React RSC security), #146 (Google Student Researcher), #152 (Copilot code-review API) and #153 (Google Agent Distraction) remain separate owners; no Forsk write in this cycle.
- Groot: PR #586 (Startup Buildathon + TPU 8tx/8i Max) and #580/#582/#583/#577/#578 remain owners; no Groot write in this cycle.
- Jaipur Engineers: current repository was reviewed; central README/queue still provides no approved non-public News Factory article lane. Keep read-only; existing readability PR #43 and batch PR #41 are untouched.
- Clever Ape Academy, CadMate India, Groot Software and Forsk Technologies remain unverified for this News Factory source/repository mapping; no writes.
- No merge, deployment, live verification, public posting or publication.

### Cycle ledger

Previous carried-forward ledger: 70 researched, 59 drafted, 59 original graphics, 33 independent QA-ready, 0 live.

This cycle adds two distinct research items (NIC Winter 2026 internship and Node.js 27 Alpha V8 changes), one original Mango article draft and one original graphic. Google/NSP/React/Node security/TPU items are status rechecks or existing owners, not duplicate story counts.

| State | Cumulative |
| --- | ---: |
| Researched | 72 |
| Drafted | 60 |
| Original graphics | 60 |
| Independent QA-ready | 33 |
| Live / published | 0 |

### Next actions

1. Retrieve the official NIC Winter 2026 guideline and verify closing date, exact eligibility, posting centres, stipend and any fee before updating or publishing PR #147.
2. Investigate Mango PHP Architecture Check run 42715210065: it failed with zero steps and logs unavailable; do not infer source failure or success.
3. Independently QA the NIC article and SVG; keep PR #147 draft/unmerged.
4. Recheck Node.js 26.x/24.x/22.x security releases on or after 11 November for actual versions and CVEs before updating Mango PR #143.
5. Recheck NMMSS before 15 November, AICTE/UGC applications before 30 November and Google Student Researcher before 4 December.
6. Preserve current brand owners and all merge/deploy/publish approval gates.


### Mango PR #147 final branch/CI reconciliation — 10 November 2026, 04:22 IST

- After task-board and work-log validation follow-ups, the Mango branch is **8 commits ahead / 0 behind main**, with exactly five changed paths. The earlier 6-commit figure in the 04:08 entry described the branch before those two follow-up commits.
- The PHP Architecture Check run 42715210065 has one failed job with an empty steps list; the log endpoint returned BlobNotFound. CI is therefore unverified/blocked, not a code-level PHP failure or pass.
- PR #147 remains open and draft. No merge, deployment or publication.


### Latest Mango branch-head check — 10 November 2026, 04:24 IST

- Current Mango branch head is 478ebcd000bfbeec34844bf1be02063b4a1395bc9. No workflow run was returned for this latest head; the combined-status endpoint returned 404/no status record.
- The earlier PHP Architecture Check run 42715210065 remains a failed zero-step job with unavailable logs. Neither result provides a source-level PHP test verdict.
- PR #147 remains a draft. Independent QA and the missing official guideline details remain blockers.


### 10 November 2026 — 04:36 IST News Factory cycle

#### New verified AI / cloud item and delivery
- Google Cloud's BigQuery release notes dated **9 November 2026** mark the maximum number of concurrently executed pipeline tasks as **GA** and three Zstandard SQL functions (`ZSTD_COMPRESS`, `ZSTD_DECOMPRESS_TO_BYTES`, `ZSTD_DECOMPRESS_TO_STRING`) as **Preview**.
- Official scheduling docs specify a maximum-concurrent-actions field from **1 to 5,000**; excess ready actions are queued. The docs also warn that if a scheduled run is still running at the next scheduled start, that next run is skipped and marked with an error. This is a control, not a performance/cost guarantee.
- Zstd compression level defaults to 3 and accepts -5 to 22; decompression default and maximum size_limit is 128 MiB. Google says a lower limit can reduce memory risk. Preview functions remain subject to Pre-GA terms.
- Separate related item: Google Cloud's Data Cloud roundup was published **5 November** and covers updates from **2–6 November**; it reports BigQuery data-agent observability GA. This is not the release-note date of the 9 November pipeline/Zstd changes.
- Groot Academy [PR #592](https://github.com/satnamkhowal/grootacademy.com/pull/592) adds one original 1,958-word English article, one original self-authored 1200×675 SVG, and one provenance JSON sidecar. Branch `content/news-factory-bigquery-pipeline-concurrency-zstd-20261110` is **4 commits ahead / 0 behind main**, 3 changed files, PR open/draft/mergeable.
- Local SVG XML parsing, 1200×675 PNG rendering and visual inspection passed; metadata JSON parsed; GitHub read-back passed for all three files. Independent editorial/technical QA and responsive browser review remain pending. No CI check-runs were returned.
- No story-specific official/reputable original YouTube video was verified; no video ID or iframe was invented. No third-party graphic was downloaded; the diagram is self-authored. No public route, sitemap, schema, redirect, PHP template or production content changed.

#### Opportunities and programme revalidation
- Google Careers currently displays **Student Researcher, 2027** with Apply, remote location India, and a **4 December 2026** deadline with rolling review. Current enrolment in Bachelor's/Master's/PhD in the listed disciplines and experience in a CS area are minimum qualifications. No stipend amount or fixed duration is published. Existing Forsk PR #146 remains owner; no duplicate article.
- NSP 2026–27 still lists NMMSS student applications to **15 November 2026** and AICTE Swanath/Pragati plus UGC PG Studies to **30 November 2026**. NSP page footer says last updated June 2026; check each current form and guideline before students rely on the deadline.
- AICTE National Internship Portal's live-opening search rendered **0 postings** at check time. Edunet and Cisco partner pages say the next cohort opens shortly; AICTE Research page shows 0 internships found; Indian Army dashboard totals show 0 posted/ongoing/completed while data panels load. These programme pages are not evidence of an active individual application. No new internship was described as open and no article was drafted.
- PM-USP J&K/Ladakh fresh-application status remains conflicting in NSP notices; do not advertise fresh applications as open without a new official clarification.

#### React / Node status
- React official GitHub releases still show patch tags **19.3.1, 19.2.9, 19.1.10 and 19.0.9**, all dated **14 October 2026**; React 19.3.0 feature release is dated **9 September**. No newer stable tag or fresh November security advisory was found. Existing Forsk PR #145 remains owner.
- Node.js official release index still lists **26.13.0 LTS** and **24.22.2 LTS** dated **28 October**, **27.0.0-alpha.0.0.0** dated **29 October** (prerelease), and **22.23.4 LTS** dated **21 October**. The 3 November advance notice schedules 26.x/24.x/22.x security releases on or shortly after **11 November**, highest severity HIGH; no patched versions or CVE ranges are in the notice yet. Existing Mango PR #143 remains owner; no duplicate draft.

#### Repository and queue coordination
- Reviewed current accessible central coordination branch and open PR #19; appended this section to the existing checkpoint rather than creating a new coordinator chat or worker lane.
- Groot current News Factory draft/media inventory contains no matching BigQuery pipeline-concurrency/Zstd draft. Existing Groot PRs #578 (S3 Tables), #580 (Cloud Pathways/GKE), #582 (TPU Sync), #583 (ISI AI-STEP) and #586 (Buildathon + TPU 8tx/8i Max) were reviewed; paths and story scopes are distinct.
- Groot repo instruction note: `.agent/README.md` names `satnamkhowal/gta` as canonical, but that repository was not present in the accessible repository list. Existing News Factory draft files and open PRs are in `satnamkhowal/grootacademy.com`; this established draft-only lane was used for PR #592. Resolve the canonical-repository pointer before any production-route work.
- Mango PR #143/#147 and Forsk PR #145/#146/#152/#153 remain existing owners; no duplicate write. Jaipur Engineers repository/root and docs inventory were inspected, but no approved non-public News Factory article lane was confirmed, so it remains read-only. Other brand repository mappings remain unverified and untouched.
- No merge, deployment, publication or indexing claim.

#### Cycle ledger
Previous carried-forward ledger at 04:24: **72 researched, 60 drafted, 60 original graphics, 33 independent QA-ready, 0 live**.

This cycle adds one distinct research item (BigQuery pipeline concurrency GA + Zstd Preview), one original draft and one original graphic. Opportunity, React and Node checks are status revalidations, not new stories.

| State | Cumulative |
| --- | ---: |
| Researched | 73 |
| Drafted | 61 |
| Original graphics | 61 |
| Independent QA-ready | 33 |
| Live / published | 0 |

#### Next actions
1. Independent editorial/technical QA and responsive browser review of Groot PR #592; keep draft/unmerged.
2. Recheck Node.js security releases on or after 11 November for actual patched versions and CVEs before updating Mango PR #143.
3. Recheck NMMSS before 15 November, AICTE/UGC schemes before 30 November, and Google Student Researcher before 4 December.
4. Recheck AICTE internship portal for actual individual postings; do not treat partner programme landing pages as active openings.
5. Resolve the Groot canonical repository pointer before any production-route work; preserve all existing brand ownership and merge/deploy/publish gates.


### Scholarship status detail addendum — 10 November 2026, 04:39 IST
- Current NSP All-Scholarships listing (AY 2026–27) shows NMMSS student applications to **15 November**; AICTE Swanath/Pragati (technical degree/diploma), UGC National Scholarship for Post Graduate Studies, ISI UG/PG stipend and PM YASASVI Top Class Education in College to **30 November**; PM YASASVI Top Class Education in Schools to **15 November**.
- The NSP Student Announcements page says PM YASASVI Top Class Schools fresh applications are currently accepted only for students outside **Rajasthan, Keralam and Karnataka**; students in those three states must wait. Do not promote it as open to Rajasthan students until NSP changes the notice.
- PM-USP J&K/Ladakh remains a separate conflict: the scheme card shows an open date of 22 October and 30 November deadline, but the student announcement says renewal applications only with a 31 October student deadline. Fresh applications are not confirmed.
- NSP pages still show “Last update on June 2026”; all deadlines are portal-listed dates, not proof that an individual student's form is valid or eligible. Verify scheme specifications, state/institute rules and the live application form before student action. These are revalidation details, not new story counts.


### News Factory cycle — 10 November 2026, 05:09 IST

#### Research summary

**1. Student, developer and community opportunities**
- Google Careers still lists **Student Researcher, 2027** as remote-eligible in India, with a **4 December 2026** deadline and rolling review. Minimum qualifications include current enrolment in a Bachelor's, Master's or PhD degree in the listed disciplines and experience in a CS area. The official listing does not publish a fixed stipend or project duration. Existing Forsk PR #146 remains the owner; no duplicate draft.
- NSP's AY 2026–27 portal page still says the portal opened from 1 June 2026 and shows a June 2026 last-update footer. This cycle did not confirm a fresh individual scheme deadline or form-state change; retain the previous portal-listed dates only as provisional and recheck each scheme's live form before student action.
- New event opportunity: the global DevFest 2026 season is listed for **1 October–31 December 2026**. Google for Developers says local events are independently run by GDG organizers and ticket prices vary by city. Local event pages do not expose separate publication dates; the new guide distinguishes event dates from the 10 November verification date.
- Current India event findings: Mangaluru 14 Nov (ticket control visible; price not stated); Bengaluru 21 Nov (KonfHub ticket link; price not confirmed); Bhopal 22 Nov (regular passes sold out, ₹399 regular pass, limited reserved-pass waitlist for working professionals/content creators); Kolkata 22 Nov (ticket control visible; price not stated); Dehradun 28 Nov (RSVP control visible, page showed 198 RSVPs, venue TBA); Bhubaneswar 28–29 Nov (two-day hackathon + DevFest, ticket control visible, price not stated); Coimbatore 12 Dec (early-bird student ₹399 / professional ₹599, current-year college ID for student pass, non-refundable, early-bird end 22 Nov 11:59 PM IST or 300 passes); Nagpur 12 Dec (listed ₹599 Business / ₹1,699 First Class; remaining inventory not confirmed); Pune 13 Dec (ticket control visible, price not stated). Surat 13 Dec is watch-only because the organizer says registration has not started.
- No upcoming citywide Jaipur DevFest 2026 listing surfaced in the official pages checked. The Jaipur DevFest result was the historical 27 December 2025 event; two Jaipur on-campus listings dated 3 November 2026 are already past and restricted to their respective campuses. This is not proof that no future Jaipur meetup will be announced.
- DevFest is a community conference, not a scholarship, paid internship or job guarantee. Local eligibility and ticket conditions control.

Primary event sources:
- https://developers.google.com/community/devfest
- https://gdg.community.dev/events/details/google-gdg-cloud-mangalore-presents-devfest-mangaluru-2026/
- https://gdg.community.dev/events/details/google-gdg-cloud-bengaluru-presents-devfest-2026/
- https://devfest.bhopal.dev/tickets
- https://gdg.community.dev/events/details/google-gdg-kolkata-presents-devfest-kolkata-2026/
- https://gdg.community.dev/events/details/google-gdg-dehradun-presents-devfest-dehradun-2026/
- https://gdg.community.dev/events/details/google-gdg-bhubaneswar-presents-gdg-devfest-2026-bhubaneswar/
- https://devfest26.gdgcbe.com/
- https://www.theticket9.com/book/devfest-coimbatore-2026
- https://gdg.community.dev/events/details/google-gdg-nagpur-presents-devfest-nagpur-2026/
- https://gdg.community.dev/events/details/google-gdg-pune-presents-devfest-pune-2026-build-secure-scale-agentic-ai-tokenization-amp-quantum/
- https://gdg.community.dev/events/details/google-gdg-surat-presents-gdg-devfest-surat-2026/

**2. React / frontend**
- React's official blog still lists **React 19.3** (9 September 2026) as its latest feature announcement; no newer November stable release or security post was found in this check. Existing Forsk PR #145 remains the owner; no duplicate article.
- Source: https://react.dev/blog

**3. Node.js / backend**
- Node.js official blog still lists **26.13.0 LTS** and **24.22.2 LTS** (28 October), and **27.0.0-alpha.0.0.0** (29 October, prerelease).
- The 3 November security notice still schedules 26.x, 24.x and 22.x security releases on or shortly after **11 November 2026**; highest severity is HIGH in each line. The notice still has no CVE IDs, affected patch ranges or patched versions. Existing Mango PR #143 remains owner; no duplicate article or graphic.
- Sources: https://nodejs.org/en/blog and https://nodejs.org/en/blog/vulnerability/november-2026-security-releases

**4. AI / cloud / developer news**
- GitHub Changelog's November page still shows the latest relevant entries on 6 November, including Copilot code-review API management and the impact dashboard. Existing Forsk PR #152 owns the code-review API story.
- Groot PR #592 already owns the 9 November BigQuery pipeline-concurrency GA / Zstandard SQL Preview article. No distinct new Google Cloud or AI announcement qualified in this cycle, so no duplicate cloud draft was created.
- Source: https://github.blog/changelog/month/11-2026/

#### New production — Forsk Coding School

- Repository: `satnamkhowal/forsk-coding-school`; main at start: `a690ef725029e8c7f96b6148e9012f82a481bd6d`.
- Reviewed Forsk `docs/ai-ops/MASTER_TASK_BOARD.md`, `SESSION_HANDOFF.md`, current News Factory drafts/media inventory, main branch, and open PR #152/#153 changed-file lists. No DevFest draft or branch existed; #152/#153 own different files.
- Created isolated branch `content/news-factory-devfest-india-20261110`.
- Draft PR [#154](https://github.com/satnamkhowal/forsk-coding-school/pull/154) is **open, draft and currently mergeable** after GitHub recomputed status; 5 changed files, 2 commits, 296 additions, 0 deletions. The PR includes the article, SVG, metadata sidecar and the paired AI task-board/session-handoff updates.
- Article: `docs/news-factory/drafts/devfest-india-2026-student-guide.md`, approximately 2.1K words, English, SEO/AEO/GEO-focused for India/Jaipur learners.
- Graphic: `docs/news-factory/media/devfest-india-2026-event-timeline.svg`, original self-authored 1200×675 SVG. Metadata sidecar: `docs/news-factory/drafts/devfest-india-2026-event-timeline.metadata.json`.
- Local SVG XML parse, 1200×675 PNG rendering and visual inspection passed. Metadata JSON parsed. No third-party artwork, photos, maps or logos were downloaded.
- Video candidate: official GDG Cloud Bhopal 2025 highlights reel, ID `z4VjNq03zzA`. The linked organizer page does not expose the upload date or independently confirm embedding permission, so the article includes a fallback watch link only; no iframe was added.
- Independent editorial/source QA and responsive browser QA remain pending. No CI workflow run or check result was returned for the PR head. No news sitemap, runtime PHP, canonical, route, schema, redirect or production content changed.

#### Repository coordination

- Mango Engineers: current open PRs #143/#147/#148/#149 reviewed at repository level; #143 continues to own Node.js readiness. No new write.
- Groot Academy: existing PR #592 (BigQuery) and #593 (Kubernetes graphic repair) plus prior News Factory owners remain intact. No new write.
- Forsk Coding School: PRs #152/#153 checked for file overlap; new #154 uses separate article/media paths and paired governance docs.
- Jaipur Engineers: canonical repo `satnamkhowal/jaipurengineers.com` and `MIGRATION-NOTES.md` read. Existing #41/#43 remain; no approved News Factory article lane was identified, so read-only.
- Other brands remain untouched unless central repository/catalogue mapping is verified. No worker chats or duplicate queues were created.
- Existing central News Factory PR #19 and branch `ops/news-factory-cycle-20261109-2209` reused; this is an append-only checkpoint update.

#### Cycle ledger

Previous carried-forward ledger: **73 researched, 61 drafted, 61 original graphics, 33 independent QA-ready, 0 live**.

This cycle adds one distinct research item (India GDG DevFest event roundup), one original draft and one original graphic. React, Node.js, Google Student Researcher and scholarship checks are revalidations, not new stories.

| State | Cumulative |
| --- | ---: |
| Researched | 74 |
| Drafted | 62 |
| Original graphics | 62 |
| Independent QA-ready | 33 |
| Live / published | 0 |

#### Next actions
1. Independent editorial/source QA and responsive review of Forsk PR #154; recheck local ticket status and fees before publication.
2. Recheck Mangaluru before 14 November; do not assume a ticket is available just because a button is visible.
3. Recheck Node.js patched versions and CVEs on or after 11 November before updating Mango PR #143.
4. Recheck NMMSS before 15 November, other portal-listed scholarship deadlines before 30 November, and Google Student Researcher before 4 December.
5. Keep all drafts unmerged and unpublished until independent QA and explicit approval.


### Forsk PR #154 CI execution addendum — 10 November 2026, 05:16 IST

- PR [#154](https://github.com/satnamkhowal/forsk-coding-school/pull/154) now includes the paired Forsk task-board/session-handoff updates and a CI-status addendum; it remains open, draft and mergeable at last check.
- Existing workflow run [42724044015](https://github.com/satnamkhowal/forsk-coding-school/actions/runs/42724044015), “Forsk learning home copy QA”, was triggered by the PR's `docs/ai-ops` changes because those paths are included in the workflow filter.
- Attempt 1 and one failed-job rerun (attempt 2) both failed before any runner/job steps were recorded: `runner_id=0`, no runner name, empty `steps` array, and no combined commit statuses. No PHP lint or learning-home regression test executed on the PR head. Treat this as a workflow/runner execution blocker, not a code-test failure or pass.
- No third rerun and no workflow configuration change were made. Independent article/source QA and responsive browser QA remain pending. The PR stays draft-only; no merge, deployment or publication.


### PR #154 state refresh — 10 November 2026, 05:18 IST

- Forsk PR [#154](https://github.com/satnamkhowal/forsk-coding-school/pull/154) now has **5 changed files, 3 commits, 306 additions and 0 deletions**; GitHub reports open/draft/mergeable. Mergeability is not independent QA or publication approval.
- The “Forsk learning home copy QA” workflow run #42724044015 failed on attempt 1 and one rerun (attempt 2) before any runner/job steps were recorded (`runner_id=0`, empty steps array, no combined status). No PHP lint or learning-home regression test executed on the PR head. Treat this as a runner/workflow execution blocker.
- Forsk task board and session handoff were updated together to record the latest PR/CI state. No third rerun, workflow-file change, merge, deployment or publication.


### News Factory cycle — 10 November 2026, 05:37 IST

#### Coordination and repository review
- Reused the existing News Factory PR #19 and branch \`ops/news-factory-cycle-20261109-2209\`; no duplicate controller or worker chat was created. Central branch compared 24 commits ahead / 0 behind main before this append.
- Verified repository default branches and read current instructions/queues before writes:
  - Mango Engineers: \`satnamkhowal/mangoengineers.com\`, main \`8eeb57fdf05341aa0a5ec31846148a37b0be3ba6\`. Read AGENTS.md, docs/agent-start-here.md, task board, integration queue and work log. Open PRs #143 and #147 both edit the task board and work log; no overlapping Mango write was made. Existing #143 owns Node.js and related news; #147 owns the NIC internship guide.
  - Groot Academy: \`satnamkhowal/grootacademy.com\`, main \`a97dc07463a352ea924af3dea22af915a6f9bdb1\`. Verified the legacy \`satnamkhowal/gta\` pointer resolves to the same repository ID 1375760757. Read .agent README, master handoff, current state, backlog, decisions, migration status, dated migration handoff, current open PRs and current News Factory inventory. No Amazon internship story/PR was present.
  - Forsk Coding School: \`satnamkhowal/forsk-coding-school\`, main \`a690ef725029e8c7f96b6148e9012f82a481bd6d\`. Read current README variants and docs/ai-ops master task board. Open PR #154 owns the task-board and session-handoff paths; no overlapping Forsk write was made. Existing #152/#153 cover other Copilot/agent topics.
  - Jaipur Engineers: \`satnamkhowal/jaipurengineers.com\`, main \`677da49970ffd2871514fd1d08a7fc94b3f42004\`. Read MIGRATION-NOTES.md; it says the je2 application history is canonical and legacy SEO/content folders must not be copied wholesale. No approved News Factory article lane was identified; read-only.
- Clever Ape Academy, CadMate India, Groot Software and Forsk Technologies remain untouched because their repository/catalogue mappings are unresolved in the central queue.

#### Research results

**1. Official student/developer opportunities — new verified Amazon India listings**
- Systems Development Engineer Intern – 2027, Job ID 10498158: https://www.amazon.jobs/en/jobs/10498158/systems-development-engineer-intern-2027
- Data Engineer Intern – 2027, Job ID 10496769: https://amazon.jobs/en-gb/jobs/10496769/data-engineer-intern-2027
- Both Amazon.jobs pages displayed an Apply now control when checked at 05:37 IST on 10 November 2026.
- Neither accessible listing displays a separate publication date, application deadline, stipend/compensation amount, internship duration or application fee. The draft records each as not stated and does not call the listings newly opened, free, paid, remote or guaranteed.
- Systems Development role: detailed qualification block lists Bachelor's or Master's in CS/Engineering or related field, Java/C/C++/Python and CS fundamentals. A generic qualification summary separately says enrolled in or completed a Bachelor's in CS/equivalent; the article flags this wording difference and directs applicants to the live form.
- Data Engineer role: final-year Bachelor's or Master's in CS/Engineering or related field; SQL, Python, RDBMS, Big Data, NoSQL, ETL and data-warehousing fundamentals. Preferred AWS S3, EMR, RDS, Redshift and Glue.
- Both listings identify India hiring locations and state applications may be considered across locations Amazon hires in India. Both mention full-time availability and a university-signed declaration for selected candidates.
- This is one combined, role-comparison opportunity article, not a claim that a single Amazon internship programme has one shared eligibility rule.

**2. React / frontend**
- Official React blog and GitHub release history rechecked. Latest listed stable patch tags remain 19.3.1, 19.2.9, 19.1.10 and 19.0.9, all dated 14 October 2026.
- No new stable release or fresh React security advisory qualified in this cycle. Existing Forsk PR #145 remains the owner of the React Server Components security catch-up.
- Sources: https://react.dev/blog and https://github.com/react/react/releases

**3. Node.js / backend**
- Official Node.js blog still lists the advance notice published 3 November 2026 for 26.x, 24.x and 22.x security releases on or shortly after 11 November.
- Highest severity is HIGH for each line. As of this 10 November check, the notice does not provide CVE IDs, affected patch ranges or patched versions; it is a pre-alert, not a completed patch release.
- Existing Mango PR #143 remains the owner. No duplicate Node.js article was created.
- Sources: https://nodejs.org/en/blog and https://nodejs.org/en/blog/vulnerability/november-2026-security-releases

**4. AI / cloud / developer news**
- GitHub Changelog published “Claude Fable 5.2 in GitHub Copilot” on 9 November 2026. It says the model is generally available to Copilot Pro+, Max, Business and Enterprise users, with gradual rollout; provider-list usage-based billing applies. Business/Enterprise administrators must enable the policy, which is off by default. Data retention is required by default for Anthropic safety classifiers; retained prompts/outputs are not used to train Anthropic models. Eligible enterprise customers may receive a time-bound zero-data-retention exemption through the end of 2026, subject to GitHub/Anthropic approval and additional controls thereafter.
- This is a distinct research candidate; no article was created in this bounded batch because current Forsk PRs #152/#153 already cover adjacent Copilot/agent topics and the Amazon student opportunity was prioritised for production.
- Source: https://github.blog/changelog/2026-11-09-claude-fable-5-2-in-github-copilot/
- Google Cloud's 9 November BigQuery pipeline concurrency GA / Zstandard Preview announcement is already owned by Groot PR #592; no duplicate article was created.

#### New production — Groot Academy
- Created isolated branch \`content/news-factory-amazon-india-internships-20261110\` from current main.
- Draft PR [#596](https://github.com/satnamkhowal/grootacademy.com/pull/596) is open and draft. It contains 4 new files, 4 commits, 328 additions / 0 deletions; compare shows 4 ahead / 0 behind main. GitHub currently reports mergeable=true; this is not independent QA or release approval.
- Article: \`docs/news-factory/drafts/amazon-india-engineering-internships-2027.md\`, 1,956 words, English, India/Jaipur-focused, with distinct role requirements, application-status caveats and FAQs.
- Original media: \`docs/news-factory/media/amazon-india-engineering-internships-2027.svg\`, self-authored 1200×675 SVG, 5,395 bytes. Metadata sidecar records source, permission, attribution, local path, alt text, dimensions and SHA-256. No third-party artwork was downloaded.
- Handoff: \`logs/2026-11-10-amazon-india-internships-news-factory.md\`.
- No story-specific official/reputable original YouTube video was verified; no video ID or iframe was added.

#### Validation and release gate
- SVG XML parsing, 1200×675 PNG rendering and visual inspection passed locally.
- Metadata JSON parsed; article and SVG were read back from the PR branch.
- PR #596 compare: 4 commits ahead / 0 behind; changed paths are exactly the article, metadata JSON, SVG and dated handoff.
- Combined GitHub commit status returned no status entries; no CI pass is claimed.
- Independent editorial/source QA and responsive browser QA remain pending.
- No merge, deployment, sitemap/route/schema/redirect change or publication.

#### Cumulative ledger
Previous carried-forward checkpoint: **74 researched, 62 drafted, 62 original graphics, 33 independent QA-ready, 0 live**.
- Added two new research items this cycle: Amazon India 2027 internship listings and GitHub Claude Fable 5.2 in Copilot.
- Added one original draft and one original graphic for the Amazon internship opportunity.
- React/Node/BigQuery checks are revalidations or existing owners, not duplicate stories.

| State | Cumulative |
| --- | ---: |
| Researched | 76 |
| Drafted | 63 |
| Original graphics | 63 |
| Independent QA-ready | 33 |
| Live / published | 0 |

#### Next actions
1. Independent editorial/source QA and responsive rendering review for Groot PR #596.
2. Reopen both Amazon job listings before any student-facing publication; confirm current Apply now status and check whether deadlines, duration, fee or compensation details have appeared.
3. Recheck Node.js security release on or after 11 November; update Mango PR #143 only after official patched versions/CVEs are published.
4. Keep the Claude Fable 5.2 story as a separate research candidate; avoid duplicating the active Forsk Copilot API/agent articles.
5. Recheck the Google Student Researcher and NSP deadline owners in their existing PRs before their listed dates.
6. Keep all new drafts unmerged and unpublished until independent QA and explicit approval.


---

### Fresh cycle — 10 November 2026, 06:06 IST

#### New verified research

**1. GitHub Actions workflow-log secret scanning — new developer-security story**

- GitHub published the announcement on **9 November 2026**; no separate event date is stated.
- The capability is **public preview**, disabled by default. It is available to eligible enterprises on GitHub Enterprise Cloud with GitHub Secret Protection or GitHub Advanced Security, including GHE.com data-residency customers.
- After a workflow run completes, GitHub scans its log for supported provider patterns. Findings appear in repository secret-scanning alerts with a link to the workflow log; supported secret types may receive validity checks, and alerts remain available after logs are deleted.
- Limits: no historical backfill; no generic, custom, AI-detected or Actions-masked values; no notifications for these alerts during the preview. The alert list must be checked directly.
- No India-specific regional availability or feature-specific price is stated. No universal-detection claim is made.
- Primary source: https://github.blog/changelog/2026-11-09-secret-scanning-detects-secrets-in-github-actions-workflow-logs/
- Supporting docs: https://docs.github.com/en/enterprise-cloud@latest/code-security/concepts/secret-security/secret-scanning ; https://docs.github.com/en/actions/concepts/security/secrets ; https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets ; https://docs.github.com/en/actions/concepts/security/openid-connect

**2. PM YASASVI Top Class Education in Schools — new current NSP listing**

- NSP's AY 2026–27 listing shows the school scheme open from **22 October 2026** and student applications open until **15 November 2026**; defective/institute verification is listed until 30 November and DNO/SNO/MNO verification until 15 December.
- The linked scheme specification covers OBC/EBC/DNT students in identified Top Class Schools from Class 9 through Class 12, with household annual income below ₹2.5 lakh, state-wise merit selection and at least 30% of awards reserved for girls.
- The linked specification states assistance up to ₹75,000 per annum for Classes 9–10 and ₹1,25,000 per annum for Classes 11–12, for covered tuition/hostel/other school charges. The PDF does not display a publication date; the current application window comes from the NSP 2026–27 listing.
- The NSP page footer still says last updated June 2026. The application form itself was not inspected; applicants should confirm the live form and school eligibility before relying on the listed window.
- Official listing: https://scholarships.gov.in/All-Scholarships
- Linked specification: https://scholarships.gov.in/public/schemeGuidelines/3061_G.pdf
- No article was created in this cycle: this is a school-stage scholarship rather than a developer/IT opportunity, and no suitable non-overlapping Forsk News Factory write lane was available while its shared task-board/handoff paths are owned by open PR #154.

**PM-USP Special Scholarship — status correction, not a new draft**

- NSP now lists the J&K/Ladakh scheme open from **22 October 2026** through **30 November 2026**.
- However, the linked AICTE specification PDF is still labelled AY 2025–26. Its domicile, admission and award conditions must not be presented as newly confirmed 2026–27 terms without an updated official guideline.
- This is restricted to J&K/Ladakh domicile, not Rajasthan. Keep on hold for current-year guideline confirmation.
- NSP listing: https://scholarships.gov.in/All-Scholarships
- Linked PDF: https://scholarships.gov.in/public/schemeGuidelines/AICTE/PM_USPY%28SSSJKL%29SchemeSpecifications.pdf

#### Revalidated existing opportunity owners

- **Google Student Researcher 2027:** official listing still shows India remote eligible, Bachelor's/Master's/PhD enrolment in specified fields, relevant CS experience, rolling review and **4 December 2026** deadline. No fixed stipend or project duration is stated. Existing Forsk PR #146 remains owner; no duplicate.
  - https://www.google.com/about/careers/applications/jobs/results/125423735539671750-student-researcher-2027
- **Amazon Systems Development Engineer Intern – 2027 (Job 10498158):** official page still displays Apply now; India location coverage and full-time commitment/university declaration are stated. No closing date, stipend, duration or application fee is shown.
  - https://www.amazon.jobs/en/jobs/10498158/systems-development-engineer-intern-2027
- **Amazon Data Engineer Intern – 2027 (Job 10496769):** official page still displays Apply now; final-year Bachelor's/Master's CS/Engineering or related field, SQL, Python and data/ETL concepts are stated. No closing date, stipend, duration or application fee is shown.
  - https://www.amazon.jobs/en-gb/jobs/10496769/data-engineer-intern-2027
- Existing Groot PR #596 remains owner of the two active Amazon roles. A separate search result for Amazon Front-End Engineer Intern – 2027 (Job 10502000) returned **HTTP 404** when opened and was excluded; it is not described as open.
  - https://www.amazon.jobs/en/jobs/10502000/front-end-engineer-intern-2027

#### React and Node.js recheck

- **React:** official React blog still lists React 19.3, published 9 September 2026, as the latest blog/release entry. No newer stable release or new React security advisory was found in this check. Existing Forsk PR #145 remains owner.
  - https://react.dev/blog
- **Node.js:** official blog still lists Node.js 26.13.0 LTS (28 October), 24.22.2 LTS (28 October) and 27.0.0-alpha.0.0.0 (29 October). The security notice was published **3 November** and says 26.x, 24.x and 22.x security releases are expected on or shortly after **11 November 2026**; highest severity is HIGH. As of this 06:06 check, no patched versions or CVE ranges are published. Existing Mango PR #143 remains owner.
  - https://nodejs.org/en/blog
  - https://nodejs.org/en/blog/vulnerability/november-2026-security-releases

#### Other AI / cloud developer updates

- GitHub's **Claude Fable 5.2 in Copilot** announcement was published 9 November; existing Forsk Copilot/agent PRs #152/#153 already cover adjacent subject matter. Keep as a research candidate; no duplicate article.
  - https://github.blog/changelog/2026-11-09-claude-fable-5-2-in-github-copilot/
- Google Cloud BigQuery pipeline-concurrency GA and Zstandard SQL Preview are already owned by Groot PR #592; no duplicate.
- The new workflow-log secret-scanning feature is distinct from pull-request secret merge protection and existing generic CI/CD guides.

#### New production — Groot Academy

- Created isolated branch content/news-factory-github-actions-log-secret-scanning-20261110 from current main a97dc07463a352ea924af3dea22af915a6f9bdb1.
- Draft PR [#597](https://github.com/satnamkhowal/grootacademy.com/pull/597) is open, draft and currently reported mergeable by GitHub. It contains four new files; branch comparison is 8 commits ahead / 0 behind main. The PR snapshot reports 8 commits and 4 changed files; no CI workflow runs or independent reviews were returned.
- Article: docs/news-factory/drafts/github-actions-workflow-log-secret-scanning-preview-november-2026.md, 2,344 words, original English, Jaipur/India learner context without claiming India-specific feature access.
- Original media: docs/news-factory/media/github-actions-workflow-log-secret-scanning-preview-20261110.svg, self-authored 1200×675 SVG. Local PNG preview rendered at 1200×675 and visually inspected.
- Metadata: docs/news-factory/drafts/github-actions-workflow-log-secret-scanning-preview-20261110.metadata.json, including source dates, rights/permission, attribution, local path, alt text, dimensions, local SHA-256 and uploaded Git blob SHA.
- Handoff: logs/2026-11-10-github-actions-workflow-log-secret-scanning-news-factory.md.
- No story-specific verified original YouTube video found; no video ID or iframe added.
- No PHP route, blog registry, sitemap, schema, redirect, production asset or live content changed.

#### Validation and release gate

- Article read-back: PASS; 2,344 words.
- Metadata JSON parse: PASS.
- SVG XML parse: PASS.
- SVG 1200×675 PNG render and visual inspection: PASS.
- GitHub read-back of all four intended paths: PASS.
- PR #597 changed-file list: exactly four intended paths; no review submissions/threads and no workflow runs returned.
- Independent editorial/security QA and responsive browser QA remain pending.
- No merge, deployment or publication.

#### Cumulative ledger

Previous carried-forward checkpoint: **76 researched, 63 drafted, 63 original graphics, 33 independent QA-ready, 0 live**.

- Added three new research items: GitHub Actions workflow-log secret scanning, PM YASASVI Top Class Schools 2026–27 listing and Microsoft Imagine Cup 2027.
- Added one original article and one original graphic for Groot Academy.
- PM-USP is a status correction; Amazon/Google listings and React/Node releases are revalidations of existing owners.

| State | Cumulative |
| --- | ---: |
| Researched | 79 |
| Drafted | 64 |
| Original graphics | 64 |
| Independent QA-ready | 33 |
| Live / published | 0 |

#### Next actions

1. Independent editorial/security QA and responsive rendering review for Groot PR #597.
2. Recheck PM YASASVI's live NSP application form and current school list before any student-facing publication; deadline shown as 15 November.
3. Obtain an updated 2026–27 AICTE guideline for PM-USP before publishing its eligibility/award details.
4. Recheck Node.js actual patched versions/CVEs on or after 11 November; update Mango PR #143 only from the official release.
5. Recheck Google Student Researcher and Amazon job listings before publication and before their application windows close.
6. Keep all drafts unmerged and unpublished until independent QA and explicit approval.


#### Brand repository audit and write-lane decision — 06:06 IST

- **Mango Engineers:** read current README, agent start guide, task board, work log and integration queue. The repository's current verified positioning says technology/programming training in Jaipur; do not infer industrial-engineering services from the brand name. Existing PR #143 owns the Node.js/security and scholarship batch; PR #147 owns NIC Digital India Internship. No new Mango write was made.
- **Groot Academy:** confirmed repository ID 1375760757; the alias satnamkhowal/gta resolves to the same repository. Read .agent/README.md, master handoff, current state, backlog, decisions and AI-ops handoff/task board. Existing PRs #592 and #596 have separate BigQuery and Amazon ownership; the new workflow-log security draft uses four unique paths in PR #597.
- **Forsk Coding School:** read README.txt, AI-ops master task board and session handoff, plus open PRs #150/#152/#153/#154. PR #154 owns the shared task-board and session-handoff paths, so no overlapping Forsk write was made. Existing PR #146 remains the Google Student Researcher owner.
- **Jaipur Engineers:** MIGRATION-NOTES identifies je2 as the canonical application and warns against copying the legacy repository wholesale. The je2 alias resolves to the same repository ID as jaipurengineers.com, but the GitHub file connector could not resolve files through the je2 alias. Open PR #41 owns batch planning, #43 owns readability and #27 owns social production. No News Factory write was made.
- **Central control:** PR #19 remains open/draft; the latest checkpoint is appended. Branch comparison is 27 ahead / 0 behind main; GitHub reports mergeable=true after refresh.


#### Additional official opportunity check — Microsoft Imagine Cup 2027

- **Current status:** Applications open. Official competition page says applications opened **2 November 2026** and the submission deadline is **28 February 2027 at 23:59 CST**. Official rules last updated **4 November 2026**; these dates are the competition/application timeline, not the publication date of a separate news article.
- **What it is:** A startup competition, not a general internship or individual coding scholarship. Eligible early-stage startups build commercially viable software-based solutions using Microsoft Azure. Seven categories include Developer Tools, Cybersecurity, Deep Tech + Physical AI and Student Startup.
- **General eligibility:** Individual team members must be at least 18; the startup must be a privately held, for-profit legal entity founded on or after **2 November 2024**, pre-seed through Series B (not Series C+), headquartered where Azure is available, and meet Microsoft for Startups requirements. It must not be an educational institution, government organisation, consultancy or agency, and must not have received more than USD 350,000 in lifetime free Startup Credits. Teams may register up to four official members.
- **Student Startup category:** In addition to the general rules, every founding-team member must be enrolled at an accredited high-school/college/university (or equivalent) at some point between **30 September 2026 and 31 May 2027**. Student Startup entries are judged separately and are not eligible for the First/Second/Third prizes.
- **India:** India is not among the comprehensive-sanctions exclusions listed in the rules, and Microsoft's Azure geography list includes India (Central India, South India and West India). India therefore appears eligible subject to all other requirements and Microsoft's verification; this is not a guarantee of acceptance or a prize.
- **Azure requirement/cost:** A valid Azure Subscription ID is mandatory. By 28 February 2027 the startup must show at least USD 1 usage on each of ten unique eligible Azure services; the FAQ says this usage must be maintained while actively competing. This can create real usage costs. The rules do not state a separate entry fee; do not describe the competition as cost-free.
- **Credits/prizes:** Eligible startups may receive USD 1,000 initial Azure credits after screening and onboarding, and may earn up to USD 150,000 in Azure Progress Credits based on verified usage and continued eligibility; neither is guaranteed. The Student Prize is USD 25,000 cash plus USD 250,000 Azure Prize Credits. The main First Prize is USD 250,000 cash plus USD 1 million Azure Prize Credits. Credits are not cash and are subject to terms/expiry.
- **Required submission:** Award Force application, startup/team details, Microsoft for Startups account and valid Azure Subscription ID, written responses, pitch deck, 2–3 minute product demonstration video and Azure architecture/technical overview. Official rules require the completed entry in English.
- **Application URL:** https://2027.imaginecup.com/ (official Award Force portal). The portal page returned a JavaScript/unsupported-browser message in this research environment; the official Imagine Cup page and FAQ still display Apply Now. No completed application was attempted.
- Official FAQ: https://imaginecup.microsoft.com/en-us/support/faq
- Official competition page: https://imaginecup.microsoft.com/en-us/compete
- Official rules (last updated 4 November 2026): https://aka.ms/ImagineCup2027TCs
- Azure geography availability: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies
- No existing Imagine Cup 2027 article or News Factory draft was found in the four verified brand repositories. No second draft was created in this run to keep the Groot write lane bounded to one new isolated article task; queue as a high-priority next-cycle candidate. Do not present Groot Academy or Forsk Coding School as eligible applicants merely because they teach technology—their education-institution status would conflict with the published Microsoft for Startups eligibility rule. The story should target eligible student founders and independent software startups.



## 10 November 2026 — Cycle 11: Microsoft Imagine Cup 2027 India guide (07:09 IST)

### Coordination and ownership
- Reused the existing central News Factory PR [#19](https://github.com/satnamkhowal/brand-growth-control-center/pull/19), branch \`ops/news-factory-cycle-20261109-2209\`, and this append-only checkpoint. The central README and \`coordination/MASTER_PENDING_TASKS_2026-10-19.md\` were read; the October master queue is an index, while the current News Factory PR/checkpoint contains the active content ownership.
- Current Forsk main at start: \`a690ef725029e8c7f96b6148e9012f82a481bd6d\`. Read \`README.txt\`, \`docs/ai-ops/MASTER_TASK_BOARD.md\`, \`docs/ai-ops/SESSION_HANDOFF.md\`, current News Factory inventory, open PRs and relevant changed-file ownership.
- Forsk PR #154 already owns shared \`docs/ai-ops/MASTER_TASK_BOARD.md\` and \`SESSION_HANDOFF.md\` updates for its DevFest work. Those shared files were not modified to avoid a collision. The new article is isolated to three unique News Factory draft/media paths; reconcile the Forsk board/handoff after PR #154 releases those paths.
- Other existing ownership preserved: Mango PR #143 owns Node.js readiness; Forsk PRs #145–#154 own React, Google Student Researcher, scholarships, Copilot/agent, DevFest and other active drafts; Groot PRs #580, #592, #596 and #597 own their respective cloud, internship and GitHub security stories. Jaipur Engineers remains read-only for this lane because no approved News Factory write scope was identified.

### 1. Official student/startup opportunity — Microsoft Imagine Cup 2027
- Official competition page still displays **Apply Now**. Official rules last updated **4 November 2026**; submission period opened **2 November 2026** and ends **28 February 2027 at 23:59 CST**. Rules update date and application opening date are recorded separately.
- India-based startups can meet the published Azure-country availability test in principle: Microsoft lists Central India (Pune), South India (Chennai), West India (Mumbai) and India South Central (Hyderabad). This is not a guarantee; all business, founder, export-control, subscription and Microsoft verification rules still apply.
- General requirements include: legal entity founded on/after 2 November 2024; privately held and for-profit; pre-seed through Series B and no Series C; no more than USD 350,000 lifetime free Startup Credits; not an educational institution, government organisation, consultancy or agency; no cryptocurrency mining; applicant at least 18 (guardian consent where required).
- Student Prize path: all founding team members must be enrolled at an accredited institution at some point between 30 September 2026 and 31 May 2027. Up to four official team members unless the competition website sets another limit. Student Startup is a separate cross-industry category and its entries are not eligible for the main First/Second/Third prizes.
- Student Prize: USD 25,000 cash plus USD 250,000 Azure prize credits. Credits are not cash; taxes and credit terms apply. Conditional Microsoft for Startups progress credits are separate and not guaranteed.
- Azure judging requirement: valid Azure Subscription ID and ten unique eligible Azure services/workloads with at least USD 1 spend each by the deadline; the official FAQ says each workload must maintain at least USD 1 spend while the startup remains actively competing. The official rules do not state an application fee; actual Azure charges may apply.
- Official FAQ lists a pitch deck, 2–3 minute product-demo video, Azure architecture/technical overview and written responses. No story-specific original YouTube video with verified ID and confirmed embed permission was found; no iframe is included.
- Sources: https://imaginecup.microsoft.com/en-us/compete ; https://aka.ms/ImagineCup2027TCs ; https://imaginecup.microsoft.com/en-us/support/faq ; https://learn.microsoft.com/en-us/startups/imagine-cup-credits-eligibility ; https://learn.microsoft.com/en-in/azure/reliability/regions-list

### 2. New Forsk Coding School draft and original media
- Repository: \`satnamkhowal/forsk-coding-school\`.
- Branch: \`content/news-factory-imagine-cup-2027-india-20261110\`, created from current main \`a690ef725029e8c7f96b6148e9012f82a481bd6d\`.
- Draft PR [#155](https://github.com/satnamkhowal/forsk-coding-school/pull/155), open and draft; compare is 3 commits ahead / 0 behind main; GitHub reports mergeable=true at latest read-back.
- Article: \`docs/news-factory/drafts/microsoft-imagine-cup-2027-india-student-startup-guide.md\`, 2,153 words, original English India-focused guide. It distinguishes the startup legal-entity requirement from an ordinary student project and explains student-founder enrolment, team size, deadline, Azure usage/cost, conditional credits and prize limitations.
- Original SVG: \`docs/news-factory/media/microsoft-imagine-cup-2027-india-eligibility.svg\`, 1200×675; SHA-256 \`c4690fc6000519c07c19f93ef97b9960f156014bbf706788c93b324da053b9fe\`. Self-authored vector; no Microsoft logo, screenshot, third-party artwork, photograph or downloaded image.
- Provenance sidecar: \`docs/news-factory/drafts/microsoft-imagine-cup-2027-india-student-startup-guide.metadata.json\`; records official source URLs, rule/application dates, fee/usage qualification, local path, licence/permission, attribution, alt text, dimensions and hash.
- Local files: \`/mnt/data/news-factory/2026-11-10/imagine-cup/microsoft-imagine-cup-2027-india-student-startup-guide.md\`, \`/mnt/data/news-factory/2026-11-10/imagine-cup/microsoft-imagine-cup-2027-india-eligibility.svg\`, \`/mnt/data/news-factory/2026-11-10/imagine-cup/microsoft-imagine-cup-2027-india-eligibility.png\`, and the metadata JSON in the same folder.
- GitHub read-back verified all three files. Compare reports exactly three new files and no unrelated paths. No CI workflow runs were returned. Independent editorial/legal/source QA and responsive browser review remain pending.
- No merge, deployment, publication, application submission or indexing claim.

### 3. Opportunity revalidation — no duplicate article
- Google Student Researcher 2027 remains listed as India remote eligible; the official listing asks applicants to apply before **4 December 2026**, reviews on a rolling basis, and requires current enrolment in a relevant Bachelor's/Master's/PhD programme plus computer-science-area experience. The public listing does not state a fixed duration or stipend amount. Existing Forsk PR #146 remains owner.
- Amazon.jobs listings currently show Apply Now for four India 2027 internships:
  - Systems Development Engineer Intern — Job ID 10498158: https://www.amazon.jobs/en/jobs/10498158/systems-development-engineer-intern-2027
  - Data Engineer Intern — Job ID 10496769: https://www.amazon.jobs/en/jobs/10496769/data-engineer-intern-2027
  - Business Intelligence Engineer Intern — Job ID 10498165: https://www.amazon.jobs/en/jobs/10498165/business-intelligence-engineer-intern-2027
  - Support Engineer Intern — Job ID 10498163: https://www.amazon.jobs/pl/jobs/10498163/support-engineer-intern-2027
- These Amazon roles require full-time availability during the internship and a university availability declaration. Role-specific degree/skill requirements differ. The inspected pages did not expose a posting date, closing date, stipend, duration or application fee. Existing Groot PR #596 owns the Amazon opportunity guide; no duplicate article or overlapping edit was made. Its owner should recheck whether to add the two newly surfaced BIE/Support roles before publication.
- Amazon Front-End Engineer Intern 2027 Job ID 10502000 appeared in search results, but opening the official listing returned HTTP 404; it is not counted as an active opportunity.
- NSP 2026–27 current listing: NMMSS and PM YASASVI Top Class Schools show 15 November; AICTE Swanath/Pragati and PM-USP J&K/Ladakh show 30 November. PM-USP remains held for updated guideline verification because its linked document is still AY 2025–26 and prior renewal-status messaging conflicts with the scheme card. No duplicate scholarship article was created.

### 4. React, Node.js and AI/cloud/developer watch
- React official blog still lists React 19.3 (9 September 2026) as the latest feature release; no newer stable release or new qualifying advisory found. Existing Forsk PR #145 remains owner.
- Node.js official advance notice (last updated 3 November) still schedules security releases for 26.x, 24.x and 22.x on or shortly after 11 November 2026; highest severity HIGH. No CVE IDs or patched versions were published at this 10 November check. Existing Mango PR #143 remains owner; no speculative patched-version article created.
- GitHub Changelog’s latest relevant entry is 9 November: secret scanning detects secrets in GitHub Actions workflow logs; existing Groot PR #597 owns the guide.
- Google Cloud 9 November Pathways on Cloud GA on GKE and BigQuery pipeline-concurrency GA/Zstandard preview are already owned by Groot PRs #580 and #592. No duplicate articles created.
- GitHub Claude Fable 5.2 Copilot announcement remains a research-only candidate due existing Forsk Copilot/API and coding-agent PR ownership; no overlapping draft created.

### 5. Validation, media and counts
- Article front matter and source links reviewed against official rules/FAQ/regions pages.
- Metadata JSON parse: PASS; SVG XML parse: PASS; 1200×675 PNG rendering: PASS; visual inspection: PASS.
- GitHub read-back: PASS for article, SVG and metadata; branch compare: 3 ahead / 0 behind, exactly three intended files.
- CI runs: none returned. Responsive browser QA: pending. Independent editorial/legal/security QA: pending.
- Original graphics added this cycle: 1. Licensed third-party downloads: 0. Verified story-specific YouTube videos/embeds: 0.
- Cumulative ledger carried forward: 79 researched, 65 drafted, 65 original graphics, 33 independent QA-ready, 0 live. Imagine Cup was already in the prior research candidate queue; this cycle converted it into one draft and one original graphic, so no new researched-item increment is claimed. QA-ready and live counts did not change.
- Next action: independent QA of PR #155; refresh the Amazon PR #596 listing set; recheck Node.js patched versions/CVEs on or after 11 November; verify scholarship forms before their listed deadlines.


## Latest cycle — 10 November 2026, 08:08 IST
- Forsk Coding School: [PR #156](https://github.com/satnamkhowal/forsk-coding-school/pull/156) adds an approximately 2,000-word original English guide to PM YASASVI Top Class Schools 2026–27, one original accessible 1200×675 SVG, and a provenance sidecar. Three intended files read back from GitHub; branch is 3 commits ahead / 0 behind main. PR is open/draft; GitHub initially reported mergeable=false, so do not infer conflict resolution or readiness.
- NSP's current AY 2026–27 scheme card lists fresh applications from 22 October through 15 November 2026; defective-application/institute verification through 30 November and DNO/SNO/MNO verification through 15 December. The student deadline is 15 November; later verification dates do not extend it.
- The current NSP announcement says fresh applications are on hold for Rajasthan, Keralam and Karnataka; no reopening date is displayed. The notice has no separate publication date. The current card is the evidence for the 2026–27 window. The linked guideline PDF does not show a clear issue date.
- The linked guideline states OBC/EBC/DNT eligibility, annual household income below ₹2.5 lakh, designated Top Class School requirement, merit selection, at least 30% girls' reservation, DBT, and maximum annual support of ₹75,000 for Classes 9–10 and ₹1,25,000 for Classes 11–12. These are caps, not guaranteed awards. NSP OTR is mandatory and free through the portal; the optional CSC-assisted end-to-end service is ₹30 inclusive of taxes. No separate scheme application fee is listed.
- Forsk's existing PR #154 currently owns the paired `docs/ai-ops/MASTER_TASK_BOARD.md` and `docs/ai-ops/SESSION_HANDOFF.md` paths; PR #156 deliberately does not touch them. Reconcile the new task-board/handoff entry after #154 releases those shared files. Groot PR #577 owns the distinct NMMSS school scholarship; no near-identical article was copied.
- Media: original self-authored SVG only; XML parse, 1200×675 PNG render, visual inspection, metadata JSON and SHA-256 checks passed. No third-party graphic was downloaded. NSP links an OTR video, but its YouTube channel, publication date and embed permission could not be verified; no video ID/iframe was added.
- React: no new stable release. Official GitHub release list shows 19.3.1, 19.2.9, 19.1.10 and 19.0.9 dated 14 October; 19.3.0 feature release is 9 September. The 14 October RSC security advisory has fixes in those patch lines; existing Forsk PR #145 remains owner.
- Node.js: official blog lists 26.13.0 LTS and 24.22.2 LTS from 28 October, 27.0.0-alpha.0.0.0 from 29 October, and the V8 15.6/Node 27 alpha technical post from 5 November. The Node.js Project's advance security notice was published 3 November and schedules 26.x/24.x/22.x security releases on or shortly after 11 November; highest severity HIGH. No CVE IDs or patched versions are yet listed. Existing Mango PR #143 owns the security-readiness article; no duplicate backend article was created.
- AI/cloud/developer: GitHub's 9 November Claude Fable 5.2 Copilot announcement and Actions workflow-log secret scanning preview were rechecked. The latter is owned by Groot PR #597; Claude Fable 5.2 remains research-only to avoid overlapping current Forsk Copilot/agent work. Google Cloud Pathways on Cloud GA on GKE (9 November) remains owned by Groot PR #580; BigQuery pipeline concurrency GA/Zstandard preview remains owned by Groot PR #592.
- Opportunities revalidated without duplicate writes: Google Student Researcher 2027 India-remote listing (4 December deadline; Forsk #146); Amazon 2027 internship listings 10498158, 10496769, 10498165 and 10498163 show Apply Now (Groot #596); Microsoft Imagine Cup 2027 remains covered by Forsk #155. The Front-End Engineer Intern listing 10502000 returned HTTP 404 and is not counted active.
- No fresh React stable release or patched Node.js security versions/CVEs were published at this check. No new story-specific YouTube video was verified. No application was submitted.
- Forsk PR #156: independent editorial/source/legal QA and responsive browser review pending; no CI run returned. No merge, deployment or publication.
- Cumulative ledger: **79 researched, 66 drafted, 66 original graphics, 33 independent QA-ready, 0 live**. PM YASASVI Schools was already in the research queue, so this cycle adds one draft and one graphic, not a new researched-item increment. Jaipur Engineers remains read-only for News Factory writes; unverified brand mappings remain untouched.
- Next action: independent QA of PR #156; recheck the live NSP school list/state application control before any publication decision; reconcile Forsk board/handoff after PR #154 releases ownership; verify actual Node.js patched versions/CVEs on or after 11 November.
