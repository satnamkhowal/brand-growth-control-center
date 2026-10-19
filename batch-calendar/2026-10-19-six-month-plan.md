# Six-month daily course batch rollout — 19 October 2026

## Corrected owner instructions
The owner clarified the earlier eight-total interpretation: EVERY course has FOUR offline and EIGHT online batch starts every day. Monday and Tuesday were examples; the implementation applies the daily schedule seven days a week. The owner confirms facilities/backups and delegates exact times. Homepage cards, ongoing/upcoming lists and six months of course schedules are requested across the brand network.

The earlier M/W/F-only 78-date draft and empty eight-allocation table are superseded. No further technology allocation is needed: each applicable website's authoritative course catalogue supplies the course list.

## Scheduled times (Asia/Kolkata / IST)
| Mode | Daily session windows |
| --- | --- |
| Offline | 08:00–10:00; 11:00–13:00; 14:00–16:00; 18:00–20:00 |
| Online | 05:00–07:00; 07:00–09:00; 09:00–11:00; 11:00–13:00; 14:00–16:00; 17:00–19:00; 20:00–22:00; 22:00–23:59 |

Fixed horizon: 2026-10-19 through 2027-04-18 inclusive, 182 days. All weekdays are included. Per course: 728 offline + 1,456 online = 2,184 scheduled starts before expired starts or explicit closures are excluded. These are owner-authorized future intake schedules, not enrolments or proof of active cohorts. Session length is not course duration.

| Month | Covered dates | Days |
| --- | --- | --- |
| October 2026 | 19–31 | 13 |
| November 2026 | 1–30 | 30 |
| December 2026 | 1–31 | 31 |
| January 2027 | 1–31 | 31 |
| February 2027 | 1–28 | 28 |
| March 2027 | 1–31 | 31 |
| April 2027 | 1–18 | 18 |

## Implementation and evidence
All five source branches are isolated: feature/daily-batches-six-months-20261019. No main merge or production publication has occurred. This central repository contains coordination only.

| Brand | Source | Catalogue courses executed in PHP CI | Review | Calendar check |
| --- | --- | --- | --- | --- |
| Groot Academy | satnamkhowal/gta | 30 | https://github.com/satnamkhowal/gta/pull/132 | https://github.com/satnamkhowal/gta/actions/runs/39228738485 — PASS |
| Forsk Coding School | satnamkhowal/forsk-coding-school | 103 | https://github.com/satnamkhowal/forsk-coding-school/pull/37 | https://github.com/satnamkhowal/forsk-coding-school/actions/runs/39228742615 — PASS |
| Mango Engineers | satnamkhowal/mangoengineers.com | 29 | https://github.com/satnamkhowal/mangoengineers.com/pull/59 | https://github.com/satnamkhowal/mangoengineers.com/actions/runs/39228746427 — PASS |
| CadMate India | satnamkhowal/CadMateIndia | 25 | https://github.com/satnamkhowal/CadMateIndia/pull/4 | https://github.com/satnamkhowal/CadMateIndia/actions/runs/39228749739 — PASS |
| Jaipur Engineers | satnamkhowal/je2 | 61 | https://github.com/satnamkhowal/je2/pull/12 | https://github.com/satnamkhowal/je2/actions/runs/39228755536 — PASS |

Each adapter reads the existing catalogue dynamically; course names/slugs are not copied to a second registry. The narrow footer mount displays the module on the homepage and recognized course pages. /batch-calendar/ provides a full calendar. Scoped CSS, course/date/mode filters, six-card summaries, 24-card calendar pagination, contextual enquiry links, IST conversion and automatic expiry handling are implemented.

Ongoing support uses operator-confirmed active records with real start/end timestamps. ongoing.json starts empty because no actual current cohort record/end date was supplied. An elapsed intake does not automatically become an active cohort. The public empty state directs students to the course team. No current students, placements, seats, fees, capacities or branch addresses were invented.

The five adapters executed successfully against 248 existing registry entries in total. This count describes catalogue entries, not published batches. Home/course/standalone PHP render checks and six Node calendar tests passed in each source. Groot desktop/mobile browser checks are additionally running; their result must be recorded separately, not assumed from PHP checks.

## Remaining brands and publishing dependencies
| Brand | Remaining dependency | Current publication |
| --- | --- | --- |
| Clever Ape Academy | Source repo not found in installed-repository search. Confirm its actual source/deployment. | NOT PUBLISHED |
| Groot Software | Current candidate source contains service/article content; no authoritative training-course catalogue verified. Map actual training catalogue before extending schedule. | NOT PUBLISHED |
| Forsk Technologies | Existing source serves template/demo identity and no verified training-course catalogue. Coordinate with its identity/source owner. | NOT PUBLISHED |

For the five implemented sites, authorized custom-domain host deployment access is still required. Existing workflows inspected are validation workflows, not a production deployment path. A plugin search for Hostinger/hosting/SFTP found no applicable Hostinger website-deployment integration (Hostinger Mail is unrelated); no unrelated hosting migration or plugin connection was initiated. The separately hosted Groot learning-paths prototype is not treated as the production domain.

Jaipur's je2 source has explicit Jaipur Engineers Hostinger setup documentation and homepage/brand/course identity; implementation is isolated there. Older candidate mapping conflicts remain noted; no live deployed commit parity is claimed.

Mango's pre-existing architecture guard rejects the exact Google Search Console verification HTML file as though it were an unconverted page. Its batch-calendar/PHP checks pass. A narrow guard repair preserves and checks the exact token while continuing to reject other root HTML page sources; rerun result is tracked on the same PR. No verification token was removed.

## Exact continuation
1. Collect latest Groot browser and Mango architecture CI results; resolve any task-caused failures.
2. Integrate five narrow PRs through existing source coordinators, preserving the user's isolated-branch/no-main-merge workflow.
3. Use the existing authorized production host publishing path, then verify each homepage, one course page and actual /batch-calendar/ URL. Record deployed revision and live content.
4. Resolve remaining three brand course/source mappings and reuse the same component with each verified catalogue.
5. Populate actual ongoing cohort lifecycle records from the operator. Future scheduled starts are already specified; do not fabricate active cohorts or six-month course lengths.
