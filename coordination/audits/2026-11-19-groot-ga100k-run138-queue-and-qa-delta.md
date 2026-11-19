# Groot Academy 100K — Run138 coordination delta

**Observed:** 2026-11-19 23:37 IST  
**Source repository:** `satnamkhowal/grootacademy.com` (requested alias `satnamkhowal/gta` resolves to the same repository ID 1375760757)  
**Source review:** [PR #907](https://github.com/satnamkhowal/grootacademy.com/pull/907), OPEN/DRAFT, child of Run137 PR #906  
**Coordination base:** Central PR #40 exact head `f8c710cb25721817666019d3e7caca673f74e5e8`

## Bounded source evidence

- GA-B00005 Run138 closes three reproduced false-positive/false-negative cases in the Python relationship-key preflight: signaling Decimal NaN, a very large finite Decimal and an arbitrary hashable custom object.
- Exact source blobs for `examples.py` and `test_examples.py` match the coordinator's executed files. Python 3.13.5: 28/28 tests pass in normal, `-O`, and `-OO`; example output and compilation pass.
- Independent editorial/code/visual review remains pending. No PHP candidate, approval, publication, deployment or indexing.
- Source implementation remains in the Groot Academy repository. No other brand source files changed.

## Canonical queue ownership and branch-copy drift

- Immutable planning queue: `content/groot-100k-controller-20261016`, blob `c12a915e...`, 29 ordered IDs.
- The only writable canonical queue remains Run61 branch `content/groot-100k-controller-20261116-run61-main-delta`, blob `f8bd604c...`; GA-B00005 is `CONTENT_QA`.
- Run137/Run138 source branch contains a read-only stale queue snapshot blob `0b0685b8...`; it still shows GA-B00005 `IDEA`. The controller's `queue_integrity` now explicitly labels it read-only and points to Run61 as the canonical writer.
- No queue rows were written in Run138. All 29 IDs and order remain preserved.

This resolves the apparent status discrepancy without creating a second writable queue or overwriting historical planning state.

## Current integration and coordination state

- Source Main: `0aa396859d3af70935280275b524a51dadc48868`.
- Shared-head PR #867 is 10 ahead / 7 behind, OPEN/DRAFT, four intended paths, zero independent reviews/threads, mergeable=false. Owner refresh must remove only the duplicate partial base/placement CSS and preserve the current unique contextual FAQ stylesheet. Existing owner handoff #7015022569 has no response; no owner branch was edited.
- Azure Actions Run137 workflow 44580840154 failed before steps with `BlobNotFound` HTTP 404; hosted assertions 0. Administrator/storage-owner diagnosis is required before retry.
- Central Main remains `70d500412703f605bc61354ab2c60188f06e15f9`; README blob `b93187c3...`. PRs #1/#2/#3 are merged; the existing AEO/GEO baseline PR #2 is reused. Central PRs #39/#40 remain OPEN/DRAFT with zero independent reviews/threads.
- README lists eight brands. Its active control board has P0 rows for Jaipur Engineers, Central coordination and Forsk Coding School; Groot Academy's 100K/P0 accountable owner, canonical queue writer and independent release approver remain unrecorded.
- Jaipur Engineers `je2` social repository versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. No assumption or ownership transfer.

## Ledger

24 complete drafts / 24 technical visual packages / 23 PHP candidates. Independent editorial/code/visual PASS 22/18/23. Fully approved / published / live verified 0/0/0.

No Central Main change, no AEO/GEO recreation, no other-brand implementation, no merge, deployment, publication or indexing.
