# News Factory cycle — 14 November 2026, 21:11 IST

## Run outcome

Four non-overlapping research tracks were checked against primary sources: (1) official student/developer programmes and funding, (2) React/frontend releases and security, (3) Node.js/backend releases and security, and (4) AI/cloud/developer announcements. Current central coordination and accessible brand repository metadata/open-PR ownership were reviewed before writing. Forsk Coding School's current main instructions, task board, session handoff, image audit and image workflow were read before its isolated documentation/media write.

**One new verified, previously unowned developer story passed the source and deduplication gates:** AWS SGLang-Neuron public preview on Trainium, announced 12 November 2026. One original Forsk Coding School article, source/SEO metadata and one original SVG architecture diagram were committed to a focused draft branch. Existing programme, React, Node and AI/cloud owners were retained. No article was merged, published or deployed.

## 1. Student / developer programmes

### Google Student Researcher, 2027 — existing Forsk owner #146

- Direct Google Careers listing checked 14 November 2026.
- The page currently displays **India — Remote eligible**, Apply, rolling review and a **4 December 2026** deadline.
- Minimum qualification includes current enrolment in a Bachelor's, Master's or PhD degree in the listed disciplines and experience in a computer-science research area.
- No stipend or fixed project duration is stated on the accessible listing.
- Existing owner retained: https://github.com/satnamkhowal/forsk-coding-school/pull/146
- Primary source: https://www.google.com/about/careers/applications/jobs/results/125423735539671750-student-researcher

### NMMSS 2026–27 — existing Forsk owner #173; deadline tomorrow

- Ministry of Education / PIB extension notice was published **31 October 2026, 5:57 PM IST**.
- Student application deadline: **15 November 2026**.
- Institute L1 verification: **30 November 2026**.
- District L2 verification: **15 December 2026**.
- This is an extension to an existing scheme, not a newly launched scholarship.
- Existing owner retained: https://github.com/satnamkhowal/forsk-coding-school/pull/173
- Primary source: https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2330936&lang=1&reg=3

### PM YASASVI Top Class Education in Schools — existing Forsk owner #156

- Current NSP announcement says fresh applications are open for eligible states.
- The same notice explicitly tells students from **Rajasthan, Keralam and Karnataka to wait**; therefore Rajasthan applicants must not be told to submit now.
- Existing owner retained: https://github.com/satnamkhowal/forsk-coding-school/pull/156
- Primary source: https://scholarships.gov.in/ViewMoreAnnouncement

No new unowned student opportunity passed the current primary-source and deduplication gates. Other active programme drafts remain with their existing owners.

## 2. React / Frontend

- Official React Blog still lists React 19.3 (9 September 2026) as the latest feature announcement; no newer November stable feature release was found.
- Latest React patch tags remain **19.3.1, 19.2.9, 19.1.10 and 19.0.9**, all dated **14 October 2026**.
- React Server Components advisories published 14 October include a Critical RCE advisory and a High Server Functions DoS advisory. The patched versions above are listed by the official React release/advisory pages.
- Existing owners retained: Forsk #145 and Mango #202.
- Sources: https://react.dev/blog ; https://github.com/react/react/releases ; https://github.com/react/react/security/advisories/GHSA-xqc2-xf4c-x3h3 ; https://github.com/react/react/security/advisories/GHSA-h3gv-c5rc-p453

## 3. Node.js / Backend

Official Node.js blog and security bulletin checked 14 November:

- **Node 22.23.5 LTS** — security release 11 November 2026.
- **Node 24.22.3 LTS** — security release 11 November 2026.
- **Node 26.13.1 LTS** — security release 11 November 2026.
- **Node 27.0.0-alpha.0.1.0** — Alpha published 12 November; not LTS and not a production recommendation.
- The 11 November bulletin covers active 22.x, 24.x and 26.x lines and includes HTTP/2, TLS/HTTPS, proxy credential, permission-model and zlib issues. Existing Node/security content owners were preserved; no duplicate article was created.
- Sources: https://nodejs.org/en/blog ; https://nodejs.org/en/blog/vulnerability/november-2026-security-releases

## 4. AI / Cloud / Developer news

### New Forsk draft — AWS SGLang-Neuron public preview

- AWS announcement publication date: **12 November 2026**.
- AWS says SGLang-Neuron became publicly available through an AWS Deep Learning Container. The project README describes the integration as a **public preview**, not GA.
- SGLang-Neuron is a platform plugin for SGLang on AWS Trainium; the README says LLM recipes require Trainium3, while listed diffusion recipes use Trn2.48xlarge.
- Published container tag: **v0.1.0-neuron-py314-sdk-2.33.0-ubuntu26.04**.
- Requirements documented by the project: Neuron SDK 2.33.0, driver 2.31.7.0 or later, Docker; EFA for disaggregated multi-node serving.
- The current AWS EC2 Region matrix retrieved 14 November lists Trn1 in Mumbai and Trn2/Trn2u in Hyderabad, but does not list Trn3 in either India Region. The article does not claim India-local Trainium3 availability.
- No universal instance price or free student allocation is stated; the article directs readers to verify actual instance/Region availability before pricing.
- AWS announcement: https://aws.amazon.com/blogs/machine-learning/deploy-frontier-ai-models-on-aws-trainium-with-sglang-neuron/
- Project: https://github.com/sgl-project/sglang-neuron
- Quickstart: https://github.com/sgl-project/sglang-neuron/blob/main/docs/getting-started/quickstart.md
- Region matrix: https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-instance-regions.html

### Existing owners retained

- GitHub Copilot selected-model retirement notice, published 13 November; effective 14 December — Forsk #185.
- Gemini 4 Hydrogen in GitHub Copilot, published 13 November — Forsk #185.
- GitHub Enterprise Server support in Copilot app, published 13 November — Mango #230.
- GitHub AI Scan REST API public preview, published 13 November — Groot #737.
- Cloudflare Kitesurf open-source update, published 13 November — Groot #743.
- Cloudflare Spend Management beta, published 13 November — Groot #745.

These topics were not re-drafted or syndicated.

### Additional AWS AgentCore Runtime update — existing owners, no duplicate

- AWS published its next-generation AgentCore Runtime update on **12 November 2026**. The announcement describes hardware-isolated Firecracker MicroVM sessions, starts under two seconds, up to 8 vCPUs / 32 GB per session, container images up to 10 GB, and up to 68% lower memory use per session through idle-memory reclamation/scale-to-zero.
- Exact prices and an India-specific Region/availability guarantee were not established in this pass; no new article was created.
- Existing related owners found in current brand PR search: Groot Academy #609 (AgentCore Runtime V2 snapshot safety and Node.js guidance) and Forsk Coding School #192 (Spring AI + Amazon Bedrock agent guide). Both were preserved.
- Primary source: https://aws.amazon.com/blogs/machine-learning/run-agents-securely-and-efficiently-with-the-next-generation-agentcore-runtime/

## 5. Forsk Coding School implementation

**Draft PR:** https://github.com/satnamkhowal/forsk-coding-school/pull/237  
**Task issue converted to PR:** #237  
**Branch:** news-factory/sglang-neuron-trainium-developer-guide-20261114-2111  
**Base at creation:** main @ 9a25fd5a11641420ac716d3fd25103e6e8362fbf  
**Head:** dc824fba0a048b1756d2e2208e070baa7937cf37

Files:
1. docs/news-factory/drafts/aws-sglang-neuron-trainium-developer-guide.md — **2,519-word** original English technical article.
2. docs/news-factory/drafts/aws-sglang-neuron-trainium-developer-guide.metadata.json — source dates, SEO fields, claims, QA and asset provenance.
3. docs/news-factory/media/aws-sglang-neuron-trainium-architecture.svg — original 1200×675 vector architecture infographic.

Local derivatives:
- /mnt/data/news-factory/2026-11-14/2111/forsk-sglang-neuron/aws-sglang-neuron-trainium-architecture.png — 1200×675, 118,145 bytes, SHA-256 406a5efc8418c7938d9efde0f8c58b7b97aff3b685ff755ac0a071eb2b25be24.
- /mnt/data/news-factory/2026-11-14/2111/forsk-sglang-neuron/aws-sglang-neuron-trainium-architecture.webp — 1200×675, 68,444 bytes, SHA-256 e9a542c36fc7cb22787a4bfd74e1aaee2813610691f9f1f8ca4b2a7a420c0c11.
- Local SVG SHA-256: 76d7605f214c71b7d6a5626c5ec56ad25393e51a3751786ca190d9981f63c88d.
- Committed GitHub SVG blob SHA: e164c917037427e17fd19d4086924b490729f876.

Asset rights basis: self-authored vector artwork; no AWS/third-party logo, screenshot, photo or downloaded graphic. Attribution, alt text, dimensions, local paths and hashes are recorded in metadata.

No story-specific official/reputable original YouTube video with verifiable ID, channel and date was found. No video ID or iframe was invented.

### Checks and blockers

- GitHub read-back of all three files: PASS.
- Article word count: 2,519; metadata count matches: PASS.
- Metadata JSON parse: PASS.
- SVG validation/render and 1200×675 dimensions: PASS.
- PNG/WebP decode and visual inspection: PASS.
- Branch comparison: **5 commits ahead / 0 behind main**.
- PR: OPEN / DRAFT; GitHub mergeable=true at last check; 3 files, 420 additions.
- Workflow runs and combined status checks returned none. This is not a CI pass.
- Independent editorial, technical/source and responsive QA: PENDING.
- No live page, browser embed or production asset integration was tested.

## 6. Repository and coordination review

- Central satnamkhowal/brand-growth-control-center existing PR #19 reviewed and reused.
- Mango Engineers, Groot Academy, Forsk Coding School, Jaipur Engineers and CadMate India repository metadata/open-PR inventories reviewed. No new writes were made to Mango, Groot, Jaipur or CadMate in this cycle. The attempted canonical repository paths for Clever Ape Academy and Forsk Technologies returned 404; no substitute repository was guessed and no writes were made.
- Forsk current main instructions, README.txt, master task board, session handoff, image audit and image production workflow were read. The task board/handoff remain untouched because existing PR #229 owns shared governance paths. The new work is limited to three documentation/media files.
- No production route, PHP, sitemap, schema, navigation, redirect, shared task-board or session-handoff file was changed.
- Central PR #19 branch remains diverged: **211 commits ahead / 5 behind main**. No rebase, force-push or merge was performed.

## 7. Run ledger

| Stage | This run |
|---|---:|
| Research tracks | 4 |
| New verified, unowned story | 1 |
| Original article drafts | 1 |
| Original SVG committed | 1 |
| Local PNG/WebP derivatives | 2 |
| New verified video embeds | 0 |
| Independent QA-ready | 0 |
| Live / published | 0 |
| Merged / deployed | 0 |

## 8. Next actions

1. Independent editorial, technical/source and responsive QA for Forsk PR #237.
2. Recheck NMMSS student application deadline on 15 November; distinguish student submission from institute/district verification.
3. Recheck Google Student Researcher 2027 India listing and 4 December deadline.
4. Recheck current React and Node security feeds; do not duplicate existing owners.
5. Check whether Trainium3 appears in the India Region matrix or account console before any more India-specific implementation guidance.
6. Continue duplicate-free AI/cloud research; evaluate AgentCore Runtime's 12 November update as a research-only candidate after brand ownership and regional/cost verification.

**No merge, deployment, live publication or indexing claim.**

## 14 November 2026 — 23:49 IST active News Factory cycle

### Four research lanes

1. **Official student/developer programmes and funding**
   - Google Student Researcher, 2027 remains live on the official Google Careers page: India / Remote eligible, rolling review, apply before **4 December 2026**. The listing states current enrolment in a Bachelor's, Master's or PhD programme in listed disciplines and relevant CS research experience; no stipend or fixed duration is stated. Existing Forsk owner #146 retained.
   - NASA Space Apps Challenge 2026 is taking place **14–15 November**. The official page says registration remains open until the hackathon closes on 15 November; project submission closes **15 November at 11:59 PM local time**. Teams may have up to six participants. Existing Forsk owner #231 retained; this is an active event, not a newly announced internship.
   - Sage IT India Scholarship is open through **15 November 2026**. Official page lists a **₹50,000** one-time award paid directly to the selected student's institution, an individual 1,000–1,500-word article, all college/university majors in India, no entry fee, and winner announcement on 30 November. No exact cutoff time is published. Existing Forsk owner #184 retained.
   - NSP AY 2026–27 currently lists NMMSS student applications through **15 November**; AICTE Pragati, Saksham and Swanath degree/diploma schemes and UGC National Scholarship for PG Studies through **30 November**. PM YASASVI Top Class Schools is listed through 30 November, but the separate NSP announcement says fresh applications are currently not available to students from **Rajasthan, Keralam and Karnataka**; those students must wait. NSP pages show a June 2026 last-update footer, so recheck the live form and scheme-specific rules before student action. Existing Forsk owners retained.
   - No new unowned student opportunity passed the official-source and deduplication gates in this run.
   - Primary sources: https://www.google.com/about/careers/applications/jobs/results/125423735539671750-student-researcher ; https://www.spaceappschallenge.org/2026/ ; https://sageitinc.com/scholarship/india ; https://scholarships.gov.in/All-Scholarships ; https://scholarships.gov.in/ViewMoreAnnouncement

2. **React / frontend**
   - Official React release list still shows **19.3.1, 19.2.9, 19.1.10 and 19.0.9**, all dated **14 October 2026**; React 19.3.0 was released 9 September. No newer November stable release was found. Existing React security/content owners retained; no duplicate draft.
   - Source: https://github.com/react/react/releases

3. **Node.js / backend**
   - Official 11 November security releases remain current: **Node 22.23.5, 24.22.3 and 26.13.1**. Node **27.0.0-alpha.0.1.0** was published 12 November and is an Alpha, not LTS/stable. No newer security release was found.
   - Existing Node security owners retained.
   - Sources: https://nodejs.org/en/blog ; https://nodejs.org/en/blog/vulnerability/november-2026-security-releases

4. **AI / cloud / developer news**
   - GitHub's **13 November 2026** public-preview announcement adds the repository_scan property to organization/repository AI Scan REST enablement endpoints. It allows GET/PATCH configuration at scale; enabling the setting does not launch a scan. A user with write access still runs scans manually, each consuming Code Security AI credits. Enterprise policy can block enablement with HTTP 422; a combined pr_scan/repository_scan update is atomic. Repository scans are default-branch only, not scheduled/on-push, do not support self-hosted runners, and findings require human review.
   - Official docs add important billing nuance: no Copilot license is required for repository AI Scan, but the feature consumes Code Security AI credits, including on public repositories; included credits may be used first, then usage is metered and budget-limited. The documentation states a 30-minute / 150,000-credit detection-step cap. No fixed INR price or India-specific regional availability list was found.
   - GitHub also published a separate **13 November** Copilot model-deprecation notice with **14 December 2026** effective date. Existing Forsk Copilot/model owner #185 remains the coordination owner; no near-identical article was created.
   - Existing GitHub/Cloudflare security topics remain with their current owners, including Forsk #204 (Actions ARM32 retirement) and Forsk #217 (Cloudflare service-token detector).
   - Primary sources: https://github.blog/changelog/2026-11-13-manage-ai-scan-for-repositories-using-the-rest-api/ ; https://docs.github.com/en/code-security/concepts/code-scanning/ai-scan-for-repositories ; https://docs.github.com/en/rest/code-scanning/code-scanning ; https://docs.github.com/en/billing/concepts/product-billing/github-advanced-security ; https://github.blog/changelog/2026-11-13-upcoming-deprecation-of-selected-github-copilot-models-in-december/

### Jaipur Engineers AI Scan task — local-only draft; repository write blocked

- Existing Jaipur issue **#52** describes the GitHub AI Scan REST API guide and expected article/media deliverables. Current open-PR search found no AI Scan PR; the issue exists, but the pre-created news-factory/github-ai-scan-rest-api-20261113-2013 branch still points to main with no draft files.
- Crucially, the current central PR #19 control record explicitly states **Jaipur Engineers remains read-only because no approved non-public News Factory draft lane was found**. That current central gate supersedes the pre-existing issue/empty branch. No Jaipur branch, commit, PR, task-board edit or issue comment was created.
- To preserve the research output without bypassing governance, a local-only original draft package was produced:
  - Article: **3,004 words**, /mnt/data/jaipur-ai-scan/github-ai-scan-rest-api-jaipur-engineers.md
  - Metadata/provenance JSON: /mnt/data/jaipur-ai-scan/github-ai-scan-rest-api-jaipur-engineers.metadata.json
  - Original 1200×675 SVG: /mnt/data/jaipur-ai-scan/github-ai-scan-repository-rollout.svg
  - Local PNG: /mnt/data/jaipur-ai-scan/github-ai-scan-repository-rollout.png
  - Local optimized WebP: /mnt/data/jaipur-ai-scan/github-ai-scan-repository-rollout.webp
- The article covers endpoint paths, repository_scan versus pr_scan, organization inheritance, enterprise policy/422 behaviour, token permissions, owner/visibility eligibility, Code Security AI-credit billing, India pricing/availability limits, public-preview caveats and a safe student lab. It does not claim Jaipur Engineers is a GitHub partner or that any Jaipur repository has AI Scan enabled.
- Media rights: original self-authored vector; no third-party logo, screenshot, photo or downloaded graphic. Source attribution, rights basis, alt text, dimensions, local paths and SHA-256 hashes are recorded in the metadata.
- No relevant original official YouTube video with independently verified video ID, channel, date and embed permission was found. No video ID or iframe was invented.
- Local checks: article read-back and 3,004-word count PASS; metadata JSON parse PASS; SVG XML/title/description/dimensions PASS; PNG/WebP render/decode PASS; visual inspection PASS. Independent editorial, security/technical and responsive browser QA remain PENDING. CI NOT RUN. No live/publication state.

### Repository and coordination review

- Central control PR #19 and its current append-only checkpoint were read before updating this file. Current compare remains **214 commits ahead / 5 behind main (diverged)**; GitHub reports mergeable=false. No rebase, force-push or merge.
- Accessible repository metadata and current open-PR inventories were checked for Mango Engineers, Groot Academy, Forsk Coding School, Jaipur Engineers, Clever Ape Academy, CadMate India, Forsk Technologies and the central control repository. Existing topic owners were retained; no other brand was written in this run.
- Central PR #19's latest control record marks Jaipur Engineers read-only for News Factory drafts. The local-only package above respects that restriction.
- No production route, PHP, sitemap, schema, navigation, redirect, shared task board or live content was changed.

### Production ledger — this run

| Stage | New count |
| --- | ---: |
| Research tracks | 4 |
| New verified unowned story | 1 |
| Original article drafts (local-only) | 1 |
| Original SVG graphics | 1 |
| Local PNG/WebP derivatives | 2 |
| Verified YouTube IDs / embeds | 0 |
| Independent QA-ready | 0 |
| Live / published | 0 |
| Merged / deployed | 0 |

### Next actions

1. Recheck Sage IT, NASA Space Apps and NMMSS deadlines on 15 November; do not imply any extension without a new official notice.
2. Recheck the current Google Student Researcher listing before its 4 December deadline.
3. Continue official React, Node, GitHub, Cloudflare, AWS and Google Cloud feeds; update existing owners instead of duplicating topics.
4. Keep the Jaipur AI Scan package local until the central control board explicitly approves a non-public Jaipur draft lane.
5. Run independent editorial, security/technical and responsive QA on the local AI Scan package before any future repository implementation.

**No merge, deployment, live publication, indexing or website implementation is claimed.**


### Ledger correction — 14 November 2026, 23:49 IST

The GitHub AI Scan REST API topic was already present as Jaipur Engineers issue #52 before this run. It is therefore **not counted as a newly discovered or newly unowned story**. This run produced a local-only 3,004-word draft package against that existing issue, but made no Jaipur repository write because central PR #19 explicitly retains the Jaipur read-only gate. Corrected production delta: **0 new unowned stories; 1 local draft package; 1 original SVG; 2 local raster derivatives; 0 GitHub brand PRs; 0 independent QA-ready; 0 live**.
