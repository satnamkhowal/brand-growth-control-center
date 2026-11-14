# News Factory cycle — 14 November 2026 (10:11 IST)

## Executive result

Four non-overlapping research lanes were checked: official student/developer opportunities; React/frontend releases and security; Node.js/backend releases and security; AI/cloud/developer announcements. One fresh, verified, unowned story passed the duplicate gate: AWS Security Hub's SBOM inventory announcement (published 6 November 2026). One original Forsk Coding School article and one original diagram were produced on an isolated branch. No merge, deployment, public publication or indexing occurred.

## Research lane 1 — official opportunities

Current windows were checked against official application pages. These are existing schemes/programmes with current windows, not all newly launched opportunities.

- **Google Student Researcher, 2027:** Google Careers page currently says India is a remote-eligible location; apply by **4 December 2026**, with rolling review. Applicants must be enrolled in a Bachelor's, Master's or PhD programme in a listed discipline and have experience in a CS area. Project duration varies by team/location; the listing does not state a stipend or fixed duration. Existing owner: [Forsk PR #146](https://github.com/satnamkhowal/forsk-coding-school/pull/146). Source: https://www.google.com/about/careers/applications/jobs/results/125423735539671750
- **Sage IT India Scholarship:** page publication timestamp is **19 October 2026**; deadline **15 November 2026**, winner announcement 30 November. ₹50,000 one-time award is paid to the winner's institution. Open to students aged 17–30 enrolled at a recognised Indian college/university, any major/degree level; individual unpublished 1,000–1,500-word article; no entry fee. No exact closing time is stated. Existing owner: [Forsk PR #184](https://github.com/satnamkhowal/forsk-coding-school/pull/184). Source: https://sageitinc.com/scholarship/india
- **NMMSS:** National Scholarship Portal currently lists the 2026–27 student application deadline as **15 November 2026**, with institute verification through 30 November and DNO/SNO/MNO verification through 15 December. This is an established scheme, not a new 2026 launch. The Ministry's revised guidelines are dated March 2022: ₹12,000/year, fresh award at Class IX, parental income ceiling ₹3.5 lakh, Class VII minimum 55% (5-point SC/ST relaxation), and eligible regular students in government, government-aided or local-body schools. Existing owner: [Forsk PR #173](https://github.com/satnamkhowal/forsk-coding-school/pull/173). Sources: https://scholarships.gov.in/All-Scholarships and https://scholarships.gov.in/public/schemeGuidelines/NMMSSGuidelines.pdf
- **VSSC academic project work:** current portal distinguishes UG downloaded-form route (next project slot 1 January–31 March 2027; receipt cut-off **15 November 2026**) from PG online route (next slot 1 January–30 June 2027; online window closes **16 November 2026, 11:59 PM IST**). Indian citizenship and minimum 60%/6.32 CGPA apply. Project work has no stipend/remuneration and no fee. INT 08 is closed; INT 09 is a separate May–July 2027 internship with a February–March 2027 application window. Existing owner: [Forsk PR #172](https://github.com/satnamkhowal/forsk-coding-school/pull/172). Sources: https://vsscinternship.vssc.gov.in/HRDD_LOGIN/beforelogincontroller, https://vsscinternship.vssc.gov.in/HRDD_LOGIN/instructionBeforLoginProj.jsp
- **NeGD Technical Internship — Winter 2026:** official MeitY/NeGD PDF sets a **20 November 2026** deadline and 50 places (40 six-month, 10 two-month). Eligibility requires at least 75% in a qualifying engineering degree; 2025/2026 graduates and 2027 final-year students are listed. Offline attendance and institution forwarding/sponsorship are required. ₹20,000/month is conditional on satisfactory performance and mentor certification; no application fee is stated in the notice. Existing owner: [Forsk PR #225](https://github.com/satnamkhowal/forsk-coding-school/pull/225). Source: https://www.meity.gov.in/static/uploads/2026/11/032b92c51d45d44365455c98ea37b0eb.pdf
- **AICTE Pragati/Saksham, UGC PG Studies and other NSP schemes:** NSP currently lists multiple 2026–27 windows through **30 November 2026**; individual eligibility and state/institution restrictions still apply. These are not fresh November launches. Existing Pragati owner: [Forsk PR #228](https://github.com/satnamkhowal/forsk-coding-school/pull/228). Source: https://scholarships.gov.in/All-Scholarships

No new unowned student programme passed the gate in this run. Existing opportunity owners were not re-commented to avoid redundant hourly status spam.

## Research lane 2 — React/frontend

No newer November stable React release was found. The official React release list still shows 19.3.1, 19.2.9, 19.1.10 and 19.0.9, all dated **14 October 2026**. The React Server Components critical RCE advisory GHSA-xqc2-xf4c-x3h3 was published 14 October and the GitHub Advisory Database record was updated 10 November; fixed versions are 19.3.1, 19.2.9, 19.1.10 and 19.0.9. Serverless/client-only React applications without an RSC server are outside this specific advisory's stated scope. Existing owners: Mango #201 and Forsk #145. Sources: https://github.com/facebook/react/releases and https://github.com/advisories/GHSA-xqc2-xf4c-x3h3

## Research lane 3 — Node.js/backend

The Node.js Project published security releases on **11 November 2026**:
- Node 22.23.5
- Node 24.22.3
- Node 26.13.1

The advisory contains **16 distinct CVEs** (7 High, 6 Medium, 3 Low); repeated CVE references in release notes do not represent extra unique CVEs. Node 27.0.0-alpha.0.1.0 was published 12 November and remains Alpha, not LTS/stable. Existing owners: Mango #143 and Groot #650. Sources: https://nodejs.org/en/blog/vulnerability/november-2026-security-releases, https://nodejs.org/en/blog/release/v24.22.3, https://nodejs.org/en/blog/release/v26.13.1, https://nodejs.org/en/blog

## Research lane 4 — AI/cloud/developer news

Fresh official GitHub changelog items dated 13 November were deduplicated against existing owners:
- Gemini 4 Hydrogen GA in Copilot — Groot issue #700.
- Repository-level AI Scan REST API public preview — Groot PR #737 and Jaipur issue #52 (same announcement; no third owner).
- Copilot app GHES support GA, requiring app 1.2.0+; GHES cloud sessions unavailable — Mango PR #230.
- Copilot model deprecations effective 14 December — existing Forsk PR #185; kept separate from that PR's 16 November retirement batch.
- GitHub Actions ARM32 Linux/Windows hosted-runner retirement effective 8 December — existing Forsk PR #204.

AWS Emulator, Cloudflare Kitesurf, AWS Continuum and AWS SDK for .NET 4.1 also have current owners in Groot/Mango. No duplicate article was opened for these topics.

## New unowned story selected — AWS Security Hub SBOM inventory

AWS published the announcement on **6 November 2026**. The current Security Hub guide documents an organisation-wide package inventory built from Amazon Inspector SBOMs. The article distinguishes the announcement date from the research date and covers EC2/ECR/Lambda examples, connected Azure VM/ACR coverage, Inspector prerequisites, account/administrator visibility, inventory refresh delay, console filters, GetSoftwareV2/GetSoftwareResourcesV2/GetSoftwareStatisticsV2, least-privilege IAM, Essentials pricing, and the Mumbai regional caveat. It explicitly distinguishes Lambda code scanning from SBOM package inventory.

The SBOM inventory has no additional feature charge within Security Hub Essentials; Essentials itself is resource-priced and has a 30-day trial. Mumbai (ap-south-1) endpoints exist for Security Hub and Inspector; the separate Inspector Lambda code-scanning Region list does not include Mumbai. The article does not promise universal Lambda coverage in Mumbai.

Duplicate gate: current searches across Mango Engineers, Groot Academy, Forsk Coding School and Jaipur Engineers found no AWS Security Hub owner. Forsk PR #212 is GitHub's SBOM API migration topic, not AWS Security Hub's package inventory, so the two are explicitly distinguished.

## Implementation — Forsk Coding School

- Tracker: [Forsk issue/PR #229](https://github.com/satnamkhowal/forsk-coding-school/pull/229)
- Branch: `news-factory/aws-security-hub-sbom-inventory-20261114-1011`
- Draft: 2,515-word original English SEO/AEO/GEO technical guide.
- Files: article Markdown; source/SEO metadata JSON; original SVG; Forsk MASTER_TASK_BOARD and SESSION_HANDOFF entries.
- Media: original 1200×675 SVG committed; local PNG and WebP derivatives created and visually inspected. SVG 6,249 bytes; PNG 125,150 bytes; WebP 63,110 bytes. Local SVG matches the GitHub blob. Provenance, permission basis, attribution, alt text, local paths, dimensions and SHA-256 values are in the metadata sidecar. No third-party graphics, logos or screenshots used.
- Video: no announcement-specific official/reputable original YouTube video ID and date were verified; no iframe or ID was fabricated.
- GitHub status: OPEN / DRAFT; 10 commits ahead, 0 behind main; mergeable=true after GitHub refresh. No public route, sitemap, schema, PHP, shared UI or production path changed.

## QA and blockers

Passed: article read-back (2,515 words); metadata JSON parse; SVG XML parse; exact local/GitHub SVG blob match; PNG and WebP decode at 1200×675; visual inspection; CLI examples checked against official AWS CLI v2 references. No live AWS account request was executed.

Pending: independent editorial QA, independent technical QA and responsive browser QA. Two `Forsk learning home copy QA` workflow runs (43559140213 and 43559232932) failed on the PR head; both job-log retrieval attempts returned BlobNotFound 404. The workflow also triggers on the shared board/handoff paths. Cause is unclassified; no CI pass is claimed. No merge, deployment, publication or indexing.

## Repository and coordination review

- Mango Engineers: read agent start guide, task board and integration queue; current Node/AWS/Copilot owners preserved.
- Groot Academy: current open AI/cloud owners checked; no AWS Security Hub SBOM owner. Existing Kitesurf/Emulator/AI Scan owners preserved.
- Forsk Coding School: read README, content radar, master task board, session handoff, News Factory draft folder and relevant existing PRs #204, #212, #225, #228; created only task #229.
- Jaipur Engineers: read current Content Radar, queue and image-production workflow. Auto Publish remains OFF; existing AI Scan overlap with Groot #737 preserved; no Jaipur write.
- Additional brands remain subject to central source/canonical mapping and brand-specific authority; no speculative write was made.

Central branch `ops/news-factory-cycle-20261109-2209` remains diverged: **195 ahead / 5 behind main**. No rebase, force-push or merge.

## Production ledger — this run

| Stage | Count |
|---|---:|
| Research tracks | 4 |
| New verified unowned stories | 1 |
| New original article drafts | 1 |
| Original graphics committed | 1 SVG |
| Local raster derivatives | 2 |
| Verified YouTube embeds | 0 |
| Independent QA-ready | 0 |
| Live / published | 0 |
| Merged / deployed | 0 |
| New Forsk task issue / Draft PR | 1 / 1 |
| Central audit files added | 1 |

## Next actions

1. Recheck NMMSS, Sage IT and VSSC UG application status on 15 November; do not infer another extension.
2. Recheck VSSC PG project-work window before 16 November, 11:59 PM IST.
3. Recheck NeGD internship before 20 November.
4. Recheck NSP 30 November programmes with their individual eligibility restrictions.
5. Recheck Google Student Researcher before 4 December.
6. Complete independent QA for Forsk PR #229 and diagnose the workflow log/runner issue only if logs become available.
7. Continue the four research lanes; open new content only for fresh, verified, unowned and brand-distinct stories.
