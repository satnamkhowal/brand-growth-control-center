# News Factory checkpoint — 2026-11-09 18:42 IST

## Window

Differential cycle from the 2026-11-09 13:30 IST checkpoint through 18:42 IST. Research lanes were run as non-overlapping tracks: official student opportunities; React/frontend security and releases; Node.js/backend security releases; AI/cloud/developer announcements.

## New research verified

### NMMSS 2026-27 deadline extension — Groot Academy

- Current portal check: 2026-11-09.
- National Scholarship Portal's 2026-27 scheme list shows student applications open until **2026-11-15**, Institute verification until **2026-11-30**, and District/State verification until **2026-12-15**.
- Akashvani reported the Ministry's deadline extension on 2026-11-01 at 11:00 IST and says One-Time Registration (OTR) is required before applying.
- Scheme benefit: ₹12,000 per year through DBT; one lakh fresh scholarships nationally each year, subject to State/UT quota and selection.
- Eligibility details in the draft are cross-checked against the March 2022 revised scheme guidelines and the Ministry's 2025-26 notice: parental income ceiling ₹3.50 lakh; at least 55% in Class VII for the Class VIII selection test, with five-percentage-point SC/ST relaxation; government/government-aided/local-body school conditions and exclusions; renewal criteria. The article instructs Rajasthan/Jaipur families to check the current State/UT notice.
- Fee: no amount was stated in the official pages reviewed; draft says to confirm only on NSP.
- Draft: https://github.com/satnamkhowal/grootacademy.com/blob/content/news-factory-nmmss-20261109/docs/news-factory/drafts/nmmss-scholarship-2026-27-apply-by-15-november.md
- Original graphic: https://github.com/satnamkhowal/grootacademy.com/blob/content/news-factory-nmmss-20261109/docs/news-factory/media/nmmss-2026-27-application-checklist.svg (1200×675).
- Draft PR #577: https://github.com/satnamkhowal/grootacademy.com/pull/577 (open, draft, unmerged).
- Independent QA: PENDING. Not live.

### React Server Components October security advisories — Forsk Coding School

- Both advisories were published **2026-10-14**; this is explicitly a catch-up guide, not a new November disclosure.
- GHSA-xqc2-xf4c-x3h3: Critical unauthenticated RCE, CVSS 9.5; the advisory lists no CVE ID.
- GHSA-h3gv-c5rc-p453: High denial of service in Server Functions, CVSS 8.2.
- Affected packages: react-server-dom-webpack, react-server-dom-parcel and react-server-dom-turbopack.
- Patched package versions: 19.0.9, 19.1.10, 19.2.9 and 19.3.1. The draft distinguishes the affected ranges for each advisory and explains that apps without a server/RSC-supporting framework, bundler or plugin are not affected according to the advisories.
- Draft: https://github.com/satnamkhowal/forsk-coding-school/blob/content/news-factory-react-rsc-security-20261109/docs/news-factory/drafts/react-server-components-october-2026-security-fixes.md
- Original graphic: https://github.com/satnamkhowal/forsk-coding-school/blob/content/news-factory-react-rsc-security-20261109/docs/news-factory/media/react-rsc-october-2026-security-matrix.svg (1200×675).
- Draft PR #145: https://github.com/satnamkhowal/forsk-coding-school/pull/145 (open, draft, unmerged).
- Independent QA: PENDING. Not live.

## Watch items and no-draft decisions

- **Node.js:** official Node.js notice says security releases for the 26.x, 24.x and 22.x lines are expected on or shortly after 2026-11-11; highest severity is HIGH. Patched versions and detailed advisories are not yet disclosed, so no premature patch guide was drafted. Recheck after the official release.
- **Google Student Researcher 2027:** India-remote opportunity remains listed with application before 2026-12-04; it was already covered in the prior checkpoint and was not duplicated.
- **Frontend:** the React advisory/release catch-up is dated 14 October, not a new 9 November release.
- **AI/cloud/developer:** no new qualifying primary-source announcement in this window; no new draft.
- **YouTube:** no story-specific official/reputable original video ID verified; embeds = 0.
- **Licensed downloads:** 0. Two original editorial SVG graphics were authored in-repository; no public images or videos were copied.

## Repository and conflict checks

- Central coordination repository: satnamkhowal/brand-growth-control-center; existing coordination branch remains ops/news-factory-20261019.
- Forsk Coding School current main at branch creation: a690ef725029e8c7f96b6148e9012f82a481bd6d. The historical content/news-factory-20261019-1410 branch was compared with main and found diverged (77 ahead / 765 behind); it was not reused or modified. New work is isolated on content/news-factory-react-rsc-security-20261109. The task board and session handoff were updated on that branch. Existing PR #144's changed file was assets/css/local-fix.css; this editorial work does not touch it.
- Groot Academy current main at branch creation: 0648b79ee0775e810251192a61b8ae6d842980f4. Existing news-factory drafts were checked for duplicates. PR #569 owns marketing/blog-factory files and PR #560 owns docs/ai-ops/SESSION_HANDOFF.md; this new work is confined to docs/news-factory/drafts and docs/news-factory/media.
- No Mango Engineers or Jaipur Engineers write: no distinct accepted story was assigned to those repositories in this bounded cycle; their current repo instructions and work ownership were not overridden.

## Validation

- GitHub read-back confirmed all four new draft/media files exist on their isolated branches.
- Both SVGs parse as XML, include title and description, and declare 1200×675 dimensions. Rendered previews were inspected.
- Article first-pass source/date/version checks were performed; **independent QA is still pending**.
- No merge, deployment, live verification or publication was performed.

## Counts

| State | Cumulative |
|---|---:|
| Researched | 60 |
| Drafted | 50 |
| Original graphics | 50 |
| Independent QA-ready | 33 |
| Live | 0 |

## Next action

1. Obtain independent editorial/security QA for PR #145 and independent eligibility/deadline QA for PR #577; keep both drafts unmerged until review.
2. Recheck the NMMSS portal before any publication and change the article's application status after 2026-11-15.
3. Recheck Node.js after the scheduled 2026-11-11 security release and only draft once affected/patched versions are published.
4. Continue the four source tracks; do not syndicate these stories to other brands.
