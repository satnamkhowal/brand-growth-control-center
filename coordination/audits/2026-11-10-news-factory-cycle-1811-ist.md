# News Factory research and draft-production checkpoint

**Checked:** 10 November 2026, 18:11 IST  
**Scope:** Mango Engineers, Groot Academy, Forsk Coding School, Jaipur Engineers and verified central coordination  
**Research tracks:** official opportunities; React/frontend; Node.js/backend; AI/cloud/developer tooling

## 1. Fresh distinct finding and delivery

### GitHub Copilot Fusion — Groot Academy

- Official announcement publication date: **28 October 2026**.
- Status checked 10 November 2026: generally available.
- Official clients: Visual Studio Code, GitHub Copilot CLI, GitHub Copilot app and JetBrains IDEs.
- Effort levels: Standard, High and Max; Fast is automatic and limited to VS Code inline chat.
- Execution patterns: Single, Cascade and Critique.
- Plan and administrator policies determine which models are available.
- No separate Fusion fee; each model call is billed at its standard rate.
- GitHub Docs states the 30% model-cost discount for paid Copilot plans runs through **30 November 2026**.
- High/Max can use more AI credits; Fusion does not start subagents; discarded drafts do not automatically undo workspace edits.

**New draft:** [Groot Academy PR #606](https://github.com/satnamkhowal/grootacademy.com/pull/606)  
Branch: `content/news-factory-copilot-fusion-ga-20261110-1811`  
Files: article Markdown, original SVG, source/media provenance JSON.  
Article: 2,155 words. Draft only; not merged or published.

Sources:
- https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/
- https://docs.github.com/en/copilot/concepts/models/copilot-fusion
- https://docs.github.com/en/copilot/concepts/models/copilot-fusion#billing-for-copilot-fusion

## 2. Opportunities and scholarships

- Google Research Scientist PhD Intern, Summer 2027, Hyderabad: an indexed Google Careers result showed an application window of **28 October–30 November 2026**, but a direct page recheck at 18:14 IST returned “Job not found / may have been taken down.” Treat the listing as **unverified / unavailable**, not open; no application recommendation or article was made. The indexed result is not enough to establish current availability.
  - Search result: https://www.google.com/about/careers/applications/jobs/results/87534302853505734-research-scientist-phd-intern-summer-2027
- Google Student Researcher 2027: India remote eligibility and 4 December 2026 deadline remain in the existing Forsk PR #146 ownership.
- Google Summer 2027 Software Engineering and Silicon Engineering PhD roles remain in Forsk PR #160 ownership.
- NSP AY 2026–27 live portal lists NMMSS to 15 November; AICTE Pragati/Saksham/Swanath and UGC PG Studies to 30 November; PM YASASVI Schools to 15 November and College to 30 November. These are existing schemes, not new November launches. Portal footer says last updated June 2026; PM-USP renewal pages conflict (31 October announcement vs 30 November All-Scholarships listing), so that renewal deadline remains unresolved.
  - https://scholarships.gov.in/All-Scholarships
  - https://scholarships.gov.in/Students

## 3. React / frontend

- Official React release tags still show 19.3.1, 19.2.9, 19.1.10 and 19.0.9, all dated 14 October 2026.
- No newer stable release was verified.
- Existing Forsk PR #145 owns the React Server Components security update; no duplicate article was created.
- https://github.com/facebook/react/releases

## 4. Node.js / backend

- The official November security advance notice was published **3 November 2026**; the scheduled release event is **11 November 2026**.
- It covers 26.x, 24.x and 22.x; highest severity is HIGH.
- At 18:11 IST on 10 November, the notice still lists no CVE IDs or patched versions. Do not treat this as a completed patch release.
- Existing Mango PR #143 owns the readiness/security notice; PR #153 owns the Node.js 27 Alpha guide.
- https://nodejs.org/en/blog/vulnerability/november-2026-security-releases

## 5. AI / cloud / developer watch

- GitHub Changelog's latest November entries are dated 9 November: Claude Fable 5.2 in Copilot and secret scanning for Actions workflow logs. Existing Forsk PR #159 and Groot PR #597 own those items.
- Copilot model deprecations are scheduled for **16 November 2026**: Claude Opus 4.8 (with an annual-plan exception), Claude Opus 5 and GPT-5.6 Terra. Alternatives are listed in the official notice. Kept as a watch item, not a second article in this bounded batch.
  - https://github.blog/changelog/2026-10-15-upcoming-deprecation-of-selected-github-copilot-models-in-mid-november
- No distinct unowned 10 November AWS/Azure/Google Cloud release was verified in this run.

## 6. Repository and ownership checks

- **Groot Academy** (`grootacademy.com`): current main observed at `99336e8d0b412f6e0f0bdc0464e0aec4b8fea2b5`; root README and current `docs/news-factory/drafts`/media queue inspected; existing open PRs #602–#605 and other News Factory owners reviewed. Copilot Fusion was absent from the current draft queue and open PR search. PR #606 is isolated to three `docs/news-factory/` files.
- **Mango Engineers**: read `AGENTS.md`, `README.md`, `docs/agent-start-here.md`, task board, work log and integration queue. Current open PRs include #143 Node.js readiness, #153 Node.js 27 Alpha and #159 ANRF; no duplicate work was created.
- **Forsk Coding School**: read `README.txt`, `README_FINAL.txt` and `docs/ai-ops/MASTER_TASK_BOARD.md`; reviewed current open PRs #145–#161. Existing Google, React, AICTE and AI/cloud owners remain untouched.
- **Jaipur Engineers**: verified `satnamkhowal/jaipurengineers.com` and read `README-INSTALL.md`; PR #43 readability and PR #41 batch/enquiry work remain owned. No News Factory write was needed.
- **Central Control Center**: read central README, existing News Factory PR #19 and cross-lane dedupe PR #20. PR #19 branch remains **57 ahead / 2 behind main, diverged** before this checkpoint addition. No rebase or merge was performed. This file is appended to the existing PR #19 branch.

## 7. Media, video and QA

- Original Groot Academy SVG: 1200×675, created for this article; no third-party graphic or copied GitHub logo.
- Local PNG and WebP derivatives rendered at 1200×675; WebP 48,254 bytes; PNG visually inspected.
- Metadata records official sources, original-asset permission/attribution, alt text, dimensions, local paths and SHA-256 hashes.
- No YouTube iframe: no relevant official video ID and embed permission could be independently verified.
- PR #606: 3 commits ahead / 0 behind main; 3 changed files; GitHub read-back passed; mergeable=true after recheck.
- No GitHub Actions workflow runs returned. Independent editorial QA and responsive/browser QA remain pending.

## 8. Cumulative News Factory ledger

Carried forward from the existing checkpoint: 92 researched, 75 drafted, 75 original graphics, 33 independent QA-ready, 0 live.

This run adds two distinct unowned research items (Copilot Fusion GA and AI applications scanning preview), two original drafts and two original infographics.

**Updated totals:** 94 researched · 77 drafted · 77 original graphics · 33 independent QA-ready · 0 live.

No merge, deployment, application submission, live publication or indexing is claimed.


### 18:14 IST direct Google Careers recheck correction
The Research Scientist PhD Intern job page cited above no longer resolves to a live listing; Google Careers displays “Job not found / This job may have been taken down.” Its search-index snippet still carries the earlier 28 Oct–30 Nov dates, but current application status is not verified. Keep it out of the open-opportunity count until the direct listing returns. Google Student Researcher 2027 remains directly accessible with Apply and a 4 December 2026 deadline.

## 18:50 IST addendum — second distinct developer-security draft

### GitHub AI applications scanning — Groot Academy

- Official announcement publication date: **28 October 2026**.
- Current status: public preview.
- Current GitHub Docs narrow the preview coverage to **indirect prompt injection (XPIA) in AI agents only**, even though the announcement describes a broader AI-risk area.
- Scans run when a pull request is created and after each new commit; no full-repository/backlog scan.
- Fork and Dependabot pull requests are excluded.
- Findings are advisory and cannot block merges.
- Feature is off by default; organisation-level enablement is separate from enabling AI Scan for pull requests.
- Requires GitHub Advanced Security on GitHub Enterprise Cloud (including data residency) and consumes AI credits on top of the licence; not available on GitHub Enterprise Server.

**New draft:** [Groot Academy PR #607](https://github.com/satnamkhowal/grootacademy.com/pull/607)  
Branch: `content/news-factory-ai-applications-scanning-preview-20261110-1811`  
Files: 2,329-word article, original SVG infographic, provenance JSON.  
Draft only; not merged or published.

Sources:
- https://github.blog/changelog/2026-10-28-code-scanning-for-ai-applications-in-public-preview/
- https://docs.github.com/en/code-security/concepts/code-scanning/ai-applications-scanning-for-pull-requests

Validation: PR #607 has 3 commits ahead / 0 behind main, 3 changed files, GitHub read-back passed, mergeable=true after recheck. No workflow runs returned. Independent editorial and responsive/browser QA remain pending.

Both new Groot PRs (#606 and #607) use distinct article/media paths. No shared task-board or site-production path was changed.


## 20:11 IST — News Factory research and draft-production cycle

### 1. New distinct story and Mango Engineers draft

Microsoft's current .NET support policy lists **10 November 2026** as the end-of-support date for both .NET 8 and .NET 9. This is a lifecycle event, not a new announcement published today. The support-policy page was last updated **25 October 2026** and lists:
- .NET 8 LTS — latest patch 8.0.33 (25 October); end of support 10 November 2026.
- .NET 9 STS — latest patch 9.0.22 (25 October); end of support 10 November 2026.
- .NET 10 LTS — latest patch 10.0.14 (25 October); active.
- .NET 11 — official download page still showed Preview / 11.0.0-rc.3 (latest release date 25 October) at the 20:11 IST check. Do not infer GA from the .NET Conf 2026 event banner.

The current support-policy table lists .NET 10 end of support as **14 November 2028**, while Microsoft's original .NET 10 launch post says **10 November 2028**. The Mango article flags this four-day discrepancy and tells readers to recheck the current policy page before fixing lifecycle dates.

**New draft:** [Mango Engineers PR #162](https://github.com/satnamkhowal/mangoengineers.com/pull/162)  
Branch: content/news-factory-dotnet-eol-20261110  
Article: docs/news-factory/drafts/dotnet-8-9-end-of-support-2026-migrate-to-dotnet-10.md — 2,081 words, original English technical guide with answer-first summary, migration checklist, SEO metadata, FAQs and Jaipur/India developer context.  
Media: one original 1200×675 SVG at docs/news-factory/media/dotnet-8-9-eol-migration-timeline.svg; local 1200×675 PNG and optimized WebP derivatives are in /mnt/data/news-factory/2026-11-10/dotnet-eol/media/. Provenance, rights, attribution, alt text, dimensions, byte sizes and SHA-256 hashes are recorded in docs/news-factory/drafts/dotnet-8-9-end-of-support-2026.metadata.json.

The article is a separate lifecycle explainer, not the owner-gated .NET course page in Mango PR #160. Mango PR #151 owns the shared task-board/work-log/integration-queue files, so this branch changes only the three new draft/media paths. Existing Node.js story ownership in Mango PR #143 is preserved.

Validation: article word count 2,081; SVG XML/accessibility/no-external-reference checks PASS; PNG rendered and visually inspected with no clipped text; WebP optimized; metadata JSON and file hashes validated; all three files read back from GitHub. Branch compare: 3 commits ahead / 0 behind main. PR creation returned mergeable=false; no CI statuses were returned, so mergeability and independent editorial/browser QA remain pending. PR stays Draft; no merge, deploy or publication.

No YouTube iframe was added: Microsoft's .NET 10 blog link resolved to a videoseries rather than a verified single video ID, and no specific official .NET 11 RC3 video was established. No video or third-party graphic was downloaded.

### 2. Student/developer opportunities — rechecked, no duplicate draft

- **Google Student Researcher, 2027:** direct Google Careers page still shows Apply; India, Remote eligible; currently enrolled Bachelor's/Master's/PhD in listed disciplines; deadline **4 December 2026**; rolling review. No stipend or application fee is stated on the listing. Existing owner: [Forsk PR #146](https://github.com/satnamkhowal/forsk-coding-school/pull/146).
- **ANRF PM ECRG 2026:** existing owner [Mango PR #159](https://github.com/satnamkhowal/mangoengineers.com/pull/159); open through **2 December 2026, 5:00 PM IST**, up to ₹60 lakh plus institutional overheads for three years, subject to Indian-citizen, doctorate, regular-position, joining-date and age/role conditions.
- **NSP AY 2026–27:** current All-Scholarships page lists NMMSS and PM YASASVI Schools through **15 November**; AICTE Swanath/Pragati/Saksham, UGC Ishan Uday/PG Studies and PM YASASVI College through **30 November**. The page footer still says last updated June 2026. PM-USP renewal remains unresolved: the All-Scholarships listing says 30 November, while the separate Students announcement says 31 October. Do not market the renewal as open without checking the logged-in application portal.
- **AICTE National Internship Portal:** current public listing snapshot showed **0 postings**. This is a portal snapshot, not evidence of a new internship opening.
- Outreachy December 2026 applications closed on 9 November; existing Groot PR #605 already describes the closed status. Google's Research Scientist PhD Intern listing remains unavailable on direct check; do not call it open.

Official links: https://www.google.com/about/careers/applications/jobs/results/125423735539671750-student-researcher ; https://anrf.gov.in/ ; https://scholarships.gov.in/All-Scholarships ; https://scholarships.gov.in/Students ; https://internship.aicte-india.org/internships

### 3. React / frontend

Official React blog and release page rechecked. Latest stable tags remain 19.3.1, 19.2.9, 19.1.10 and 19.0.9, all dated **14 October 2026**. No newer stable release or new official security advisory was found in this check. Existing security-story owner: [Forsk PR #145](https://github.com/satnamkhowal/forsk-coding-school/pull/145). No duplicate article.

Sources: https://react.dev/blog ; https://github.com/react/react/releases

### 4. Node.js / backend

The official Node.js advance notice remains last updated **3 November 2026** and schedules security releases on or shortly after **11 November 2026** for 26.x, 24.x and 22.x. Highest severity is HIGH; the advance notice still contains no CVE IDs or patched versions. The download page currently lists 26.13.0 LTS, 24.22.2 LTS and 22.23.4 LTS. Existing Mango PR #143 owns the readiness story; no duplicate or premature patched-version claim was created.

Sources: https://nodejs.org/en/blog/vulnerability/november-2026-security-releases ; https://nodejs.org/en/download

### 5. AI / cloud / developer news

- Google Cloud's **10 November** open AI-native Kubernetes stack article (OpenRL, llm-d 1.0, KubeRay/Kueue, Agent Substrate, gVisor and TorchTPU) is already owned by [Groot PR #608](https://github.com/satnamkhowal/grootacademy.com/pull/608).
- GitHub Changelog's latest visible entries are 9 November: Claude Fable 5.2 in Copilot and secret scanning in GitHub Actions workflow logs. Existing owners [Forsk PR #159](https://github.com/satnamkhowal/forsk-coding-school/pull/159) and [Groot PR #597](https://github.com/satnamkhowal/grootacademy.com/pull/597) are preserved.
- Google Cloud's Gemini for Healthcare announcement is dated 10 November but is a U.S.-only preview for healthcare organisations, not a useful education/developer opportunity for these brands; excluded from the draft queue.
- No additional distinct AWS/Azure/Google Cloud developer story without an existing owner was verified.

Sources: https://cloud.google.com/blog/topics/developers-practitioners/the-open-ai-native-stack-on-kubernetes-from-open-models-to-distributed-inference-and-agents/ ; https://github.blog/changelog/ ; https://cloud.google.com/blog/products/ai-machine-learning/gemini-for-healthcare

### 6. Repository and ownership review

- **Mango Engineers** — current main and agent-start/task-board/work-log/integration-queue reviewed; current open PRs #143, #147, #151, #153, #156, #159, #160 reviewed. New PR #162 is file-disjoint from the active .NET course candidate (#160) and shared SEO audit (#151).
- **Groot Academy** — current .agent handoff/state/backlog/decisions read; these documents are older than the active PR set. Current News Factory PRs #605–#608, #603, #602 and #597 reviewed; no new write because the current opportunities/AI-cloud topics already have owners.
- **Forsk Coding School** — README, AI-ops master task board and session handoff reviewed; the board/handoff is dated 14 October, while current News Factory PRs #145–#161 own React, Google, AICTE, scholarships and AI/cloud topics. No write.
- **Jaipur Engineers** — canonical repository verified as satnamkhowal/jaipurengineers.com; README-INSTALL.md read. Root README.md, AGENTS.md and docs/ai-ops/MASTER_TASK_BOARD.md were not present. Current open PR #43 owns readability work, #41 owns enquiry-first batch planning, and #27 owns social planning. No News Factory article write.
- Central README lists eight brands, but this run did not verify canonical writable repositories for Clever Ape Academy, CadMate India, Groot Software and Forsk Technologies; no writes were made to those brands.

### 7. Central coordination and cumulative ledger

This addendum is appended to the existing News Factory checkpoint file on PR #19's branch. At pre-write comparison the central branch was **60 commits ahead / 2 behind main (diverged)**; no rebase or merge was attempted. PR #20's separate Groot 100K deduplication audit remains open and untouched.

Carried-forward ledger: 95 researched, 78 drafted, 78 original graphics, 33 independent QA-ready, 0 live. This run adds one distinct researched lifecycle story, one article draft and one original infographic.

**Updated ledger:** 96 researched · 79 drafted · 79 original graphics · 33 independent QA-ready · 0 live.

No brand article was merged, deployed, published or submitted to an application portal in this run.
