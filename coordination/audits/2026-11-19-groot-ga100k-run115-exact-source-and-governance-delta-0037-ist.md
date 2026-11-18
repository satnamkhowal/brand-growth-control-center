# Groot Academy 100K — Central coordination delta, Run 115

**Observed:** 2026-11-19 00:37 IST  
**Central Main:** `21af139cc32a7b67aab6908c61edeb5998bd4544`  
**Parent:** Central PR #31 head `ac5e01e3f19e298b4c966270e8d43c3770ae45b7`  
**Scope:** coordination evidence only; no Central Main or other-brand source changes.

## Verified source delta

- Canonical source repository is `satnamkhowal/grootacademy.com` (requested alias `satnamkhowal/gta`, repository ID 1375760757); brand remains Groot Academy, not Mango Engineers.
- Source Main is `9821d9a39afa6bbd992e9a9e430d2f375c8553b1`. Since shared-head PR #867's merge base `c3c7f6a`, the two Main-only commits modify only `includes/alumni-cards.php` and `includes/alumni-data.php`; no overlap with the four source repair paths.
- Source PR #867 remains OPEN/DRAFT at `07bf832`, 9 ahead / 2 behind current Main, four intended files, zero independent reviews/threads. Exact-source local evidence: five Git blob matches, PHP 8.4.24 syntax 4/4, Python 3.13.5 rendered tests 2/2, duplicate-base negative control 2/2 rejected, duplicate stylesheet with differing cache query 2/2 rejected. This is not PHP 8.0 hosted CI or independent approval. Exact-head Actions still fails before steps with Azure BlobNotFound HTTP 404.
- GA-B00006 recovery PR #507 remains OPEN/DRAFT at head `72f24de4`, recorded base `9c90902f`; compare to Main `9821d9a` is 4 ahead / 82 behind, 22 original additions / 0 deletions. Owner refresh required; dependent #654 → #660 → #664 remains owner-controlled.
- GA-B00006 exact PHP/metadata contract has four genuine mismatches: robots, date_published, date_modified and display_date. Featured-image ALT matches. Preserve PR #755's date-less/noindex contract; PRs #755/#785/#813 have zero independent reviews. No source-owner metadata change is authorized until #755 is independently reviewed.
- Existing Python examples and authored SVG are complete; no asset regeneration or new article occurred.

## Queue and release accounting

- Original queue `c12a915e` and active canonical queue `0b0685b8` both contain the same 29 unique ordered IDs GA-B00001–GA-B00029. Active queue remains authoritative; zero queue writes.
- Ledger remains 23 complete drafts / 23 technical visuals / 23 PHP candidates; independent editorial/code/visual PASS 22/18/23; fully approved/published/live 0/0/0.
- Queue IDs, research proposals and GA-B00014 refresh are not finished articles.

## Central governance delta

- Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`; README still lists eight brands but only three active owner/status rows. Groot Academy's dedicated 100K/P0 accountable owner, canonical queue writer and independent release approver are not recorded.
- Central PR #31 remains OPEN/DRAFT with zero independent reviews; this report is a coordination-only child of its exact head. PR #30 remains the parent chain. PRs #1/#2/#3 are merged; reuse the existing AEO/GEO PR #2 baseline.
- Safety PR #28 remains OPEN/DRAFT. The unsafe merge-all workflow is still on Main and was not dispatched.
- Jaipur Engineers `je2` social vs `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved; no assumption is made that either repository is incorrect.

## Owner actions / exact continuation

1. Source reviewer independently reviews PR #867; Actions administrator diagnoses BlobNotFound before any PHP 8.0/Python 3.12 retry.
2. Recovery owner refreshes #507 against Main `9821d9a`, then aligns #654 → #660 → #664 to exact preceding heads.
3. Independent reviewer reviews PR #755's date-less/noindex contract; only then may the source owner reconcile the four PHP/metadata mismatches and request rendered shared-schema review.
4. Complete full-root PHP/schema/route/browser/accessibility/HTTP/MIME gates. Keep all five recovery pages out of registry/sitemap and noindex until approval.
5. Central owner records one accountable Groot 100K/P0 owner, one canonical queue writer and one independent release approver. Keep new IDs/batches HOLD until the governance decision is explicit.

No ownership reassignment, Central Main write, other-brand implementation, merge, deployment, publication or indexing.
