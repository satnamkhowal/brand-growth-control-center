# Central coordination delta — Groot Academy 100K, Run 107

**Observed:** 2026-11-18 16:44 IST  
**Scope:** coordination-only delta on the existing Groot audit PR #30 branch. No Central Main write, no other-brand source change, no ownership reassignment and no repeated all-brand crawl.

## Central baseline and existing ownership

- Current Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; Main README blob `b93187c353f8112a57fffab4b383e64236976394`.
- Main lists eight brands but only three active control-board rows. Groot Academy still has no dedicated 100K/P0 accountable owner row, canonical queue writer or independent release approver.
- PR #1 (Jaipur social), #2 (AEO/GEO baseline) and #3 (coordination audit) are CLOSED/MERGED. Reuse PR #2's existing baseline; do not recreate its crawl or queue.
- Existing coordination PR #17 (Groot repository-alias/release-blocker delta) and PR #27/#28/#29/#30 remain OPEN/DRAFT. PR #28's unsafe merge-sweep removal is not merged; the workflow remains on Main and was not triggered.
- Jaipur Engineers `je2` social vs `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. Preserve both workstreams and their owners; no repository role is inferred.

## Groot source delta

The supplied alias `satnamkhowal/gta` resolves to the same GitHub repository ID `1375760757`, currently named `satnamkhowal/grootacademy.com`.

Existing source QA PR [#855](https://github.com/satnamkhowal/grootacademy.com/pull/855) was repaired on its existing two-file QA branch; no third overlapping code branch was created. Current source head: `424ced6f0b708b776b5750bcaa1d5008d8614366`.

- Four source commits extend `_json_ld_root_objects()` to traverse nested node objects used as ordinary property values and supported graph/included/reverse/list/set/map containers.
- `@nest` is treated as properties of the same node; `@value` JSON literal payloads are not traversed; `@propagate:false` and explicit child contexts are preserved; unsupported custom map containers/contexts fail closed.
- Ten regression methods were added to the same two existing QA files.
- Python 3.13.5 focused differential using exact committed helper bodies: **10/10 PASS**.
- Full committed suite, conforming JSON-LD processor, PHP 8.0 and independent review remain NOT RUN/PENDING.
- PR #855 remains OPEN/DRAFT with 0 independent reviews / 0 review threads. Non-approval handoff: [source PR comment 6977210385](https://github.com/satnamkhowal/grootacademy.com/pull/855#issuecomment-6977210385).
- Exact-head Actions run [44294294245](https://github.com/satnamkhowal/grootacademy.com/actions/runs/44294294245), job `134767159338`, failed before steps (`steps: []`, no log URL). Direct log fetch returned Azure `BlobNotFound` HTTP 404 at `2026-11-18T11:26:26.3231643Z`; hosted assertions 0. Administrator diagnosis required; no retry.

## Main, GA-B00006, queue and ledger

- Source Main is `f9c900e64baa3979e50c04e7293e246369e8f4b5`. Its latest commit changes four alumni-only paths (`assets/css/groot-alumni.css`, `includes/alumni-cards.php`, `includes/alumni-profile.php`, `index.php`); no blog/factory/queue/registry/sitemap overlap.
- GA-B00006 remains `PUBLISH_PR`, not approved or live. Recovery PR #507 is OPEN/DRAFT at `72f24de4`; direct compare to current Main is 4 ahead / 49 behind with 22 original article/companion paths and 0 independent reviews. Content repairs #782/#785 and date-contract prerequisite #755 remain Draft/unreviewed; four PHP/metadata differences and exact-Main release gates remain.
- Original and active canonical queues retain the same 29 ordered IDs GA-B00001–GA-B00029. Active writable queue SHA remains `0b0685b89c8833f9f8b49d7e223c166145082956`; no queue write.
- Ledger remains 23 complete drafts / 23 technical visuals / 23 PHP candidates; independent editorial/code/visual PASS 22/18/23; fully approved/published/live verified 0/0/0. Planning PR #62's 29 IDs and Research PR #68's 14 proceed proposals plus GA-B00014 in-place refresh remain preserved; none are counted as extra finished articles.
- No new article, image, PHP candidate, registry entry, sitemap URL, deployment, publication or indexing.

## Existing owner actions

1. Independent reviewer evaluates source PR #855 and its #840/#853/#849/#848/#847 ancestry, plus #755's date-less/noindex contract.
2. GitHub Actions/storage administrator diagnoses Azure BlobNotFound before any retry; then the source owner runs the full committed suite, a conforming JSON-LD processor and PHP 8.0 on a healthy runner.
3. Source owner refreshes #507 against current Main and preserves #507→#654→#660→#664 plus #782/#785; reconciles GA-B00006 metadata and completes exact-Main PHP/schema/H1/canonical/robots/route/registry/sitemap/browser/accessibility/HTTP/MIME gates.
4. Central owner records one accountable Groot 100K/P0 owner, one canonical queue writer and one independent release approver. Keep new IDs/batches HOLD until governance and evidence-based batch criteria are resolved.
5. Existing central mapping owner resolves Jaipur repository/deployed-origin roles using explicit evidence; no assumption that either repository is wrong.

This report changes coordination evidence only. No Central Main change, source ownership reassignment, self-approval, merge, deployment, publication or mass indexing.
