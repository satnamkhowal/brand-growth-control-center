# News Factory cycle — 15 November 2026, 16:09 IST

## Scope and execution

Four non-overlapping research lanes were rechecked against primary sources:

1. Official student/developer opportunities, internships, scholarships and grants.
2. React/frontend releases and security advisories.
3. Node.js/backend releases and security advisories.
4. AI/cloud/developer product and platform announcements.

The existing News Factory checkpoint and queue were read before writing. Brand repository ownership and current PR inventories were checked where accessible. No worker chats or duplicate task registries were created.

**One new, sufficiently verified and previously unowned story was selected:** Google AlloyDB Express Preview. One original Mango Engineers article draft and one original SVG graphic were implemented on an isolated branch. No merge, rebase, deployment, publication or application submission occurred.

## 1. Student, developer, scholarship and opportunity lane

### Google Student Researcher 2027 — existing Forsk owner #146

- Official Google Careers page currently shows **Apply**, **India — Remote eligible**, and a **4 December 2026** deadline.
- Applications are reviewed on a rolling basis.
- Minimum qualifications include current enrolment in a Bachelor's, Master's or PhD programme in the listed fields and relevant computer-science experience.
- No stipend or application fee is published on the listing.
- Existing owner retained; no duplicate article.

Source: https://www.google.com/about/careers/applications/jobs/results/125423735539671750

### VSSC academic project work / internship — existing Forsk owner #172

- Official portal: https://vsscinternship.vssc.gov.in/HRDD_LOGIN/beforelogincontroller
- BE/BTech/BSc/Diploma: next academic project slot **1 January–31 March 2027**; portal lists **15 November 2026** as last date, but no closing hour. At 16:09 IST, hour-level form acceptance was not verified; do not promise the form remains open.
- ME/MTech/Integrated MTech/MSc/Integrated MSc/BS-MS: next slot **1 January–30 June 2027**; online window ends **16 November 2026, 11:59 PM IST**.
- Internship INT 08 is closed. Next INT 09 is **1 May–31 July 2027**, with application window **15 February–15 March 2027**.
- Existing owner received a status comment; no duplicate article.

### National Means Cum Merit Scholarship — existing Forsk owner #173

- NSP AY 2026–27 list currently displays student applications through **15 November 2026**, with no closing hour.
- The same portal footer says last update June 2026; live form response/receipt status was not independently tested.
- Treat this as the portal's displayed date, not proof that a form submission is accepted at this exact hour.
- Existing owner received a status comment.

Source: https://scholarships.gov.in/All-Scholarships

### Sage IT India Scholarship 2026 — existing Forsk owner #184

- Sponsor page was re-opened in this cycle. It still displays the **15 November 2026** submission deadline and **30 November 2026** winner announcement.
- Source publication timestamp: **19 October 2026, 07:00:17 -05:00**.
- Eligibility: recognised Indian college/university students aged 17–30, all majors; individual unpublished 1,000–1,500-word Word article; no entry fee.
- Award: one-time **₹50,000** paid directly to the selected student's institution.
- No closing hour is displayed; form/receipt status was not independently tested.
- Existing owner received a corrected status comment; no duplicate article.

Source: https://sageitinc.com/scholarship/india

### GIFT FutureLab Grand Challenge 2026–27 — existing Forsk owner #179

- Official page remains live and states applications close **20 November 2026**.
- Open to students and researchers from technical, management and other higher-education institutions across India; individuals and teams may apply.
- Total award pool **₹6,00,000**: ₹3,00,000 / ₹2,00,000 / ₹1,00,000.
- Grand Finale scheduled for **22 December 2026 at IIT Gandhinagar**.
- Application fee is not confirmed in the FAQ; do not call participation free.
- Existing owner received a status comment; no duplicate article.

Source: https://iieciitgn.com/gfc/

### Other opportunity owners retained

- NeGD Winter internships remain with Forsk #180 / #225; no duplicate article was created.
- DRDO TBRL paid internship remains with Forsk #236; direct DRDO-hosted amended notice verification remains pending in its existing PR.
- No old or closed programme was presented as newly open.

## 2. React / frontend

- Official React release list remains unchanged: **19.3.1, 19.2.9, 19.1.10 and 19.0.9**, all dated **14 October 2026**.
- Official React blog still identifies React 19.3 (9 September 2026) as the latest feature release.
- No new November stable release or November security advisory was found.
- Existing Forsk PR #145 received a status comment; Mango PR #202 remains an existing owner. No duplicate article.

Sources:
- https://github.com/react/react/releases
- https://react.dev/blog

## 3. Node.js / backend security

- Official Node.js Project bulletin dated **11 November 2026** confirms patched releases **22.23.5, 24.22.3 and 26.13.1**.
- The bulletin lists **16 CVEs: 7 High, 6 Medium and 3 Low**; highest severity is High.
- Areas include HTTP/2 remote process abort, heap-memory disclosure and resource exhaustion; TLS callback crashes and client-certificate policy bypass; proxy credentials in error messages; and Permission Model issues.
- Existing Mango PR #143 / #229 remain owners. PR #143 received a current status comment. No duplicate article.

Source:
- https://nodejs.org/en/blog/vulnerability/november-2026-security-releases

## 4. AI / cloud / developer news

### New unowned story — Google AlloyDB Express Preview

- **New Mango Engineers draft:** [PR #266](https://github.com/satnamkhowal/mangoengineers.com/pull/266).
- Dedicated launch announcement publication date: **4 November 2026**.
- Google Data Cloud roundup publication date: **12 November 2026**.
- Current technical documentation last updated: **10 November 2026**.
- Product stage: **Preview / Pre-GA**, not general availability.
- Current supported-region list includes Singapore (asia-southeast1), but not Mumbai (asia-south1) or Delhi (asia-south2). The article does not equate Singapore with India or claim Indian developers are categorically blocked.
- Google pricing page says billing starts **December 2026**. Monthly free tier: **50 compute units and 2 GiB storage per billing account for the first 12 months**. Compute is not billed while paused; used storage remains billable.
- Technical limitations: PostgreSQL 18 only; 1 or 2 vCPU; 20 GB storage cap; max_connections 200; no SLA, HA, backups/PITR, cross-region replication, CMEK, committed-use discounts or Terraform/Config Connector support.
- No scholarship, cash grant or guaranteed student cloud credit is implied.
- Four files committed to an isolated branch: 2,067-word article, metadata JSON, original 1200×675 SVG and provenance JSON. Local 1200×675 PNG/WebP derivatives are available but not committed.
- No story-specific original YouTube video with a verifiable ID, channel, upload date and embedding suitability was confirmed; no iframe or video download.

Official sources:
- https://cloud.google.com/blog/products/databases/introducing-alloydb-express-for-rapid-testing-and-prototyping
- https://docs.cloud.google.com/alloydb/docs/express-overview
- https://cloud.google.com/alloydb/pricing
- https://cloud.google.com/blog/products/data-analytics/whats-new-with-google-data-cloud

### Existing AI/cloud owners — no duplicate stories

- Google Data Cloud connectors / governed conversational analytics remain owned by Mango PR #215.
- Gemini 4 Hydrogen in GitHub Copilot remains owned by Mango PR #253.
- GitHub Enterprise Server support in the Copilot app remains owned by Mango PR #230.
- Google A2UI 1.0 remains owned by Mango PR #260.
- Google ADK / AgentCore and other existing platform topics retain their current owners.

## Repository and concurrency audit

### Central coordination

- Read central README, existing PR #19 and the existing 15:10 IST checkpoint file.
- Existing central PR #19 branch remains diverged from main at **230 commits ahead / 5 behind** when compared in this run.
- This checkpoint is appended as a new dated file to the same existing PR #19 branch. No rebase, force-push or merge was attempted.

### Mango Engineers

- Read README.md, AGENTS.md, docs/agent-start-here.md, docs/task-board.csv, docs/work-log.md and docs/integration-queue.md.
- Read current open PR inventory (100 recent open PRs) and searched News Factory branches for AlloyDB Express.
- Existing Mango PR #215 owns Data Cloud connectors; no AlloyDB Express draft or branch was found.
- Created isolated branch `news-factory/alloydb-express-preview-india-cost-limits-20261115-1609` from current main and opened PR #266.
- PR #266 is **OPEN / DRAFT / UNMERGED**, 4 commits ahead / 0 behind main, 4 added files. GitHub initially reported mergeable=false; no merge was attempted.
- The shared task board/work log/integration queue were not edited because multiple active Mango PRs own shared coordination files. Task ID is recorded in the PR and article metadata.

### Forsk Coding School

- Current open PR inventory and existing topic owners were checked.
- Root README.md and AGENTS.md paths were not available through the connected repository read; no new Forsk source write was attempted.
- Existing owner status comments were added to PRs #145, #146, #172, #173, #179 and #184.

### Groot Academy

- Accessible `grootacademy.com` alias has `.agent/README.md` mapping the canonical repository to `satnamkhowal/gta`, branch `main`.
- The canonical `satnamkhowal/gta` repository was not available in the connected repository inventory/search during this run. No Groot write was made.

### Jaipur Engineers and other brands

- Central queue continues to mark Jaipur Engineers read-only for new News Factory article lanes; no new Jaipur write was made.
- Unverified brand mappings were left untouched.

## Production ledger — this run only

| Stage | New count |
| --- | ---: |
| Research lanes checked | 4 |
| New unowned verified stories selected | 1 |
| Original English article drafts | 1 |
| Original committed SVG graphics | 1 |
| Local PNG / WebP derivatives | 1 / 1 |
| Verified YouTube embeds | 0 |
| Existing-owner status comments | 7 |
| Independent QA-ready | 0 |
| Live / published | 0 |
| Merged / deployed | 0 |

### Mango PR #266 checks

- Four intended files were read back from GitHub.
- Local article word count: **2,067**.
- Metadata and provenance JSON parse: PASS.
- SVG XML parse: PASS.
- PNG and WebP decode: PASS, both 1200×675.
- PNG visually inspected.
- Independent editorial, cloud pricing/region and technical review remain pending.
- GitHub CI / workflow status was not established in this checkpoint; do not infer a pass.
- No public route, PHP, sitemap, schema, redirect, shared component, merge, deployment, publication or indexing change.

## Next actions

1. Independently review Mango PR #266 for factual accuracy, region/pricing language and preview limitations; keep it draft until QA is complete.
2. Recheck the VSSC PG project application window before **16 November 2026, 11:59 PM IST**.
3. Recheck GIFT FutureLab and NeGD deadlines on **20 November 2026**; verify any application form response state before telling students to submit.
4. Preserve the 15 November NMMSS and Sage IT deadline caveats; no hour-level form acceptance was confirmed.
5. Recheck Google Student Researcher before **4 December 2026**.
6. Continue monitoring official React/Node release sources and existing owners; do not create duplicate release articles.
7. Resolve canonical GTA repository access before any Groot content write.

No merge, deployment, publication, application submission, live verification or uninterrupted background execution is claimed.
