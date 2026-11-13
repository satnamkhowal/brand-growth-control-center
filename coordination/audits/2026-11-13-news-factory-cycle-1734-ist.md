# News Factory cycle — 13 November 2026, 17:34 IST

**Scope:** Four non-overlapping tracks: official student/developer programmes; React/frontend releases and security; Node.js/backend releases and security; AI/cloud/developer news. Mango Engineers, Groot Academy, Forsk Coding School, Jaipur Engineers and central coordination were reviewed. One new unowned technical story was retained as a Mango draft. An attempted Forsk draft was closed after the full existing checkpoint revealed that the same HackIndia story was already owned by Mango PR #220. No worker chats were created.

## 1. New retained draft — Mango Engineers

### Google Cloud's updated GKE + Cloud SQL RAG architecture
- Draft PR: https://github.com/satnamkhowal/mangoengineers.com/pull/223
- Issue: https://github.com/satnamkhowal/mangoengineers.com/issues/222
- Branch: `news-factory/gke-cloudsql-rag-architecture-20261113-1734`
- Task: `NF-MANGO-GKE-CLOUDSQL-RAG-20261113`
- Article: **2,858-word** original English SEO/AEO/GEO guide.
- Files:
  - `docs/news-factory/drafts/google-cloud-gke-cloud-sql-rag-architecture-mango-engineers-2026.md`
  - `docs/news-factory/drafts/google-cloud-gke-cloud-sql-rag-architecture-mango-engineers-2026.metadata.json`
  - `docs/news-factory/media/google-cloud-gke-cloud-sql-rag-architecture.svg`
  - `docs/work-log.md` — append-only task record.
- Google Cloud Architecture Center release notes list the document update on **12 November 2026**; the guide says **Last reviewed 2026-11-12 UTC**. This is a documentation/reference-architecture update, not a new GKE or Cloud SQL product launch, API version or GA announcement.
- Architecture covered: regional GKE Autopilot, Cloud Storage ingestion, Ray Data/Ray jobs, Cloud SQL for PostgreSQL + pgvector, LangChain retrieval, inference on GKE and responsible-AI filtering.
- Updated design considerations cover IAP, Workload Identity Federation for GKE, private Cloud SQL connectivity/Language Connectors, VPC Service Controls, Sensitive Data Protection, Model Armor, audit logs, GPU reservations/Dynamic Workload Scheduler, Cloud SQL HA/cost trade-offs, Ray Operator, GKE Inference Quickstart, vLLM, GKE Inference Gateway, IVFFlat/HNSW indexes and Cloud SQL Enterprise Plus data cache.
- Sample-code caveats: explicitly experimental/not production, creates billable resources, omits the Pub/Sub notification component and uses a notebook/manual trigger. The updated guide says TGI is archived and recommends considering an actively maintained engine such as vLLM for production.
- No fixed price or India-specific regional availability is claimed; the article directs readers to workload-specific pricing and regional checks.
- Distinct from Mango PR #215 (Gemini Enterprise Data Cloud connectors), PR #204 (BigQuery JSON_FLATTEN/principal-aware reservations) and PR #220 (Gemini 4 Carbon + HackIndia).

### Original graphic
- One original self-authored 1200×675 SVG committed to Mango PR #223; no Google diagram, logo or third-party graphic copied.
- Local PNG preview (1200×675) visually inspected; local WebP preview (1200×675) decoded. PNG/WebP are local QA derivatives only, not committed.
- Source, original-work permission, attribution, alt text, local paths, dimensions, file sizes and SHA-256 values are recorded in metadata.
- No story-specific official/reputable original YouTube video ID and publication date were verified; no iframe or video download.

## 2. Existing opportunity owner retained — HackIndia / 13th Protocol

The full existing queue/checkpoint was read after an initial Forsk duplicate was prepared. The story is already included in **Mango PR #220** with the Gemini 4 Carbon article:
- https://github.com/satnamkhowal/mangoengineers.com/pull/220
- HackIndia article: `docs/news-factory/drafts/13th-protocol-ai-hackathon-2026-india-registration-prizes-deadline.md`
- Existing owner retained; no second brand copy should remain.

Current source verification:
- HackIndia event page shows registration open at 13 Nov 17:34 IST and states 18 Nov 2026, **23:00 IST**.
- Organiser-listed Unstop page states 18 Nov 2026, **00:00 IST**. The 23-hour time conflict remains unresolved; safest guidance is to complete both registrations before 17 Nov and confirm with the organiser.
- Unstop says both Unstop and HackIndia registration are required, every team member must register, teams have 2–4 members, and the preliminary round requires a PPT of up to seven slides plus a LinkedIn post tagging Voyager Coding Club and HackIndia.
- Event: 28–29 Nov 2026 at KCCITM, Greater Noida; only shortlisted teams reach the offline final.
- Unstop calls the final 24 hours; HackIndia's displayed 28 Nov 08:00 to 29 Nov 12:00 IST schedule spans 28 hours. Exact duration needs organiser confirmation.
- Free entry; ₹60,000 cash pool (₹30K/₹20K/₹10K); 40,000 Sharp Rewards and US$150 OpenAI API credits are displayed separately with incomplete allocation terms. Travel/accommodation reimbursement is not stated.
- Event page does not show publication date. Footer build timestamp 13 Nov 11:27 UTC is not treated as publication date. Not an OpenAI-run programme.
- Sources:
  - https://hackindia.org/2026/13th-protocol-an-ai-hackathon-2026
  - https://unstop.com/hackathons/13th-protocol-an-ai-hackathon-2026-voyager-coding-club-1794890
  - https://unstop.com/competitions/1794890/register

### Duplicate prevention action
- A separate Forsk PR #220 and issue #219 were briefly created with the same HackIndia topic before the full 17:07 central checkpoint addendum was read.
- After confirming Mango PR #220 already owns the story, the Forsk PR was **closed without merge** and issue #219 was **closed as duplicate**. No Forsk file was merged or published. Its closed branch remains only as an audit trail.
- Forsk duplicate PR: https://github.com/satnamkhowal/forsk-coding-school/pull/220
- Forsk duplicate issue: https://github.com/satnamkhowal/forsk-coding-school/issues/219

## 3. Official opportunities and programmes

### Google Student Researcher, 2027
- Official Google Careers page currently shows Apply available.
- Location: **India / Remote eligible**.
- Application deadline: **4 December 2026**; rolling review.
- Minimum qualification: currently enrolled in Bachelor's, Master's or PhD in a listed quantitative/computing/natural-science discipline and experience in a relevant computer-science area.
- Preferred: full-time enrolment and returning to the degree after the engagement; research experience/publications and programming-language experience.
- No stipend amount is published on the listing.
- Existing Forsk owner: PR #146; no duplicate article.
- Official source: https://www.google.com/about/careers/applications/jobs/results/125423735539671750-student-researcher

### NeGD Winter Internship 2026
- Official NeGD Careers page currently lists both Technical and Non-Technical Winter Internship 2026, Delhi-NCR, with a **20 November 2026** deadline.
- Both linked advertisement PDFs returned **403 Forbidden** in this check. Eligibility, duration, stipend and detailed application terms therefore remain unverified; do not invent them.
- Existing Non-Technical owner: Forsk PR #180. Technical listing not drafted because its PDF was inaccessible.
- Official listing: https://negd.gov.in/careers/

### NMMSS / VSSC / other existing opportunity owners
- NMMSS student application deadline remains 15 November 2026; ₹12,000/year from the earlier official verification; Forsk PR #173.
- VSSC UG academic project deadline 15 November and PG academic project deadline 16 November; Forsk PR #172. INT 08 internship is closed; INT 09 is a separate 2027 intake.
- Google Student Researcher and NeGD owners preserved; NIC Digital India Internship Winter 2026 remains distinct from MeitY's Digital India Internship Scheme.
- AICTE portal snapshot previously showed zero live postings; this is not evidence that all Indian internships are closed.

## 4. React / frontend
- Official React repository release list shows 19.3.1, 19.2.9, 19.1.10 and 19.0.9, all dated **14 October 2026**; React 19.3.0 was published **9 September 2026**.
- No new November stable React release found.
- Existing owners preserved: Forsk PR #145 and Mango PR #202.
- Sources:
  - https://github.com/facebook/react/releases
  - https://react.dev/blog/2026/09/09/react-19-3

## 5. Node.js / backend
- Official 11 November security bulletin: **16 unique CVEs** (7 High, 6 Medium, 3 Low).
- Patched release lines: Node **22.23.5**, **24.22.3**, **26.13.1**, all dated 11 November 2026.
- Node **27.0.0-alpha.0.1.0** was published 12 November and remains Alpha, not LTS.
- Existing owners preserved: Mango PR #143 (security readiness), Mango PR #153 (Node 27 Alpha), Groot alias PR #650. No duplicate Node article.
- Sources:
  - https://nodejs.org/en/blog/vulnerability/november-2026-security-releases
  - https://nodejs.org/en/blog

## 6. Repository and coordination review

### Mango Engineers
- Canonical accessible repository: https://github.com/satnamkhowal/mangoengineers.com
- Read `AGENTS.md`, `docs/agent-start-here.md`, `docs/task-board.csv`, `docs/work-log.md`, `docs/integration-queue.md`, current main and current PR/issue/branch ownership.
- Main base for PR #223: `51aa38209430bd916999073d4c710064fd864b8f`.
- PR #223 branch comparison: **6 ahead / 0 behind**, 4 changed files. Draft only; no shared PHP, public route, blog index, sitemap, schema, redirect, navigation, CSS/JS, forms or live page changed.

### Groot Academy
- Accessible alias `satnamkhowal/grootacademy.com` contains `.agent/README.md`, which names `satnamkhowal/gta` as canonical.
- Canonical `satnamkhowal/gta` was not available in installed repository search. No new Groot write was made; alias PRs are not treated as canonical implementation authority.

### Forsk Coding School
- Existing PR/issue queues and available project documentation were reviewed. Root `README.md` and `AGENTS.md` were not found; other project-specific deployment/SEO/news documentation was inspected.
- Forsk duplicate PR #220 was closed without merge; issue #219 closed as duplicate. No retained Forsk article in this cycle.

### Jaipur Engineers
- Accessible canonical repository and current PR/issue queues reviewed. Existing CRISP, Google and other opportunity owners preserved. No new unowned story warranted a Jaipur draft in this cycle; no files written.

### Central coordination
- Existing PR #19: https://github.com/satnamkhowal/brand-growth-control-center/pull/19
- Branch: `ops/news-factory-cycle-20261109-2209`.
- Current comparison: **164 ahead / 5 behind main**, diverged; GitHub reports mergeable=false. This checkpoint is appended as a new dated file only. No rebase, merge or deployment.

## 7. Production ledger

| Stage | This run |
|---|---:|
| Research tracks checked | 4 |
| New unique unowned story retained | 1 (GKE + Cloud SQL RAG architecture) |
| Original English article drafts retained | 1 (2,858 words) |
| Original SVG graphics retained | 1 |
| Local PNG/WebP derivatives retained | 2 |
| Existing HackIndia article owner | Mango PR #220 |
| Duplicate Forsk draft | Closed, not counted |
| Verified new YouTube embeds | 0 |
| Independent QA-ready | 0 |
| Live / published | 0 |
| Merged / deployed | 0 |
| Central checkpoint commits | 1 (after this file is added) |

### Mango PR #223 validation boundary
- Metadata JSON parsed after GitHub read-back.
- SVG 1200×675; local Git blob hash matches GitHub file.
- PNG preview visually inspected; WebP decoded; both 1200×675.
- GitHub Actions run 43424446650 (PHP Architecture Check) completed with failure on the PR head. Job `php-architecture` returned zero steps; log download returned BlobNotFound; combined commit status had no status entries. Cause is unclassified; do not attribute it to the docs-only change without logs.
- GitHub PR metadata reports mergeable=false. No merge or rerun attempted.
- Independent editorial, cloud architecture/security, pricing/region and responsive/browser QA remain pending.
- No public URL changed and no live publication is claimed.

## 8. Next actions
1. Independent editorial, cloud-security and pricing/region QA of Mango PR #223.
2. Investigate the unclassified PHP Architecture Check failure and PR mergeability before any integration; do not merge.
3. Recheck NMMSS on 14–15 November and VSSC UG/PG windows on 15–16 November.
4. Recheck NeGD PDFs and eligibility before any technical internship draft.
5. Recheck the single HackIndia owner in Mango PR #220 for the conflicting registration cutoff and event-duration schedule.
6. Resolve canonical Groot `satnamkhowal/gta` access before any new Groot writes.
7. Continue official React, Node.js and AI/cloud source checks; draft only genuinely unowned stories.

**No merge, deployment or publication occurred in this cycle.**