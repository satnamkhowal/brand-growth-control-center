# Groot Academy public hub cards 16–20 — central coordination delta

**Observed:** 2026-11-11 05:37 IST  
**Source repository:** `satnamkhowal/grootacademy.com` (legacy alias `satnamkhowal/gta`, repository ID 1375760757)  
**Source main:** `99336e8d0b412f6e0f0bdc0464e0aec4b8fea2b5`  
**Central main:** `f76c20abf6c1ea6c45de073c5acbcd936333098c`  
**Central review branch:** `audit/groot-100k-crosslane-20261110-1443`

## New bounded evidence

Groot Academy's current public blog hub lists 60 guides. Cards 16–20 were retrieved from their displayed destinations (5/5). The exact current-main source check found:

- Root-level PHP files: 5/5.
- Blog registry entries: 5/5.
- `sitemap-pages.xml`: 5/5.
- `.htaccess` route/canonical rules: 5/5.
- `blogs/sitemap.xml`: 0/5, expected for these root-level routes.

Card 20's click-follow reader attempt errored, but the exact URL without the trailing slash loaded the article. Treat this as a retrieval fallback, not a confirmed HTTP 404. All five topics have distinct learner tasks: internship evaluation, technical resume evidence, fresher skill sequencing, responsible AI-assisted engineering and browser foundations. No source correction, new GA-B ID or refresh was warranted.

Detailed evidence remains in the Groot source repository: [route sample 16–20 report](https://github.com/satnamkhowal/grootacademy.com/blob/qa/groot-100k-current-main-20261109/marketing/blog-factory/work/B0002/qa/2026-11-11-public-hub-route-sample-16-20-0537-ist.md).

## Coordination-only status

- Central main README still lists eight brands and three active control-board rows; Groot's active row remains missing.
- Central PRs #1/#2/#3 remain merged; reuse the existing all-brand AEO/GEO baseline from PR #2.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved; no ownership transfer is inferred.
- Central main's latest observed commit is `f76c20a`, the corrective revert removing the accidentally written draft audit; no source or central-main change was made by this run.
- Central PR #20 remains open/Draft. Current compare is 24 commits ahead / 2 behind main, with 17 audit files; submitted reviews 0 and review threads 0. This is a review queue, not approved central policy.
- Groot PR #569 remains a separate open Draft requiring owner-led base reconciliation and independent review. Source implementation stays in Groot Academy's repository.

## Boundaries and next action

Public content retrieval and GitHub source mapping do not establish raw HTTP status, served canonical/robots, schema validity, deployed bytes or Search Console indexation. The current execution container cannot resolve `github.com` or `grootacademy.com`, so origin-level tests remain blocked.

Central owner: independently review PR #20 and reconcile the missing Groot active control-board row without taking over source ownership. Existing central AEO/GEO and PR #3 follow-ups are reused, not recreated. Groot owner: retain the 100K queue and release gates; no new batch before the documented Master priority/capacity alignment and existing technical blockers.

No central main, other-brand source, queue, publication, deployment or indexing changes. No self-approval or self-merge.
