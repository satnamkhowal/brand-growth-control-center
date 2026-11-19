# Central coordination delta — Groot Academy 100K Run 128

Observed: 2026-11-19 13:37 IST

## Scope and ownership
Coordination-only successor to Central PR #34. Source implementation remains in `satnamkhowal/grootacademy.com`; requested alias `satnamkhowal/gta` resolves to the same repository ID 1375760757. This report does not reassign owners or change Central Main.

## Source-side delta
- Current Groot Main is `f1b9033815baebf372c8d05760d6f7f9622b546b`.
- Main's current FAQ-aware shared blog layout/head differs from the prior recovery base. The shared blog layout calls the contextual FAQ helper; the helper suppresses generated FAQs when the article already has a FAQ heading.
- Current nested blog head still emits duplicate base and placement stylesheet tags because root `head.php` emits the authoritative versions. Source PR #867 is OPEN/DRAFT, 10 ahead / 2 behind current Main, four intended files, zero independent reviews. Its refresh must preserve the new contextual FAQ stylesheet.
- Historical recovery PR #507 is OPEN/DRAFT, 5 ahead / 2 behind current Main, 22 original additions, zero independent reviews. Intrinsic image sizing PR #654 is exactly two intended shared-layout files relative to #507 and must be ported onto the current FAQ-aware layout after #507 refresh.
- GA-B00006 metadata PR #868 is OPEN/DRAFT, a one-file child of #785, with `noindex,follow` and no display/published/modified dates. Reviews: 0. The #755/#760/#778/#788 date/parser gates remain independently unreviewed.
- GA-B00005 code repair PR #884 and provenance/checkpoint PR #888 remain Draft/unreviewed; existing article and visuals were reused, not regenerated.

Source checkpoint: [Run 128 report and source PR #890](https://github.com/satnamkhowal/grootacademy.com/pull/890).

## Queue and production accounting
- Canonical queue remains `content/groot-100k-controller-20261116-run61-main-delta`, blob `d1f700f12ffe0fcf323f2d2b8dd67b1bfc959102), 29 unique ordered IDs.
- GA-B00005 remains RESEARCH; GA-B00006 remains PUBLISH_PR. Run 127's `0b0685b` queue copy is stale and untouched.
- Planning PR #62's 29 IDs remain preserved. Research PR #68 still represents 14 proceed proposals plus the GA-B00014 in-place refresh; these are not finished articles.
- Carried-forward ledger: 24 complete drafts / 24 technical visual packages / 23 PHP candidates; independent component PASS 22/18/23; fully approved/published/live 0/0/0. No new article, image or PHP candidate in Run 128.

## Central Main and governance
- Central Main remains `21af139cc32a7b67aab6908c61edeb5998bd4544`, unchanged.
- Central PR #1/#2/#3 are merged; reuse the existing AEO/GEO PR #2 baseline. PR #33 and #34 remain OPEN/DRAFT with zero independent reviews. PR #28's unsafe merge-all workflow remains Draft and was not dispatched.
- Central README still lists eight brands but only three active owner/status rows; Groot Academy's dedicated 100K/P0 owner row, canonical queue writer and independent release approver are not recorded.
- The Jaipur Engineers `je2` social workstream versus `jaipur-engieneers` candidate website/deployed-origin mapping remains unresolved. Do not assume either repository/workstream is wrong based only on a name or rename.
- Groot Main's `MASTER-PLAN.md` still says 10,000 possible IDs, not validated opportunities; `MASTER_TASK_BOARD.md` keeps Blog Factory P3/hold and HAO-008 P3/REVIEW. The user-authorized 100K/P0 target remains explicit, but Master-owner alignment and batch-growth criteria are missing. New IDs/batches remain HOLD.

## Next actions
1. Source owners refresh #867 and #507 to current Main, preserve FAQ behavior and original payloads, then reconcile #654 and the existing child stack sequentially.
2. Obtain independent reviews of #884/#867/#507/#868 and the #755/#760/#778/#788 QA gates; do not self-approve.
3. Azure administrator diagnoses the repeated pre-step Actions BlobNotFound issue before any hosted retry.
4. Finish PHP 8.0/8.4 full-root/schema/route/browser/accessibility/HTTP/MIME release gates; keep drafts noindex and out of registry/sitemap until approved.
5. Central owner records Groot's accountable 100K/P0 owner, canonical queue writer and independent release approver. Preserve the existing AEO/GEO baseline and current brand owners.

No Central Main/source Main/queue write, owner reassignment, merge, deployment, publication or mass indexing.
