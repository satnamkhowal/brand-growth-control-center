# News Factory cycle — 15 November 2026, 04:11 IST

## Run outcome

Four non-overlapping research lanes were checked against current primary sources and existing brand ownership. One new, previously unowned AI/cloud story passed deduplication and fit CadMate India's verified CAD/engineering-design audience. One original English technical guide, metadata sidecar and original SVG were committed to an isolated draft branch. Existing student-programme, React and Node owners were preserved.

No article was merged, published or deployed. This checkpoint continues the existing News Factory PR #19 and existing coordination/audits directory.

## 1. Student / developer programmes

### Deadline-day items — 15 November 2026

- **NMMSS AY 2026–27:** Ministry of Education / PIB notice published 31 October confirms student submission closes 15 November; institute L1 verification 30 November and district L2 verification 15 December. Existing Forsk owner: [PR #173](https://github.com/satnamkhowal/forsk-coding-school/pull/173). Primary source: https://www.dsel-education.gov.in/static/uploads/2026/11/d4b8ca5e528a05abde6f7ada8777e842.pdf
- **Sage IT India Scholarship:** sponsor page is dated 19 October and still lists 15 November submission deadline, ₹50,000 one-time award paid to the student's institution, age 17–30, recognised Indian college/university enrolment, all majors, individual unpublished 1,000–1,500-word article, no entry fee. No closing hour is published. Existing Forsk owner: [PR #184](https://github.com/satnamkhowal/forsk-coding-school/pull/184). Source: https://sageitinc.com/scholarship/india
- **VSSC UG Academic Project Work:** current HRDD portal says BE/BTech/BSc/Diploma downloaded-form route for 1 Jan–31 Mar 2027 has 15 November receipt deadline. This is academic project work, not the VSSC internship intake. Existing Forsk owner: [PR #172](https://github.com/satnamkhowal/forsk-coding-school/pull/172). Source: https://vsscinternship.vssc.gov.in/HRDD_LOGIN/beforelogincontroller
- **NASA Space Apps 2026:** current local-event schedules show 15 November global project-submission deadline at 23:59 local time, but the global event page returned HTTP 502 in this pass. Existing Forsk owner: [PR #231](https://github.com/satnamkhowal/forsk-coding-school/pull/231). Verify the local event/team dashboard timer before action: https://www.spaceappschallenge.org/2026/
- **VSSC PG Academic Project Work:** ME/MTech/Integrated MTech/MSc/BS-MS online route remains open through 16 November 2026, 23:59 IST. Existing Forsk owner #172. The downloaded UG form and online PG route must not be conflated.

### Upcoming items

- **NeGD Technical Internship — Winter 2026:** official careers index still lists Technical and Non-Technical Winter Programme roles in Delhi-NCR with 20 November deadline. The index itself does not show the full eligibility/stipend terms; use the linked official advertisement before student-facing claims. Existing Forsk owner: [PR #225](https://github.com/satnamkhowal/forsk-coding-school/pull/225). Source: https://negd.gov.in/careers/
- **Google Student Researcher, 2027:** Google Careers currently shows India — Remote eligible, Apply, rolling review, 4 December 2026 deadline. Current enrolment in Bachelor's/Master's/PhD in listed disciplines is required; no fixed stipend or duration is stated on the listing. Existing Forsk owner: [PR #146](https://github.com/satnamkhowal/forsk-coding-school/pull/146). Source: https://www.google.com/about/careers/applications/jobs/results/125423735539671750-student-researcher
- **NSP AY 2026–27:** current scheme list shows AICTE Pragati, Saksham, Swanath and UGC National Scholarship for PG Studies through 30 November. Each scheme's own specifications and current state/discipline criteria still need checking; do not infer universal eligibility from the list. Existing Forsk owners retained. Source: https://scholarships.gov.in/All-Scholarships

### Eligibility caution

Existing Forsk INSPIRE-SHE 2025 PR #167 contains a material 2025 guideline correction, but the 2025 call and post-offer PDF timed out/returned 502 when independently opened in this pass. Keep independent eligibility/source QA pending; do not treat the latest subject-list/award interpretation as independently revalidated in this run. No new student opportunity without a verified unowned topic was found.

## 2. React / frontend

- Official React release page still lists 19.3.1, 19.2.9, 19.1.10 and 19.0.9, all dated 14 October 2026; React 19.3 feature announcement is 9 September.
- No new November stable React release or security advisory found in this pass.
- Existing owners retained: Forsk #145 and Mango #202.
- Sources: https://react.dev/blog ; https://github.com/react/react/releases

## 3. Node.js / backend

- Latest official security bulletin remains 11 November 2026.
- Patched LTS versions: Node 22.23.5, 24.22.3 and 26.13.1.
- Bulletin covers 16 CVEs: 7 High, 6 Medium and 3 Low. Node 27.0.0-alpha.0.1.0 (12 November) remains Alpha, not LTS.
- Existing Mango owners #143 and #229 retained.
- Sources: https://nodejs.org/en/blog/vulnerability/november-2026-security-releases ; https://nodejs.org/en/blog/release

## 4. AI / cloud / developer news

### New verified, previously unowned story — Google Cloud agentic HPC at SC26

- Google Cloud Blog publication date: **13 November 2026**.
- SC26 event dates: **15–20 November 2026**; venue: McCormick Place, Chicago, Illinois, USA. Publication date and event dates are recorded separately.
- The article describes reusable agent skills paired with Cluster Toolkit blueprints, quota and regional-capacity preflight, human approval before deployment, IAM/Kueue/budget guardrails, Cloud Logging provenance, AlphaEvolve with Cloud Batch, HPC/AI hardware and Managed Lustre.
- It is a technical announcement/demonstration preview, not a new certification, a blanket GA claim or a universal India-availability promise.
- Current Google Cloud region documentation reviewed 15 November lists H4D, C4A and G4 among Mumbai machine families; Delhi lists G4 in the displayed zones. A4X/A5X are not shown in those India entries. Quota and zone capacity still require live project checks.
- No fixed end-to-end price or free student-credit claim is made.
- Primary sources:
  - https://cloud.google.com/blog/topics/hpc/whats-new-in-hpc-and-ai-at-sc26
  - https://sc26.supercomputing.org/attendees/chicago/
  - https://docs.cloud.google.com/cluster-toolkit/docs/overview
  - https://docs.cloud.google.com/compute/docs/regions-zones
  - https://cloud.google.com/products/compute/pricing

### CadMate India draft delivery

- Task: NF-CADMATE-GC-AGENTIC-HPC-SC26-20261115.
- Issue converted to [OPEN / DRAFT PR #5](https://github.com/satnamkhowal/cadmateindia.com/pull/5).
- Original English article: **3,159 words**.
- SEO/AEO/GEO metadata JSON.
- Original self-authored **1200×675 SVG** workflow infographic.
- Local 1200×675 PNG and optimized WebP derivatives rendered, decoded and visually inspected; SHA-256 and rights/provenance recorded in metadata.
- GitHub read-back: all 3 intended files present; article word count matches metadata; JSON parse PASS; SVG title/description/dimensions PASS.
- Branch: news-factory/google-cloud-agentic-hpc-sc26-20261115-0411; **3 commits ahead / 0 behind main**, exactly 3 files.
- No third-party logos, screenshots, photographs or downloaded graphics used.
- No story-specific official/reputable YouTube video with verified ID, channel, date and embedding permission was established; no iframe added.
- Independent editorial, cloud/HPC technical, India-region/cost and responsive QA pending.
- GitHub reported mergeable=false when the draft PR was created; branch compare shows no behind commits. Combined status and workflow-run queries returned no checks. Recheck mergeability/CI before review; do not interpret this as a diagnosed content conflict or a test pass.

### Existing AI/developer owners preserved

- **Correction from the 05:04 audit:** Forsk PR #185 is correctly based on GitHub's 15 October notice for Claude Opus 4.8, Claude Opus 5 and GPT-5.6 Terra retiring on **16 November**. A 15 November comment incorrectly conflated it with the separate 13 November / **14 December** notice; that comment (#6884026363) has been edited to withdraw the wrong instruction. Keep PR #185's original title and model list. The separate December notice is already recorded in comments #6865739827 and #6869517067.
- AWS Emulator local testing: Mango #250.
- Google Cloud ADK workflow patterns: Mango #251.
- GitHub AI Scan API: existing Jaipur/Groot ownership as recorded in previous checkpoints.
- No duplicate story was opened for those existing owners.

## 5. Repository and coordination audit

Repositories/brand mappings reviewed: central Brand Growth Control Center, Mango Engineers, Groot Academy (grootacademy.com), Forsk Coding School, CadMate India, and the accessible Jaipur-related certificate repositories. Jaipur Engineers' canonical implementation repository remains unresolved in the central mapping; no Jaipur write was made. Clever Ape, Groot Software and Forsk Technologies mappings remain subject to the central verification notes.

- CadMate root README and docs/SOURCE_OF_TRUTH.md read before writes.
- CadMate open PR #4 owns only course.php, its CAD portfolio QA script and workflow. The new draft touches only docs/news-factory/drafts/ and docs/news-factory/media/.
- CadMate closed PR #3 / branch content/google-agentic-architect-2026-11-12 was inspected; it is a separate certification explainer, and its branch is diverged (9 ahead / 1 behind). It was not reused, rebased or merged.
- Mango README, AGENTS.md, agent-start guide, task board, work log and integration queue were read. Existing News Factory owners for ADK, AWS Emulator, Cloud SQL, Node and React were preserved.
- Groot 100K controller issue #401 was read: the one-million goal is aspirational and evidence-gated; the canonical 29-ID queue remains under its existing owner/approver gates. No new Groot content ID was opened.
- Forsk current PR/issue ownership was reviewed; existing scholarship, React, Node and Copilot tasks were not duplicated.
- Central README and master pending queue were read. This update continues existing News Factory PR #19 and its coordination/audits directory.

Central News Factory branch ops/news-factory-cycle-20261109-2209 compares **217 ahead / 5 behind main**, diverged. No rebase, force-push or merge was performed.

## 6. Production ledger — this run only

| Stage | New count |
|---|---:|
| Research lanes | 4 |
| New verified unowned stories | 1 |
| Original English article drafts | 1 |
| Original SVG graphics | 1 |
| Local PNG/WebP derivatives | 2 |
| New GitHub draft PRs | 1 |
| Verified YouTube links/embeds | 0 / 0 |
| Independent QA-ready | 0 |
| Live / published | 0 |
| Merged / deployed | 0 |

**Next action:** independent QA of CadMate PR #5; recheck its mergeability/CI; validate the INSPIRE-SHE 2025 PDF eligibility claims before approval; correct Forsk #185's stale 16 November title via its owner; recheck today's programme deadlines and the next NeGD/Google/NSP dates.