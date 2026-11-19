# Groot Academy 100K — Run139 coordination delta

**Observed:** 2026-11-20 00:43 IST  
**Central Main:** `70d500412703f605bc61354ab2c60188f06e15f9`  
**Source repository:** requested alias `satnamkhowal/gta` resolves to GitHub repository ID `1375760757`, current name `satnamkhowal/grootacademy.com`.  
**Source Main:** `0aa396859d3af70935280275b524a51dadc48868`  
**Canonical queue branch:** `content/groot-100k-controller-20261116-run61-main-delta` at `dffdf5677f95d9b9d903167c2fc2bac5b28c6205`.

## Verified deltas

### 1. One canonical queue, stale copies kept read-only

- Immutable planning queue blob: `c12a915e06c8100a350b21338311651df0f35094`, 29 ordered IDs.
- Active Run61 queue blob: `f8bd604cfe37d4b865f4ccf022ddd29e2d114694`, same 29 IDs/order; GA-B00005 is `CONTENT_QA`.
- Main historical queue blob: `a42107125efd657e21f29face2b3e0392c165376`, same IDs/order but stale statuses. Do not overwrite the active queue from Main.
- Run61 controller still pointed to the older active blob `0b0685b89c8833f9f8b49d7e223c166145082956`. Source Draft PR [#908](https://github.com/satnamkhowal/grootacademy.com/pull/908) corrects the checkpoint pointer and records the Run139 evidence; it is a docs-only child of source queue PR #817. It does not modify the queue.
- Source PR #817 and child #908 remain Draft/unreviewed. No second writable queue is introduced.

### 2. GA-B00005 source and visual branches are not yet reconciled

- Canonical Run61 companion blob `a6f1aab682486141374138bbdedcb63f9567ff11` stringifies raw keys. A focused Python 3.13.5 exact-source differential with integer `101` on one side and text `"101"` on the other reproduced a false-confidence `ok=True`.
- A strict type guard and regression suite exist in separate Draft PR [#907](https://github.com/satnamkhowal/grootacademy.com/pull/907), with parent chain #903 → #905 → #906. It reports `same_key_type=False` and the text key as unmatched. This is not integrated into the Run61 queue branch and has zero independent reviews.
- The generated featured WebP blob `751c9eeaba4fe89e84e88af7f71f2ffb82e4f32c` exists in the separate #886/#888/#907 candidate chain but is absent from the canonical Run61 GA-B00005 folder, although its metadata references it. The canonical branch has an authored SVG. No image was regenerated.
- Source owner should reconcile the exact code, tests, WebP, SVG, metadata and provenance once, after independent editorial/code/visual review. Do not copy or merge the separate candidate chain as if it were approved.

### 3. Current Main changed shared blog integration

Source Main advanced from Run61's last-observed `388e4a7058ce02897110b3ed114ccd441e2a5875` to `0aa396859d3af70935280275b524a51dadc48868` (42 commits ahead, 0 behind). Relevant paths changed:

- `blogs/_shared/blog-layout.php`
- `blogs/_shared/partials/head.php`
- root `head.php`
- `blogs/index.php`
- `includes/contextual-faqs.php`
- `assets/css/groot-contextual-faqs.css`

The current root head and shared blog partial each emit a base element and placement stylesheet; the partial also owns the unique contextual-FAQ stylesheet. The shared layout calls the contextual FAQ helper, which suppresses generated FAQs when the article already contains an FAQ heading. Draft PR #867's old patch removes duplicate base/placement references but also removes the unique FAQ stylesheet. It remains owner-controlled and has zero independent reviews. No central action should change source implementation; the Groot source owner must refresh it against current Main, preserve the unique CSS exactly once and obtain independent review before PHP candidate work.

### 4. Independent review and release status

Current review-submission checks returned zero on source PRs #755, #760, #778, #788, #840, #841, #843, #844, #867, #817, #886, #888, #903, #905, #906 and #907. Draft/source checks are not independent approval.

GA-B00005 remains CONTENT_QA; no PHP candidate, approval, registry/sitemap entry, publication or live verification. GA-B00006 remains in the historical recovery/PUBLISH_PR path with date-less/noindex, exact-Main PHP/schema/route/browser/accessibility/HTTP/MIME and release gates open. Azure Actions pre-step/log-storage `BlobNotFound HTTP 404` remains an administrator/storage-owner issue; no blind retry.

## Central coordination state

- Current Main README still registers eight brands but has only three active owner/status rows: Jaipur Engineers, Central coordination and Forsk Coding School. Groot Academy's dedicated P0 owner, canonical queue writer and independent release approver row is missing.
- PR #1 (Jaipur social), #2 (all-brand AEO/GEO) and #3 (coordination mapping/follow-ups) are merged. Reuse PR #2's existing AEO/GEO baseline; do not recreate its queue.
- Existing Central PR #41 is OPEN/DRAFT with zero reviews and is based on the previous Central Main head; it is not merged status. The current Main commit `70d5004` links the canonical source queue review PR.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. Preserve both workstream records; do not infer either repository is wrong.

## Owner boundaries and next action

| Workstream | Owner boundary | Exact next action |
|---|---|---|
| Groot 100K queue | Groot source controller | Keep Run61 as the only writable queue; independent review GA-B00005 and reconcile its separate code/image branches once |
| Shared blog integration | Groot source owner | Refresh/review #867 against current Main; preserve contextual FAQ CSS exactly once |
| GA-B00006 recovery | Existing source PR owners + independent reviewer | Complete #755 → #760/#778/#788 review sequence and exact-Main release gates |
| Azure Actions storage | Repository/admin storage owner | Diagnose BlobNotFound before any hosted retry |
| Central ownership row | Central coordinator | Record accountable Groot P0 owner, one queue writer and one independent release approver |
| Jaipur mapping | Existing Central mapping owner | Record production website, social repository and deployed-origin evidence separately |

No source implementation, queue, central README/control board, ownership assignment, merge, deployment, publication or indexing changed in this coordination delta. No other brand files were touched.


## Run140 delta — 2026-11-20 01:03 IST

- Reused the existing Groot 100K/P0 coordination lane and the merged AEO/GEO PR #2 baseline; no fresh multi-brand crawl or duplicate AEO/GEO audit was run.
- New source evidence: the OPEN/DRAFT Groot PR #908 queue candidate had one GA-B00005 row with 20 cells under its 19-column header. The current `validate_queue.py` used `csv.DictReader` but ignored the extra `None`-key cell. Groot Run140 repairs the candidate row, adds strict extra/missing/malformed CSV checks and six regression cases (6/6 coordinator-local PASS). The canonical Run61 PR #817 queue remains unchanged at blob `f8bd604cfe37d4b865f4ccf022ddd29e2d114694`; all 29 planning IDs/order remain intact. Source implementation and tests stay in the Groot repository; this central report records coordination only.
- Current source Main `0aa396859d3af70935280275b524a51dadc48868` is seven commits beyond shared-head PR #867's base `9821d9a39afa6bbd992e9a9e430d2f375c8553b1`. The exact PR #867 partial patch deletes only duplicate base and placement stylesheet references; it does not delete `groot-contextual-faqs.css`. This corrects the previous Run139 report wording. PR #867 remains owner-controlled, OPEN/DRAFT and unreviewed; current-Main refresh and rendered review remain pending.
- Central Main remains `70d500412703f605bc61354ab2c60188f06e15f9`. PR #1/#2/#3 remain merged; existing AEO/GEO PR #2 baseline is reused. Central PR #42 remains OPEN/DRAFT with independent review pending.
- The control board still lists eight brands but only three active owner/status rows; Groot's dedicated 100K/P0 accountable owner, canonical queue writer and independent release approver remain unrecorded. Jaipur Engineers `je2` social versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. No owner or repository was reassigned.
- No Central Main write, source implementation, merge, deployment, publication or indexing occurred.

**Next central action:** central owner records Groot's accountable P0 owner, canonical queue writer and independent release approver, while the existing source owners complete the GA-B00005 and shared-head review gates. Preserve the Jaipur mapping as unresolved until deployed-origin evidence is available.


### Run140 strict-base-queue correction

- A strict CSV parse of the actual Run61 PR #817 base blob `f8bd604cfe37d4b865f4ccf022ddd29e2d114694` fails at line 6 with `unexpected "M" after closing quote` in the GA-B00005 notes. The base queue is malformed; it was not changed in Run140.
- The prior Run139 report attributed blob `a056ec6d...` to the Run61 base. That blob was actually the PR #908 candidate. The repaired PR #908 candidate is now `7f0c005fec5cd2ad1e3691864019a97d480632f3`: strict CSV parse PASS, 29 rows, 19 fields per row, unique IDs and exact planning PR #62 order. It is the sole correction candidate, not yet canonical; independent review and owner-controlled integration remain pending.
- The queue validator now rejects extra/missing cells and malformed quotes; seven coordinator-local Python 3.13.5 regression tests pass 7/7. This is not a hosted Actions result or independent approval.
- No Central Main or canonical PR #817 base write occurred. Keep the single queue owner and do not create a second queue.
