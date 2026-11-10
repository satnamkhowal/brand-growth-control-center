# News Factory cycle — 11 November 2026, 02:01 IST

## Executive status

Two new documentation-only draft PRs were produced. Both have original English content, one original 1200×675 SVG each, and source/media provenance sidecars. No article was merged, deployed, published or indexed.

- Groot Academy: https://github.com/satnamkhowal/grootacademy.com/pull/609 — AWS Bedrock AgentCore Runtime V2 snapshot safety and Node.js guidance.
- Forsk Coding School: https://github.com/satnamkhowal/forsk-coding-school/pull/170 — Science Academies Summer Research Fellowship 2027 India eligibility guide.

## New draft deliveries

### Groot Academy — AgentCore Runtime V2

- Original GA announcement: 18 September 2026. AWS Weekly Roundup: 9 November 2026; the roundup is not the GA date.
- Article: 2,349 words; snapshot lifecycle, V2 opt-in, Mumbai Region (ap-south-1), AWS-reported P75 cold-start benchmark caveats, 120-second health requirement, startup/request-state separation, current listed consumption rates and pricing caveats.
- Important AWS-documented Node.js caveat: crypto.randomBytes(), randomUUID(), randomInt() and getRandomValues() can repeat across restored instances, including in the request handler. The guide explains the /dev/urandom workaround and per-request state design.
- Original media: self-authored 1200×675 SVG; local PNG 111,760 bytes, visually inspected; optimized WebP 52,954 bytes. Provenance records sources, dates, permission, attribution, alt text, paths, dimensions and SHA-256 hashes.
- No relevant official/reputable YouTube ID plus embed permission was verified; no iframe was invented.
- PR base main 99336e8d0b412f6e0f0bdc0464e0aec4b8fea2b5; 3 commits ahead / 0 behind; 3 added paths; latest PR-info mergeable=true. No workflow run returned. Independent editorial/source QA and responsive/browser QA pending.

Official sources:
- https://aws.amazon.com/blogs/machine-learning/the-new-agentcore-runtime-elastic-optimized-and-consistently-fast-starts/
- https://aws.amazon.com/blogs/aws/aws-weekly-roundup-agentcore-runtime-v2-amazon-dynamodb-bulk-put-items-and-more-november-9-2026/
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-v2-optimize.html
- https://aws.amazon.com/bedrock/agentcore/pricing/

### Forsk Coding School — Science Academies SRFP 2027

- Official announcement date: 10 September 2026. Application deadline: 30 November 2026.
- Programme: two-month guided research project during calendar year 2027; summer preferred.
- India-wide standard SRFP. Course/year list includes BE/BTech/BCA second/third year and MCA first year; 65% average in core subjects excluding languages; teachers teaching in a college/university may apply without the marks threshold; PhD students are ineligible, while integrated PhD first/second year is separately listed.
- Required: Class X onward marksheets (JPEG, each <=700 KB), 150–250-word specific project-interest note, one current teacher contact for recommendation. One application only; no hard copies.
- Selected candidates receive entitled round-trip train fare and a monthly fellowship for living expenses. The public announcement does not state the fellowship amount or an application fee.
- Explicitly distinguishes the India-wide SRFP from separate region-restricted FAST-SF 2027; do not apply FAST-SF state restrictions to standard SRFP.
- Article: 2,084 words, original English, eligibility matrix, application steps, India/Jaipur clarification, FAQs and official source links.
- Original media: self-authored 1200×675 SVG; local PNG 121,611 bytes, visually inspected; optimized WebP 52,498 bytes. Metadata records official sources, permission, attribution, alt text, paths, dimensions and SHA-256 hashes.
- No programme-specific verified YouTube ID plus embed permission; no iframe.
- PR base main a690ef725029e8c7f96b6148e9012f82a481bd6d; 4 commits ahead / 0 behind; 3 added paths; latest PR-info mergeable=true. No workflow run returned. Independent editorial/source QA and responsive/browser QA pending.

Official sources:
- https://webjapps.ias.ac.in/fellowship2027/
- https://webjapps.ias.ac.in/fellowship2027/application_instructions.jsp
- https://insaindia.res.in/
- https://insaindia.res.in/scroll_news_pdf/FAST-SF-2027-Announcement-Website-Eng-Hindi.pdf
- https://webjapps.ias.ac.in/fastsf2027/application_instructions.jsp

## Opportunity and programme track

No new Google Student Researcher opening was found; the existing Forsk owner was retained. The official Google Careers listing remains Apply / India Remote, with a 4 December 2026 deadline and rolling review. The listing does not state a stipend amount or application fee.

Other current official opportunities were rechecked and existing owners were updated rather than duplicated:

- ANRF PM ECRG: official homepage says open until 2 December 2026, 5 PM. Up to ₹60 lakh plus overheads over three years; up to 700 grants/year. Eligibility includes Indian citizenship (specific PIO/OCI route), doctorate or specified medical qualification, regular academic/research position, application within two years of joining and age conditions. Existing Mango PR #159 remains owner.
- IIIT Guwahati MeitY project internship: notice dated 30 October; one full-time CSE/allied UG/PG intern; 15 November deadline; online selection 20 November; tentative 10 months; ₹15,000/month through 15 September 2027. Hostel unavailable; on-campus preferred, remote exceptional. Separate TIH IITG vacancy closed 10 November. Existing Forsk PR #163 remains owner.
- CMI Computer Science Summer 2027: 31 January 2027 deadline; programming background, typically after second year; one month to a semester; fellowship amount not stated; hostel usually arranged; no travel support. Existing Forsk PR #164 remains owner. CMI Mathematics route has a separate 30 November 2026 deadline through the Academies SRFP.
- PM YASASVI Top Class Schools: NSP card lists 15 November 2026, but the Student Announcements page says fresh applications from Rajasthan, Keralam and Karnataka students must wait. The linked guideline covers OBC/EBC/DNT students in identified top-class schools, household income below ₹2.5 lakh, and assistance caps of ₹75,000/year for Classes 9–10 and ₹1,25,000/year for Classes 11–12. Existing Forsk PR #156 remains owner; do not direct Rajasthan students to submit until NSP changes the restriction.
- PM YASASVI Top Class College: NSP AY 2026–27 card lists 30 November 2026. Existing Forsk PR #166 remains owner.
- PM-USP CSSS renewal: NSP All-Scholarships listing says 30 November, while Student Announcements says student application closed 31 October. Conflict remains; do not describe it as confirmed open.
- Google Student Researcher and other current Google internship listings remain with existing Forsk PRs #146 and #160; no duplicates.

Sources:
- https://www.google.com/about/careers/applications/jobs/results/125423735539671750
- https://anrf.gov.in/
- https://anrfonline.in/ANRF/ecrg_anrf?HomePage=New
- https://www.iiitg.ac.in/vacancy-for-project-intern-position-in-a-1
- https://www.cmi.ac.in/admissions/internships.php
- https://scholarships.gov.in/All-Scholarships
- https://scholarships.gov.in/Students

## React / frontend

No new stable release was found. Official React release tags remain 19.3.1, 19.2.9, 19.1.10 and 19.0.9, all dated 14 October 2026.

The official React advisory GHSA-xqc2-xf4c-x3h3 was published 14 October 2026: Critical, CVSS 9.5, no known CVE; affects react-server-dom-webpack, react-server-dom-parcel and react-server-dom-turbopack through the listed 19.0.8/19.1.9/19.2.8/19.3.0 ranges; patched versions are 19.0.9/19.1.10/19.2.9/19.3.1. Existing Forsk PR #145 remains owner.

Sources: https://github.com/react/react/releases · https://github.com/react/react/security/advisories/GHSA-xqc2-xf4c-x3h3

## Node.js / backend

The official Node.js security page still shows only the advance notice for Wednesday, 11 November 2026, last updated 3 November 2026. It says releases for 26.x, 24.x and 22.x will arrive on or shortly after 11 November; highest severity HIGH in each line. As of 02:01 IST, the notice has no CVE IDs, affected patch ranges or patched versions. The release blog still lists 26.13.0 LTS and 24.22.2 LTS from 28 October, 26.12.1 Current from 21 October and 22.23.4 LTS from 21 October; 27.0.0-alpha.0.0.0 is prerelease. Existing Mango PR #143 remains owner; no release is claimed until actual tags/posts appear.

Sources: https://nodejs.org/en/blog/vulnerability/november-2026-security-releases · https://nodejs.org/en/blog/release

## Other AI / cloud / developer news

AWS's 9 November roundup also covered DynamoDB bulk put items, Web Answer on Bedrock AgentCore, Lambda queue mode for self-managed Kafka event sources and Security Hub SBOM inventory for EC2/ECR/Lambda. Existing owners were reviewed; no additional article was created in this bounded batch to avoid overlapping current AgentCore Web Search, Nitro Sandbox and AI/cloud drafts. These are candidate follow-ups for later deduplicated research, not new draft counts.

## Repository and coordination review

- Central PR #19 current compare: 68 ahead / 2 behind main, diverged; latest PR-info says mergeable=true, but no rebase/merge was attempted.
- Central PR #20 current compare: 21 ahead / 2 behind main, diverged; no rebase/merge was attempted.
- Groot current main and open PR inventory reviewed; .agent handoff/current-state/backlog/decisions and migration instructions read. #609 uses three unique News Factory documentation paths only; no 100K queue, route, sitemap, schema, shared course data or production file changed.
- Forsk open PR inventory reviewed. Root README/AGENTS and expected .agent, .github, docs/README, docs/news-factory/README, task-board and work-log instruction paths were not present on accessible default branch. Existing News Factory conventions were followed; #170 changes only three unique News Factory documentation paths.
- Mango open PR inventory and existing News Factory owners reviewed; comments only, no new source files.
- Jaipur repository mapping remains unresolved in central audit; root README/AGENTS were not accessible. No Jaipur write made.
- Clever Ape and other unverified/ambiguous brand mappings remain untouched.
- No brand PR was merged, deployed, published or indexed.

## Checks and blockers

- Groot #609: GitHub read-back passed for article, SVG and metadata; 3 ahead / 0 behind; mergeable=true. Local SVG XML/dimensions, PNG render/visual inspection and WebP optimization passed. No workflow runs returned; independent editorial/source QA and browser QA pending.
- Forsk #170: GitHub read-back passed for article, SVG and metadata; 4 ahead / 0 behind; mergeable=true. Local SVG XML/dimensions, PNG render/visual inspection and WebP optimization passed. No workflow runs returned; independent editorial/source QA and browser QA pending.
- Forsk #156 and #163/#164/#166 received current official status comments; Mango #143/#159 and Forsk #145/#146 also received revalidation comments.
- No relevant YouTube video ID plus embedding permission was independently verified for the two new drafts; no video was downloaded/re-uploaded and no iframe was claimed tested.
- Central PR #19 remains diverged by two commits; central PR #20 remains diverged by two commits. Both are left untouched except the existing PR #19 checkpoint comment; no rebase/merge.
- No live publication, deployment, application submission or indexing occurred.

## Incremental production ledger

| Status | This run |
|---|---:|
| New distinct research items | 2 (AgentCore Runtime V2 technical guide; SRFP 2027 opportunity) |
| New original article drafts | 2 |
| New original SVG graphics | 2 |
| Local PNG/WebP preview derivatives | 4 |
| Independent QA-ready articles | 0 |
| Live/published articles | 0 |

Historical cumulative totals were not recalculated from the full archive in this run; use the central master ledger for cumulative counts.