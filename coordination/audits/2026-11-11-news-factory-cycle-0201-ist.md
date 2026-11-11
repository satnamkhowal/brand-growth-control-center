# News Factory cycle — 11 November 2026, 02:01 IST

## Executive status

Two new documentation-only draft PRs were produced. Both have original English content, one original 1200×675 SVG each, and source/media provenance sidecars. No article was merged, deployed, published or indexed.

- Groot Academy: https://github.com/satnamkhowal/grootacademy.com/pull/609 — AWS Bedrock AgentCore Runtime V2 snapshot safety and Node.js guidance.
- Forsk Coding School: https://github.com/satnamkhowal/forsk-coding-school/pull/170 — Science Academies Summer Research Fellowship 2027 India eligibility guide.

## New draft deliveries

### Groot Academy — AgentCore Runtime V2

- Original GA announcement: 18 September 2026. AWS Weekly Roundup: 9 November 2026; the roundup is not the GA date.
- Article: 2,349 words; snapshot lifecycle, V2 opt-in, Mumbai Region (ap-south-1), AWS-reported P75 cold-start benchmark caveats, 120-second health requirement, startup/request-state separation, current listed consumption rates and pricing caveats.
- Important AWS-documented Node.js caveat: crypto.randomBytes(), randomUUID(), randomInt() and getRandomValues() can repeat across restored instances, including in the request handler. The guide explains the /dev/urandom workaround and per-request state design.
- Original media: self-authored 1200×675 SVG; local PNG 111,760 bytes, visually inspected; optimized WebP 52,954 bytes. Provenance records sources, dates, permission, attribution, alt text, paths, dimensions and SHA-256 hashes.
- No relevant official/reputable YouTube ID plus embed permission was verified; no iframe was invented.
- PR base main 99336e8d0b412f6e0f0bdc0464e0aec4b8fea2b5; 3 commits ahead / 0 behind; 3 added paths; latest PR-info mergeable=true. No workflow run returned. Independent editorial/source QA and responsive/browser QA pending.

Official sources:
- https://aws.amazon.com/blogs/machine-learning/the-new-agentcore-runtime-elastic-optimized-and-consistently-fast-starts/
- https://aws.amazon.com/blogs/aws/aws-weekly-roundup-agentcore-runtime-v2-amazon-dynamodb-bulk-put-items-and-more-november-9-2026/
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-v2-optimize.html
- https://aws.amazon.com/bedrock/agentcore/pricing/

### Forsk Coding School — Science Academies SRFP 2027

- Official announcement date: 10 September 2026. Application deadline: 30 November 2026.
- Programme: two-month guided research project during calendar year 2027; summer preferred.
- India-wide standard SRFP. Course/year list includes BE/BTech/BCA second/third year and MCA first year; 65% average in core subjects excluding languages; teachers teaching in a college/university may apply without the marks threshold; PhD students are ineligible, while integrated PhD first/second year is separately listed.
- Required: Class X onward marksheets (JPEG, each <=700 KB), 150–250-word specific project-interest note, one current teacher contact for recommendation. One application only; no hard copies.
- Selected candidates receive entitled round-trip train fare and a monthly fellowship for living expenses. The public announcement does not state the fellowship amount or an application fee.
- Explicitly distinguishes the India-wide SRFP from separate region-restricted FAST-SF 2027; do not apply FAST-SF state restrictions to standard SRFP.
- Article: 2,084 words, original English, eligibility matrix, application steps, India/Jaipur clarification, FAQs and official source links.
- Original media: self-authored 1200×675 SVG; local PNG 121,611 bytes, visually inspected; optimized WebP 52,498 bytes. Metadata records official sources, permission, attribution, alt text, paths, dimensions and SHA-256 hashes.
- No programme-specific verified YouTube ID plus embed permission; no iframe.
- PR base main a690ef725029e8c7f96b6148e9012f82a481bd6d; 4 commits ahead / 0 behind; 3 added paths; latest PR-info mergeable=true. No workflow run returned. Independent editorial/source QA and responsive/browser QA pending.

Official sources:
- https://webjapps.ias.ac.in/fellowship2027/
- https://webjapps.ias.ac.in/fellowship2027/application_instructions.jsp
- https://insaindia.res.in/
- https://insaindia.res.in/scroll_news_pdf/FAST-SF-2027-Announcement-Website-Eng-Hindi.pdf
- https://webjapps.ias.ac.in/fastsf2027/application_instructions.jsp

## Opportunity and programme track

No new Google Student Researcher opening was found; the existing Forsk owner was retained. The official Google Careers listing remains Apply / India Remote, with a 4 December 2026 deadline and rolling review. The listing does not state a stipend amount or application fee.

Other current official opportunities were rechecked and existing owners were updated rather than duplicated:

- ANRF PM ECRG: official homepage says open until 2 December 2026, 5 PM. Up to ₹60 lakh plus overheads over three years; up to 700 grants/year. Eligibility includes Indian citizenship (specific PIO/OCI route), doctorate or specified medical qualification, regular academic/research position, application within two years of joining and age conditions. Existing Mango PR #159 remains owner.
- IIIT Guwahati MeitY project internship: notice dated 30 October; one full-time CSE/allied UG/PG intern; 15 November deadline; online selection 20 November; tentative 10 months; ₹15,000/month through 15 September 2027. Hostel unavailable; on-campus preferred, remote exceptional. Separate TIH IITG vacancy closed 10 November. Existing Forsk PR #163 remains owner.
- CMI Computer Science Summer 2027: 31 January 2027 deadline; programming background, typically after second year; one month to a semester; fellowship amount not stated; hostel usually arranged; no travel support. Existing Forsk PR #164 remains owner. CMI Mathematics route has a separate 30 November 2026 deadline through the Academies SRFP.
- PM YASASVI Top Class Schools: NSP card lists 15 November 2026, but the Student Announcements page says fresh applications from Rajasthan, Keralam and Karnataka students must wait. The linked guideline covers OBC/EBC/DNT students in identified top-class schools, household income below ₹2.5 lakh, and assistance caps of ₹75,000/year for Classes 9–10 and ₹1,25,000/year for Classes 11–12. Existing Forsk PR #156 remains owner; do not direct Rajasthan students to submit until NSP changes the restriction.
- PM YASASVI Top Class College: NSP AY 2026–27 card lists 30 November 2026. Existing Forsk PR #166 remains owner.
- PM-USP CSSS renewal: NSP All-Scholarships listing says 30 November, while Student Announcements says student application closed 31 October. Conflict remains; do not describe it as confirmed open.
- Google Student Researcher and other current Google internship listings remain with existing Forsk PRs #146 and #160; no duplicates.

Sources:
- https://www.google.com/about/careers/applications/jobs/results/125423735539671750
- https://anrf.gov.in/
- https://anrfonline.in/ANRF/ecrg_anrf?HomePage=New
- https://www.iiitg.ac.in/vacancy-for-project-intern-position-in-a-1
- https://www.cmi.ac.in/admissions/internships.php
- https://scholarships.gov.in/All-Scholarships
- https://scholarships.gov.in/Students

## React / frontend

No new stable release was found. Official React release tags remain 19.3.1, 19.2.9, 19.1.10 and 19.0.9, all dated 14 October 2026.

The official React advisory GHSA-xqc2-xf4c-x3h3 was published 14 October 2026: Critical, CVSS 9.5, no known CVE; affects react-server-dom-webpack, react-server-dom-parcel and react-server-dom-turbopack through the listed 19.0.8/19.1.9/19.2.8/19.3.0 ranges; patched versions are 19.0.9/19.1.10/19.2.9/19.3.1. Existing Forsk PR #145 remains owner.

Sources: https://github.com/react/react/releases · https://github.com/react/react/security/advisories/GHSA-xqc2-xf4c-x3h3

## Node.js / backend

The official Node.js security page still shows only the advance notice for Wednesday, 11 November 2026, last updated 3 November 2026. It says releases for 26.x, 24.x and 22.x will arrive on or shortly after 11 November; highest severity HIGH in each line. As of 02:01 IST, the notice has no CVE IDs, affected patch ranges or patched versions. The release blog still lists 26.13.0 LTS and 24.22.2 LTS from 28 October, 26.12.1 Current from 21 October and 22.23.4 LTS from 21 October; 27.0.0-alpha.0.0.0 is prerelease. Existing Mango PR #143 remains owner; no release is claimed until actual tags/posts appear.

Sources: https://nodejs.org/en/blog/vulnerability/november-2026-security-releases · https://nodejs.org/en/blog/release

## Other AI / cloud / developer news

AWS's 9 November roundup also covered DynamoDB bulk put items, Web Answer on Bedrock AgentCore, Lambda queue mode for self-managed Kafka event sources and Security Hub SBOM inventory for EC2/ECR/Lambda. Existing owners were reviewed; no additional article was created in this bounded batch to avoid overlapping current AgentCore Web Search, Nitro Sandbox and AI/cloud drafts. These are candidate follow-ups for later deduplicated research, not new draft counts.

## Repository and coordination review

- Central PR #19 current compare: 68 ahead / 2 behind main, diverged; latest PR-info says mergeable=true, but no rebase/merge was attempted.
- Central PR #20 current compare: 21 ahead / 2 behind main, diverged; no rebase/merge was attempted.
- Groot current main and open PR inventory reviewed; .agent handoff/current-state/backlog/decisions and migration instructions read. #609 uses three unique News Factory documentation paths only; no 100K queue, route, sitemap, schema, shared course data or production file changed.
- Forsk open PR inventory reviewed. Root README/AGENTS and expected .agent, .github, docs/README, docs/news-factory/README, task-board and work-log instruction paths were not present on accessible default branch. Existing News Factory conventions were followed; #170 changes only three unique News Factory documentation paths.
- Mango open PR inventory and existing News Factory owners reviewed; comments only, no new source files.
- Jaipur repository mapping remains unresolved in central audit; root README/AGENTS were not accessible. No Jaipur write made.
- Clever Ape and other unverified/ambiguous brand mappings remain untouched.
- No brand PR was merged, deployed, published or indexed.

## Checks and blockers

- Groot #609: GitHub read-back passed for article, SVG and metadata; 3 ahead / 0 behind; mergeable=true. Local SVG XML/dimensions, PNG render/visual inspection and WebP optimization passed. No workflow runs returned; independent editorial/source QA and browser QA pending.
- Forsk #170: GitHub read-back passed for article, SVG and metadata; 4 ahead / 0 behind; mergeable=true. Local SVG XML/dimensions, PNG render/visual inspection and WebP optimization passed. No workflow runs returned; independent editorial/source QA and browser QA pending.
- Forsk #156 and #163/#164/#166 received current official status comments; Mango #143/#159 and Forsk #145/#146 also received revalidation comments.
- No relevant YouTube video ID plus embedding permission was independently verified for the two new drafts; no video was downloaded/re-uploaded and no iframe was claimed tested.
- Central PR #19 remains diverged by two commits; central PR #20 remains diverged by two commits. Both are left untouched except the existing PR #19 checkpoint comment; no rebase/merge.
- No live publication, deployment, application submission or indexing occurred.

## Incremental production ledger

| Status | This run |
|---|---:|
| New distinct research items | 2 (AgentCore Runtime V2 technical guide; SRFP 2027 opportunity) |
| New original article drafts | 2 |
| New original SVG graphics | 2 |
| Local PNG/WebP preview derivatives | 4 |
| Independent QA-ready articles | 0 |
| Live/published articles | 0 |

Historical cumulative totals were not recalculated from the full archive in this run; use the central master ledger for cumulative counts.

## 2026-11-11 — News Factory cycle, 03:03 IST

### New delivery — Mango Engineers

- Opened Draft PR #166: https://github.com/satnamkhowal/mangoengineers.com/pull/166
- Branch: `content/news-factory-bigquery-dataframes-20261111-0303`; base: `main@8eeb57fdf05341aa0a5ec31846148a37b0be3ba6`; compare: 3 commits ahead / 0 behind.
- Three new paths only: a 2,100-word English guide, an original 1200×675 SVG, and a JSON provenance/SEO sidecar.
- Topic: Google Cloud's BigQuery DataFrames `.bigquery` accessor article, published 6 November 2026. No separate event date was stated.
- Covers embeddings, similarity, forecasting, TabFM prediction, `if_()`, IAM, billing, India-region caveats, synthetic student project and FAQs.
- TabFM and TimesFM 3.0 are labelled Preview as stated in official sources; the whole accessor is not described as GA.
- Distinct from Groot PR #592 (BigQuery pipeline concurrency/Zstandard SQL); no matching BigQuery DataFrames accessor draft was found in Mango's open PR inventory.
- Original SVG source is committed. PNG preview (126,583 bytes) was visually inspected; WebP derivative (44,636 bytes) was optimized locally but neither derivative is committed. Asset metadata records source, self-authored permission, attribution, alt text, dimensions and hashes.
- No relevant verified YouTube ID plus embed permission; no iframe. No video download/re-upload.

Primary sources:
- https://cloud.google.com/blog/products/data-analytics/bigquery-ai-functions-in-pandas
- https://dataframes.bigquery.dev/
- https://docs.cloud.google.com/bigquery/docs/permissions-for-ai-functions
- https://docs.cloud.google.com/bigquery/docs/locations
- https://docs.cloud.google.com/bigquery/docs/best-practices-costs
- https://docs.cloud.google.com/bigquery/docs/control-genai-costs
- https://cloud.google.com/model-garden/pricing
- https://cloud.google.com/blog/products/data-analytics/tabfm-adds-predictive-ml-to-bigquery

### Research tracks — current status

- **Opportunities:** Google Careers' Student Researcher, 2027 page currently displays Apply, India / Remote eligible, and a 4 December 2026 deadline with rolling review. Existing Forsk PR #146 remains owner; no duplicate. Official MeitY Digital India Internship Scheme 2026 schedule shows applications closed 29 April 2026 and internship completed 31 July; do not promote it as open. E&ICT Academy IIT Roorkee's official course listing shows seven Winter Training and Internship offerings (Generative AI & Prompt Engineering, Data Science using Python, Machine Learning & Agentic AI, AI-Powered Full Stack Web Development, Ethical Hacking & Cyber Security, Semiconductor Technology, IoT & Edge AI), each listing ₹8,000 incl. GST and 29 November 2026 application deadline. Detailed individual course pages did not expose duration, eligibility, schedule, stipend or internship deliverables in this check; hold a full article until those facts are verified. A separate IIT Roorkee FDP on Recent Cyber Security Trends and Technologies lists ₹500, 16–20 November 2026, with application deadline 14 November on the E&ICT course listing; distinguish it from student internships.
- **React/frontend:** Official React releases page still lists 19.3.1, 19.2.9, 19.1.10 and 19.0.9, all dated 14 October 2026. No newer stable tag or November release was found. Existing Forsk PR #145 remains owner for the October RSC advisory.
- **Node.js/backend:** Official 11 November security notice still states releases are expected on or shortly after 11 November and HIGH is the highest severity in 26.x, 24.x and 22.x. At 03:03 IST the notice had no CVE IDs or patched versions; no release article is created ahead of the actual release.
- **AI/cloud/developer:** The BigQuery DataFrames accessor article is assigned to Mango PR #166. TPU Sync (9 November) already has Groot PR #582; no duplicate. Other current AI/cloud owners remain unchanged.

### Repository/access audit

- Mango: read `AGENTS.md`, `docs/agent-start-here.md`, `docs/task-board.csv`, `docs/work-log.md`, `docs/integration-queue.md`, latest main commit and open News Factory PR inventory before the new branch. No matching BigQuery accessor draft existed.
- Mango shared task-board file is also changed by open PR #51; this cycle did not modify the shared task board or work log to avoid a conflicting write. Task ID `NF-ME-BIGQUERY-DATAFRAMES-20261111-0303` is recorded here; add the task-board row after the existing shared-file PR is reconciled.
- Forsk: open PR inventory was read; current default-branch README/AGENTS content requests returned 404 through the connector, so no write was made.
- Groot: README is only `# gta`; root AGENTS.md was not present. Open News Factory PR inventory checked; no write was made.
- Jaipur Engineers: verified candidate repository `satnamkhowal/jaipur-engieneers` has no accessible README and no open News Factory PRs in this check. Canonical repository/brand mapping remains unresolved; no write was made.
- Other listed brands remain read-only unless canonical repo and instructions are verifiable.

### Checks and blockers

- Mango PR #166 read-back passed for article, SVG and metadata; metadata JSON parsed; SVG dimensions 1200×675; local PNG/WebP dimensions verified; PNG visually inspected; WebP optimized.
- GitHub compare: 3 ahead / 0 behind, 3 added files. PR snapshot reports `mergeable=false`; do not merge.
- Workflow run 42907577880 (PHP Architecture Check) completed with failure. The job step list was empty and log download returned BlobNotFound; combined commit status returned no statuses. Cause is unknown and must not be represented as a content failure or a pass.
- Code snippets were matched to official documentation but not executed against a paid Google Cloud project. Independent editorial/source QA and responsive browser QA pending.
- No PR merged; no deployment, live publication, application submission or indexing.

### Incremental ledger for this cycle

| Status | Increment |
|---|---:|
| New distinct verified research items | 1 (BigQuery DataFrames accessor article, publication 6 Nov) |
| New original article drafts | 1 |
| New original SVG graphics | 1 |
| Local PNG/WebP derivatives | 2 |
| Independent QA-ready | 0 |
| Live / published | 0 |

Prior cumulative archive counts are not recalculated here.


## 2026-11-11 — News Factory cycle, 03:03 IST (second production item)

### New Mango Engineers draft

- Opened Draft PR #167: https://github.com/satnamkhowal/mangoengineers.com/pull/167
- Branch: `content/news-factory-ple-benchmark-20261111-0303`; base `main@8eeb57fdf05341aa0a5ec31846148a37b0be3ba6`; compare: 3 commits ahead / 0 behind.
- Three documentation-only files: 2,051-word original English article, original 1200×675 SVG infographic, JSON provenance/SEO sidecar.
- Topic: Google's Physical-Engineering's Last Exam (PLE), announced 3 November 2026; no separate event date stated. arXiv paper v2 date is 30 October 2026.
- Facts reconciled: 85 total tasks = 29 public dev + 56 hidden; disciplines: mechanical 30, electrical 27, civil 18, structural 10; 6-hour task limit; gated Hugging Face dev set.
- Licence distinction: dataset CC BY 4.0; Google research code Apache 2.0.
- Competition page had no deadline, prize amount or entry fee listed; no India-specific eligibility list was found. Article directs readers to current Kaggle rules.
- Google/Mercor announcement says 13 sponsored models can run free; current competition guide lists eight model IDs. Discrepancy is disclosed; live guide is used for implementation.
- Strong safety caveat: benchmark is not a professional licence, engineering approval or evidence of Indian BIS/NBC/IS compliance.
- Original vector graphic created in-house; no PLE screenshots or third-party graphics reused. Local PNG (122,545 bytes) visually inspected and local WebP (48,624 bytes) optimized; only SVG source is committed. Metadata records source, permission, attribution, alt text, dimensions and hashes.
- No suitable verified YouTube ID plus embed permission; no iframe.

Primary sources:
- https://cloud.google.com/blog/products/ai-machine-learning/introducing-physical-engineerings-last-exam-for-agents
- https://ple-bench.com/
- https://ple-bench.com/competition
- https://ple-bench.com/competition/guide
- https://ple-bench.com/competition/agents
- https://github.com/google-research/ple
- https://huggingface.co/datasets/google/physical-engineerings-last-exam
- https://arxiv.org/abs/2610.30537
- https://www.mercor.com/blog/introducing-physical-engineering-s-last-exam-ple-with-google-cloud-ai-research/

### Opportunities and programme verification

- **Google Student Researcher, 2027:** direct Google Careers page still displays Apply, India / Remote eligible, deadline 4 December 2026 and rolling review. Minimum degree enrolment includes Bachelor's, Master's or PhD in listed fields. Stipend and application fee are not stated. Existing Forsk PR #146 remains owner; a status comment with the direct listing was added.
- **Science Academies SRFP 2027:** official application and instruction pages confirm deadline 30 November 2026, two-month fellowship during 2027, students/teachers studying or teaching in India, listed degree/year combinations, 65% core-subject average for students, PhD students ineligible, one application per candidate, mark-sheet upload requirements and a current teacher contact for recommendation. Selected fellows receive entitled round-trip train fare plus a monthly fellowship; the amount is not stated. Existing Forsk PR #170 remains owner; official-status comment added.
- **Digital India Internship — Winter 2026:** official NIC portal (last updated 11-11-2026) shows registration starts 2 November 2026 and duration 1 December 2026–31 January 2027, **offline mode only**. The public page does not expose the closing date, stipend or full eligibility in text. The official guideline PDF timed out in web and container retrieval. An E&ICT Academy social post claims 13 November deadline, 50 seats and ₹10,000/month, but those claims are not confirmed by the accessible official portal/PDF; do not publish them as verified until the guideline is accessible.
- **E&ICT Academy IIT Roorkee Winter Training and Internship listing:** official course catalogue currently lists seven courses (Generative AI & Prompt Engineering, Data Science using Python, Machine Learning & Agentic AI, AI-Powered Full Stack Web Development, Ethical Hacking & Cyber Security, Semiconductor Technology, IoT & Edge AI), each showing ₹8,000 incl. GST and 29 November 2026 application deadline. Detailed individual course pages did not expose duration, eligibility, timetable, stipend or internship deliverables in this check; hold a full opportunity article until these facts are confirmed. The separate FDP on Recent Cyber Security Trends and Technologies is listed for 16–20 November 2026, ₹500 incl. GST, deadline 14 November; do not conflate an FDP with a student internship.

### React / Node.js / AI-cloud

- **React:** official releases page still shows 19.3.1, 19.2.9, 19.1.10 and 19.0.9, all dated 14 October 2026. No newer stable release or fresh November advisory found. Existing Forsk PR #145 remains owner.
- **Node.js:** official 11 November security notice still describes a planned release on or shortly after 11 November; HIGH is the highest severity across 26.x, 24.x and 22.x. At 03:03 IST, no CVE IDs or patched versions were listed. Releases page latests: 26.13.0 LTS (28 Oct), 24.22.2 LTS (28 Oct), 22.23.4 LTS (21 Oct); 27.0.0-alpha.0.0.0 (29 Oct) is pre-release. Existing Mango PR #143 remains owner; no premature patch article.
- **AI/cloud:** PLE is a new Mango topic. BigQuery DataFrames accessor remains Mango PR #166. Groot PR #608 already covers OpenRL, llm-d, KubeRay, Agent Substrate and gVisor; Groot #609 covers AgentCore Runtime V2. No duplicate created.

### Repository access and coordination

- Mango: latest main, root AGENTS, `docs/agent-start-here.md`, task board, work log, integration queue and open PR inventory checked before writes. PR #166 and #167 are separate, non-overlapping topics.
- Mango task-board/work-log files were not edited because existing open PR #51 also modifies those shared files. Both new task IDs are recorded in this checkpoint; add task-board rows after #51 is reconciled.
- Forsk: open PR inventory checked; README/AGENTS contents still returned 404 through the connector. Status comments were added to existing PRs #146 and #170; no source-file write.
- Groot Academy: README is only `# gta`; root AGENTS absent. Existing #608/#609 owners preserved; no write.
- Jaipur Engineers: `jaipurengineers.com` README/AGENTS unavailable through connector; existing PR #44 owner preserved; no write.
- CadMate India and Forsk Technologies repositories were inspected read-only; no suitable new article/queue owner was established. Groot Software candidate repositories remain ambiguous. Clever Ape Academy root README is unavailable. No write to these repositories.

### PR / QA state

- Mango PR #167: 3 ahead / 0 behind, 3 added files; read-back passed; metadata JSON valid; SVG XML and 1200×675 dimensions valid; local PNG visually inspected; WebP optimized.
- Mango PR #167 workflow run 42908957857, PHP Architecture Check: **failure**. Job step summary unavailable; log download returned BlobNotFound; combined status returned no statuses. Cause unknown. PR snapshot says `mergeable=false`; leave Draft.
- Mango PR #166 remains Draft; prior run 42907577880 PHP Architecture Check also failed with unavailable job/log data (BlobNotFound). No CI pass is claimed.
- Both articles' code/competition procedures are source-checked; no paid Cloud code execution or competition entry was performed.
- Independent editorial/source QA and responsive browser QA remain pending for #166 and #167.
- No merge, deployment, publication, application submission or indexing.

### Incremental ledger for this cycle

| Status | Increment |
|---|---:|
| New verified distinct research items | 1 (PLE benchmark) |
| New original article drafts | 1 |
| New original SVG graphics | 1 |
| Local PNG/WebP derivatives | 2 |
| Existing opportunity status rechecks | 2 (Google Student Researcher, SRFP 2027) |
| New opportunity leads held for more evidence | 2 (DII Winter 2026, E&ICT IIT Roorkee winter courses) |
| Independent QA-ready | 0 |
| Live / published | 0 |

Prior cumulative archive counts are not recalculated here.
