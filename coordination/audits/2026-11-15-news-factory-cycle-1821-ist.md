# News Factory research and draft cycle — 15 November 2026, 18:21 IST

## Outcome

Four non-overlapping research lanes were checked against primary sources where available: (1) student/developer programmes and opportunities, (2) React/frontend releases and security, (3) Node.js/backend releases and security, and (4) AI/cloud/developer announcements.

One new unowned opportunity was selected and implemented as an isolated Forsk Coding School draft PR. Existing story owners were retained for React, Node.js, Google opportunities, AlloyDB Express, AWS Elastic Beanstalk, A2UI and Copilot model retirements. No article was merged, deployed or published.

## New original draft — Forsk Coding School

- PR #241: https://github.com/satnamkhowal/forsk-coding-school/pull/241
- Branch: \`news-factory/vytron-26-india-student-hackathon-20261115-1809\`
- Base: \`main@9a25fd5a11641420ac716d3fd25103e6e8362fbf\`
- Repository read-back article count: 2,762 words by the News Factory regex counter.
- Article: \`docs/news-factory/drafts/vytron-2026-india-student-hackathon-guide.md\`
- Metadata: \`docs/news-factory/drafts/vytron-2026.metadata.json\`
- Original 1200×675 SVG: \`docs/news-factory/media/vytron-2026-three-rounds-and-entry-details.svg\`
- Provenance: matching \`.provenance.json\`
- Task handoff: \`docs/ai-ops/handoffs/news-factory-vytron-2026-11-15.md\`

### VYTRON verification and conflict handling

Primary organiser page: https://vytron26.droidecks.sbs/  
Organizer-listed Unstop page: https://unstop.com/hackathons/vytron26-droidecks-1786652

- Official event page publication date is not displayed; page checked 15 November 2026.
- Official page: fully online, India-wide, team size 2–4, ₹79 per member, three rounds, ₹1,00,000+ mixed reward pool.
- **Deadline conflict:** official event page says 30 November 2026; Unstop page, marked as listed by Droidecks, says 25 November 2026 at 12:00 AM IST. Draft uses the earlier 25 November timestamp as conservative cutoff until organiser confirms an extension.
- **Registration-link conflict:** official site links to \`https://forms.gle/6PcXwy5WrUd59M1D6\`; Unstop lists \`https://forms.gle/9r5Qj42Np9nZ6yhc7\`. Neither form's response/acceptance state was independently confirmed. Draft instructs applicants to confirm the correct form with organiser before entering personal data or paying.
- Unstop says event timing is tentatively after 15 December 2026 and separately lists ₹50,000 / ₹30,000 / ₹15,000 cash awards, five ₹1,000 special awards and internship offers from UpskiilsBharat. The official event site does not itemise these benefits; draft keeps them as listing-level details and requires organiser confirmation.
- Exact age, degree, year-of-study and institution restrictions are not consistently specified.
- No official/reputable original YouTube video with a verifiable ID, channel, upload date and confirmed embed permission was found; no iframe included.

### Media

- Original self-authored SVG, no third-party artwork, logo, screenshot or photo reused.
- Provenance, attribution, local path, alt text and dimensions recorded.
- Local PNG and WebP derivatives generated and visually inspected; SVG committed as the web asset.

## Other research-lane findings and owner routing

### 1. Student / developer programmes

- VYTRON 2026 is the only new unowned opportunity selected in this bounded batch; deadline and form conflicts are explicitly disclosed.
- Google Student Researcher 2027 remains with Forsk PR #146.
- Google Software Engineering PhD Intern, Summer 2027 remains a research lead; Google Careers lists an Apply control and India location choices, but no closing deadline was displayed. No duplicate article created.
- CMI CS Summer 2027 remains with Forsk PR #164.
- IIT Madras Protocol Zero remains with Forsk PR #239; no duplicate.
- PMSS CAPF / State-UT Police scholarship remains with Jaipur PR #47 (student application deadline 30 November 2026).
- NRSC student-project guide remains with Mango PR #265.
- Other deadline-day forms without independently confirmed response status were not promoted as confirmed-open opportunities.

### 2. React / frontend

- React feature release 19.3 is dated 9 September 2026; latest official patch tags remain 19.3.1, 19.2.9, 19.1.10 and 19.0.9, all dated 14 October 2026.
- GHSA-xqc2-xf4c-x3h3 was published 14 October 2026, is Critical (CVSS 9.5), and carries CVE-2026-126187. Patched RSC package versions are 19.0.9 / 19.1.10 / 19.2.9 / 19.3.1.
- Separate GHSA-h3gv-c5rc-p453 remains High.
- Existing Forsk PR #145 remains the sole owner; a correction comment is already present. No duplicate article or new owner comment added.

Sources:
- https://github.com/facebook/react/releases
- https://github.com/react/react/security/advisories/GHSA-xqc2-xf4c-x3h3
- https://react.dev/blog/2026/09/09/react-19-3

### 3. Node.js / backend

- Official Node.js security bulletin date: 11 November 2026.
- Patched versions: 22.23.5, 24.22.3 and 26.13.1.
- Bulletin lists 16 vulnerability entries (7 High / 6 Medium / 3 Low); highest severity High.
- Existing Mango PR #143 remains the sole Node.js story owner; no duplicate article or owner comment added.

Source: https://nodejs.org/en/blog/vulnerability/november-2026-security-releases/

### 4. AI / cloud / developer news

- GitHub's 13 November Copilot model-retirement update remains with Forsk PR #185.
- AWS Elastic Beanstalk AL2023 Node.js platform/security update remains with Groot PR #774.
- AlloyDB Express Preview remains with Mango PR #266.
- A2UI 1.0 remains with Groot PR #658.
- No additional AI/cloud story met the unowned-and-verified threshold in this bounded batch.

Source: https://github.blog/changelog/month/11-2026/

## Repository review and concurrency

- Central PR #19 remains open/draft and diverged: 233 commits ahead / 5 behind \`main\`; GitHub reports mergeable=false. This audit is append-only on the existing PR branch. No rebase, force-push or merge.
- Mango Engineers: accessible repo \`satnamkhowal/mangoengineers.com\`; current relevant owners #143, #265 and #266 reviewed. No VYTRON duplicate found; no Mango write.
- Groot Academy: accessible repo \`satnamkhowal/grootacademy.com\`; current relevant owners #774 and #658 reviewed. Existing \`.agent\` documentation references a separate \`gta\` canonical repository that is not accessible in this connector session; no new Groot write.
- Forsk Coding School: current \`main\` SHA read; master task board, session handoff, worker registry and relevant PRs #145, #185 and #239 reviewed. New PR #241 uses distinct VYTRON paths. Controller-owned shared task-board/session-handoff files were not modified.
- Jaipur Engineers: accessible repo \`satnamkhowal/jaipurengineers.com\`; PMSS owner #47 and GITAM challenge #56 reviewed. No new Jaipur story/write.
- Clever Ape Academy repository is visible in the accessible repository list, but no current verified story was selected and no write was made.

## Checks and status ledger

- Forsk PR #241: 5 files, 5 initial commits; after metadata/handoff count correction, branch has 7 commits ahead / 0 behind \`main\`.
- GitHub read-back of all five PR files: PASS.
- Metadata JSON and provenance JSON parse: PASS.
- SVG XML parse / 1200×675 render: PASS.
- Local PNG/WebP decode and visual inspection: PASS.
- PR-triggered workflow runs returned: none.
- Commit status checks returned: none; CI is not verified.
- Independent editorial/security QA: PENDING.
- Verified video embeds: 0.
- New original graphics: 1 SVG (with local PNG/WebP derivatives).
- New draft PRs: 1.
- QA-ready: 0.
- Live / merged / deployed: 0.

## Next actions

1. Resolve VYTRON's deadline and Google Forms-link conflict with organiser before any publication or application-status claim beyond the conservative cutoff.
2. Independent editorial and technical review of Forsk PR #241.
3. Continue rechecking official student-programme deadlines and React/Node release pages.
4. Keep current React, Node, AWS, AlloyDB, A2UI and Copilot owner boundaries; do not create duplicates.
5. Do not merge, deploy or publish without approval.
