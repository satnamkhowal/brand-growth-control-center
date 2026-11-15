# News Factory research and draft cycle — 15 November 2026, 17:37 IST

## Outcome

Four non-overlapping research lanes were checked: official student/developer opportunities; React/frontend releases and security; Node.js/backend releases and security; AI/cloud/developer announcements.

One new unowned story was implemented as an isolated Forsk Coding School draft PR. Existing owners were retained for React, Node.js, CMI, Google Student Researcher, AlloyDB Express and A2UI. No article was merged, deployed or published.

## New original draft

- Forsk Coding School PR #239: https://github.com/satnamkhowal/forsk-coding-school/pull/239
- Branch: `news-factory/protocol-zero-iitm-student-ctf-2026-27-20261115-1737`
- Base: `main@9a25fd5a11641420ac716d3fd25103e6e8362fbf`
- 2,264-word original English SEO/AEO/GEO guide: `docs/news-factory/drafts/iit-madras-protocol-zero-student-ctf-hackathon-2026-27.md`
- Metadata and source/status caveats: matching `.metadata.json`
- Original accessible 1200×675 SVG timeline, provenance and alt text: `docs/news-factory/media/iit-madras-protocol-zero-student-ctf-hackathon-2026-27-timeline.svg` and `.provenance.json`
- Task-specific handoff: `docs/ai-ops/handoffs/news-factory-protocol-zero-2026-11-15.md`

### Protocol Zero verification

Official page: https://cystar.iitm.ac.in/protocol-zero-boot-hack-ctf/  
Registration destination: https://unstop.com/p/protocol-zero-centre-for-cybersecurity-trust-and-reliability-iit-madras-cystar-1798676

- The official page does not display its original publication date; it separately lists the call-for-participation start as 7 November 2026.
- The page lists registration until 30 November 2026, 23:59 IST. The linked Unstop destination is listed, but live response/acceptance state was not independently confirmed.
- Eligibility: currently enrolled UG/PG students at recognised institutions across India; age 18+; teams of 2–3; individual entry prohibited; cross-institution teams allowed.
- Top-three awards: ₹2.5 lakh / ₹2 lakh / ₹1.5 lakh. An additional ₹4 lakh is collectively distributed among onsite-final teams. The ₹10 lakh aggregate is across different awards/teams, not a per-person prize.
- Paid Summer 2027 internships are listed for top performers at IIT Madras and partner institutes; count, duration and stipend are not stated.
- Final CTF: 12–13 March 2027 at Shiv Nadar University, Chennai; finalists must attend in person.
- Registration fee, travel support and final reward split are not stated on the official page. Draft does not call the event free.
- Code of conduct limits offensive testing to organiser-provided environments; IP is owned by the organising institutions under the published clause.

No story-specific original video with a verifiable ID, channel, upload date and confirmed embed permission was found; no iframe was included.

## Other opportunity-lane findings

- CMI Computer Science Summer 2027 is already owned by Forsk PR #164; its 31 January 2027 deadline and form remain covered. No duplicate created.
- IIIT Guwahati's MeitY-funded project internship lists 15 November 2026 as the application date (one vacancy; ₹15,000/month; 10 months). The date is today, no closing hour is stated, and the linked Google Form response state could not be verified; no new article was created at the end of the stated date.
- Google Software Engineering PhD Intern, Summer 2027 is listed on Google Careers with an Apply control, India location choices including Bengaluru, Hyderabad and Pune, and a 12+ week paid internship. No application deadline is displayed. It was retained as a research lead rather than opening another Google PhD-internship article in this bounded batch.
- Existing Forsk PR #146 remains the Google Student Researcher 2027 owner.

## React / frontend

- React's feature release page still identifies React 19.3 (9 September 2026) as the current feature release; no new November stable release was found.
- Patched React tags remain 19.3.1, 19.2.9, 19.1.10 and 19.0.9 (14 October 2026).
- Existing owner: Forsk PR #145.
- Important metadata correction: upstream GHSA-xqc2-xf4c-x3h3 was published 14 October; the GitHub Advisory Database record was published/reviewed/updated 10 November and now lists CVE-2026-126187. The existing article still contains a contradictory sentence saying no CVE is listed. A correction request was added to PR #145; no owner-branch file edit was made.
- Separate High DoS advisory GHSA-h3gv-c5rc-p453 remains distinct.

Sources:
- https://react.dev/blog/2026/09/09/react-19-3
- https://github.com/advisories/GHSA-xqc2-xf4c-x3h3
- https://github.com/react/react/security/advisories/GHSA-h3gv-c5rc-p453
- https://github.com/facebook/react/releases

## Node.js / backend

- Official security bulletin date: 11 November 2026.
- Patched lines: Node 22.23.5, 24.22.3 and 26.13.1.
- Bulletin index lists 16 entries (7 High / 6 Medium / 3 Low). The individual release pages separately list CVE-2026-123873 (heap-snapshot destination) while the bulletin lists CVE-2026-106071 (wildcard Permission Model over-grant); these are distinct low-severity descriptions, not aliases.
- Existing Mango PR #143 already records both identifiers separately and is the sole owner. No duplicate Node article created.
- Node 27.0.0-alpha.0.1.0 (12 November) remains Alpha, not an LTS/stable replacement.

Sources:
- https://nodejs.org/en/blog/vulnerability/november-2026-security-releases/
- https://nodejs.org/en/blog/release/v22.23.5
- https://nodejs.org/en/blog/release/v24.22.3
- https://nodejs.org/en/blog/release/v26.13.1
- https://nodejs.org/en/blog

## AI / cloud / developer news

Existing owners retained:
- Mango PR #266 — AlloyDB Express Preview guide.
- Groot PR #658 — A2UI 1.0 generative UI guide.
- Forsk PR #185 — GitHub Copilot model retirement guide and separate December 14 addendum.

Google Cloud's November 12 Data Cloud roundup and AlloyDB documentation were rechecked; no duplicate AlloyDB Express article was created. No new AI/cloud article was opened in this bounded cycle.

## Repository review and concurrency

- Central PR #19 remains open/draft and diverged: 232 commits ahead / 5 behind `main`; GitHub reports mergeable=false. This checkpoint is append-only. No rebase, force-push or merge.
- Mango Engineers: read README, AGENTS, agent-start guide, task board, work log and integration queue. Existing AlloyDB Express PR #266 and Node.js PR #143 retained; no Mango write.
- Groot Academy: read .agent README, current state, backlog, decisions, GO-5 handoff and migration status. Existing A2UI PR #658 retained; no Groot write.
- Forsk Coding School: read README.txt, ops/task-queue, master task board, session handoff, image audit and image workflow. New PR #239 is file-disjoint from active PR #145/#164 content ownership. Shared `docs/ai-ops/MASTER_TASK_BOARD.md` and `SESSION_HANDOFF.md` were not modified because both active PRs already touch those files; the new task-specific handoff records this limitation.
- Jaipur Engineers: verified `satnamkhowal/jaipurengineers.com` as the current repository target (`je2` resolves by redirect); read README-INSTALL, migration notes, content radar, queue, backlog, content calendar and existing PR #47. No Jaipur write; existing PM Scholarship owner PR #47 retained.

## Checks and status ledger

- Local article word count: 2,264.
- SVG XML parse: PASS.
- Metadata JSON parse: PASS.
- Provenance JSON parse: PASS.
- 1200×675 PNG render and visual inspection: PASS.
- GitHub read-back of all five PR #239 files: PASS.
- Forsk branch compare: 5 ahead / 0 behind main.
- Independent editorial/security QA: PENDING.
- Verified video embeds: 0.
- New graphics: 1 original SVG.
- New draft PRs: 1.
- QA-ready: 0.
- Live / merged / deployed: 0.

## Next actions

1. Independent editorial/security review of Forsk PR #239.
2. Confirm Unstop form acceptance and any fee before publishing Protocol Zero details.
3. Resolve the contradictory CVE sentence in Forsk PR #145.
4. Continue checking official Node.js/React release pages and dated opportunity windows.
5. Do not merge, deploy or publish without approval.
