# Groot Academy public hub cards 11–15: coordination-only delta

Observed: 2026-11-11 04:36 IST  
Source repository: `satnamkhowal/grootacademy.com` (repository ID `1375760757`; requested `satnamkhowal/gta` alias)  
Source main: `99336e8d0b412f6e0f0bdc0464e0aec4b8fea2b5`  
Central main: `f76c20abf6c1ea6c45de073c5acbcd936333098c` (latest observed)

## New evidence

A bounded public-hub sample opened cards 11–15. All five exact displayed destinations returned readable article content with visible H1, category and update date. Current-main source checks found 5/5 registry entries and 5/5 `sitemap-pages.xml` entries; 0/5 in `blogs/sitemap.xml` is expected because these are root-level routes.

- Card 11: Java vs Python comparison — https://grootacademy.com/java-vs-python-which-language-should-you-learn-first/
- Card 12: AI chatbot architecture — https://grootacademy.com/ai-chatbot-development/
- Card 13: cloud software-development guide — https://grootacademy.com/cloud-in-software-development/
- Card 14: DBMS in applications — https://grootacademy.com/database-management-guid/
- Card 15: website login systems — https://grootacademy.com/website-login-system-guide/

Card 13's initial crawler click-follow returned 403, but direct exact-URL retrieval succeeded; this is not a confirmed origin HTTP 403. Card 15's click-follow snapshot was one week old, while a direct URL open retrieved readable content today. Neither proves raw HTTP status, redirect headers, served canonical/robots, rendered schema, deployed bytes or Search Console indexation.

Card 12 is the existing `/ai-chatbot-development/` URL covered by GA-B00014's in-place REFRESH. It is not a new article or a new 100K queue ID. The established `database-management-guid` slug should not be duplicated with a corrected spelling absent an owner-reviewed redirect/canonical plan.

Detailed source-lane report: https://github.com/satnamkhowal/grootacademy.com/blob/qa/groot-100k-current-main-20261109/marketing/blog-factory/work/B0002/qa/2026-11-11-public-hub-route-sample-11-15-0436-ist.md

## Coordination status (delta-only)

- The requested `gta` alias still resolves to repository ID 1375760757 / `grootacademy.com`; implementation remains in the Groot source repository.
- Central main and its README/audit mapping were not changed. Existing PR #1/#2/#3 remain merged; PR #2's AEO/GEO baseline is reused, not recreated.
- Existing central mapping gaps remain with their owners: README has eight listed brands while the active control board has three rows (Groot row absent); Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website/deployed-origin reconciliation remains unresolved. No ownership was reassigned.
- Central PR #20 remains a draft coordination-only review branch with no independent review at this checkpoint.

## Release and accounting boundary

- No article, bitmap image, queue ID, production route, registry, sitemap, deployment or publication change.
- Canonical queue remains 29 unique IDs; complete drafts 23; independent approvals 0; published/live-verified factory articles 0.
- This public sample is existing-site discovery/content evidence, not a factory completion count.
- Master-owner priority alignment, GA-B00029 full-root PHP/schema/authorized-origin HTTP gates, Actions/storage administrator diagnosis, PR #533/#569 owner reconciliation and GA-B00016/GA-B00022 independent accessibility/release gates remain open.

No source implementation, central main, other brand repository, merge, deployment, public publishing or indexing was changed by this coordination delta.
