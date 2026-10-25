# Forsk hourly execution — 24 October 2026

Hourly task Resume Forsk SEO fixes is enabled in Asia/Kolkata at the owner's request. Resume pending tasks from GitHub; skip completed work and active ownership, checkpoint interruptions. Credits and access limits still apply; no uninterrupted background guarantee.

First source repair: draft PR https://github.com/satnamkhowal/forsk-coding-school/pull/55 ; commit 6bb8f57676ce4a380dbf6c120e2f21db920bebe7. Official boilerplate restored in both GSC-reported AMP stories. Full validator, merge, host deployment and GSC Validate Fix remain pending. Detailed current checkpoint: https://github.com/satnamkhowal/forsk-coding-school/blob/main/docs/seo/GSC-RESUME-CHECKPOINT-2026-10-24.md . Existing GSC audit tasks remain the queue; PR54 owns blog pilots. No other issue claimed fixed.

## Verified follow-up

Full amphtml-validator@1.0.38 executed against both patched complete HTML documents: aws.html PASS; android.html PASS. PR #55 reviewed as exactly two boilerplate-line replacements and merged to main as f56881389148382b2fdb2e08dc3581c3116a8f95. This supersedes pending-validator/merge notes above. Host deployment and GSC Validate Fix still pending; do not claim live recovery. Next: retrieve both public HTML pages, compare/validate deployed output, then trigger GSC validation with verified access. Other audit tasks remain open.

## 24 October 2026 21:48 IST — AMP continuation verified

FCS-GSC-03 advanced. Fresh main/open-PR review found only PR54 editorial pilots; no competing AMP PR. AWS and Android public HTML fetched again and both PASS amphtml-validator@1.0.38 using downloaded official validator_wasm.js. Their source repair is now verified deployed; GSC Validate Fix was NOT submitted in this run.

Claude story existing full source FAILS mandatory boilerplate validation; one-line replacement PASS. PR56 https://github.com/satnamkhowal/forsk-coding-school/pull/56 merged as c5634c68a4d0eac01cff565a60c8294925904416 (one file, one line). Immediate public fetch still FAILS the old boilerplate: host publication PENDING. No content/metadata edits, workflow restoration or indexing claims. Initial validator CDN timeout recovered by fetching the official validator once; this is not a site failure.

Next: verify Claude host publication and full live AMP PASS, then GSC validation when authenticated access is available. Broader all-story/template audit and factual story review remain open. FCS-GSC-01/02/04–08 remain open; keep PR54 ownership separate. No new automation created.

## 24 October 2026 22:47 IST — FCS-GSC-03 Claude deployment verified

Bounded task completed: verify the previously pending Claude AMP publication. Source repair remains merge c5634c68a4d0eac01cff565a60c8294925904416 (PR56); no duplicate repair or deployment was initiated.

Fresh public GET https://forskcodingschool.com/web-stories/claude-fable-5-1-coding-students-september-2026/ returned HTTP 200 at the same effective URL. Complete downloaded HTML PASS with amphtml-validator@1.0.38 and official validator_wasm.js. Its amp-boilerplate exactly matches the previously tested repaired source. Self-referencing canonical is present. Live HTML SHA-256: 40a9d882f4629d7a96c8e112cd4a928e1c949e8f9ebf28d3b69765145e01d13b. This supersedes the previous Claude host-publication blocker. AWS/Android live PASS evidence remains in the preceding entry; they were not reworked.

States: source merged; Claude host publication verified; Google Search Console Validate Fix NOT submitted; Google recrawl/indexing and traffic recovery NOT verified. Authenticated GSC access was not tested in this run. Broader story/template coverage and editorial fact checks remain open, so FCS-GSC-03 is not fully closed.

Ownership check: fresh main and open PR review found PR57 (draft) owning final-year guide briefs and shared restored-content renderer changes, with PHP lint/render/schema/mobile/link QA pending. Do not duplicate those edits or infer its draft is abandoned. PR54 continues to own editorial pilots. Owner-paused workflows were not changed.

Next action: with verified authenticated GSC access, validate the reported repaired AMP URLs and record Google validation state; otherwise proceed to bounded FCS-GSC-02 current-error reproduction while respecting PR57 and PR54 ownership. No new code changes required for this verification.

Implementation checkpoint commit: da2fc2f0599c185309cf681aaa20e31bb1798297.

## 24 October 2026 23:47 IST — FCS-GSC-02 Core Java live reproduction

Bounded task: reproduce the specifically documented dedicated Core Java host 404 before attempting any repair. Latest reviewed main checkpoint was da2fc2f0599c185309cf681aaa20e31bb1798297. Open drafts remain PR57 (final-year guide/shared renderer) and PR54 (editorial pilots); neither scope was edited. Read the audit, SESSION_HANDOFF, MASTER_TASK_BOARD, existing recovery notes and current root rewrite rules. No competing Core Java repair was found.

Verified public GET evidence:
- /core-java-course-jaipur: HTTP 200, no redirect, one H1 "Core Java Course in Jaipur", self canonical https://forskcodingschool.com/core-java-course-jaipur and robots index/follow.
- /core-java-course-jaipur.php: HTTP 301 to the extensionless canonical, followed by HTTP 200; exactly one redirect, no observed loop, no X-Robots-Tag exclusion in captured response headers.
- Referenced assets/images/core-java-course-jaipur-forsk-coding-school.webp: HTTP 200, image/webp, 234864 bytes, valid RIFF/WEBP signature.
- Canonical GET HTML SHA-256: da47c64811c545f82f634c8bbabf8c317af2c34624c6b5d4bb6ae6be6afdd26d.
- Current source core-java-course-jaipur.php blob: 47a85ebaaac5b173d0a4b9e24d66ef1444b3bd73; root .htaccess blob: 4690f3521ab432b75ce2a22b40af97ac105a414b.

Conclusion: the earlier dedicated Core Java host-404 blocker is no longer reproducible and is superseded by the above live evidence. No runtime patch, redirect, link reversal, workflow restoration or deployment was needed or performed. Existing Java Full Stack card's verified Java Programming destination remains untouched. This confirms current availability, not when or which deployment restored it, editorial claim accuracy, responsive quality or Google indexing.

FCS-GSC-02 remains OPEN: exact examples for the historical 19 5xx / 10 redirect errors still require GSC export and current reproduction; do not mark all technical errors resolved from this one page. Next action: obtain those specific example URLs through authenticated GSC access, or continue existing recovery-map triage with a bounded sample. PR57/54 QA and broader AMP/GSC validation remain separate work.

Source evidence checkpoint: 6063e7bb8b47bea63d4fa2a865b7551e1b0380ab.

## 25 October 2026 — FCS-GSC-07 bounded sitemap discovery audit

Reviewed main 6063e7bb8b47bea63d4fa2a865b7551e1b0380ab, required source/central audits and handoff. Open PR54 editorial pilots, PR57 final-year/shared renderer and PR58 brochure documentation retain their ownership; no overlapping edits. Browser connection attempt returned Unknown tool(browser.js), so authenticated GSC state/export/Validate Fix could not be checked. GitHub and public HTTP reads remained available.

Live GET/XML checks:
- /sitemap_index.xml: HTTP 404. This corroborates the old submitted path's fetch problem, not failure of the current sitemap.
- /robots.txt: HTTP 200 and Sitemap: https://forskcodingschool.com/sitemap.xml; source agrees (blob a8e43eaaa916d027137ba59d8a5002106cd8a323).
- /sitemap.xml: HTTP 200 application/xml, valid sitemapindex, 8 distinct child locations; source agrees (blob 3612243865731ea35bdd85ad6ac671f576d675d4).
- All eight child sitemaps returned HTTP 200 and parsed successfully with Python ElementTree: sitemap-pages.xml 138 loc entries; blog/blogs-sitemap.xml 2095; images-sitemap.xml 31; branches/branches-sitemap.xml 2; news-sitemap.xml 38; local-student-resources-sitemap.xml 5; colleges-in-jaipur/colleges-sitemap.xml 31; recovered-pages-sitemap.xml 9. Counts are parsed loc entries, not unique sitewide pages or indexed totals. No duplicate loc text within each sampled child.
- Core Java canonical occurs in sitemap-pages.xml. Final-year guide canonical https://forskcodingschool.com/final-year-project-ideas/ occurs in recovered-pages-sitemap.xml; its absence from sitemap-pages.xml is NOT a missing-sitemap fault.

No runtime patch or duplicate sitemap entry warranted. No sitemap submitted/removed in GSC, no workflow enabled, no deployment initiated. XML parse success does not validate all child URLs' status/canonical/indexability, image schema semantics, profile identities or Google processing.

Next: when authenticated GSC access returns, review retirement/removal of obsolete sitemap_index.xml submission; current robots discovery already uses the new index. Continue separate mentor sitemap/profile inventory and bounded URL status/canonical checks. FCS-GSC-07 remains OPEN for those gates; higher-priority query/5xx/redirect-example work still awaits GSC evidence. No source-code task or indexing recovery is claimed complete.

Source checkpoint commit: b511cd2597f440e0d239bddbb7e5af8acf47b57f.

## 25 October 2026 — FCS-GSC-05 recovery deployment and indexing-gate reconciliation

Reviewed latest main b511cd2597f440e0d239bddbb7e5af8acf47b57f and required audits/handoff. Open PR54, PR57 and PR58 scopes remain untouched. Reused docs/ai-ops/gsc-report-recovery-20261016.md (blob 2122205ba2164f8147531522495acc9e0a0b8961) and existing recovery decisions, rather than recreating articles or redirects.

Bounded live check: all nine URLs listed in recovered-pages-sitemap.xml were fetched with GET and parsed with Python HTMLParser. Each returned HTTP 200 at its original URL, exactly one H1 and one matching self canonical, meta robots index/follow and no X-Robots-Tag exclusion. This advances the earlier sitemap XML-only check to page-level response/canonical/directive verification:
- https://forskcodingschool.com/final-year-project-ideas/
- https://forskcodingschool.com/5-mini-python-data-science-ai-projects-you-can-build-in-30-minutes/
- https://forskcodingschool.com/it-career-roadmap-for-students/
- https://forskcodingschool.com/10-java-projects-to-master-java-programming-beginner-to-advanced-guide/
- https://forskcodingschool.com/ai-project-ideas-beginner-advanced/
- https://forskcodingschool.com/data-science-roadmap-step-by-step-guide-to-become-a-data-scientist-in-2026/
- https://forskcodingschool.com/dsa-in-python-complete-beginner-guide-with-examples/
- https://forskcodingschool.com/why-classroom-learning-not-enough-software-jobs/
- https://forskcodingschool.com/it-courses-non-it-students-jaipur/

Control sample from the existing decisions registry: /courses/core-java-j2se-course-in-jaipur/lessons/what-is-java/ is CREATE with indexing_approved=false. Its live response is HTTP 200, matching self canonical, HTML robots noindex/follow AND X-Robots-Tag noindex/follow. This sample confirms the intended editorial gate remains deployed; it does not establish all 193 worksheets' behavior.

No restoration, new URL, redirect, code patch or blanket noindex removal was needed. The nine substantive guide URLs are available and permit indexing; that is not proof Google indexed them, accepted content quality, or restored rankings. PR57's proposed content remains draft, not included in this deployment claim. No responsive/editorial review was performed by these HTTP checks. No GSC action, deployment or paused-workflow change occurred.

Next: retain these nine URLs as existing recovered canonicals in subsequent 404 deduplication; inspect other legacy paths against the decisions registry before restoring. Review worksheets individually before indexing approval. GSC loss-query and exact 5xx/redirect-error exports remain unavailable pending authenticated access; FCS-GSC-05 stays OPEN for full reconciliation. Completed checks should not be repeated absent changes or a regression signal.

Source checkpoint commit: 94d3c1a89dbb527cf535d54c046a3241e60de21e.

## 25 October 2026 — FCS-GSC-07 mentor sitemap repair ready for review

Resumed existing branch fix/mentor-sitemap-approved-20261025 after fresh main/open-PR review. Main was 94d3c1a89dbb527cf535d54c046a3241e60de21e; PR54,57,58 did not overlap. Required audits/handoff reread. Previous interrupted preparation had created the branch but no commit; reused it.

Confirmed mismatch: live mentors/mentors-sitemap.xml had 501 distinct entries: directory plus 500 catalogue records. Public catalogue JSON matched source Git blob 4df2d89a00829555256bc2420a480a275e3d69d4; all 500 records fail the verified publishing gate. Directory and first/last catalogue profile samples were live noindex. This is not a claim that all 500 pages were fetched or that identities are proven fictitious.

Changed ONLY mentors/mentors-sitemap.xml: four approved_for_index profiles selected from existing real-instructor-profiles.php blob 1613a69b192a98a323551705b82568e252c6a92a: Satnam Singh, Shivanshi Paliwal, Jayakshi Agrawal and Kirti Sharma. Excluded pending Jivan profile and unverified catalogue; no biography, identity, claim, noindex gate or workflow edits.

Commit: 626fedca492589cce947a45d1855136b97af90c5.
PR59: https://github.com/satnamkhowal/forsk-coding-school/pull/59 (one changed file; ready for review, not merged).
Tests: XML parse and exactly four unique approved URLs PASS; fresh GET of all four on 25 October returned HTTP 200, unchanged final URL, self canonical, indexable meta robots and no X-Robots-Tag exclusion. Temporary validation script indentation typo corrected before successful execution. No PHP changes or CI run.

State: tested source repair committed on branch; review/integration pending; served repaired sitemap and Google processing NOT verified. PR creation returned mergeable=false; do not infer conflict cause from that initial value—refresh PR state before integration. No deployment or GSC submission performed. Next: review exact one-file diff, refresh mergeability, integrate through normal process, then verify live XML contains exactly these four URLs. Check any sitemap generator before regeneration so it cannot reintroduce the catalogue. FCS-GSC-07 remains open through release verification.

Source checkpoint: 65592c575dc29935a987bd2bd723e73bb27a5070.

## 25 October 2026 — FCS-GSC-07 PR59 merged; publication pending

Fresh audit/handoff/checkpoint and open-PR review confirmed existing mentor branch ownership. Compared main 65592c575dc29935a987bd2bd723e73bb27a5070 with branch: exactly one sitemap file changed; behind-main commit only documents prior work. Reviewed complete final XML at head 626fedca492589cce947a45d1855136b97af90c5 and unchanged approved registry blob 1613a69b192a98a323551705b82568e252c6a92a. Prior XML/four-profile live tests remain applicable; no implementation changes since those tests.

Independent COMMENTED review submitted 25 Oct 04:58:56 UTC corroborated exact approved set, four live canonicals/indexable robots, mergeability and lack of review threads. Fresh thread list empty. No independent APPROVED status or CI success is claimed. Normal GitHub merge succeeded with expected-head guard; no protections bypassed and owner-paused workflows untouched.

PR59 merged as 505818d7fa8dff58881186077b55526deee058f9. Immediately subsequent public GET /mentors/mentors-sitemap.xml returned HTTP 200 and parsed successfully but still contained 501 unique URLs; served Git blob d1a6b2e5ef801277b6e1d59c9ee996711ee17079 matches OLD source. Therefore source integration COMPLETE, host publication PENDING. Expected new XML blob is 90349c4c306794e6f77ef181bc13caad7a270080 containing exactly four approved URLs.

Next: after established host publication, fetch this sitemap and verify new blob/four exact approved URLs, then separately verify Google processing when GSC access is available. Do not repeat/recreate PR59 or report live repair/indexing recovery yet. No host deployment action or GSC submission performed. Future generator audit remains separate; do not run an old generator that repopulates the unverified catalogue.

Source checkpoint commit: 8d842ff3ab3ff7a9f354a0c9254eb7f62a8ddd25.

## 25 October 2026 — FCS-GSC-07 mentor sitemap host publication verified

Fresh required audits/handoff/checkpoints, main history and open PRs reviewed: main 8d842ff3ab3ff7a9f354a0c9254eb7f62a8ddd25; PR54/57/58 remain separate. No edits to those scopes and no repeated sitemap repair.

Public GET https://forskcodingschool.com/mentors/mentors-sitemap.xml returned HTTP 200 at the same URL. XML parsed successfully and contains exactly the four approved profile URLs: satnam-singh-java-backend-trainer-jaipur, shivanshi-paliwal-java-programming-trainer-jaipur, jayakshi-agrawal-data-analytics-trainer-jaipur, kirti-sharma-data-science-machine-learning-trainer-jaipur (all under /mentors/ with trailing slash). Computed Git blob 90349c4c306794e6f77ef181bc13caad7a270080 exactly matches the tested merged XML.

This supersedes the previous old-501-entry host-publication blocker. PR59 source merge 505818d7fa8dff58881186077b55526deee058f9 and host publication are now COMPLETE for this bounded sitemap fix. Earlier four destination HTTP/canonical/robots tests remain recorded separately. No deployment command, workflow revival, GSC submission or indexing request was performed. Google processing/indexing/traffic effects remain UNVERIFIED.

Next: check GSC processing when authenticated access is available; audit any mentor sitemap generator before running it to prevent reintroducing unverified catalogue entries. Continue other unfinished tasks without redoing this repair. Broader FCS-GSC-07 and FCS-GSC-01/02/03/04/05/06/08 acceptance gates are not closed by this result.

Source checkpoint commit: 75a4ae02197f63fff3c1f9a5e200ac0247b1e979.


## 25 October 2026 — FCS-GSC-07 publishing instructions regression guard

REVIEW: documentation-only PR60 https://github.com/satnamkhowal/forsk-coding-school/pull/60 on docs/mentor-publishing-20261025, head ab14cc1f4b5f6ec1ffbc697da6fcc19e49cf6e07. Fresh main 75a4ae02197f63fff3c1f9a5e200ac0247b1e979 and PR54/57/58 changed-file lists confirmed no overlapping ownership. Existing PR59 repair remains complete; not repeated.

Corrected mentors/README-MENTOR-PROFILES.txt, mentors/MENTOR-PROFILE-STRATEGY.txt and README-SITEMAP-PLACEMENT.txt: legacy verified=true alone is insufficient under includes/head.php's explicit approval guard; real-instructor-template.php derives that approval from approved_for_index. Old ZIP/catalogue/draft inventories must not overwrite the four-approved-profile sitemap. Root sitemap currently has eight children and does not include the separately submitted mentor sitemap.

Checks: documentation cross-checked with head.php blob 5637300f4a6b66665e1f87da08e48edfc6d72ff1, registry 1613a69b192a98a323551705b82568e252c6a92a, real instructor template and root sitemap 3612243865731ea35bdd85ad6ac671f576d675d4. GitHub compare confirms exactly three text files, no runtime/workflow/approval changes. PHP/render tests not applicable; no CI, deployment or GSC action. Targeted searches for mentors-sitemap.xml and generate mentors found no executable generator; this does not rule out an external generator.

Next: review PR60 before normal integration. Separately audit the 31 historical images-sitemap.xml page/image pairs against approved, indexable profile canonicals; existing placement instructions treated image existence as sufficient, which is not approval. No claim that these 31 entries have been validated. P0 loss-query/5xx/redirect examples remain blocked on authenticated GSC evidence; PR57/54 remain active independent scopes. Google processing/indexing/traffic recovery remains unverified.

Source checkpoint commit: 645d1d5ab42688279e315bec23f73708c4f86559.


## 25 October 2026 — FCS-GSC-07 image sitemap repair tested

REVIEW: PR61 https://github.com/satnamkhowal/forsk-coding-school/pull/61, branch fix/image-sitemap-approved-20261025, commit 92a47e2407027edce48ec33f8e9bd6424eb68bc4, XML blob bff5d91d32b4bed3e97e1037031be87760833a7e. Main checked at e74070622eb3726cf316f47a8100ed84c6786be3; required audits/handoff and PR54/57/58/60 file lists refreshed, no overlap. Earlier attempt stopped on usage-limit review failure before any remote edit; local files were absent, so no prior test completion was assumed.

Confirmed current source and served images-sitemap.xml match old blob 3b820e12a303d63daf94de56070b7dd2becfc578. All 31 listed profile URLs individually fetched: HTTP 200 and HTML noindex. None belongs to the four approved real instructor records. Replaced only this XML with four approved profile/portrait pairs selected from registry 1613a69b192a98a323551705b82568e252c6a92a (approved_for_index=true and photo_ready=true): Satnam Singh / assets/images/mentors/satnam_sir.webp; Shivanshi Paliwal / assets/images/mentors/shiib.jpg; Jayakshi Agrawal / assets/images/mentors/jaykshi.png; Kirti Sharma / assets/images/mentors/kiti.jpg. No identity claim, photo, page or publishing gate modified.

Tests PASS: XML parse; 31 distinct old URLs; four approved replacements disjoint from old set; four fresh profile GETs HTTP 200 unchanged URL, exact self canonical, indexable robots, no X-Robots-Tag exclusion. Each approved portrait occurs in its profile HTML and GET returns HTTP 200 unchanged URL with image content type. Pillow verify succeeds: WEBP 16500 bytes, JPEG 191854, PNG 864496, JPEG 149829 respectively. Curl/Python audit exited 0. PR reports exactly one changed file. No PHP/CI/browser-layout test applicable to XML-only patch; no workflow revival.

State: tested branch commit and draft PR only; review/integration pending, repaired host publication and GSC processing/indexing unverified. Live sitemap still old at pre-change check. Next: review PR61 exact diff, integrate via normal process, verify served blob/four pairs; then separately check GSC processing with authenticated access. PR60 documentation review remains separate. P0 query/error examples still await GSC evidence; PR54/57 active work remains untouched.

Source checkpoint: 1ffaabf4151ac6d903426c002f6ceb008414e568.


## 25 October 2026 — FCS-GSC-07 PR61 integrated; host pending

PR61 merged normally as 9be4c0cc2d4971340acd2ac6d3502543bd1b7b58, expected head 92a47e2407027edce48ec33f8e9bd6424eb68bc4. Fresh required audit/handoff/open-PR review and compare confirmed exactly images-sitemap.xml changed; the three newer main commits touched only checkpoints. Registry approval/photo flags remain at blob 1613a69b192a98a323551705b82568e252c6a92a and root index already references images-sitemap.xml.

Reviewed full XML and retained prior same-head page HTTP/canonical/robots/image-decode tests. This run repeated XML parse, four unique page/image pairs and exact blob check PASS (bff5d91d32b4bed3e97e1037031be87760833a7e). Local patch materialization initially added an extra trailing newline; normalized the temporary copy to source bytes and hash passed; remote code was unchanged. Separate COMMENTED review recorded 12 static checks, not an APPROVED review or release evidence. Its caution against merging on the comment alone was retained: integration used the existing approved registry, previous actual HTTP/image tests, current-main comparison and fresh exact-file checks. No review threads; marked ready, mergeable=true, then normal expected-head merge. No protections bypassed, CI claims or paused workflow changes.

Immediate post-merge public GET https://forskcodingschool.com/images-sitemap.xml returned HTTP 200, valid XML but 31 entries; Git blob 3b820e12a303d63daf94de56070b7dd2becfc578 matches OLD source. Source integration COMPLETE; repaired host publication PENDING. No deployment command or GSC action was performed; indexing/traffic effects unverified.

Next: verify established host publication serves expected bff5d91d32b4bed3e97e1037031be87760833a7e with four approved pairs, then GSC processing separately. Do not recreate PR61 or repeat its implementation. PR60 documentation review and other FCS-GSC acceptance gates remain open; PR54/57 ownership preserved.

Source checkpoint: 9a62c5b9356fe3c1c7e915d30a77734bc9cd800f.


## 25 October 2026 — FCS-GSC-07 image sitemap publication verified

Fresh required audits/handoff/checkpoint, main history and open PRs checked: main 043e47f6e7a91c31bf88ae9c839d66a1d73d7d6b; PR60/58/57/54 remain separate. No repeated implementation or edits to their scopes.

Public GET https://forskcodingschool.com/images-sitemap.xml returned HTTP 200 at the same effective URL. Python ElementTree parse and uniqueness assertions PASS: exactly four page/image pairs for Satnam Singh, Shivanshi Paliwal, Jayakshi Agrawal and Kirti Sharma. Served Git blob bff5d91d32b4bed3e97e1037031be87760833a7e exactly matches current main and the tested PR61 XML. This supersedes the earlier old-31-entry host-publication blocker.

Bounded PR61 source integration (merge 9be4c0cc2d4971340acd2ac6d3502543bd1b7b58) and host publication are COMPLETE. Earlier profile HTTP/canonical/robots and portrait decode checks remain recorded separately; no claim of a fresh full page/image re-audit. No deployment command, workflow revival, GSC submission or indexing request performed. Google processing/indexing/traffic effects remain UNVERIFIED.

Next: check GSC processing when authenticated access is available. Do not recreate or routinely repeat PR61. Continue unfinished queue, including PR60 documentation review, PR57 final-year QA and PR54 editorial validation within their existing ownership. FCS-GSC-07 overall and other audit acceptance gates remain open; completed image sitemap publication does not close them.

Source checkpoint: a3fe9c3684a4d6f3d406b11467a161f2ea945236.
