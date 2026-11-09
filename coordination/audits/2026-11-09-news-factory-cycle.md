# News Factory research and draft-production checkpoint

Date: 9 November 2026 (Asia/Kolkata)  
Research window: current-source verification completed during the 22:09 IST cycle  
Scope: Mango Engineers, Groot Academy, Forsk Coding School and Jaipur Engineers. No other brand was written because the central source-mapping queue still marks its repository/catalogue identity unresolved.

## Coordination baseline

- Central repository main observed at `31af61b9a796472b7eb13d6b254aa6d9dc2ecc34`.
- Central README says this repository is coordination-only and implementation belongs in each verified brand repository.
- Existing central coordination PRs #17 and #18 remain open draft PRs. They record Groot's repository rename/alias and the 100K controller/runtime delta; neither was edited by this cycle.
- Groot repository identity was verified as `satnamkhowal/gta` renamed to `satnamkhowal/grootacademy.com` (same repository ID 1375760757). The current content repository is `grootacademy.com`.
- Jaipur Engineers identity was verified as `satnamkhowal/je2` renamed to `satnamkhowal/jaipurengineers.com` (same repository ID 1369588932). `MIGRATION-NOTES.md` still identifies the `je2` application history as canonical; no Jaipur content write was made.
- The central queue continues to mark Clever Ape, CadMate, Groot Software and Forsk Technologies source/catalogue mapping as unresolved. No write was made to those repositories.
- The existing News Factory inventory and open PRs were inspected before creating a new article. No duplicate Cloud Pathways draft or media path existed.

## Research results

### 1. Student, developer and scholarship opportunities

Current official listings were rechecked:

- Google Careers — Research Scientist PhD Intern, Summer 2027, Hyderabad: the official page shows an application opening date of 28 October 2026 and closing date of 30 November 2026. Minimum qualifications include current PhD enrolment in a relevant technical field, ML experience, and Python/Java programming. The page shows an Apply control. Public compensation is not stated.  
  Source: https://www.google.com/about/careers/applications/jobs/results/87534302853505734-research-scientist-phd-intern-summer-2027
- Google Careers — Student Researcher, 2027: the official page shows India as the remote-eligible location and asks applicants to complete the application before 4 December 2026; rolling review is stated. Bachelor's, Master's and PhD enrolment are listed as eligible degree levels, subject to the role's subject and experience requirements.  
  Source: https://www.google.com/about/careers/applications/jobs/results/125423735539671750
- National Scholarship Portal 2026–27: NMMSS student applications are listed through 15 November 2026. AICTE Pragati technical-degree and technical-diploma schemes are listed through 30 November 2026. The portal footer still says last updated June 2026, so status must be rechecked on the live portal immediately before any student action. These are existing schemes, not newly announced November openings.  
  Source: https://scholarships.gov.in/All-Scholarships

No new opportunity article was added because existing drafts already cover Google internship/research and scholarship stories in Mango PR #143 and Groot PR #577. The deadlines are recorded here as a watch item, not as new draft counts.

### 2. React / frontend

- The official React release list still shows 19.3.1, 19.2.9, 19.1.10 and 19.0.9, all dated 14 October 2026.
- The two current React Server Components advisories checked are GHSA-xqc2-xf4c-x3h3 (Critical) and GHSA-h3gv-c5rc-p453 (High), both published 14 October. The current patched tags include 19.3.1, 19.2.9, 19.1.10 and 19.0.9 for the affected package lines.
- Existing Forsk PR #145 already owns the React Server Components security catch-up. No duplicate article or graphic was created.

Sources:
- https://github.com/facebook/react/releases
- https://github.com/facebook/react/security/advisories/GHSA-xqc2-xf4c-x3h3
- https://github.com/facebook/react/security/advisories/GHSA-h3gv-c5rc-p453

### 3. Node.js / backend

- The Node.js advance notice was published on 3 November 2026 and last updated the same day.
- It says 26.x, 24.x and 22.x security releases are expected on or shortly after 11 November 2026; the highest severity in each line is HIGH.
- As checked on 9 November, the notice does not list CVE IDs, affected patch ranges or patched versions. This remains a readiness notice, not a published patch.
- Mango PR #143 already owns the Node.js readiness article and graphic. No duplicate was created.

Source: https://nodejs.org/en/blog/vulnerability/november-2026-security-releases

### 4. AI / cloud / developer infrastructure

- Google Cloud published the Cloud Pathways GA announcement on 9 November 2026. Cloud Pathways is GA on GKE; the separate Cluster Director integration for Slurm clusters remains Preview.
- Google lists TPU v5e, v5p, Trillium (v6e) and Ironwood (TPU 7x) support on GKE, with versioned Pathways images supporting JAX 0.10.1+.
- The current official GKE TPU availability table does not list a Mumbai or Delhi TPU zone. The listed APAC Trillium zone is Tokyo.
- Cloud TPU prices are listed per chip-hour; the draft records selected on-demand examples and warns that GKE, storage, networking and other services add cost.

Sources:
- https://cloud.google.com/blog/topics/ai-infrastructure/cloud-pathways-a-distributed-ml-runtime-is-ga
- https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus
- https://cloud.google.com/tpu/pricing
- https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/run-workloads-pathways

## New production this cycle

### Groot Academy — Cloud Pathways guide

- Repository: `satnamkhowal/grootacademy.com`
- Base main: `0648b79ee0775e810251192a61b8ae6d842980f4`
- Branch: `content/news-factory-cloud-pathways-gke-ga-20261109`
- Draft PR: https://github.com/satnamkhowal/grootacademy.com/pull/580
- Files:
  - `docs/news-factory/drafts/cloud-pathways-gke-ga-november-2026.md`
  - `docs/news-factory/media/cloud-pathways-gke-ga-20261109.svg`
  - `docs/news-factory/drafts/cloud-pathways-gke-ga-november-2026.metadata.json`
- Output: one original English article draft (2,382 words), one original 1200×675 SVG, one source/media provenance JSON sidecar.
- The article distinguishes publication date from event date, records GKE GA versus Slurm Preview, explains India TPU-zone limits, documents prerequisites and IAM, and includes point-in-time TPU chip-hour examples.
- The SVG was authored for this article; no third-party graphics were downloaded. Local working path: `/mnt/data/news-factory/2026-11-09/cloud-pathways-gke-ga.svg`.
- Read-back checks: article and SVG exist on the branch; metadata JSON parses; SVG XML parses locally and has title/description and 1200×675 dimensions. No external image or linked media is embedded.
- Independent editorial/technical QA: PENDING. Browser rendering: NOT RUN. Workflow runs/status checks: none returned for the draft commit. PR remains open and unmerged.

## Existing News Factory work preserved

- Mango Engineers PR #143 — five existing draft topics (Django security, Gemini Omni 1.2 Flash, Google Research Scientist PhD Intern, Node.js November security notice, AICTE Pragati). React RSC material was intentionally left with Forsk to avoid cross-brand duplication.
- Forsk Coding School PR #145 — React Server Components October security catch-up.
- Groot Academy PR #577 — NMMSS scholarship draft.
- Groot Academy PR #578 — AWS S3 Tables managed Hive-to-Iceberg draft.
- Groot Academy PR #580 — new Cloud Pathways draft from this cycle.

All remain review/draft items. No merge, deployment, publication, indexing claim or production verification is made.

## Cycle counts

| Metric | This cycle |
| --- | ---: |
| New verified research items added to the queue | 1 Cloud Pathways GA item; existing openings/releases revalidated |
| New article drafts | 1 |
| New original graphics | 1 |
| New licensed external downloads | 0 |
| Verified story-specific YouTube embeds | 0 |
| Independent QA-ready drafts | 0 |
| Live/published articles | 0 |

## Next exact actions

1. Obtain independent technical/editorial review and browser rendering for Groot PR #580; do not merge before those gates.
2. On or after 11 November, recheck the Node.js official notice for actual patched versions, CVEs and affected ranges before converting the readiness article into a patch guide.
3. Recheck NMMSS on the live NSP portal before 15 November and Pragati before 30 November; if a deadline/status changes, update existing drafts rather than creating duplicates.
4. Keep React advisories and the existing Forsk PR #145 as the single React security content owner.
5. Continue source-mapping verification before writing for the remaining central brands.


## Additional opportunity draft — Forsk Coding School

A second distinct opportunity article was added after the first checkpoint commit:

- Official source: https://www.google.com/about/careers/applications/jobs/results/125423735539671750
- Current listing checked 9 November 2026: Student Researcher, 2027; India — Remote eligible; apply before 4 December 2026; rolling review.
- The listing does not state an opening date, fixed duration, stipend/salary amount or application-fee details. The article preserves those unknowns.
- It distinguishes this Bachelor's/Master's/PhD opportunity from the separate PhD-only Research Scientist PhD Intern role in Hyderabad.
- Repository: `satnamkhowal/forsk-coding-school`; base main `a690ef725029e8c7f96b6148e9012f82a481bd6d`.
- Branch: `content/news-factory-google-student-researcher-2027-20261109`.
- Draft PR: https://github.com/satnamkhowal/forsk-coding-school/pull/146
- Files: `docs/news-factory/drafts/google-student-researcher-2027-india.md`, `docs/news-factory/media/google-student-researcher-2027-india.svg`, and `docs/news-factory/drafts/google-student-researcher-2027-india.metadata.json`.
- Output: one original 2,113-word English opportunity guide, one original 1200×675 SVG and one source/media provenance sidecar.
- Read-back: all three files verified; metadata JSON parsed; SVG title/description/dimensions verified; local XML parse and PNG rendering passed.
- Independent editorial QA remains PENDING. No YouTube ID was verified and no iframe was added. No external media was downloaded. No merge, publication or application was performed.

Updated cycle production totals: 2 new article drafts, 2 original SVG graphics, 0 external licensed downloads, 0 verified YouTube embeds, 0 independent QA-ready drafts and 0 live articles.


## Additional scholarship research and draft — Forsk Coding School

A third distinct article was produced from the current NSP 2026-27 list:

- **AICTE Swanath Scholarship:** NSP lists degree and diploma scheme cards as open from 1 June through 30 November 2026 when checked on 9 November.
- The linked AICTE guideline is dated **May 2025**, and states ₹50,000 per annum, up to 2,000 annual awards (1,000 degree / 1,000 diploma), qualifying category requirements, an income ceiling of ₹8 lakh, regular-mode AICTE-approved study and a restriction on other Central/State/AICTE-sponsored scholarships.
- The NSP page footer still states last update June 2026; the draft preserves this staleness caveat and instructs applicants to recheck the live form.
- Repository: `satnamkhowal/forsk-coding-school`; base main `a690ef725029e8c7f96b6148e9012f82a481bd6d`.
- Branch: `content/news-factory-aicte-swanath-2026-27-20261109`.
- Draft PR: https://github.com/satnamkhowal/forsk-coding-school/pull/147
- Files: `docs/news-factory/drafts/aicte-swanath-scholarship-2026-27.md`, `docs/news-factory/media/aicte-swanath-2026-27.svg`, and `docs/news-factory/drafts/aicte-swanath-scholarship-2026-27.metadata.json`.
- Output: one original 2,106-word English guide, one original 1200×675 SVG and one source/media provenance sidecar.
- Read-back: all three files verified; metadata JSON parsed; SVG title/description/dimensions verified; local XML parse and PNG rendering passed.
- Independent editorial QA remains PENDING. No YouTube ID was verified and no iframe was added. No external media was downloaded. No merge, publication or application was performed.

### Research hold — AICTE Saksham

NSP currently lists AICTE Saksham degree and diploma cards through 30 November 2026, but the linked degree guideline is dated July 2020. It contains older scheme-year wording and must not be presented as a fully current 2026-27 eligibility guide without a newer AICTE/NSP clarification. No draft was produced from that stale guideline.

Updated cycle production totals: 3 new article drafts, 3 original SVG graphics, 0 external licensed downloads, 0 verified YouTube embeds, 0 independent QA-ready drafts and 0 live articles.


## Jaipur Engineers write boundary

The canonical `je2` alias resolves to `satnamkhowal/jaipurengineers.com` (repository ID 1369588932). Its current tree contains a live `news/` PHP article directory and `news/article-template.php`, but the inspected main branch has no `docs/news-factory/` draft lane and no root `AGENTS.md`. No article was added to the live news directory or a guessed draft path. Jaipur remains research-only until an approved draft convention or an isolated non-public draft path is established.


## Revalidation — 9 November 2026, 23:09 IST

### Fresh primary-source status

- **Google Student Researcher, 2027:** the live Google Careers page still shows India — Remote eligible, an Apply control, rolling review, Bachelor's/Master's/PhD enrolment and a request to complete the application before **4 December 2026**. The listing does not state an opening date, fixed duration or stipend/salary amount. Existing single-owner draft: Forsk PR #146. No duplicate was created.
- **Google Research Scientist PhD Intern, Summer 2027:** the live Google Careers listing shows Hyderabad, PhD enrolment, an opening date of **28 October 2026** and closing date of **30 November 2026**. Compensation is not stated on the public listing. Existing single-owner draft: Mango PR #143.
- **NSP 2026–27:** current scheme cards show NMMSS student applications through **15 November 2026**; AICTE Swanath degree and diploma through **30 November 2026**; AICTE Pragati degree and diploma through **30 November 2026**. The portal footer still says “Last update on June 2026”, so each status must be checked again immediately before publication or student submission. Swanath's linked guideline is dated **May 2025** and states ₹50,000 per year, up to 2,000 annual awards, an ₹8 lakh income ceiling, AICTE-approved regular-mode study and category/other-scholarship conditions. Existing single-owner drafts: Groot PR #577 (NMMSS), Forsk PR #147 (Swanath), Mango PR #143 (Pragati).
- **PM YASASVI Top Class Education in College:** NSP currently lists applications through 30 November, but the linked guideline is marked “as amended from 2023–2024” and the current notified institution/slot list was not independently confirmed. Research hold; no draft.
- **React:** official release history remains 19.3.1, 19.2.9, 19.1.10 and 19.0.9, all dated 14 October 2026. The two current React Server Components advisories checked are also dated 14 October. Forsk PR #145 remains the single React security content owner.
- **Node.js:** official advance notice remains dated 3 November 2026 and says 26.x, 24.x and 22.x security releases are expected on or shortly after 11 November, with HIGH as the highest severity in each line. No CVE IDs, affected patch ranges or patched versions are listed yet. Mango PR #143 remains the single Node.js readiness owner.
- **Cloud Pathways:** Google Cloud's official post is dated 9 November 2026; GKE is GA and the separate Cluster Director/Slurm integration is Preview. Google says the versioned Pathways images support JAX 0.10.1+. The current GKE TPU table lists no Mumbai or Delhi TPU zone; the listed APAC Trillium zone is Tokyo. The official pricing page confirms the article's selected examples ($1.20 v5e, $4.20 v5p, $3.24 Trillium and $12.00 Ironwood per chip-hour in the named regions). Groot PR #580 remains the single owner.

### Repository and PR reconciliation

- Central main remains 31af61b9a796472b7eb13d6b254aa6d9dc2ecc34; this checkpoint branch is 4 commits ahead / 0 behind and changes only this checkpoint file.
- Groot Academy canonical content repository is satnamkhowal/grootacademy.com. Its main advanced to a97dc07463a352ea924af3dea22af915a6f9bdb1 with one unrelated file, docs/ENGLISH-COMMUNICATION-IMAGE-WORKFLOW.md. PR #580 is 3 commits ahead / 1 behind; no changed-path overlap with the new draft/media files. Do not merge blindly; retain normal independent review.
- Forsk Coding School main remains a690ef725029e8c7f96b6148e9012f82a481bd6d. PRs #145, #146 and #147 are separate, 3 commits ahead / 0 behind each, with distinct owned paths.
- Mango Engineers main remains 8eeb57fdf05341aa0a5ec31846148a37b0be3ba6. PR #143 is 34 commits ahead / 0 behind and owns its five documented topics; PR #144 is a separate ME-B022 graphic handoff.
- Jaipur Engineers canonical repository is verified as satnamkhowal/jaipurengineers.com (the renamed je2 application). MIGRATION-NOTES.md says the current application is canonical; root README and AGENTS.md were not found, and no News Factory draft lane was identified. No Jaipur write was made.
- No unverified brand repository was used.

### Independent revalidation and production accounting

- Groot PR #580: independent article/source fact-check passed for publication date, GKE GA vs Slurm Preview, JAX minimum, GKE TPU region caveat, pricing basis and IAM/prerequisite claims. SVG source checks passed for 1200×675 dimensions, title/description, closed root element, no script, no external href and no embedded image. Browser rendering was not run; the metadata's prior local working path was not present in this run's local filesystem. Keep the PR **draft / not QA-ready** until media rendering and local-path provenance are resolved.
- Forsk PR #146 and #147: current official listing/guideline facts were rechecked; both SVG sources have 1200×675 dimensions, title/description and no script, external href or embedded image. Local rendering was not independently repeated in this run. Keep both **draft / not QA-ready** pending independent editorial and media review.
- This revalidation run added **0 article drafts, 0 graphics, 0 licensed external downloads and 0 YouTube embeds**. The preceding 22:09 cycle's checkpoint production remains **3 new drafts / 3 original SVGs / 0 independent QA-ready / 0 live**. No merge, deployment, publication, application submission or indexing action occurred.

### Next actions

1. Recheck NMMSS before 15 November and the current Google/AICTE application pages before their listed deadlines.
2. On or after 11 November, recheck Node.js for actual release tags, CVEs, affected ranges and patched versions before replacing the readiness guide with a patch guide.
3. Complete independent browser/media rendering and editorial review for Groot #580 and Forsk #146/#147.
4. Verify the current PM YASASVI notified-institution/slot list before deciding whether a separate article is useful.
5. Keep all current PRs unmerged and unpublished until their independent gates and owner approval are complete.


## Fresh research and draft-production cycle — 10 November 2026, 00:25 IST

### Four-track source scan

Research was split into four non-overlapping tracks: student/developer opportunities; React/frontend; Node.js/backend; and AI/cloud/developer infrastructure. Primary sources were used for all facts. No YouTube lead was promoted without official corroboration.

#### 1. Student, internship and scholarship status

- **Google Student Researcher, 2027:** the live Google Careers listing still shows India as remote-eligible, Bachelor's/Master's/PhD enrolment, rolling review and an instruction to complete the application before **4 December 2026**. The listing does not state an opening date, fixed duration or stipend. Existing single-owner draft remains Forsk PR #146; no duplicate.
  Source: https://www.google.com/about/careers/applications/jobs/results/125423735539671750
- **Google Research Scientist PhD Intern, Summer 2027:** the official Hyderabad listing shows an opening date of **28 October 2026**, closing date **30 November 2026**, current PhD enrolment in a relevant technical field, ML experience and Python/Java. Public compensation is not stated. Existing single-owner draft remains Mango PR #143; no duplicate.
  Source: https://www.google.com/about/careers/applications/jobs/results/87534302853505734
- **UGC National Scholarship for Post Graduate Studies 2026–27:** NSP currently lists the scheme window from **16 September to 30 November 2026**. The linked UGC scheme page says 10,000 slots per annum and ₹1,50,000 per annum for two years; the linked guideline expresses this as ₹15,000 per month for 10 months per year. Core conditions include Indian students in the first year of their first recognised PG degree, regular/full-time mode, below 30 at admission to the first PG semester/year and an eligible institution with a valid AISHE code. The FAQ says there is no income criterion, 30% of slots are reserved for women, and a student may not hold another scholarship/monetary benefit at the same time. The 2021 guideline PDF carries a 2026–27 note saying the 2025–26 HEI criteria may continue; institution eligibility must be checked. The NSP footer still says last update June 2026, so recheck the live form immediately before publication or submission. Existing single-owner draft remains Forsk PR #149; no duplicate.
  Sources: https://scholarships.gov.in/All-Scholarships ; https://www.ugc.gov.in/Scholarships/stu_Scholarship6 ; https://scholarships.gov.in/public/schemeGuidelines/Guidelines_NATIONAL_SCHOLARSHIP_FOR_POSTGRADUATE_STUDIES_UGC_2324.pdf ; https://scholarships.gov.in/public/FAQ/FAQ_NSPG.pdf
- **NMMSS:** NSP lists the student application deadline as **15 November 2026**. Existing Groot PR #577 remains the owner.
- **AICTE Swanath and Pragati:** NSP lists the relevant 2026–27 student application deadlines as **30 November 2026**. Existing Forsk PR #147 and Mango PR #143 remain the owners.
- **PM YASASVI Top Class Education in College:** NSP lists the student deadline as 30 November, but the current notified institution/slot list was not independently confirmed against the linked older guideline. Keep on research hold; no new draft.

#### 2. React / frontend

- The official React blog still lists React 19.3, published **9 September 2026**, as the latest major blog release in the checked feed. No new stable release or new React security advisory was found in this cycle.
- Existing Forsk PR #145 remains the single owner for the October 2026 React Server Components security catch-up. No duplicate.
Sources: https://react.dev/blog ; https://github.com/facebook/react/releases

#### 3. Node.js / backend

- The official Node.js security notice was last updated **3 November 2026**. It says new security versions for 26.x, 24.x and 22.x are expected on or shortly after **11 November 2026**, with HIGH as the highest severity in each line.
- As of this 10 November 00:25 IST check, the notice still lists no CVE IDs, affected patch ranges or patched versions. It remains an advance notice, not a published patch. Existing Mango PR #143 remains the single readiness-guide owner.
Source: https://nodejs.org/en/blog/vulnerability/november-2026-security-releases

#### 4. AI / cloud / developer infrastructure

- **AWS Nitro Sandboxes:** AWS published its announcement on **9 November 2026**. It says the feature is available in all commercial AWS Regions on most Nitro-based EC2 instances, at no additional charge. Detailed EC2 documentation requires an instance type that supports Nitro Enclaves. EKS pods opt in through isolated/confidential RuntimeClasses; ECS documentation scopes isolated/confidential tasks to ECS Managed Instances; self-managed EC2 supports confidential and direct modes. Confidential-mode secrets must be gated by verified attestation; optional EKS network isolation removes the network device, IMDS and Pod Identity credentials. No separate event date is stated.
  Sources: https://aws.amazon.com/about-aws/whats-new/2026/11/nitro-sandboxes-eks-ecs-ec2/ ; https://docs.aws.amazon.com/eks/latest/userguide/sandboxing.html ; https://docs.aws.amazon.com/AmazonECS/latest/developerguide/isolated-confidential-tasks.html ; https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nitro-sandboxes.html
- **Google TPU Sync:** Google Cloud published the introduction on **9 November 2026**. TPU Sync is an open-source C++ model-state layer for KV-cache tiering and weight transfer across TPU HBM, host DRAM, storage and remote nodes. The blog reports workload-specific results: Qwen3 235B median KV-transfer latency around 230 ms (from several seconds); 60% average TTFT reduction for 235B and 90% for 480B in controlled low-concurrency tests; separate 64K prefix-cache tests report up to 90% lower average TTFT, over 50% higher throughput and 30% lower P99 inter-token latency. The July 2026 test configuration and workload caveats are recorded in the draft. The upstream repository says APIs are evolving, only development/nightly wheels are available before the first stable release, and stable deployments should pin a tag or LKG commit. Its current README lists v7x/v6e hardware and JAX 0.12.0/0.11.2 compatibility. The current Compute Engine TPU region table lists no India zone for v7x or v6e. Current on-demand examples are Ironwood in Iowa at US$12/chip-hour and Trillium in Tokyo at US$3.24/chip-hour; these are infrastructure prices, not a TPU Sync fee.
  Sources: https://cloud.google.com/blog/topics/ai-infrastructure/introducing-tpu-sync-fast-kv-cache-and-weight-transfer-on-tpu ; https://github.com/google/tpu-sync ; https://github.com/google/tpu-sync/blob/main/LICENSE ; https://docs.cloud.google.com/tpu/docs/regions-zones ; https://cloud.google.com/tpu/pricing

### New draft production

#### Forsk Coding School — AWS Nitro Sandboxes

- Main baseline: `a690ef725029e8c7f96b6148e9012f82a481bd6d`
- Branch: `content/news-factory-aws-nitro-sandboxes-20261110`
- Draft PR #150: https://github.com/satnamkhowal/forsk-coding-school/pull/150
- Head: `fc83d8794922d43fdb86954231aa260dc2f5af33`
- Files: one 2,333-word English guide, one original 1200×675 SVG, one source/media provenance JSON.
- The guide distinguishes EKS opt-in, ECS Managed Instances, self-managed EC2 modes, KMS attestation, network isolation, supported instance types and cost. It is distinct from the existing Google Agent Compute Engine preview article.
- Local SVG: `/mnt/data/news-factory/2026-11-10/aws-nitro-sandboxes-eks-ecs.svg`.
- GitHub compare: 3 commits ahead / 0 behind main; PR state open/draft; mergeable state clean.
- Read-back: all three files fetched; metadata JSON parsed; SVG has 1200×675 dimensions, title/description and no external href or script. Local XML parse and 1200×675 CairoSVG render passed.
- Independent editorial/security QA and browser rendering: PENDING. No CI check runs were returned.

#### Groot Academy — Google TPU Sync

- Canonical repository alias verified: `satnamkhowal/gta` redirects to `satnamkhowal/grootacademy.com` (same repository ID).
- Main baseline: `a97dc07463a352ea924af3dea22af915a6f9bdb1`
- Branch: `content/news-factory-google-tpu-sync-20261110`
- Draft PR #582: https://github.com/satnamkhowal/grootacademy.com/pull/582
- Head: `a774b49e443ee9c61c13c085f9dac3aa198ee341`
- Files: one 2,506-word English guide, one original 1200×675 SVG, one source/media provenance JSON.
- The guide is distinct from existing Groot PR #580 (Cloud Pathways GA on GKE): it covers TPU Sync's KV-cache/model-state library, RL weight transfer, software maturity, India TPU-region constraints and per-chip-hour pricing. No changed-path overlap with #580.
- Local SVG: `/mnt/data/news-factory/2026-11-10/google-tpu-sync-architecture.svg`.
- GitHub compare: 3 commits ahead / 0 behind main; PR state open/draft; mergeable state clean.
- Read-back: all three files fetched; metadata JSON parsed; SVG has 1200×675 dimensions, title/description and no external href or script. Local XML parse and 1200×675 CairoSVG render passed.
- Independent editorial/technical QA and browser rendering: PENDING. No CI check runs were returned.

### Repository coordination and no-write decisions

- Central main remains `31af61b9a796472b7eb13d6b254aa6d9dc2ecc34`. The existing central News Factory checkpoint PR #19 was reused; this section is appended to its existing checkpoint file.
- Forsk main remains `a690ef725029e8c7f96b6148e9012f82a481bd6d`; PRs #145, #146, #147 and #149 remain separate and unchanged. New PR #150 owns three new paths only.
- Groot main remains `a97dc07463a352ea924af3dea22af915a6f9bdb1`; existing PR #580 remains unchanged. New PR #582 owns three new paths only.
- Mango main remains `8eeb57fdf05341aa0a5ec31846148a37b0be3ba6`; PR #143 continues to own Node.js readiness and existing opportunity drafts; PR #144 remains a separate graphics task. No Mango write was needed.
- Jaipur Engineers remains the renamed `je2` application at `satnamkhowal/jaipurengineers.com`. Its main tree has a live `news/` directory but no approved non-public News Factory draft lane; no article was placed in a live route or guessed path.
- No unverified brand repository was used.

### Media, video and publication gates

- Two original self-authored SVGs were produced; each is 1200×675, self-contained and has title/description and alt text.
- Provenance records include original source, ownership/licence, attribution, repository path, local path and dimensions.
- External graphic downloads: **0**. No third-party graphics were assumed reusable.
- Verified story-specific YouTube IDs/embedding permission: **0**. No iframe was created.
- New drafts are **RESEARCHED_DRAFT**, not QA-ready. Browser rendering and independent editorial/security review remain pending.
- No merge, deployment, publication, application submission or indexing action occurred.

### Cycle ledger

| Metric | Carried-forward before this cycle | This cycle | Resulting ledger |
| --- | ---: | ---: | ---: |
| Researched items | 61 | +2 | 63 |
| Drafted articles | 51 | +2 | 53 |
| Original graphics | 51 | +2 | 53 |
| Independent QA-ready | 33 | +0 | 33 |
| Live/published | 0 | +0 | 0 |

Existing opportunity drafts and the React/Node readiness items were revalidated, not counted as new drafts. The two new research items are AWS Nitro Sandboxes and Google TPU Sync.

### Next exact actions

1. Obtain independent editorial/security QA for Forsk PR #150 and independent technical/editorial QA for Groot PR #582; run browser rendering for both SVGs.
2. Recheck the Node.js official notice on or after 11 November for actual CVEs, affected ranges and patched versions before replacing the readiness guide.
3. Recheck NMMSS before 15 November, and UGC/AICTE/Google application pages before their listed 30 November and 4 December deadlines.
4. Verify PM YASASVI Top Class College's current institution/slot list before deciding whether a separate article is useful.
5. Keep both new PRs draft-only. No merge, deployment or publication without independent QA and owner approval.
