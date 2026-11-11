# News Factory cycle — 12 November 2026, 04:04 IST

## Summary

Four non-overlapping research lanes were checked against primary sources and current open PR ownership. One distinct, recent unowned backend story was selected for Groot Academy: Node.js 27 Alpha and its V8 15.6 compatibility changes. One original graphic was committed with the draft. Existing opportunity, React, Node security and AI/developer owners were preserved.

## 1. Student, developer and opportunity lane

- **Google Student Researcher 2027:** official Careers listing currently says apply before **4 December 2026**, rolling review, Remote eligible in India. Currently enrolled Bachelor's/Master's/PhD students in listed disciplines with CS-area experience. No stipend or application fee stated. Existing owner: Forsk PR #146.
- **NeGD Non-Technical Winter Internship 2026:** MeitY listing published **11 November 2026**, deadline **20 November 2026**. Existing Forsk PR #180 is based on the distinct November PDF and records 12 positions, ₹15,000/month conditional remuneration paid after completion/report acceptance, 2–3 month tentative duration and mandatory institutional forwarding. Google Form response acceptance remains unverified; retain the caution.
- **NeGD Technical Internship 2026:** separate MeitY listing published 11 November with 20 November due date. Current technical PDF and form were not retrievable; do not reuse the May Summer PDF (its 15 June deadline is closed). Research-only lead; no new article.
- **DIBD/BHASHINI Young Professionals:** MeitY listing dated 10 November, 8 positions, due 10 December. Detailed advertisement/eligibility and application route not verified; no article yet.
- **Near deadlines:** NMMSS 15 November (Forsk #173); VSSC UG project 15 November and PG project 16 November (Forsk #172); SDEF scholarship 30 November (Forsk #178). No duplicate opportunity drafts.

Primary links:
- https://www.google.com/about/careers/applications/jobs/results/125423735539671750-student-researcher
- https://www.meity.gov.in/offerings/vacancies?page=1&target_lang=en
- https://www.meity.gov.in/whats-new
- https://scholarships.gov.in/All-Scholarships

## 2. React / frontend lane

- React core latest visible stable tags remain 19.3.1, 19.2.9, 19.1.10 and 19.0.9, all dated 14 October 2026; no newer November React core release found. Existing Forsk #145 remains owner.
- Official React Native GitHub Releases index now exposes **0.89.0-rc.1**, published **10 November 2026 at 01:35 UTC**, explicitly Pre-release. Notes include DevTools WebSocket inspection, shareable Metro transform cache, corrected framework WebSocket initiator and Android renderer fix. Existing Groot #644 remains sole owner. A source-verification comment was added: https://github.com/satnamkhowal/grootacademy.com/pull/644#issuecomment-6809071281

Primary links:
- https://github.com/react/react/releases
- https://github.com/react/react-native/releases
- https://reactnative.dev/releases/overview

## 3. Node.js / backend lane

- **New unowned story:** Node.js 27.0.0-alpha.0.0.0 released 29 October; Node.js team's V8 15.6 explainer published 5 November. V8 15.6.75.13, annual cycle (six months Alpha plus six months Current before LTS), serialization incompatibility, heap defaults/snapshots, OpenSSL 4.1 and API changes are covered. Alpha is explicitly not production-ready.
- **New Groot Academy Draft PR #650:** https://github.com/satnamkhowal/grootacademy.com/pull/650
- **Current production security releases:** Node.js 26.13.1, 24.22.3 and 22.23.5 were published 11 November. Existing Mango #143 remains sole owner of the security-update story; CVE-2026-126051 is listed in 24.x/26.x, not 22.x. No duplicate security article.

Primary links:
- https://nodejs.org/en/blog/release/v27.0.0-alpha.0.0.0
- https://nodejs.org/en/blog/announcements/notable-v8-changes-from-node-js-26-to-27-alpha
- https://nodejs.org/en/about/previous-releases
- https://nodejs.org/en/blog/release/v26.13.1
- https://nodejs.org/en/blog/release/v24.22.3
- https://nodejs.org/en/blog/release/v22.23.5

## 4. AI / cloud / developer lane

- GitHub issue types and fields became generally available for personal-account repositories on 11 November; existing Forsk #182 owns the student-team guide.
- Gemini 4 Carbon became available for developers on 10 November through paid-tier API access in Google AI Studio and Android Studio; existing Forsk #168 owns the story.
- No new sufficiently verified, unowned AI/cloud announcement was selected.

## Repository and coordination review

- Mango Engineers, Groot Academy, Forsk Coding School and central control repository default branches are main; their current task/instruction files and open PR ownership were reviewed before writing.
- Jaipur website repository lookup returned 404 in this run. No Jaipur write was attempted.
- Groot's existing GA-B00016 browser gate and 100K blog queue were not modified.
- Central PR #19 branch ops/news-factory-cycle-20261109-2209 was reused. It remains open/draft and diverged from main; no rebase or merge was attempted.

## New delivery and QA ledger

- Groot PR #650: one original English article draft (about 1,544 words), one original self-authored 1200×675 SVG, and a provenance JSON sidecar; one commit, three files, 214 additions.
- Local PNG and WebP derivatives were generated and decoded at 1200×675; they are local only and not committed in the PR.
- Media provenance records source, permission basis, attribution, alt text, dimensions and local paths. No third-party graphic or logo was downloaded.
- No YouTube video met the required ID/channel/date/embed-permission checks; no iframe or video download.
- GitHub read-back, metadata JSON parse, SVG tag balance and local image decoding/dimensions passed.
- Independent editorial QA, technical/security QA and responsive browser QA remain pending. No workflow run or commit status was returned; CI pass is not claimed.
- No merge, deployment, publication or application submission occurred.

| Stage | This cycle |
|---|---:|
| Research lanes | 4 |
| New verified unowned story selected | 1 |
| New article drafts | 1 |
| Original SVG committed | 1 |
| Local optimized PNG/WebP | 2 |
| Verified video embeds | 0 |
| Independent QA-ready increment | 0 |
| Live/published increment | 0 |

Next actions: independent QA of Groot #650; recheck the NeGD Technical Internship current PDF/form and BHASHINI Young Professional advertisement; monitor 15–20 November deadlines; keep Node.js 27 Alpha separate from the supported LTS security updates.
