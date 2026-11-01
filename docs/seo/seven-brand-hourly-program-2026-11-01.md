# Seven-brand SEO & editorial operations — 2026-11-01

**Scope:** coordination only. This repository is the control plane; implementation belongs in each brand's own verified repository. The owner requests research, HD brand graphics, safe GitHub PR integration and hourly reports, with an aspirational **100 QA-approved articles per brand per day**. This is a **target, not a claim of delivery**, and is subject to distinct user intent, reviewer capacity, source accuracy and Google's scaled-content-abuse policy.

## Brand ownership / authoritative candidates

| Brand | Website | Implementation repository | Unique editorial focus | Source confidence / gate |
| --- | --- | --- | --- | --- |
| Groot Academy | https://grootacademy.com/ | `satnamkhowal/gta` | Original course guides, programming, data, software careers | Verified repo; reuse existing blog registry and draft blog-factory controller PR #405; do not shortcut review-only PRs |
| Jaipur Engineers | https://jaipurengineers.com/ | `satnamkhowal/je2` | Software engineering / Java-backend / job-relevant projects | Verified repo; continue existing `seo/continuous-growth-20261016` checkpoints and existing PR ownership |
| Forsk Coding School | verify primary canonical from repo | `satnamkhowal/forsk-coding-school` | Practical coding tutorials, authentic student projects, original instructor examples | Verified repo; preserve existing Forsk SEO/GSC recovery task, URLs and draft QA boundaries |
| Mango Engineers | https://mangoengineers.com/ | `satnamkhowal/mangoengineers.com` | Programming, full stack, analytics, AI/DevOps training in Jaipur | Repo README names the site; use `docs/agent-start-here.md` and `docs/task-board.csv`; do not mistake for industrial design firm |
| Clever Ape Academy | https://cleverapeacademy.com/ | `satnamkhowal/clp` | Digital marketing, SEO, advertising, campaign analytics and adjacent courses | Repo `includes/config.php` names exact site/brand/logo; **do not use `cleverape.in`** (not current academy site) |
| Swiggy Wala | https://swiggywala.com/ | **NOT YET LOCKED**: compare `satnamkhowal/swiggy-wala-new-website` vs `satnamkhowal/swiggy-wala-website` | Jaipur taxis, airport transfers, Rajasthan routes and practical travel guides | Both repos contain Swiggy Wala site configuration. Current live site could not be fetched; determine deployment/source authority before writing public routes or merges |
| CadMate India | https://cadmateindia.com/ | `satnamkhowal/CadMateIndia` — **VERIFIED AUTHORITATIVE IMPLEMENTER** | AutoCAD, BIM, Revit, SolidWorks, CATIA, CAD workflows | Live title, H1, course tracks, enquiry wording, locations and footer match current PHP source; `cadmateindia.com` is a legacy static mirror. Evidence: `docs/seo/authoritative-repository-audit-2026-11-01.md` |

Keep every brand's logo, colours, business facts, author identity, internal links, schema and canonical domain separate. Cross-brand links only when editorially relevant and transparent, never to boost ranks artificially. Do not fabricate course, placement, certification, price, date, travel amenity or location claims.

## Scheduling and concurrency

One existing task automation `6ad22138e75c819197983646ed12a562` was upgraded on 2026-11-01 to **Seven Brand SEO Growth**, hourly from 02:15 Asia/Kolkata, preserving the Jaipur Engineers workstream. The account's limit is five active task automations; the other Groot/Forsk operations remain separately scheduled. Automation is **one bounded execution per hour**, not a permanently running process. Re-enter from saved GitHub checkpoints each run; do not start competing workers on locked files or duplicate existing schedules.

## Hourly production cycle

1. Read latest `main`, project instructions, open PRs, last run ledger, topic claims and CI before edits; freeze overlapping routes/assets and identify a single highest-value bounded batch.
2. Research actual demand and user intent using relevant official docs, Search Console when connected and credible current sources; compare existing content and cross-brand search-intent overlap. Claim non-overlapping topic IDs and drafts before creation.
3. Draft useful original content: question/problem, prerequisites, practical examples, tested examples/code as appropriate, expert/source attribution, limitations and accessible formatting. Do not use repetitive templates, generic thin articles, fake testimonials or copied sources.
4. Design graphics only from genuinely authorized brand assets; record exact logo version, image source/licence and prompt/provenance. Use high-resolution editable/master assets where feasible (e.g. 2048x1152 source), appropriate cropped 1200x630 Open Graph and responsive optimized WebP/AVIF derivatives, text-free or sparse-text illustrations, width/height, accessible alt text and actual on-page crops. The HD source is not a reason to serve huge payloads. If no actual image generation or authorized logo exists, mark `IMAGE_BLOCKED`; a prompt alone is not an image.
5. Per article and targeted existing page validate distinct search intent, accurate title/H1, meta description, self-canonical/redirects, semantic headings, relevant genuine internal links, structured data matching visible content, breadcrumb where appropriate, sitemap ownership, robots/indexability only for ready pages, unique OG image, alt, lazy loading / eager hero, mobile/keyboard/accessibility, image compression, performance/CLS, forms/CTAs and absence of broken links.
6. Use isolated feature branch and precise file ownership; record SHA and changed paths. Open PR; validate source tests, PHP lint / rendered preview / HTTP / device smoke and CI if present, seek independent QA. **Merge only new scoped PRs that satisfy all required gates**, with safe deployment implications; preserve explicit PR-specific no-merge approvals and do not turn merge into silent production deployment. No direct-to-main pushes or force pushes.
7. Separate verified lifecycle states: `IDEA`, `CLAIMED`, `DRAFT`, `FACT_CHECKED`, `IMAGE_READY`, `QA_PASS`, `PR_OPEN`, `MERGED`, `DEPLOYED`, `LIVE_VERIFIED`, `GSC_INDEXED_OBSERVED`; keep `BLOCKED`/`UNKNOWN` and evidence for missing checks. Sitemap presence does not mean Google indexing.

## Hourly evidence ledger schema

One row per brand per hourly cycle, with:
`run_at_ist,brand,repo,main_sha,topic_claims_new,articles_drafted,articles_fact_checked,articles_qa_pass,articles_committed,articles_merged,images_hd_created,images_web_optimized,images_committed,prs_opened,prs_merged,deployed_confirmed,live_pages_verified,gsc_index_observed,qa_blockers,source_links,branch,commit_shas,pr_links,next_action,owner`.

Every report states the real measured results (including zero), delta since prior run, daily progress toward 100 **per brand**, and cumulative milestones separately. No extrapolated counts, no invented rank/index statistics.

## First production safety gates

- Confirm Swiggy Wala deployment identity before implementation; do not modify both candidates. CadMate is locked to `satnamkhowal/CadMateIndia` by the 2026-11-01 authority audit.
- Read Clever Ape's `clp` logo path and URLs; avoid mistakenly reusing the historical `cleverape.in` domain, which currently presents unrelated content.
- Preserve existing Groot Academy controller PR #405 and its validation/independent review blockers; coordinate with the existing worker registry rather than opening a duplicate.
- Review existing Jaipur Engineers and Forsk image queues before generating any HD graphics.
- Begin with small QA-complete batches (e.g. 1–3 per brand), measure real content value, then scale responsibly. **100/day per site is not achievable by declaring articles complete without evidence.**

## Reference standards
- Google Search Central: https://developers.google.com/search/docs/essentials/spam-policies
- Helpful content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Image SEO: https://developers.google.com/search/docs/appearance/google-images


## Verified portfolio ledger — 2026-11-01, Jaipur Engineers DSA Java lab batch

Counts below are for this bounded batch only. “QA passed” means repository exact-head contract/CI passed; it is not deployment, live availability, indexing, traffic, lead or ranking evidence.

| Brand | Planned | Drafted | Fact checked | QA passed | Committed | PR open | Merged | Images created | Deployed | Live | Indexed | Daily aspiration progress |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- | --- |
| Jaipur Engineers | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | NO | 0 | UNKNOWN | 1/100 QA-approved draft; 0/100 published |
| Groot Academy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NO CHANGE | 0 | UNKNOWN | 0/100; separate existing lane not duplicated |
| Forsk Coding School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NO CHANGE | 0 | UNKNOWN | 0/100; separate existing lane not duplicated |
| Mango Engineers | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NO CHANGE | 0 | UNKNOWN | 0/100 |
| Clever Ape Academy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NO CHANGE | 0 | UNKNOWN | 0/100 |
| Swiggy Wala | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | BLOCKED | 0 | UNKNOWN | 0/100; authoritative implementer unresolved |
| CadMate India | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NO CHANGE | 0 | UNKNOWN | 0/100 |

Jaipur Engineers evidence:
- Draft PR: https://github.com/satnamkhowal/je2/pull/30
- Exact head: `18335fe101b64a335a38fe93e6aca82c414e644e`; exact main base `009658fac7383a73099d5933a1619c96fba061e7`.
- Four intended files: one improved existing PHP guide, one Java 17 lab, one exact contract and one focused workflow.
- Focused CI run 41313139978 SUCCESS; NPE regression run 41313139790 SUCCESS.
- Broader GSC recovery run 41313139762 FAILED after the improved DSA route passed, on the separate legacy `debugging-techniques-fixing-code-errors` canonical.
- No image generated because the known Jaipur image queue path remains unavailable and no audited page-specific image need was approved.
- No merge or deployment. Live, GSC indexing, GA4 engagement, qualified leads and ranking remain UNKNOWN.

Next owned action: repair the unrelated legacy debugging stub as a separate bounded Jaipur Engineers batch, or wait for fresh GSC/GA4 evidence before selecting another page. Swiggy Wala implementation remains blocked until deployment authority is evidenced. Do not use control-plane counts as content-production counts.


## Verified portfolio ledger — 2026-11-01, Jaipur Engineers debugging-guide restoration

Counts below are for this bounded batch only. No new article body was drafted: one existing substantive resource was restored to its canonical public wrapper and exact-head QA passed.

| Brand | Planned | Drafted | Fact checked | QA passed | Committed | PR open | Merged | Images created | Deployed | Live | Indexed | Daily aspiration progress |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- | --- |
| Jaipur Engineers | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | NO | 0 | UNKNOWN | 0/100 new drafts; 1 existing resource restored and QA-passed |
| Groot Academy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NO CHANGE | 0 | UNKNOWN | 0/100; separate existing lane not duplicated |
| Forsk Coding School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NO CHANGE | 0 | UNKNOWN | 0/100; separate existing lane not duplicated |
| Mango Engineers | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NO CHANGE | 0 | UNKNOWN | 0/100 |
| Clever Ape Academy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NO CHANGE | 0 | UNKNOWN | 0/100 |
| Swiggy Wala | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | BLOCKED | 0 | UNKNOWN | 0/100; authoritative implementer unresolved |
| CadMate India | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NO CHANGE | 0 | UNKNOWN | 0/100 |

Jaipur Engineers evidence:
- Draft PR: https://github.com/satnamkhowal/je2/pull/31
- Exact head `eac4339ae8d3b1af6f0c8111eecbc36aab02c2e6`; exact base `009658fac7383a73099d5933a1619c96fba061e7`; 3 commits ahead, 0 behind, 3 intended files.
- Restored the exact existing debugging guide owner; did not create another URL or duplicate article body.
- Focused CI run 41317608669 SUCCESS: PHP lint, rendered clean canonical, LearningResource schema, internal links and seven-case Node boundary contract.
- Broader recovery run 41317608621 FAILED on the independent DSA stub that remains isolated in draft PR #30.
- No image generated: known Jaipur queue remains unavailable and no approved image need was established.
- No merge/deployment. Live, GSC indexing, GA4 engagement, qualified leads and ranking remain UNKNOWN.

Next owned action: independently review PRs #30 and #31, reconcile them only against the latest main, and run the combined recovery suite before any owner-approved merge.


## Verified portfolio ledger — 2026-11-02, Jaipur Engineers recovery integration

Counts below are for this bounded integration batch only. No new article body was drafted; two independently owned existing resources were reconciled and tested together.

| Brand | Planned | Drafted | Fact checked | QA passed | Committed | PR open | Merged | Images created | Deployed | Live | Indexed | Daily aspiration progress |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- | --- |
| Jaipur Engineers | 1 | 0 | 2 | 1 | 1 | 1 | 0 | 0 | NO | 0 | UNKNOWN | 0/100 new drafts; 2 existing resources pass combined focused QA |
| Groot Academy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NO CHANGE | 0 | UNKNOWN | 0/100; separate existing lane not duplicated |
| Forsk Coding School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NO CHANGE | 0 | UNKNOWN | 0/100; separate existing lane not duplicated |
| Mango Engineers | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NO CHANGE | 0 | UNKNOWN | 0/100 |
| Clever Ape Academy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NO CHANGE | 0 | UNKNOWN | 0/100 |
| Swiggy Wala | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | BLOCKED | 0 | UNKNOWN | 0/100; authoritative implementer unresolved |
| CadMate India | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NO CHANGE | 0 | UNKNOWN | 0/100 |

Jaipur Engineers evidence:
- Integrator draft PR: https://github.com/satnamkhowal/je2/pull/32
- Exact merge `b60207d2609243ea193947cec94139d980923523`; exact main base `009658fac7383a73099d5933a1619c96fba061e7`; 8 commits ahead, 0 behind, 7 intended files.
- Source PRs #30/#31 remain open, draft and unmerged.
- DSA focused run 41343323524 SUCCESS; debugging focused run 41343323598 SUCCESS; NPE regression 41343323413 SUCCESS.
- Full recovery run 41343323359 passed both integrated canonical owners and then failed on the next independent logical-thinking stub.
- No image generation, merge or deployment. Live, GSC indexing, GA4 engagement, qualified leads and ranking remain UNKNOWN.

Next owned action: human-review PR #32 as the single integrator candidate. Audit the logical-thinking stub in a separate branch; do not widen the integration diff.
