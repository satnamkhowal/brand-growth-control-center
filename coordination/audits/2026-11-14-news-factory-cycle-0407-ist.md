# News Factory cycle — 14 November 2026, 04:07 IST

## Run summary

Four non-overlapping research tracks were checked against primary sources: student/developer opportunities; React/frontend releases and security; Node.js/backend releases and security; and AI/cloud/developer announcements. Current repository instructions, queues, branches and open PR ownership were reviewed before writing.

**One new unowned story cleared the source and deduplication gates:** GitHub Enterprise Server support in the GitHub Copilot app, announced 13 November 2026. One original Mango Engineers article and one original vector infographic were committed to an isolated draft branch. Existing opportunity, React, Node.js and cloud-news owners were preserved.

## Coordination and repository review

- Central repository `satnamkhowal/brand-growth-control-center`: README and coordination guidance read; existing News Factory PR #19 remains OPEN/DRAFT and unmerged. Its branch `ops/news-factory-cycle-20261109-2209` is **182 commits ahead / 5 behind main** and diverged. No rebase or merge performed.
- Mango Engineers: README, AGENTS.md, `docs/agent-start-here.md`, `docs/task-board.csv`, `docs/work-log.md` and `docs/integration-queue.md` reviewed. Main at draft-branch creation: `51aa38209430bd916999073d4c710064fd864b8f`. Existing PRs #143, #202, #204, #218 and #229 reviewed. No matching GHES Copilot-app branch or open PR was found before creating the isolated task branch.
- Groot Academy: README, `.agent` governance/handoff files, migration status and latest migration log reviewed. Existing AI/cloud owners including PR #732 and #737 retained.
- Forsk Coding School: README.txt, `docs/ai-ops/MASTER_TASK_BOARD.md` and `docs/ai-ops/SESSION_HANDOFF.md` reviewed. Existing Google, scholarship, VSSC, React and internship owners retained.
- Jaipur Engineers: README and current Content Radar queue reviewed. Auto Publish remains OFF. No write was made.
- Only new paths under Mango `docs/news-factory/drafts/` and `docs/news-factory/media/` were added. Shared task boards, work logs, integration queues, site routes, sitemaps, schemas, redirects and production files were not changed.

## Track 1 — official student programmes, internships and scholarships

Current status checks are not presented as newly opened unless the source says so.

| Opportunity | Verified status and terms | Existing owner / action |
|---|---|---|
| Google Student Researcher 2027 | Current Google Careers listing: India, Remote eligible; apply by **4 December 2026**; rolling review. Bachelor's/Master's/PhD enrollment in listed research fields and experience in a CS area. Listing does not publish stipend or a fixed project duration. The listing itself has no separate publication date. | Forsk PR #146 retained; no duplicate. |
| Sage IT India Scholarship 2026 | Sponsor page published **19 October 2026**; submission deadline **15 November 2026**; ₹50,000 one-time award paid directly to the institution; individual 1,000–1,500-word original article; all majors/degree levels; ages 17–30; no entry fee. | Forsk PR #184 retained. |
| National Means-cum-Merit Scholarship (NMMSS) | NSP AY 2026–27 card currently lists student application through **15 November 2026**; institute verification through 30 November and DNO/SNO/MNO through 15 December. Scheme is for eligible Class IX students selected from Class VIII; annual award ₹12,000. | Forsk PR #173 retained. |
| VSSC academic project work | Current VSSC portal: BE/BTech/BSc/Diploma next Jan–Mar 2027 slot has downloaded-form/email submission deadline **15 November 2026**. ME/MTech/Integrated MSc/BS-MS online window closes **16 November 2026 at 23:59 IST**. The previous INT 08 internship slot is closed; INT 09 is a separate May–July 2027 internship with application window 15 February–15 March 2027. Portal does not show a publication date; project period and application deadline are separate. | Forsk PR #172 retained. |
| AICTE Pragati — technical degree and diploma | Current NSP cards show applications from 1 June through **30 November 2026**, defective/institute verification through 15 December, DNO/SNO/MNO through 31 December. Linked detailed scheme PDFs are dated **July 2020 / 2020–21**; NSP footer still says last updated June 2026. Do not describe the old PDFs as new 2026–27 guidelines. | Forsk PR #228 retained; a current-status/source-date comment was added. |
| AICTE Saksham — technical degree and diploma | Current NSP cards show applications through **30 November 2026**. Linked detailed PDFs are July 2020. Those guidelines state at least 40% disability, family income ceiling ₹8 lakh, first-year or second-year lateral-entry admission in an AICTE-approved technical course, and ₹50,000/year; verify the live application form and current scheme rules before publication. | Forsk PR #183 retained; no new graphic because the existing repository image workflow blocks featured media until a canonical article page or publication handoff exists. |
| Swami Dayanand Education Foundation 2026–27 | Official page currently shows applications through **30 November 2026**; eligible first-year professional UG students; minimum 80% in Class XII; family income up to ₹12 lakh; up to ₹50,000/year and maximum ₹2 lakh over four years, subject to renewal. | Forsk PR #178 retained. |
| IIIT Kottayam Network Science Winter Internship 2026 | Current live page: application deadline **20 November 2026**, starts **25 November 2026**, minimum four weeks, UG/PG CS/Maths/Data Science/related fields, fee **₹5,000**; no stipend amount is stated. The live page says **Online** while its linked brochure says **Hybrid (Online + Offline)**. Page has no visible publication date; 25 November is the start date. Do not promise offline attendance until the lab confirms the mode in writing. | Forsk PR #227 retained; exact current page/brochure discrepancy comment added. |
| PM-USP Special Scholarship Scheme for J&K and Ladakh | NSP All-Scholarships card shows a fresh listing from 22 October to 30 November, while the separate NSP student-announcement text describes renewal applications closing 31 October. Fresh/renewal status needs clarification; no article created. | Held; no new draft. |

Primary sources:
- Google Careers: https://www.google.com/about/careers/applications/jobs/results/125423735539671750-student-researcher-2027
- Sage IT: https://sageitinc.com/scholarship/india
- NSP All-Scholarships: https://scholarships.gov.in/All-Scholarships
- VSSC portal: https://vsscinternship.vssc.gov.in/HRDD_LOGIN/beforelogincontroller
- SDEF: https://www.swamidayanand.org/india-scholarships-2026-27
- IIIT Kottayam live page: https://netsci.iiitkottayam.ac.in/internship.php
- IIIT Kottayam brochure: https://netsci.iiitkottayam.ac.in/assets/docs/NetSci_Winter_InternCall_26.pdf

## Track 2 — React / frontend

- No new November stable React release found in the official release/advisory pages checked.
- React **19.3.1** was released **14 October 2026**.
- React Server Components RCE advisory GHSA-xqc2-xf4c-x3h3 was published 14 October; GitHub Advisory Database currently lists CVE-2026-126187 and fixed versions **19.0.9 / 19.1.10 / 19.2.9 / 19.3.1**. The upstream React advisory page still displays “No known CVE” in its current page snapshot, so cite the GitHub Advisory Database when using the CVE identifier.
- Server Functions DoS advisory GHSA-h3gv-c5rc-p453 was also published 14 October, High severity, CVSS 8.2; same fixed version lines.
- No duplicate article created; Forsk PR #145 and Mango PR #202 remain owners.

Primary sources:
- React 19.3.1: https://github.com/react/react/releases/tag/v19.3.1
- React RCE GitHub Advisory Database: https://github.com/advisories/GHSA-xqc2-xf4c-x3h3
- React Server Functions DoS advisory: https://github.com/react/react/security/advisories/GHSA-h3gv-c5rc-p453

## Track 3 — Node.js / backend

- Official Node.js security release date: **11 November 2026**.
- Patched versions: **22.23.5**, **24.22.3**, **26.13.1**.
- The security bulletin index lists **16 CVEs** (7 High, 6 Medium, 3 Low). The individual release pages list a separate low-severity **CVE-2026-123873** (heap-snapshot destination check), while the bulletin lists **CVE-2026-106071** (Permission Model wildcard filesystem over-grant). They are distinct descriptions; the union of identifiers visible across the bulletin and release notes is 17. CVE-2026-123872 is one identifier repeated for multiple TLS fixes, not three unique CVEs.
- Mango PR #143's current draft already distinguishes the 16-entry bulletin from the additional release-note CVE. No duplicate article/comment required.
- Node **27.0.0-alpha.0.1.0**, published 12 November, remains Alpha and is not a stable/LTS production recommendation.

Primary sources:
- Security bulletin: https://nodejs.org/en/blog/vulnerability/november-2026-security-releases
- Node 22.23.5: https://nodejs.org/en/blog/release/v22.23.5
- Node 24.22.3: https://nodejs.org/en/blog/release/v24.22.3
- Node 26.13.1: https://nodejs.org/en/blog/release/v26.13.1

## Track 4 — AI / cloud / developer news

### New unowned story selected

**GitHub Enterprise Server support in the GitHub Copilot app**
- GitHub Changelog publication date: **13 November 2026**; no separate event date stated.
- Status: generally available, previously opt-in preview.
- Available in GitHub Copilot app **1.2.0 and later**; no separate feature release number.
- Connect GHES after first signing in with GitHub.com or GHE.com; supported context includes remote repositories, issues and pull requests.
- Explicit limitation: GHES cloud sessions are unavailable.
- Requests require a cloud account with a Copilot licence or a separately configured model provider.
- No separate feature-specific price, India-specific country list or India-specific price is published. The draft does not claim a blanket India availability guarantee.
- No current relevant original YouTube video was verified; no video ID or iframe was invented.

Sources:
- GitHub Changelog: https://github.blog/changelog/2026-11-13-github-enterprise-server-support-in-the-github-copilot-app/
- GHES setup documentation: https://docs.github.com/en/enterprise-server@3.22/copilot/copilot-on-ghes/sign-in-on-copilot-app
- Copilot plans: https://github.com/features/copilot/plans

Existing cloud/developer owners retained: Groot PR #732 (AWS EC2 Image Builder + DevOps Agent), Groot PR #737 (GitHub AI Scan repository REST API), Forsk PR #221 (Google Cloud Agent Registry Skills GA), and existing Gemini 4 Hydrogen Node.js/Copilot topic branch. No duplicate cross-brand article created.

## Production completed this run

### Mango Engineers — new isolated draft PR #230

- PR: https://github.com/satnamkhowal/mangoengineers.com/pull/230
- Branch: `news-factory/github-copilot-app-ghes-support-20261114-0407`
- Article: `docs/news-factory/drafts/github-copilot-app-ghes-support-guide-2026.md` — **2,013 words**, original English, answer-first, India/Jaipur context, setup steps, requirements, cloud-session limitation, licensing/cost caveats, security checklist and FAQ.
- Metadata: `docs/news-factory/drafts/github-copilot-app-ghes-support-guide-2026.metadata.json` — source dates, GA/version, status, pricing/India caveats, SEO/AEO/GEO, video status and media provenance.
- Original graphic: `docs/news-factory/media/copilot-ghes-setup-workflow.svg` — self-authored **1200×675** vector infographic. No third-party logo, screenshot, photograph or icon reused.
- Local optimized derivatives:
  - `/mnt/data/news-factory/2026-11-14/0407/mango-copilot-ghes/copilot-ghes-setup-workflow.png` — 1200×675, 104,092 bytes.
  - `/mnt/data/news-factory/2026-11-14/0407/mango-copilot-ghes/copilot-ghes-setup-workflow.webp` — 1200×675, 52,014 bytes.
  - Original SVG: 1200×675, 4,516 bytes, SHA-256 `a6654d225da94938cfc8767e47e80f046cb795601f03c271682fcebfcb337343`.
- Media source/license/permission: original News Factory artwork; no third-party permission required. Attribution: Mango Engineers News Factory. Alt text and dimensions recorded in metadata.
- No relevant current official/reputable original YouTube video was verified; no video ID, iframe or downloaded video.

### Validation and release gate

- GitHub read-back of all three committed files: PASS.
- Metadata JSON parse: PASS.
- Article word count (2,013), relative SVG reference and source-date separation: PASS.
- SVG XML parse, 1200×675 dimensions and zero external image references: PASS.
- PNG/WebP decoding and visual inspection: PASS.
- Main comparison: **3 commits ahead / 0 behind**, exactly three added files.
- PR #230 is **OPEN / DRAFT**, **mergeable=true**, not merged.
- PHP Architecture Check run **43522326809** failed before executing any step. The first job returned an empty step list and its log endpoint returned BlobNotFound 404. One retry was accepted; the retry also completed failure with an empty step list and BlobNotFound 404. This is a runner/log-provisioning blocker, not a code or article validation result. No passing CI result is claimed.
- Independent editorial review, responsive browser QA and production publication remain pending.
- Forsk PR #227 and #228 received source/status verification comments; no duplicate draft or new graphic was created there.

## Production ledger

| Stage | New count this run |
|---|---:|
| Research tracks checked | 4 |
| New unowned stories cleared | 1 |
| Original articles drafted | 1 |
| Original graphics committed | 1 SVG |
| Local optimized derivatives | 2 (PNG, WebP) |
| Verified story-specific YouTube embeds | 0 |
| Independent QA-ready articles | 0 |
| Live / published articles | 0 |
| Merged / deployed PRs | 0 |

## Blockers and next actions

1. Resolve the Mango PHP Architecture Check runner/log provisioning failure; do not interpret empty steps/BlobNotFound as a content failure or pass.
2. Complete independent editorial and responsive browser QA for Mango PR #230; keep it Draft.
3. Recheck Sage IT, NMMSS and VSSC UG before **15 November**; VSSC PG before **16 November 23:59 IST**.
4. Recheck IIIT Kottayam's online-vs-hybrid mode with the lab before anyone pays the ₹5,000 fee.
5. Recheck Google Student Researcher before **4 December** and SDEF before **30 November**.
6. Keep PM-USP J&K/Ladakh fresh-versus-renewal status on hold until the NSP wording is unambiguous.
7. Continue the four source lanes and create another article only when a fresh, verified, unowned topic clears the current queue and branch checks.

**No merge, deployment, publication or live indexing was performed.**
