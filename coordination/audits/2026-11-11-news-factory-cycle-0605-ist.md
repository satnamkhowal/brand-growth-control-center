# News Factory cycle — 11 November 2026, 06:05 IST research snapshot

## Summary

Four non-overlapping lanes were rechecked: official student/developer opportunities; React/frontend; Node.js/backend security; AI/cloud/developer announcements. Central coordination and the four verified brand repositories were reviewed before writes.

**This cycle produced two distinct Forsk Coding School drafts:**
1. Git security update announced by GitHub on 10 November 2026 — six CVEs and patched Git maintenance versions.
2. NMMSS 2026–27 — Ministry of Education deadline extension to 15 November 2026, published by PIB on 31 October.

Both drafts are in one isolated branch and one open Draft PR. Each has an original 1200×675 SVG infographic and provenance/QA sidecar. PNG and WebP derivatives were rendered locally, visually inspected and dimension-checked, but are not committed.

No third-party graphics or videos were downloaded. No YouTube iframe was added because no story-specific video ID and embedding availability were verified. No merge, deployment, publication, indexing or application submission occurred.

## 1. Official student / developer opportunities

### New draft — NMMSS 2026–27 deadline extension (Forsk PR #173)

- Ministry of Education / PIB publication date: **31 October 2026, 5:57 PM IST**.
- Student application deadline: **15 November 2026**.
- Institute Nodal Officer (L1) verification: **30 November 2026**.
- District Nodal Officer (L2) verification: **15 December 2026**.
- National Scholarship Portal applications have been open since 1 June 2026.
- OTR is mandatory before applying; NSP describes a unique 14-digit OTR based on Aadhaar or Aadhaar Enrolment ID.
- The Ministry's PIB release says the scheme provides one lakh fresh scholarships each year to eligible Class IX students who qualify in the selection examination conducted by their State/UT.
- Amount: **₹12,000 per year**, paid through DBT.
- Core conditions in official scheme information: State Government / Government-aided / local self-government school; parental income not above ₹3.50 lakh per year; at least 55% or equivalent grade in Class VII for appearing in the selection test, with five-percentage-point relaxation for SC/ST students.
- Renewal through Classes X–XII depends on prescribed academic requirements.
- The national application deadline does not replace the State/UT selection examination or selection list.
- The 2026 PIB deadline notice does not state an application fee; article does not claim a blanket fee-free service.

**Portal discrepancy disclosed:** the NSP student homepage still shows a June 2026 last-update footer and older announcement text. The dated 31 October PIB release is the source for the revised 15 November deadline. The article tells families to confirm that the NMMSS form is accepting submissions through their OTR login and to contact the school / State/UT nodal authority if the portal still blocks a selected candidate. It does not present the extension as a new scholarship launch.

Sources:
- https://www.pib.gov.in/PressReleasePage.aspx?PRID=2330936&lang=1&reg=3
- https://scholarships.gov.in/Students
- https://www.education.gov.in/nmms
- https://dsel.education.gov.in/sites/default/files/update/PIB2167076.pdf

### Existing opportunity status rechecks — no duplicate drafts

- **Google Student Researcher 2027 — Forsk PR #146 remains owner.** The official listing was previously checked for India / Remote eligibility and a 4 December 2026 deadline; no new article was opened.
- **Google PhD Fellowship 2026 — closed.** Google's current programme page says the 2026 cycle closed on 30 April 2026. It is not described as newly open.
- **VSSC Academic Project Work 2027 — Forsk PR #172 remains owner.** The 15 November UG and 16 November PG route cut-offs remain close; no duplicate draft was opened.
- Other existing scholarship, internship, fellowship and NITI Aayog PR owners were preserved. NITI Aayog's monthly 1–10 application window has passed for November; next scheduled window is 1–10 December, not a new November opportunity.

## 2. React / frontend

- The official React blog still lists React 19.3 (9 September 2026) as the latest stable announcement.
- No new November stable release or security advisory was found in the current official blog snapshot.
- Existing Forsk PR #145 remains the React Server Components security owner.
- No duplicate React article was created.

Sources:
- https://react.dev/blog
- https://github.com/facebook/react/releases

## 3. Node.js / backend security

- The official Node.js blog still lists the 26.x, 24.x and 22.x security releases as scheduled on or shortly after **11 November 2026**.
- Highest severity in the advance notice is HIGH for each release line.
- At the 06:05 IST snapshot, the official blog still lists the advance notice dated 3 November; latest entries shown are V8 26→27 Alpha announcement (5 November), Node 27 Alpha (29 October), Node 24.22.2 LTS (28 October) and Node 26.13.0 LTS (28 October).
- No 11 November patched release tags or CVE IDs were published in the official Node blog snapshot at this check.
- Existing Mango PR #143 remains the Node.js security owner. No premature patch article was created.

Sources:
- https://nodejs.org/en/blog
- https://nodejs.org/en/blog/vulnerability/november-2026-security-releases
- https://github.com/nodejs/node/releases

## 4. AI / cloud / developer news

### New draft — Git security update (Forsk PR #173)

- GitHub Blog publication date: **10 November 2026**.
- Six CVEs: CVE-2026-111760, CVE-2026-113408, CVE-2026-114467, CVE-2026-114469, CVE-2026-105437 and CVE-2026-114466.
- Patched Git versions: **2.56.1, 2.55.1, 2.54.1, 2.53.1, 2.52.1, 2.51.3 and 2.50.2**.
- The article distinguishes the recursive-clone issue (the linked GHSA page rates it High, CVSS 8.0) from the other five issues and does not assign them one shared severity.
- It covers local Git, bundled Git, self-hosted CI runners, GitHub-hosted services and GitHub Enterprise Server.
- GHSA metadata for CVE-2026-111760 still showed “Patched versions: none” in the page snapshot while the dated GitHub Blog and v2.56.1 release notes identify fixed versions. The article flags this metadata lag and directs readers to the release notes/vendor package for actual installed versions.

Sources:
- https://github.blog/open-source/git/git-security-vulnerabilities-announced-7/
- https://github.com/git/git/blob/v2.56.1/Documentation/RelNotes/2.56.1.adoc
- https://github.com/git/git/security/advisories/GHSA-vp2w-7xxj-jvxr
- https://git-scm.com/downloads
- https://docs.github.com/en/enterprise-server/release-notes

### Existing developer-news owners preserved

- Gemini 4 Carbon in GitHub Copilot — GitHub Changelog publication 10 November; existing Forsk PR #168.
- C++ Language Server MSBuild auto-configuration — GitHub Changelog publication 10 November; existing Forsk PR #171.
- Dependabot alerts pause on inactive repositories from 8 December — existing Forsk PR #165.
- No duplicate article or graphic was created for these topics.

## 5. Repository review and ownership

### Central control center
- Root README confirms this repository is coordination-only and each brand implementation stays in its own source repository.
- No root AGENTS.md was found.
- Existing News Factory PR #19 remains the append-only checkpoint lane; PR #20 was not modified.
- PR #19 branch ops/news-factory-cycle-20261109-2209 was **74 commits ahead / 2 behind** central main before this checkpoint. It remains diverged; do not rebase or merge without owner-led reconciliation.

### Mango Engineers — satnamkhowal/mangoengineers.com
- Current README and AGENTS.md reviewed. README directs workers to docs/agent-start-here.md; AGENTS requires task claim, current task-board/work-log/integration-queue review, preservation of public .html URLs and no unsupported business claims.
- Current open PR inventory checked. Existing Node.js security / opportunity / news owners remain active.
- No Mango write was made.

### Groot Academy — satnamkhowal/grootacademy.com
- Current README contains only "# gta"; no root AGENTS.md found.
- Current open PR inventory checked. Existing OpenSearch clone-upgrade PR #611 and other News Factory/SEO/graphics owners remain active.
- No Groot write was made; the canonical 100K blog queue requires topic-level deduplication before another draft.

### Forsk Coding School — satnamkhowal/forsk-coding-school
- Root README.md and AGENTS.md are not present. Read README.txt, README_FINAL.txt and README-DEPLOYMENT-10000-BLOGS.txt. The latter identifies the 10,000-blog manifest and image-manifest paths and warns that public blog pages/images are a separate deployment operation.
- Current open PR inventory checked; PR #172 and all existing opportunity, React, Copilot, Dependabot and internship owners were preserved.
- Repository search found no exact NMMSS or CVE-2026-111760 draft match in the indexed source search or open PR titles.
- The blog/new-10000-blog-seo-manifest.csv path exists, but the GitHub file fetch returned empty content. A complete 10K manifest scan therefore could not be independently confirmed in this run. No public blog renderer, route, sitemap, task board or shared deploy file was changed.
- Only isolated docs/news-factory/drafts/, media/ and metadata/ paths were added.

### Jaipur Engineers — satnamkhowal/jaipurengineers.com
- Canonical repository metadata and open PR inventory checked. Root README.md and AGENTS.md were not found.
- Existing NITI Aayog internship and enquiry/readability work owners remain active.
- No Jaipur News Factory write was made; no new approved isolated content lane was established.

### Other brands
- Clever Ape Academy, CadMate India, Groot Software and Forsk Technologies were not given new writes. Their canonical repository/source mappings remain unverified for this cycle.

## 6. Implementation and QA

### Forsk Coding School PR #173
- PR: https://github.com/satnamkhowal/forsk-coding-school/pull/173
- Branch: news-factory-git-security-nmmss-20261111-0605
- Compare against current main: **6 commits ahead / 0 behind**.
- Exactly six new paths: two article drafts, two original SVGs and two provenance/QA JSON sidecars.
- Additions: 545; deletions: 0.
- GitHub PR status after refresh: OPEN / DRAFT / mergeable=true.
- Article read-back word counts: Git security **2,050**; NMMSS **1,846**.
- Both metadata JSON files parsed successfully and match article word counts.
- Both SVG files read back with 1200×675 dimensions and rendered successfully.
- Local PNG/WebP derivatives were generated and visually inspected; all are 1200×675. They are local only, not committed.
- No workflow runs were returned for the PR head; no CI pass is claimed.
- Independent editorial QA and responsive/browser QA remain pending.

### Media
- Original SVG graphics committed: **2**.
- Local raster derivatives: **4** (2 PNG + 2 WebP).
- Third-party graphics downloaded: **0**.
- YouTube video IDs with verified story relevance and embed availability: **0**; no iframe added.
- Videos downloaded or re-uploaded: **0**.

## 7. Production ledger

| Status | Increment this cycle |
|---|---:|
| New distinct actionable research items | 2 (Git security release; NMMSS deadline extension) |
| React / Node release status rechecks | 2 lanes; no new release articles |
| Existing AI/Copilot owners revalidated | 3; no duplicates |
| New original article drafts | 2 |
| Existing articles materially rewritten | 0 |
| Original SVG graphics | 2 |
| Local PNG/WebP derivatives | 4 |
| Independent QA-ready articles | 0 |
| Live / published articles | 0 |

Carried-forward checkpoint from 05:02 IST: 74 researched, 62 drafted, 62 original graphics, 33 independent QA-ready, 0 live. Adding this cycle's verified increments gives a **provisional cumulative ledger of 76 researched, 64 drafted, 64 original SVG graphics, 33 independent QA-ready and 0 live**. These cumulative figures are carried forward from the prior checkpoint, not independently reconciled against the entire historical archive.

## 8. Next actions

1. Independent editorial/source QA and responsive/browser QA for both articles in Forsk #173.
2. Recheck the NMMSS application form through OTR login and the PIB extension before 15 November; keep the NSP/PIB discrepancy visible.
3. Recheck official Node.js tags/advisories when the 11 November security releases actually publish; update Mango #143 only with real CVEs and patched versions.
4. Keep Forsk #145 as React owner unless the official React blog announces a new release/advisory.
5. Preserve existing Google Student Researcher, VSSC, Copilot, C++ language-server, Dependabot and NITI Aayog owners.
6. Resolve the empty Forsk 10K manifest fetch before claiming complete manifest-level deduplication.
7. Preserve central PR #19 divergence and PR #20; owner-led reconciliation only. No merge or deployment without approval.

## Pull request links
- Forsk Coding School — Git security + NMMSS drafts, PR #173: https://github.com/satnamkhowal/forsk-coding-school/pull/173
- Forsk Coding School — VSSC Academic Project Work 2027, PR #172: https://github.com/satnamkhowal/forsk-coding-school/pull/172
- Forsk Coding School — Google Student Researcher 2027, PR #146: https://github.com/satnamkhowal/forsk-coding-school/pull/146
- Forsk Coding School — React Server Components security owner, PR #145: https://github.com/satnamkhowal/forsk-coding-school/pull/145
- Mango Engineers — Node.js security owner, PR #143: https://github.com/satnamkhowal/mangoengineers.com/pull/143
- Groot Academy — OpenSearch clone-upgrade owner, PR #611: https://github.com/satnamkhowal/grootacademy.com/pull/611
- Central News Factory coordination PR #19: https://github.com/satnamkhowal/brand-growth-control-center/pull/19


## Official Google Student Researcher 2027 revalidation — 11 November 2026

The live Google Careers listing was opened again after the initial four-lane snapshot:

- Listing title: Student Researcher, 2027.
- Application status: page displays Apply.
- Country / location: India; Remote eligible.
- Deadline: **4 December 2026**; Google says applications are reviewed on a rolling basis and encourages early application.
- Minimum enrolment: Bachelor's, Master's or PhD in Computer Science, Linguistics, Statistics, Biostatistics, Applied Mathematics, Operations Research, Economics or Natural Sciences.
- Relevant computer-science experience required in an area such as NLP, HCI, Computer Vision, Machine Learning, Deep Learning, Algorithmic Foundations of Optimization, Quantum Information Science, Data Science or Software Engineering.
- The candidate must remain located in one of the listed country locations for the full engagement. Project duration and location vary by team.
- The listing does not publish a stipend amount, application fee or one fixed programme duration.

Official listing: https://www.google.com/about/careers/applications/jobs/results/125423735539671750

This is a status revalidation for the existing Forsk PR #146 owner, not a new story or draft. A status-only comment was added to that PR; ownership remains unchanged.
