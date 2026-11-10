# Groot Academy — GA-B00016 browser evidence delta

**Date:** 10 November 2026, 17:22 IST  
**Source repository:** `satnamkhowal/grootacademy.com` (same Groot Academy repository formerly addressed as `satnamkhowal/gta`)  
**Implementation PR:** [#569](https://github.com/satnamkhowal/grootacademy.com/pull/569)

## New source evidence

The existing GA-B00016 local HTML lab was rechecked against exact Git source identity:

- Git blob SHA-1: `1e6832c50d3416fabfea7cb90c81c34202e20254`
- SHA-256: `3368e946adb76cbe297f5853a0efcd351e01b3aee6b9790e812bd2d6c6fe61b0`
- Headed Chromium 144 / Python Playwright 1.57 / Xvfb / XTest: real desktop browser zoom at 200% and 400%, 12/12 assertions PASS.
- Measurements: DPR 2/4, `innerWidth` 640/320, `visualViewport.scale=1`; corrected row fits, long token wraps, and keyboard focus reaches the final link with a visible 3px outline.
- Previously recorded exact-source viewport/layout+keyboard evidence: 40/40; CSS-viewport reflow: 18/18. These are distinct local-lab runs.

The article and metadata in the source PR branch were corrected because they still claimed Chromium was unavailable and real zoom was untested. The implementation checkpoint commit is [83dea057](https://github.com/satnamkhowal/grootacademy.com/commit/83dea0576b33abe027481f12ae026ecd2372e90e); the complete article/metadata/README/report commits are linked from that branch history.

## State and limitations

- GA-B00016 remains `CONTENT_QA`; this is not independent editorial/browser/release approval.
- Tests load the exact lab with local `page.set_content`; production-page navigation, live HTTP/MIME, PHP/schema, registry/route and deployment remain unverified.
- No new article, image, queue ID, route, registry entry, publication, merge or deployment.
- Factory counts unchanged: 29 canonical IDs, 23 complete drafts, 23 visuals, 23 PHP candidates, 18 independent code passes, approved 0, live 0.

## Coordination

- Source implementation remains exclusively in the Groot Academy repository.
- Central PR #20 is the coordination-only audit successor; this file is appended on its existing isolated branch, not central `main`.
- Central PR #1/#2/#3 remain merged. Existing AEO/GEO baseline from PR #2 is reused.
- The central control board still lacks a Groot active row; HAO-008 is P3/REVIEW while the user's controller remains P0. No priority/ownership override was made.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website mapping remains unresolved; this delta does not assume either is incorrect.

**Next action:** continue GA-B00029 full-root PHP and authorized-origin HTTP/MIME gates, then obtain independent PR #569/recovery review. No new batch or GA-B00005 brief until the Master owner resolves HAO-008 priority and queue disposition.
