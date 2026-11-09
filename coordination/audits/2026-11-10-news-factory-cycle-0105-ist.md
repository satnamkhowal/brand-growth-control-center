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
- PR is open, draft, 6 commits ahead / 0 behind main, and GitHub currently reports it mergeable.
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
- TPU article contains responsive iframe markup using `youtube-nocookie`, a descriptive title, lazy loading, fullscreen support and a fallback watch link. Browser playback was not tested.
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
