# Groot Academy public hub route sample 06–10 — coordination delta

Observed: 2026-11-11 03:36 IST  
Source implementation repository: `satnamkhowal/grootacademy.com` (alias `satnamkhowal/gta`)  
Coordination only: no central main or other brand source changes.

## Evidence

Groot's public [blog hub](https://grootacademy.com/blogs/) displays 60 guides. The next five destinations were retrieved individually:

| Card | Destination | Result |
|---:|---|---|
| 06 | [Spring Boot and Microservices Career Guidance](https://grootacademy.com/blogs/spring-boot-microservices-career-guide-jaipur/) | Content retrieved |
| 07 | [Software Technologies 2026](https://grootacademy.com/software-technologies-2026/) | Click-follow initially errored; direct canonical retry retrieved content |
| 08 | [How E-Commerce Websites Work](https://grootacademy.com/how-ecommerce-websites-work/) | Content retrieved |
| 09 | [Python Developer Roadmap](https://grootacademy.com/python-developer-roadmap/) | Click-follow initially errored; direct canonical retry retrieved content |
| 10 | [Frontend Developer Roadmap](https://grootacademy.com/frontend-roadmap-2026/) | Retrieved, but crawler says “crawled 2 months ago”; stale evidence |

The first-pass click-follow errors for cards 07 and 09 are not raw HTTP status evidence and must not be reported as confirmed 404s.

## Current-main source reconciliation

At Groot main `99336e8d0b412f6e0f0bdc0464e0aec4b8fea2b5`:
- All five slugs are in `blogs/_shared/blog-registry.php`.
- Card 06's `/blogs/` route is in `blogs/sitemap.xml`.
- Root-level cards 07–10 are in `sitemap-pages.xml`.
- The sitemap index references both sitemap families.

The split is correct; no sitemap or registry repair is indicated by this sample. Card 10's stale public snapshot shows an older WordPress-style page and an unverified “5000+ Students Trained” claim. Current-main PHP source exists with a 13 Oct 2026 modified date, but no fresh authorized-origin rendering was established. Do not reuse the stale claim or infer deployed parity.

Detailed source-repository evidence: [Groot QA report](https://github.com/satnamkhowal/grootacademy.com/blob/qa/groot-100k-current-main-20261109/marketing/blog-factory/work/B0002/qa/2026-11-11-public-hub-route-sample-06-10-0336-ist.md).

## Coordination boundary

- This route sample does not add a 100K article or queue ID.
- The canonical 29-ID queue and all current draft/approval/live counts remain unchanged.
- Groot release/recovery implementation remains in the Groot repository.
- Central PR #1/#2/#3 remain merged; reuse PR #2's existing AEO/GEO baseline and PR #3's four original follow-ups. No new baseline or duplicate follow-up was created.
- Central README still lists eight brands but only three active control-board rows; Groot's row remains a central-owner reconciliation item.
- Jaipur Engineers `je2` social vs `jaipur-engieneers` candidate website mapping remains unresolved; no ownership transfer or inference is made.

## Exact next action

Keep Master-owner P3/P0 and 10K/100K/M4 reconciliation plus existing PHP/schema/HTTP/recovery gates ahead of new article production. Continue a small cards 11–15 retrieval sample only after those blockers are checkpointed. Central main and other source repositories remain untouched.
