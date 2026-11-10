# Groot Academy — News Factory Amazon 2027 internship overlap delta
**Observed:** 2026-11-10 15:40 IST  
**Scope:** Coordination-only delta; no brand-source implementation or queue ownership change.

## New evidence
Groot News Factory PRs [#596](https://github.com/satnamkhowal/grootacademy.com/pull/596) and [#603](https://github.com/satnamkhowal/grootacademy.com/pull/603) were compared against each other and the canonical 100K queue.

- PR #596: 1,956-word draft covering Systems Development Engineer Intern 2027 (10498158) and Data Engineer Intern 2027 (10496769); four changed files including an original 1200×675 SVG, metadata and task log.
- PR #603: 1,784-word draft covering Business Intelligence Engineer Intern 2027 (10498165) and Support Engineer Intern 2027 (10498163); three changed files including an original 1200×675 SVG and metadata.
- Exact job IDs do not overlap, but both drafts target the broad “Amazon India 2027 internships” reader intent and repeat a similar quick-answer, eligibility/location, application-status, deadline/compensation, preparation, checklist and FAQ structure.
- Finding: **high umbrella-intent overlap; no exact job-ID duplication**. Different roles alone do not justify two broad pages.
- Recommendation to the News Factory owner: consolidate all four listings into one useful guide, or materially differentiate the two role-family intents, titles and outlines and cross-link them before publication.
- Both PRs remain Draft/unmerged; independent editorial/source and responsive-browser QA are pending. Their recorded base snapshots differ (#596: `a97dc07463a352ea924af3dea22af915a6f9bdb1`; #603: `99336e8d0b412f6e0f0bdc0464e0aec4b8fea2b5`), so exact-current-main revalidation is required before integration.

## 100K boundary
- The canonical queue still contains 29 IDs. Neither PR has a 100K ID or a matching Amazon-specific queue intent.
- Current-main registry has one adjacent general `internship-for-it-students` entry; current blog sitemap has no Amazon/internship URL hit.
- No queue row, article count, owner, public route, PHP, schema, sitemap or production file changed.
- The full evidence report is committed in the Groot source repository: [News Factory overlap review](https://github.com/satnamkhowal/grootacademy.com/blob/qa/groot-100k-current-main-20261109/marketing/blog-factory/reconciliation/news-factory-amazon-pr596-pr603-overlap-20261110-1540-ist.md).

## Existing Groot release gates
PR #569 remains Draft with no submitted reviews or review threads. GA-B00029 remains TECH_QA, noindex,follow and publication-unapproved. Authorized production HTTP/MIME and full-root PHP rendering remain pending; the current execution container cannot resolve GitHub or grootacademy.com. The Master board continues to hold HAO-008 at P3/REVIEW. The central AEO/GEO PR #2 baseline and all other brand ownership remain unchanged.

## Next actions
1. News Factory owner resolves #596/#603 consolidation or distinct-intent scope; no coordinator edits to their files.
2. Groot owner obtains an authorized PHP/network runner for GA-B00029 and independent review for PR #569 and the five-article recovery stack.
3. Master owner resolves HAO-008 priority/queue disposition before new 100K batches or GA-B00005 integration.
4. Central owner may add the verified Groot active row through the existing reviewed control-board process; no direct README/main edit was made here.
