# News Factory research and draft-production checkpoint

Date: 9 November 2026 (Asia/Kolkata)  
Research window: current-source verification completed during the 22:09 IST cycle  
Scope: Mango Engineers, Groot Academy, Forsk Coding School and Jaipur Engineers. No other brand was written because the central source-mapping queue still marks its repository/catalogue identity unresolved.

## Coordination baseline

- Central repository main observed at `31af61b9a796472b7eb13d6b254aa6d9dc2ecc34`.
- Central README says this repository is coordination-only and implementation belongs in each verified brand repository.
- Existing central coordination PRs #17 and #18 remain open draft PRs. They record Groot's repository rename/alias and the 100K controller/runtime delta; neither was edited by this cycle.
- Groot repository identity was verified as `satnamkhowal/gta` renamed to `satnamkhowal/grootacademy.com` (same repository ID 1375760757). The current content repository is `grootacademy.com`.
- Jaipur Engineers identity was verified as `satnamkhowal/je2` renamed to `satnamkhowal/jaipurengineers.com` (same repository ID 1369588932). `MIGRATION-NOTES.md` still identifies the `je2` application history as canonical; no Jaipur content write was made.
- The central queue continues to mark Clever Ape, CadMate, Groot Software and Forsk Technologies source/catalogue mapping as unresolved. No write was made to those repositories.
- The existing News Factory inventory and open PRs were inspected before creating a new article. No duplicate Cloud Pathways draft or media path existed.

## Research results

### 1. Student, developer and scholarship opportunities

Current official listings were rechecked:

- Google Careers — Research Scientist PhD Intern, Summer 2027, Hyderabad: the official page shows an application opening date of 28 October 2026 and closing date of 30 November 2026. Minimum qualifications include current PhD enrolment in a relevant technical field, ML experience, and Python/Java programming. The page shows an Apply control. Public compensation is not stated.  
  Source: https://www.google.com/about/careers/applications/jobs/results/87534302853505734-research-scientist-phd-intern-summer-2027
- Google Careers — Student Researcher, 2027: the official page shows India as the remote-eligible location and asks applicants to complete the application before 4 December 2026; rolling review is stated. Bachelor's, Master's and PhD enrolment are listed as eligible degree levels, subject to the role's subject and experience requirements.  
  Source: https://www.google.com/about/careers/applications/jobs/results/125423735539671750
- National Scholarship Portal 2026–27: NMMSS student applications are listed through 15 November 2026. AICTE Pragati technical-degree and technical-diploma schemes are listed through 30 November 2026. The portal footer still says last updated June 2026, so status must be rechecked on the live portal immediately before any student action. These are existing schemes, not newly announced November openings.  
  Source: https://scholarships.gov.in/All-Scholarships

No new opportunity article was added because existing drafts already cover Google internship/research and scholarship stories in Mango PR #143 and Groot PR #577. The deadlines are recorded here as a watch item, not as new draft counts.

### 2. React / frontend

- The official React release list still shows 19.3.1, 19.2.9, 19.1.10 and 19.0.9, all dated 14 October 2026.
- The two current React Server Components advisories checked are GHSA-xqc2-xf4c-x3h3 (Critical) and GHSA-h3gv-c5rc-p453 (High), both published 14 October. The current patched tags include 19.3.1, 19.2.9, 19.1.10 and 19.0.9 for the affected package lines.
- Existing Forsk PR #145 already owns the React Server Components security catch-up. No duplicate article or graphic was created.

Sources:
- https://github.com/facebook/react/releases
- https://github.com/facebook/react/security/advisories/GHSA-xqc2-xf4c-x3h3
- https://github.com/facebook/react/security/advisories/GHSA-h3gv-c5rc-p453

### 3. Node.js / backend

- The Node.js advance notice was published on 3 November 2026 and last updated the same day.
- It says 26.x, 24.x and 22.x security releases are expected on or shortly after 11 November 2026; the highest severity in each line is HIGH.
- As checked on 9 November, the notice does not list CVE IDs, affected patch ranges or patched versions. This remains a readiness notice, not a published patch.
- Mango PR #143 already owns the Node.js readiness article and graphic. No duplicate was created.

Source: https://nodejs.org/en/blog/vulnerability/november-2026-security-releases

### 4. AI / cloud / developer infrastructure

- Google Cloud published the Cloud Pathways GA announcement on 9 November 2026. Cloud Pathways is GA on GKE; the separate Cluster Director integration for Slurm clusters remains Preview.
- Google lists TPU v5e, v5p, Trillium (v6e) and Ironwood (TPU 7x) support on GKE, with versioned Pathways images supporting JAX 0.10.1+.
- The current official GKE TPU availability table does not list a Mumbai or Delhi TPU zone. The listed APAC Trillium zone is Tokyo.
- Cloud TPU prices are listed per chip-hour; the draft records selected on-demand examples and warns that GKE, storage, networking and other services add cost.

Sources:
- https://cloud.google.com/blog/topics/ai-infrastructure/cloud-pathways-a-distributed-ml-runtime-is-ga
- https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus
- https://cloud.google.com/tpu/pricing
- https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/run-workloads-pathways

## New production this cycle

### Groot Academy — Cloud Pathways guide

- Repository: `satnamkhowal/grootacademy.com`
- Base main: `0648b79ee0775e810251192a61b8ae6d842980f4`
- Branch: `content/news-factory-cloud-pathways-gke-ga-20261109`
- Draft PR: https://github.com/satnamkhowal/grootacademy.com/pull/580
- Files:
  - `docs/news-factory/drafts/cloud-pathways-gke-ga-november-2026.md`
  - `docs/news-factory/media/cloud-pathways-gke-ga-20261109.svg`
  - `docs/news-factory/drafts/cloud-pathways-gke-ga-november-2026.metadata.json`
- Output: one original English article draft (2,382 words), one original 1200×675 SVG, one source/media provenance JSON sidecar.
- The article distinguishes publication date from event date, records GKE GA versus Slurm Preview, explains India TPU-zone limits, documents prerequisites and IAM, and includes point-in-time TPU chip-hour examples.
- The SVG was authored for this article; no third-party graphics were downloaded. Local working path: `/mnt/data/news-factory/2026-11-09/cloud-pathways-gke-ga.svg`.
- Read-back checks: article and SVG exist on the branch; metadata JSON parses; SVG XML parses locally and has title/description and 1200×675 dimensions. No external image or linked media is embedded.
- Independent editorial/technical QA: PENDING. Browser rendering: NOT RUN. Workflow runs/status checks: none returned for the draft commit. PR remains open and unmerged.

## Existing News Factory work preserved

- Mango Engineers PR #143 — five existing draft topics (Django security, Gemini Omni 1.2 Flash, Google Research Scientist PhD Intern, Node.js November security notice, AICTE Pragati). React RSC material was intentionally left with Forsk to avoid cross-brand duplication.
- Forsk Coding School PR #145 — React Server Components October security catch-up.
- Groot Academy PR #577 — NMMSS scholarship draft.
- Groot Academy PR #578 — AWS S3 Tables managed Hive-to-Iceberg draft.
- Groot Academy PR #580 — new Cloud Pathways draft from this cycle.

All remain review/draft items. No merge, deployment, publication, indexing claim or production verification is made.

## Cycle counts

| Metric | This cycle |
| --- | ---: |
| New verified research items added to the queue | 1 Cloud Pathways GA item; existing openings/releases revalidated |
| New article drafts | 1 |
| New original graphics | 1 |
| New licensed external downloads | 0 |
| Verified story-specific YouTube embeds | 0 |
| Independent QA-ready drafts | 0 |
| Live/published articles | 0 |

## Next exact actions

1. Obtain independent technical/editorial review and browser rendering for Groot PR #580; do not merge before those gates.
2. On or after 11 November, recheck the Node.js official notice for actual patched versions, CVEs and affected ranges before converting the readiness article into a patch guide.
3. Recheck NMMSS on the live NSP portal before 15 November and Pragati before 30 November; if a deadline/status changes, update existing drafts rather than creating duplicates.
4. Keep React advisories and the existing Forsk PR #145 as the single React security content owner.
5. Continue source-mapping verification before writing for the remaining central brands.


## Additional opportunity draft — Forsk Coding School

A second distinct opportunity article was added after the first checkpoint commit:

- Official source: https://www.google.com/about/careers/applications/jobs/results/125423735539671750
- Current listing checked 9 November 2026: Student Researcher, 2027; India — Remote eligible; apply before 4 December 2026; rolling review.
- The listing does not state an opening date, fixed duration, stipend/salary amount or application-fee details. The article preserves those unknowns.
- It distinguishes this Bachelor's/Master's/PhD opportunity from the separate PhD-only Research Scientist PhD Intern role in Hyderabad.
- Repository: `satnamkhowal/forsk-coding-school`; base main `a690ef725029e8c7f96b6148e9012f82a481bd6d`.
- Branch: `content/news-factory-google-student-researcher-2027-20261109`.
- Draft PR: https://github.com/satnamkhowal/forsk-coding-school/pull/146
- Files: `docs/news-factory/drafts/google-student-researcher-2027-india.md`, `docs/news-factory/media/google-student-researcher-2027-india.svg`, and `docs/news-factory/drafts/google-student-researcher-2027-india.metadata.json`.
- Output: one original 2,113-word English opportunity guide, one original 1200×675 SVG and one source/media provenance sidecar.
- Read-back: all three files verified; metadata JSON parsed; SVG title/description/dimensions verified; local XML parse and PNG rendering passed.
- Independent editorial QA remains PENDING. No YouTube ID was verified and no iframe was added. No external media was downloaded. No merge, publication or application was performed.

Updated cycle production totals: 2 new article drafts, 2 original SVG graphics, 0 external licensed downloads, 0 verified YouTube embeds, 0 independent QA-ready drafts and 0 live articles.


## Additional scholarship research and draft — Forsk Coding School

A third distinct article was produced from the current NSP 2026-27 list:

- **AICTE Swanath Scholarship:** NSP lists degree and diploma scheme cards as open from 1 June through 30 November 2026 when checked on 9 November.
- The linked AICTE guideline is dated **May 2025**, and states ₹50,000 per annum, up to 2,000 annual awards (1,000 degree / 1,000 diploma), qualifying category requirements, an income ceiling of ₹8 lakh, regular-mode AICTE-approved study and a restriction on other Central/State/AICTE-sponsored scholarships.
- The NSP page footer still states last update June 2026; the draft preserves this staleness caveat and instructs applicants to recheck the live form.
- Repository: `satnamkhowal/forsk-coding-school`; base main `a690ef725029e8c7f96b6148e9012f82a481bd6d`.
- Branch: `content/news-factory-aicte-swanath-2026-27-20261109`.
- Draft PR: https://github.com/satnamkhowal/forsk-coding-school/pull/147
- Files: `docs/news-factory/drafts/aicte-swanath-scholarship-2026-27.md`, `docs/news-factory/media/aicte-swanath-2026-27.svg`, and `docs/news-factory/drafts/aicte-swanath-scholarship-2026-27.metadata.json`.
- Output: one original 2,106-word English guide, one original 1200×675 SVG and one source/media provenance sidecar.
- Read-back: all three files verified; metadata JSON parsed; SVG title/description/dimensions verified; local XML parse and PNG rendering passed.
- Independent editorial QA remains PENDING. No YouTube ID was verified and no iframe was added. No external media was downloaded. No merge, publication or application was performed.

### Research hold — AICTE Saksham

NSP currently lists AICTE Saksham degree and diploma cards through 30 November 2026, but the linked degree guideline is dated July 2020. It contains older scheme-year wording and must not be presented as a fully current 2026-27 eligibility guide without a newer AICTE/NSP clarification. No draft was produced from that stale guideline.

Updated cycle production totals: 3 new article drafts, 3 original SVG graphics, 0 external licensed downloads, 0 verified YouTube embeds, 0 independent QA-ready drafts and 0 live articles.
