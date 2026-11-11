# Groot Academy public hub cards 21–25 — central coordination delta

**Observed:** 11 November 2026 06:42 IST  
**Source repository:** `satnamkhowal/grootacademy.com` (legacy alias `satnamkhowal/gta`, repository ID 1375760757)  
**Source main:** `99336e8d0b412f6e0f0bdc0464e0aec4b8fea2b5`  
**Central main:** `f76c20abf6c1ea6c45de073c5acbcd936333098c`  
**Central review branch:** `audit/groot-100k-crosslane-20261110-1443`

## New bounded evidence

The public Groot Academy blog hub lists 60 guides. Cards 21–25 were opened directly (5/5 readable content retrieval). Current-main source checks found:

- Root-level PHP sources using the shared blog layout: 5/5.
- Exact registry keys: 5/5.
- `sitemap-pages.xml` entries: 5/5.
- `.htaccess` route/canonical rule groups: 5/5.
- `blogs/sitemap.xml` entries: 0/5, expected for these root-level pages.

Cards 23 and 24 initially returned click-follow retrieval errors, but exact URLs opened successfully. Do not classify those first attempts as route 404s.

## Repair finding

One genuine broken internal link was found in card 23, the Open Source Contributions guide:

- Old href `/software-development-coding-career-guide-jaipur/` returned a public 404.
- Correct canonical `/blogs/software-development-coding-career-guide-jaipur/` is reachable.
- The destination PHP file exists at `blogs/software-development-coding-career-guide-jaipur/index.php`.
- A one-line source correction and focused regression test are in Groot [PR #614](https://github.com/satnamkhowal/grootacademy.com/pull/614), OPEN/DRAFT. The local fixture regression assertions passed 3/3. No production merge/deployment is claimed.

Card 25's public crawler snapshot is two months old and displays an older WordPress-style heading and a historical `5000+ students trained` claim. Current-main PHP source instead uses the shared blog layout and newer metadata. Treat the crawler snapshot as stale; do not reuse its old count claim or infer deployed parity from it.

Detailed source evidence: [Groot route sample 21–25 report](https://github.com/satnamkhowal/grootacademy.com/blob/qa/groot-100k-current-main-20261109/marketing/blog-factory/work/B0002/qa/2026-11-11-public-hub-route-sample-21-25-0642-ist.md).

## Coordination-only status

- Central main README still lists eight brands and three active control-board rows; Groot's active row remains missing.
- Existing central PRs #1/#2/#3 and PR #2's AEO/GEO baseline are reused; no duplicate baseline or follow-up created.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved; no ownership transfer is inferred.
- Groot canonical queue remains 29 IDs; 23 complete original drafts, 23 technical visuals, 23 PHP candidates, 18 independent code passes, independent approvals 0, published 0, live-verified 0. No queue row or count changed.
- Groot PR #569 remains a separate OPEN/DRAFT controller/review branch requiring owner-led base reconciliation and independent review. PR #614 is a separate, narrowly scoped source repair. Central does not take source ownership.

## Boundaries and next action

Public content retrieval and GitHub source mapping do not establish raw origin HTTP/MIME, served canonical/robots, rendered JSON-LD, deployed bytes or Search Console indexation. Container DNS still cannot resolve `github.com` or `grootacademy.com`; origin-level checks remain blocked.

Central owner: independently review PR #20 and reconcile the missing Groot active control-board row without taking over source ownership. Reuse PR #2's AEO/GEO baseline and PR #3's existing follow-ups. Groot owner: independently review PR #614, keep 100K release gates and the canonical queue intact, and preserve the Master priority/capacity hold before any new batch.

No central main, other-brand source, Groot main, queue, deployment, publication or indexing changes. No self-approval or self-merge.


## CI runner/log artifact delta — 11 November 2026, 06:42 IST

- Groot PR #614 workflow run [42938984790](https://github.com/satnamkhowal/grootacademy.com/actions/runs/42938984790) and PR #569 runs [42939224874](https://github.com/satnamkhowal/grootacademy.com/actions/runs/42939224874) / [42939225079](https://github.com/satnamkhowal/grootacademy.com/actions/runs/42939225079) concluded failure.
- Each job exposed `steps: null`; downloading job logs returned Azure `BlobNotFound`. No assertion-level result is available. Do not call this a code/test failure or PASS without logs.
- Repository Actions/storage administrator diagnosis is required; no blind retry. PR #614 remains a narrow source fix Draft; PR #569 remains a separate controller Draft. Source ownership stays in Groot Academy. Central main and other brand repositories are untouched.
