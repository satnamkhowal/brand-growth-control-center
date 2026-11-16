# News Factory research and draft cycle — 16 November 2026, 08:03 IST

## Outcome

Four non-overlapping lanes were checked against current primary sources and the existing brand PR/issue inventory. One fresh cloud release was verified: **Google SecOps Publisher Agent 2.7.2**, listed as available in Google Cloud release notes dated **15 November 2026**. The Mango Engineers local draft from the previous production pass was revalidated and updated with its original graphic and a clearly labelled background-video fallback link. The existing IICT Winter Internship 2026 Forsk guide was also revalidated and updated with its original graphic and live-form caveat.

**No new article draft or brand GitHub PR was created in this run.** Other fresh topics already have owners, and the two local drafts are waiting for a safe repository handoff. No article was merged, deployed or published.

## 1. Official programmes and opportunities

- **Google Student Researcher 2027 — Forsk PR #146.** Google Careers still displays Apply, India / Remote eligible, rolling review and a **4 December 2026** completion deadline. Minimum qualification: current Bachelor's, Master's or PhD enrolment in a listed discipline plus experience in a relevant computer-science research area. Stipend, fixed duration and application fee are not stated. Existing owner retained; not described as a new opening.
- **IICT Winter Internship 2026 — local Forsk draft.** The official circular is dated **22 September 2026**; registration is listed through **30 November 2026**; first training day is **10 December 2026**. It is a 45-day online, fee-based and non-stipendiary programme: 15 days of coursework plus 30 days of project work, stated capacity 1,070, training fee **₹970**. The official registration form page is accessible and shows applicant fields plus a Proceed to Pay control, but form submission, payment acceptance and remaining seats were not tested. The official page warns users to register only through IICT's own website. This is not a paid job or scholarship.
- **NeGD Winter 2026 technical and non-technical internships — Forsk PRs #225 and #180.** The current careers page still lists **20 November 2026**. The two role tracks remain separately owned. Form response/acceptance was not tested; no duplicate article created.
- **VSSC academic project work — Forsk PR #172.** The live HRDD portal still has a status contradiction: the PG current project slot is labelled closed, while the same page prints an online window through **16 November 2026, 11:59 PM**. The page does not establish that the form is accepting submissions. Existing owner comment at 07:05 IST already records this uncertainty; no duplicate comment or “open” claim added. The UG 15 November date has passed; INT 08 is closed and INT 09 is a separate 2027 internship intake.

## 2. React / frontend

- React 19.3 remains the latest feature release, dated **9 September 2026**.
- Latest official patch tags remain **19.3.1, 19.2.9, 19.1.10 and 19.0.9**, all dated **14 October 2026**.
- The 14 October React Server Components advisories remain the latest verified security items: Critical RSC remote-code-execution and High Server Functions denial-of-service advisories. No newer stable React release or advisory was found.
- Existing Forsk PR #145 remains the sole owner; its CVE wording correction/independent QA remains pending. No duplicate article created.

## 3. Node.js / backend

- The **11 November 2026** security release remains current for **22.23.5, 24.22.3 and 26.13.1**. The official bulletin lists 16 vulnerability entries (7 High, 6 Medium, 3 Low); highest severity is High.
- **Node.js 27.0.0-alpha.0.1.0**, dated **12 November**, remains Alpha and is not a production/LTS replacement.
- Existing owners retained: Mango PR #143 (November security guide) and #229 (Node 27 Alpha); Groot PR #650. No duplicate article created.

## 4. AI / cloud / developer news

- **Google SecOps Publisher Agent 2.7.2 — fresh, verified, locally drafted.** The 15 November Google Cloud release note lists alert lazy loading for remote actions, a fix for installing integrations with interdependent dependency files, a remote-agent deletion directory-permission fix, and Publisher stability/security updates. The note does not enumerate CVEs or state a price change. Google architecture docs confirm the Publisher/Remote Agent task flow and TLS on TCP 443; onboarding requires an active Standard, Enterprise or Enterprise Plus package registration and a signed contract. The local Mango draft is revalidated; no GitHub owner/PR was found for this exact release. A new Mango PR was held because current PRs #143, #282 and #283 edit shared task-board/work-log files and AGENTS requires a task claim before editing.
- **GitHub AI Scan for repositories REST API** — published **13 November**, public preview. Existing Groot PR #737 and Jaipur issue #52 already own the same story; no duplicate.
- **GitHub Copilot model deprecations effective 14 December** — published **13 November**. Existing Forsk PR #185 owns the update; no duplicate.
- Google Cloud Quotas, Gemini Enterprise/Antigravity and Apigee updates are already represented in active Mango/Groot/Jaipur work. No duplicate article opened.

## Repository and concurrency review

- **Central:** reused existing News Factory PR #19 and branch `ops/news-factory-cycle-20261109-2209`. The branch compares **235 commits ahead / 5 behind main (diverged)**. This checkpoint is append-only; no rebase, force-push or merge.
- **Mango Engineers:** read `AGENTS.md`, `docs/agent-start-here.md`, task board, work log and integration queue. Rules require a task claim before editing. Open PRs #143, #282 and #283 touch shared task-board/work-log paths; no brand commit or shared-file write was made.
- **Forsk Coding School:** read `README.txt`, master task board, worker registry and session handoff. Root `README.md` / `AGENTS.md` were absent at checked paths; the worker registry reserves master board/session-handoff aggregation to the controller. Existing PRs #145, #146, #172, #180, #185, #225, #241 and #250 remain owners. No new branch or PR.
- **Groot Academy:** canonical accessible repository is `satnamkhowal/grootacademy.com`; AI Scan is already owned by PR #737, and other current AI/cloud/Node.js topics have active owners. No new write.
- **Jaipur Engineers:** `docs/content-radar.md` keeps Auto Publish OFF; AI Scan is already owned by issue #52 and other current stories have active owners. No new write.

## Local draft and media handoff

- Mango: existing Google SecOps Publisher Agent 2.7.2 draft revalidated; original infographic embedded. The official Google Cloud YouTube candidate is **“Introducing Google Security Operations”**, video ID `VT4xpfPaD1w`, verified Google Cloud channel, published **20 June 2024**. It is general product background, not a 2.7.2 walkthrough. Embed permission/playback could not be verified; the article includes only a labelled fallback link, no iframe.
- Forsk: existing IICT Winter Internship guide revalidated; original two-phase infographic embedded. No suitable programme-specific original video with verified ID/date/embed permission was found.
- Two original self-authored SVG graphics and their 1200×675 PNG/WebP derivatives were retained and validated. No third-party artwork or video was downloaded/reuploaded.
- Local package contains both Markdown drafts, metadata, SVG/PNG/WebP assets and this cycle report; these files have not been committed to brand repositories.

## Checks and status ledger

| Stage | This run |
|---|---:|
| Research lanes checked | 4 |
| Fresh verified stories | 1 (Google SecOps Publisher Agent 2.7.2) |
| New article drafts created | 0 |
| Existing local drafts revalidated/updated | 2 |
| New graphics created | 0 |
| Existing original graphics validated | 2 SVG + 2 PNG + 2 WebP |
| Verified YouTube embeds | 0 |
| New brand GitHub PRs / commits | 0 |
| Independent QA-ready | 0 |
| Live / merged / deployed | 0 |

Metadata JSON parse, SVG XML parse, PNG/WebP decode and 1200×675 dimensions passed. Both images were visually inspected. Independent editorial, technical and eligibility QA remain pending. No browser embed test, application submission, CI pass, merge, deployment or publication is claimed.

## Next action

After Mango PRs #282/#283 release the shared task-board/work-log paths, claim the Google SecOps 2.7.2 draft as a distinct News Factory task and open an isolated draft PR. Independently QA the two local drafts before any merge or publication decision.
