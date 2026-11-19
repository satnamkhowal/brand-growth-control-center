# Groot Academy 100K — Run 21 coordination delta

**Observed:** 2026-11-14 22:36 IST  
**Scope:** coordination-only delta on the existing cross-lane audit branch. No central Main, brand source Main, queue, ownership, deployment, publication, or indexing change.

## Verified source identity and controller state

- The requested legacy alias `satnamkhowal/gta` resolves to the canonical private repository `satnamkhowal/grootacademy.com`, repository ID `1375760757`. This is Groot Academy; no Mango Engineers repository was used.
- Original controller branch `content/groot-100k-controller-20261016` was read first. The active reviewed successor remains `content/groot-100k-controller-20261114-run16`, source PR #750, based on the run-13 controller parent. PR #750 is OPEN/DRAFT and unmerged.
- Source Main observed at `e1f629ecd0bffb9d3eafaaadbd6f5bf226950e6f`; latest observed commit changes `courses/index.php` only. No overlap with blog factory, shared blog head/layout, registry, sitemap, or controller paths.
- The canonical 100K queue remains 29 ordered IDs, SHA `c12a915e06c8100a350b21338311651df0f35094`. Counts remain 23 complete drafts, 23 technical visuals, 23 PHP candidates; component PASS 22 editorial / 18 code / 23 visual; fully approved / published / live verified 0 / 0 / 0. GA-B00014 remains a refresh, not a new article. New IDs/assets in this run: 0.

## New source release blocker: unsupported dates on recovery candidates

The five GA-B00006–GA-B00010 PHP pages at recovery PR #660 head `df9431cf47fe16b4a4854b27b36918181c722889` all set visible `display_date=November 1, 2026` and schema inputs `date_published/date_modified=2026-11-01`.

Original controller metadata for GA-B00006–GA-B00009 leaves both schema dates null. The expected GA-B00010 metadata path was not readable in this bounded pass, so its date provenance remains unknown. Current Main's shared blog layout prints `display_date`; the shared SEO partial emits `date_published/date_modified` into BlogPosting JSON-LD and article published/modified meta tags. The candidate dates therefore affect both visible page content and structured data.

The source controller's Run 21 report records the evidence and recommendation: remove all three fields until source-backed and owner-approved, or provide provenance and reconcile metadata; retain `noindex,follow`; add a null-date negative test to QA PR #664. A coordinator finding was posted on PR #660 (comment ID `6881275735`). It is not an independent review or release approval.

Source evidence: [Run 21 report](https://github.com/satnamkhowal/grootacademy.com/blob/content/groot-100k-controller-20261114-run16/marketing/blog-factory/work/B0002/qa/2026-11-14-ga100k-run21-recovery-date-metadata-consistency-2236-ist.md).

## Recovery stack and ownership boundary

Current-main comparisons from `e1f629e`:
- #507: 4 ahead / 35 behind; 22 recovery additions.
- #625: 7 ahead / 35 behind; four paths.
- #654: 9 ahead / 35 behind.
- #660: 19 ahead / 35 behind.
- #664: 32 ahead / 35 behind.
- #713: 12 ahead / 9 behind; four base-path repair paths.

The stacked parents remain mismatched: #654 base `68db39f` does not equal #507 head `72f24de`; #660 base `fc25231` does not equal #654 head `5bf6531`; #664 base `46dcc21` does not equal #660 head `df9431c`. Existing source owners must reconcile these branches and inspect intended-only diffs. No branch was rewritten here.

#625 and #713 share exactly three blobs (shared partial head `5d6b335c...`, PHP render fixture `94e3b855...`, Python test `935a48a1...`) but retain distinct Spoken English and blog-base-path workflows. Preserve both; integrate shared files once.

Azure Actions `BlobNotFound` remains a pre-step storage failure. No hosted assertions ran and no blind retry was attempted.

## Central coordination delta

- Central Main README blob `b93187c` still lists eight brands but only three active control-board rows; Groot Academy's dedicated active row remains missing. This unchanged board gap is not re-audited here.
- Central PRs #1/#2/#3 are merged. Existing AEO/GEO baseline PR #2 is reused; no duplicate baseline or task queue was created.
- Central PRs #17/#18/#20 remain OPEN/DRAFT, unmerged; their existing ownership and reports are preserved. This report is appended to the existing PR #20 cross-lane audit branch, not Main.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved with its existing central owner. No mapping or ownership was changed.

## Exact next action

1. Source owner resolves the unsupported date fields on #660 and adds the null-date regression to #664.
2. Source owners refresh #507/#625/#713 against current Main and reconcile #654 → #660 → #664 exact parent heads.
3. Administrator diagnoses Azure Actions storage before any retry.
4. Independent full GA-B00006 release review and hosted PHP 8.0/full-root/schema/route/browser/AT/HTTP/MIME gates remain required.
5. Central owner reviews the missing Groot active row and existing repository-role mapping through the existing coordination process; no source ownership transfer is implied.

No merge, deployment, publication, indexing, owner reassignment, or central Main write was performed.


## Follow-up — GA-B00006 optimized-mode regression evidence

The finished Python companion contains `assert` statements, which Python removes under `-O` and `-OO`. A separate coordinator-run harness now loads the exact companion and performs nine explicit checks that remain active in all modes. Python 3.13.5 results: 9/9 PASS in normal, `-O`, and `-OO`; `py_compile` passes for both files. This is coordinator-run evidence, not independent code approval.

- [Harness](https://github.com/satnamkhowal/grootacademy.com/blob/content/groot-100k-controller-20261114-run16/marketing/blog-factory/work/B0002/qa/ga-b00006-optimized-contract-check.py)
- [Updated source report](https://github.com/satnamkhowal/grootacademy.com/blob/content/groot-100k-controller-20261114-run16/marketing/blog-factory/work/B0002/qa/2026-11-14-ga100k-run21-recovery-date-metadata-consistency-2236-ist.md)
