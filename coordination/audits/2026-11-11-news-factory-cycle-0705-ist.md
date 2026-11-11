# News Factory cycle — 11 November 2026, 07:05 IST

## Summary

This run completed four non-overlapping research lanes and produced two new, brand-specific draft PRs:

1. **Mango Engineers — NCDC January 2027 internship guide**, focused narrowly on the official Mathematics/Biostatistics and MSc Statistics eligibility routes. Draft PR #170.
2. **Groot Academy — DynamoDB bulk put items GA guide**, focused on S3 ingestion, performance tiers, India-region availability, pricing caveats and operational limits. Draft PR #615.

Each draft has an original self-authored 1200×675 SVG and a provenance sidecar. Four local raster derivatives (two PNG and two WebP) were generated, visually inspected and dimension-checked. No third-party image or video was downloaded. No story-specific YouTube ID and embedding availability were verified, so no iframe was added.

No merge, deployment, live publication, indexing or application submission occurred. Both PR creation responses initially reported `mergeable=false`; after GitHub metadata refresh, both PR snapshots report `mergeable=true`. They remain Draft pending independent QA and approval.

## 1. Official student, developer and scholarship opportunities

### New draft — NCDC January 2027 internship (Mango Engineers PR #170)

- Official source: https://ncdc.mohfw.gov.in/includes/Work_With_Us/internship.php
- The NCDC page footer says **Last Updated On 04-11-2026**. It does not state a separate original publication date.
- The page lists an online application window of **1–30 November 2026**.
- Document verification is listed for **8–9 December 2026** at the DPD Division.
- Selected candidates are to be informed to join from **1 January 2027**, subject to Director NCDC approval.
- Duration: **2–6 months**, depending on suitability and division requirements.
- Application fee: **₹500** by demand draft to Director, NCDC, payable at Delhi; the draft is to be submitted at document verification.
- No stipend/remuneration amount is published on the page.
- **IDSP** lists Mathematics and Biostatistics graduates among eligible backgrounds; it lists five tentative seats per year and up to six months.
- **Centre for Environment and Occupational Health, Climate Change and Health** lists MSc Statistics among several eligible disciplines; it lists six tentative seats per year and up to six months.
- Generic BTech Computer Science, BTech IT, BCA, MCA, AI and software-engineering degrees are not listed as standalone eligibility for these data-related routes.
- The NCDC page says the coordinating division submits a proposed plan of action for the 2027 cycle for approval; the page does not state the approval outcome. The article retains this caveat.
- The official page links to a Google Form. During this run the link redirected to Google sign-in, so the form itself could not be independently inspected. The article directs applicants to use the official page's link and confirm form status before paying.

**Article:** `docs/news-factory/drafts/ncdc-internship-2027-statistics-biostatistics-eligibility.md` — 1,935 words.  
**Original SVG:** `docs/news-factory/media/ncdc-internship-2027-eligibility.svg` — 1200×675.  
**Metadata:** `docs/news-factory/drafts/ncdc-internship-2027-statistics-biostatistics-eligibility.metadata.json`.  
**PR:** https://github.com/satnamkhowal/mangoengineers.com/pull/170

Mango's current Data Analytics and Data Science course pages were checked before adding contextual internal links:
- https://mangoengineers.com/data-analytics-course-jaipur
- https://mangoengineers.com/data-science-course-jaipur

The article clearly states that course enrolment or a short analytics certificate does not confer NCDC eligibility.

### Existing Google opportunity — revalidated, no duplicate

- Official Google Careers listing: https://www.google.com/about/careers/applications/jobs/results/125423735539671750
- **Student Researcher, 2027** still displays an Apply control.
- Location: **India — Remote eligible**.
- Deadline: **4 December 2026**; Google says applications are reviewed on a rolling basis.
- Minimum enrolment: Bachelor's, Master's or PhD in the listed disciplines, including Computer Science, Statistics, Biostatistics, Applied Mathematics, Operations Research, Economics and Natural Sciences.
- Relevant computer-science experience is required; preferred qualifications include research and programming experience.
- Applicants must remain in a country location specified by the listing for the full engagement.
- No stipend, application fee or fixed programme duration is published on the listing.
- Existing Forsk PR #146 remains the owner. A 07:05 IST status comment was added; no duplicate article was created.

### Existing deadlines rechecked

- **NMMSS 2026–27:** PIB's 31 October 2026 release continues to state the revised student deadline of **15 November 2026**, L1 verification by 30 November and L2 verification by 15 December. Existing Forsk PR #173 remains the owner. A status comment was added. Source: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2330936&lang=1&reg=3
- **VSSC Academic Project Work 2027:** existing Forsk PR #172 remains the owner. The current VSSC instructions page confirms Indian-citizen eligibility, the 60% / CGPA 6.32 minimum, MSc Computer Science in Data Analytics and Data Science among eligible postgraduate subjects, unclassified-area restriction, no stipend/remuneration/financial assistance, and no VSSC project-work fee. The separate UG and PG route deadlines already recorded in PR #172 remain distinct: 15 November and 16 November 2026 respectively. Source: https://vsscinternship.vssc.gov.in/HRDD_LOGIN/instructionBeforLogin.jsp
- No additional scholarship or grant was promoted as newly open in this run. Existing AICTE, UGC, ANRF, NITI Aayog and other opportunity owners were preserved.

## 2. React / frontend

- Official React blog: https://react.dev/blog
- Latest stable announcement remains **React 19.3**, dated **9 September 2026**.
- Official release page still lists the latest maintenance tags as **19.3.1, 19.2.9, 19.1.10 and 19.0.9**, all dated **14 October 2026**.
- The 14 October React Server Components advisory GHSA-xqc2-xf4c-x3h3 is Critical, CVSS 9.5, and now lists CVE-2026-126187. Patched package versions are 19.0.9, 19.1.10, 19.2.9 and 19.3.1.
- The existing second RSC advisory GHSA-h3gv-c5rc-p453 remains within Forsk PR #145's existing security-update scope.
- No new November React stable release or new November React security advisory was found.
- Existing Forsk PR #145 remains the sole React RSC security owner; a 07:05 IST recheck comment was added.

Sources:
- https://react.dev/blog
- https://github.com/react/react/releases
- https://github.com/react/react/security/advisories/GHSA-xqc2-xf4c-x3h3

## 3. Node.js / backend security

- Official release index: https://nodejs.org/en/blog/release
- Latest visible release tags at 07:05 IST:
  - Node.js 26.13.0 LTS — 28 October 2026.
  - Node.js 24.22.2 LTS — 28 October 2026.
  - Node.js 26.12.1 Current — 21 October 2026.
  - Node.js 24.22.1 LTS and 22.23.4 LTS — 21 October 2026.
  - Node.js 27.0.0-alpha.0.0.0 — 29 October 2026.
- The official advance notice is dated **3 November 2026, 23:00 UTC** and schedules security releases for 26.x, 24.x and 22.x on or shortly after **11 November 2026**. Highest severity is HIGH in each line.
- At 07:05 IST, the official release index had not yet listed the 11 November patched releases. The advance notice still does not disclose CVE IDs, affected patch ranges or patched versions.
- Existing Mango PR #143 remains the Node.js security-readiness owner. A 07:05 IST status comment was added; no premature patched-release article was created.

Sources:
- https://nodejs.org/en/blog/release
- https://nodejs.org/en/blog/vulnerability/november-2026-security-releases
- https://github.com/nodejs/nodejs.org/blob/main/apps/site/pages/en/blog/vulnerability/november-2026-security-releases.md

## 4. AI / cloud / developer news

### New draft — Amazon DynamoDB bulk put items GA (Groot Academy PR #615)

- Official GA announcement publication date: **5 November 2026**.
- AWS Weekly Roundup mention: **9 November 2026**. This is a later roundup date, not the original announcement date.
- No separate launch event date is stated.
- The feature loads S3 data into existing active DynamoDB tables through a managed asynchronous operation.
- Input formats: line-delimited DynamoDB JSON or Amazon Ion; gzip and zstd compression are optional.
- Each item may carry its own condition expression, supporting insert-only and version-guarded writes.
- Standard tier: up to **100 GB** per operation; available in all commercial AWS Regions and AWS GovCloud (US).
- Accelerated tier: up to **1 TB** per operation; the current regional list includes Asia Pacific (Mumbai) and Asia Pacific (Hyderabad).
- The AWS Database Blog's US East (N. Virginia) examples are **$0.10/GB Standard** and **$0.20/GB Accelerated**. These are not India price quotes. The article directs readers to the current regional pricing page.
- The article includes table/account concurrency limits, global-table and vector-index launch restrictions, whole-item-only behaviour, S3 error reports, downstream stream-consumer considerations, current pricing-page caveats and the critical warning that cancellation does not roll back already-written items.
- No claim is made that Groot Academy is an AWS partner, reseller or customer.
- Groot's AWS Cloud Computing course route was verified before adding an internal learning link: https://grootacademy.com/courses/aws-course-jaipur/

**Article:** `docs/news-factory/drafts/dynamodb-bulk-put-items-s3-import-guide-2026.md` — 2,696 words.  
**Original SVG:** `docs/news-factory/media/dynamodb-bulk-put-items-architecture.svg` — 1200×675.  
**Metadata:** `docs/news-factory/drafts/dynamodb-bulk-put-items-s3-import-guide-2026.metadata.json`.  
**PR:** https://github.com/satnamkhowal/grootacademy.com/pull/615

Primary sources:
- https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-dynamodb-now-supports-bulk-put-items/
- https://aws.amazon.com/blogs/database/introducing-bulk-put-items-for-amazon-dynamodb-load-data-from-amazon-s3-into-existing-tables-at-scale/
- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BulkPutItems.Tiers.html
- https://aws.amazon.com/dynamodb/pricing/
- https://aws.amazon.com/blogs/aws/aws-weekly-roundup-agentcore-runtime-v2-amazon-dynamodb-bulk-put-items-and-more-november-9-2026/

### Existing AI/cloud owners preserved

- Groot PR #611 remains the OpenSearch clone-upgrade owner; DynamoDB bulk put items is a separate service and distinct topic.
- Existing AgentCore Runtime V2, Google AI-native Kubernetes, S3 Tables, BigQuery and other cloud drafts were not regenerated.
- Groot's 100K content controller remains on GA-B00016. The 29-row `marketing/blog-factory/queue/blogs.csv` was inspected; no DynamoDB bulk put items topic was present. The queue/controller were not changed.

## 5. Repository review and ownership

### Central control center

- Central News Factory PR #19 remains the append-only checkpoint lane. PR #20 (Groot 100K deduplication) was not modified.
- Before the new 07:05 audit append, PR #19's branch `ops/news-factory-cycle-20261109-2209` was **76 commits ahead / 2 behind** central main. The last observed comparison before this audit amendment was **82 commits ahead / 3 behind**; the branch remains diverged, and no rebase or merge was attempted.
- Brand implementation stays in each brand repository.

### Mango Engineers

- Read current `AGENTS.md`, `docs/agent-start-here.md`, task board, work log and integration queue.
- PR #151 owns shared task-board/work-log/integration-queue files; they were not modified.
- PR #143 owns Node.js readiness; #162 .NET 11; #163 Rubrik DevOps Protection; #170 is the new NCDC opportunity draft.
- PR #170 is limited to three new News Factory paths; no PHP route, course page, sitemap, schema, navigation or production asset path changed.

### Groot Academy

- Read `.agent/README.md`, `.agent/MASTER-HANDOFF.md`, `.agent/CURRENT-STATE.md`, `.agent/BACKLOG.md`, `.agent/DECISIONS.md`, migration status, blog-publishing instructions, 100K controller and queue.
- PR #611 owns OpenSearch clone upgrades; PR #615 is a distinct DynamoDB bulk put items guide.
- The 100K controller's GA-B00016 browser gate and runtime blockers remain unchanged. No blog registry, PHP route, migration map, sitemap, shared course data or production file was modified.

### Forsk Coding School

- Read current `README.txt` and `docs/ai-ops/MASTER_TASK_BOARD.md`.
- Existing PR #145 owns React RSC security, #146 Google Student Researcher, #172 VSSC, #173 Git security/NMMSS, #168 Copilot Gemini, #171 C++ language server and #165 Dependabot.
- Fresh status comments were added to #145, #146, #172 and #173. No new Forsk article was opened in this run.

### Jaipur Engineers

- Canonical repository remains `satnamkhowal/jaipurengineers.com`; root README/AGENTS were not found in the current read.
- Existing NITI Aayog and other opportunity owners remain untouched.
- No Jaipur write was made because no separate approved News Factory draft lane was established.

### Other brands

Clever Ape Academy, CadMate India, Groot Software and Forsk Technologies were not given new writes; their canonical repository/source mappings remain unverified for this cycle.

## 6. Implementation and QA

### Mango Engineers PR #170
- URL: https://github.com/satnamkhowal/mangoengineers.com/pull/170
- Branch: `content/news-factory-ncdc-internship-20261111-0705`
- Initial compare: 3 commits ahead / 0 behind main; after the seat-count and provenance refreshes, final compare is 11 commits ahead / 0 behind; exactly three additive files.
- After source-wording correction, the article, SVG and provenance JSON were updated sequentially. No shared file was changed.
- GitHub read-back: article 1,935 words; metadata JSON parses and records 1,935; SVG has 1200×675 dimensions, title/description and no scripts/external hrefs.
- Local PNG: 1200×675, 124,103 bytes, visually inspected.
- Local WebP: 1200×675, 57,860 bytes; dimensions and SHA-256 recorded in metadata.
- PR creation initially reported `mergeable=false`; after GitHub metadata refresh the PR snapshot reports `mergeable=true`. Independent editorial/source QA and responsive/browser QA remain pending.
- Two PHP Architecture Check runs on the earlier and current Mango PR heads (42941486566 and 42941989357) completed with failure. The latest job, php-architecture (130265737584), exposes no steps; fetching its log returned Azure Blob Storage BlobNotFound (404). The earlier job showed the same no-steps / BlobNotFound pattern. Combined status list is empty. This is an infrastructure/log-retrieval blocker, not a confirmed source-code defect; no blind rerun was started and no CI pass is claimed.

### Groot Academy PR #615
- URL: https://github.com/satnamkhowal/grootacademy.com/pull/615
- Branch: `content/news-factory-dynamodb-bulk-put-20261111-0705`
- Initial compare: 3 commits ahead / 0 behind main; after two pricing/provenance updates, final compare is 5 commits ahead / 0 behind; exactly three additive News Factory files.
- GitHub read-back: article 2,696 words; metadata JSON parses and records 2,696; SVG has 1200×675 dimensions, title/description and no scripts/external hrefs.
- Local PNG: 1200×675, 125,774 bytes, visually inspected.
- Local WebP: 1200×675, 48,060 bytes; dimensions and SHA-256 recorded in metadata.
- PR creation initially reported `mergeable=false`; after GitHub metadata refresh the PR snapshot reports `mergeable=true`. Independent editorial/source QA and responsive/browser QA remain pending.
- No PR-triggered workflow runs or combined status checks were returned for the Groot PR head; no CI pass is claimed.

### Video and media policy

- Original SVG graphics committed: **2**.
- Local raster derivatives: **4** (2 PNG + 2 WebP).
- Third-party graphics downloaded: **0**.
- Story-specific official/reputable YouTube IDs with verified embedding availability: **0**; no iframe added.
- Videos downloaded or re-uploaded: **0**.
- All media provenance sidecars record source, permission basis, attribution, alt text, dimensions, local paths and SHA-256 hashes.

## 7. Production ledger

| Status | Increment this cycle |
|---|---:|
| New distinct researched items | 2 (NCDC January 2027 internship; DynamoDB bulk put items GA) |
| Existing opportunity status rechecks | 3 (Google Student Researcher, NMMSS and VSSC); NCDC is counted as a new research item |
| React / Node status rechecks | 2 lanes; no new release articles |
| New English article drafts | 2 |
| Existing articles materially rewritten | 0 |
| Original SVG graphics | 2 |
| Local PNG/WebP derivatives | 4 |
| Independent QA-ready articles | 0 |
| Live / published articles | 0 |

Carried-forward checkpoint from 06:05 IST: 76 researched, 64 drafted, 64 original SVG graphics, 33 independent QA-ready, 0 live. Adding the two new distinct research items, two drafts and two SVGs gives a **provisional cumulative ledger of 78 researched, 66 drafted, 66 original SVG graphics, 33 independent QA-ready and 0 live**. This is a carried-forward ledger, not a fresh reconciliation of the entire historical archive.

## 8. Next actions

1. Independent editorial/source QA and responsive/browser QA for Mango #170 and Groot #615.
2. Keep both new PRs Draft. Their refreshed GitHub snapshots now report `mergeable=true`, but independent QA and explicit approval are still required before any merge. Investigate the latest Mango PHP Architecture Check run 42941989357 / job 130265737584 through repository administrators because the job has no visible steps and its log endpoint returned BlobNotFound; the earlier run 42941486566 showed the same pattern. Do not blindly rerun.
3. Recheck NCDC's official form and the 2027 approval status before the 30 November window closes; the form redirected to Google sign-in in this run.
4. Recheck the official Node.js release index and security advisories when the 11 November patches actually publish; update Mango #143 only with real CVEs and patched versions.
5. Keep Forsk #145 as React owner unless the official React team announces a new release/advisory.
6. Monitor NMMSS 15 November and VSSC 15/16 November application cut-offs; keep existing owners.
7. Preserve central PR #19 divergence and PR #20; owner-led reconciliation only. No merge or deployment without approval.

## Pull request links

- Mango Engineers — NCDC Internship 2027: https://github.com/satnamkhowal/mangoengineers.com/pull/170
- Groot Academy — DynamoDB bulk put items GA: https://github.com/satnamkhowal/grootacademy.com/pull/615
- Mango Engineers — Node.js security owner: https://github.com/satnamkhowal/mangoengineers.com/pull/143
- Forsk Coding School — React RSC security owner: https://github.com/satnamkhowal/forsk-coding-school/pull/145
- Forsk Coding School — Google Student Researcher: https://github.com/satnamkhowal/forsk-coding-school/pull/146
- Forsk Coding School — VSSC Academic Project Work: https://github.com/satnamkhowal/forsk-coding-school/pull/172
- Forsk Coding School — Git security / NMMSS: https://github.com/satnamkhowal/forsk-coding-school/pull/173
- Groot Academy — OpenSearch clone-upgrade owner: https://github.com/satnamkhowal/grootacademy.com/pull/611
- Central News Factory coordination: https://github.com/satnamkhowal/brand-growth-control-center/pull/19

## 11 November 2026 — 12:10 IST research / ownership recheck

### Opportunity and scholarship lane
- Google Student Researcher, 2027 remains directly listed with an Apply control: India / Remote eligible; currently enrolled Bachelor's, Master's or PhD candidates in the named disciplines; relevant CS-area experience; apply before 4 December 2026; rolling review. No stipend amount or publication date is displayed. Existing Forsk PR #146 remains owner. Official page: https://www.google.com/about/careers/applications/jobs/results/125423735539671750-student-researcher-2027
- Google Careers' current India internship search results still list Software Engineering PhD Intern, Summer 2027 (job 109976286780105414) and Silicon Engineering Intern, PhD, Summer 2027 (job 109375266236572358). The two direct detail URLs did not load in this check, so today's Apply state, qualifications and deadlines are not reverified. Forsk PR #160 retains its 10 November direct-page verification as historical evidence only; do not upgrade the current status based on search-result snippets. Search page: https://www.google.com/about/careers/applications/jobs/results/cloud?hl=en&location=India&q=Internship
- VSSC current portal: INT 08 internship is closed; INT 09 is scheduled for 1 May–31 July 2027 with applications 15 February–15 March 2027. For UG/BE/BTech/BSc/Diploma academic project forms, the current Oct–Dec 2026 slot is closed; the next Jan–Mar 2027 slot lists 15 November 2026 as the form-submission deadline. For ME/MTech/Integrated MTech/MSc/BS-MS, the next Jan–June 2027 slot accepts online applications 15 October 2026 10:00 AM–16 November 2026 11:59 PM. The page also states Indian citizenship and at least 60% / CGPA 6.32 in its general project instructions. Existing Forsk PR #172 remains owner. Official portal: https://vsscinternship.vssc.gov.in/HRDD_LOGIN/beforelogincontroller
- NSP AY 2026–27 currently lists NMMSS student applications through 15 November 2026; defective/institute verification through 30 November and L2 through 15 December. AICTE Swanath (Technical Degree) and several other named schemes are listed through 30 November. The portal footer still says “Last update on June 2026”; treat the displayed dates as current portal status, but re-open each scheme's live form and current guideline before advising an individual applicant. Existing Forsk PR #173 / existing scheme owners remain unchanged. Official portal: https://scholarships.gov.in/All-Scholarships

### React / frontend lane
- React's latest stable blog announcement remains 19.3 (9 September 2026). Official patch tags remain 19.3.1, 19.2.9, 19.1.10 and 19.0.9, all dated 14 October 2026; no newer stable tag was found.
- The 14 October security advisories remain the current owner scope: critical unauthenticated RCE GHSA-xqc2-xf4c-x3h3 / CVE-2026-126187 and high Server Functions DoS GHSA-h3gv-c5rc-p453. Fixed RSC package versions include 19.0.9, 19.1.10, 19.2.9 and 19.3.1. Existing Forsk PR #145 remains owner; no duplicate article. Sources: https://github.com/react/react/releases and https://github.com/react/react/security/advisories

### Node.js / backend lane
- The official Node.js blog release index still lists 26.13.0 LTS (28 October), 24.22.2 LTS (28 October), 22.23.4 LTS (21 October), and 27.0.0-alpha.0.0.0 (29 October, Alpha). No 11 November security patch tag or CVE bulletin was visible at 12:10 IST.
- The security notice title refers to the planned release date (11 November); the notice itself was published/last updated 3 November 2026, schedules 26.x/24.x/22.x updates “on or shortly after” 11 November, and rates the highest issue HIGH. It does not disclose CVE IDs, affected patch ranges or fixed versions. Existing Mango PR #143 remains owner; do not mark patches shipped. Sources: https://nodejs.org/en/blog/release and https://nodejs.org/en/blog/vulnerability/november-2026-security-releases

### AI / cloud / developer lane
- GitHub's November changelog currently shows its latest entries dated 10 November: Enterprise Copilot seat-management API support, Gemini 4 Carbon in Copilot, C++ MSBuild auto-configuration and the inactive-repository Dependabot policy. Existing Forsk PRs #176, #168, #171 and #165 remain owners; no duplicate stories.
- AWS ElastiCache Serverless Valkey 9 search announcement (10 November) remains Groot PR #617; DynamoDB bulk-put GA remains Groot PR #615. No distinct new 11 November AWS/GCP/Azure developer announcement was verified.
- Research-only candidate, not a new news story: Microsoft's Azure AI Cloud Developer Associate / AI-200 exam. Certification page last updated 7 October; study guide last updated 30 October. The official guide lists a 120-minute exam and four domains: containerized Azure solutions (20–25%), AI data management (25–30%), connecting/consuming Azure services (20–25%), and securing/monitoring/troubleshooting (20–25%). India-specific exam price is not published on the page (price varies by proctored country); exam languages shown do not include Hindi. Official pages: https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-cloud-developer-associate/ and https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200
- Official Microsoft Learn video candidate: “Preparing for Exam AI-200: Develop containerized solutions on Azure (1 of 4)”, video ID XHOBLJQZBCU, channel Microsoft Learn, source https://www.youtube.com/watch?v=XHOBLJQZBCU (linked from the Microsoft Learn certification page). Exact upload date and embed availability were not independently verified; no iframe or embed-tested claim is recorded.

### Repository / ownership gate
- Forsk's current master board and session handoff require paired updates. Open News Factory PRs #160, #175 and #176 all modify those shared governance files; no new Forsk article branch was started to avoid conflicting edits.
- Mango's current News Factory ownership includes PRs #143 and #171; shared task-board/work-log paths are not reused for a new draft. Existing PR #170 remains its separate article/media scope.
- Groot alias satnamkhowal/grootacademy.com still points in its repository instructions to canonical satnamkhowal/gta; the canonical repository was not present in the accessible installed-repository search. Existing alias PRs #615/#617 were not modified; no new write until canonical identity is resolved.
- Jaipur Engineers remains read-only: no approved non-public News Factory article lane was found. Clever Ape Academy, CadMate India, Groot Software and Forsk Technologies remain unverified repository/source mappings; no writes.
- Central PR #19 remains diverged: 85 commits ahead / 4 behind current main. This append-only checkpoint is on the existing PR branch; no rebase, merge, PR #20 change or deployment.

### Production delta for this run
- New fully verified unowned story candidates: 0.
- Research-only content candidate: 1 (AI-200 guide; no new announcement and no safe non-overlapping write lane).
- Existing opportunity/release status lanes rechecked: Google Student Researcher, Google PhD listings, VSSC, NSP, React, Node.js and AI/cloud.
- New article drafts: 0; new original SVGs: 0; PNG/WebP derivatives: 0; verified YouTube embeds: 0; independent QA-ready increment: 0; live increment: 0.
- No third-party graphics or videos downloaded/re-uploaded. No new article was forced from an old announcement.

### Ledger reconciliation note
- The 07:05 checkpoint's carried-forward provisional ledger was 78 researched / 66 drafted / 66 original SVGs / 33 independent QA-ready / 0 live.
- Four subsequent News Factory PRs were verified on GitHub after that checkpoint: Mango #171, Forsk #175, Groot #617 and Forsk #176. Provisional carried-forward totals are therefore 82 researched / 70 drafted / 70 original SVGs / 33 independent QA-ready / 0 live. This remains a carried-forward estimate, not a full historical archive reconciliation.
