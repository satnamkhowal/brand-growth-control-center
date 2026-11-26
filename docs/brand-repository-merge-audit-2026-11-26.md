# Brand Repository and PR Merge Audit — 26 November 2026

## Scope and method

Read-only audit of the eight canonical brand repositories defined in `data/brand-repository-locks.json`. Branch listing and open-PR search were performed through the connected GitHub account. Branch listing returns at most 100 entries per page; open-PR search returns at most 100 results. A returned cursor means the branch inventory is incomplete and must be paginated before claiming exhaustive coverage. PR classification below is a triage estimate based on titles and descriptions, not authoritative GitHub draft metadata.

## Canonical repository lock

| Brand | Canonical repo | Lock status |
|---|---|---|
| Jaipur Engineers | `satnamkhowal/jaipurengineers.com` | Locked |
| Mango Engineers | `satnamkhowal/mangoengineers.com` | Locked |
| Forsk Coding School | `satnamkhowal/forsk-coding-school` | Locked |
| Groot Academy | `satnamkhowal/grootacademy.com` | Locked |
| Clever Ape Academy | `satnamkhowal/cleverapeacademy.com` | Locked |
| CadMate India | `satnamkhowal/cadmateindia.com` | Locked |
| Groot Software | `satnamkhowal/grootsoftware.com` | Locked |
| Forsk Technologies | `satnamkhowal/forsktechnologies.com` | Locked |

## Snapshot summary

| Brand | Branches returned (page 1) | Cursor | Open PRs returned | Draft/HOLD-like triage | Initial merge disposition |
|---|---:|---|---:|---:|---|
| Jaipur Engineers | 100 | Yes | 48 | 24 | No merge; current-main/CI blockers |
| Mango Engineers | 100 | Yes | 100 (search cap) | 96 | No merge; huge stacked review queue; pagination required |
| Forsk Coding School | 100 | Yes | 100 (search cap) | 81 | No merge; pagination and security/release review required |
| Groot Academy | 100 | Yes | 100 (search cap) | 41 | No merge; pagination and stacked blog-factory QA required |
| Clever Ape Academy | 32 | Yes | 6 | 3 | No merge; selected PRs diverged from main |
| CadMate India | 9 | Yes | 2 | 1 | No merge; PR #6 has no independent review or CI evidence yet |
| Groot Software | 46 | Yes | 8 | 1 | No merge; PRs selected for analysis diverged and/or have QA HOLD |
| Forsk Technologies | 40 | Yes | 7 | 2 | No merge; selected PRs diverged and enquiry-form release blockers |

## Jaipur Engineers detailed triage

Canonical repo: `satnamkhowal/jaipurengineers.com`.

- 48 open PRs returned; 24 appear Draft/HOLD from title/body triage. The PR search returned all 48 in this snapshot.
- Branch search returned the first 100 branches and cursor `MTAw`; further pagination is required for a complete branch inventory.
- PR #147 (combined enquiry/calendar/Java communication replacement): **HOLD**. Description explicitly says exact-head Actions failed before executable steps and PHP/security, browser, form-delivery, staging and deployment checks are unverified.
- PR #154 (Java Spoken English/presentation practice): **HOLD**. Description records exact-head CI jobs failed before steps/logs and GitHub mergeability false.
- PR #112 (BroadcastChannel guide): branch `content/broadcastchannel-tabs-guide`; compare `main...head` is diverged, 5 ahead / 320 behind, with five scoped files (new article, SVG, catalogue, content registry, sitemap). Needs current-main restack and exact-head tests.
- PR #72 (Promises/async-await guide): branch `blogs/javascript-async-await-guide-2026-11`; compare is diverged, 5 ahead / 358 behind, with four scoped files (new article, SVG, catalogue, sitemap). Needs current-main restack and rendered/canonical/schema/sitemap validation.
- No Jaipur Engineers PR was merged during this audit.

## Selected small-repository PR analysis

### CadMate India — PR #6
- Branch: `seo/cad-bim-portfolio-communication-current-main-20261122-run133`.
- Compare to main: **ahead 3 / behind 0**; three files changed (QA workflow, `course.php`, Python QA tests).
- PR description reports manual source assertions 6/6 passed, including course-group gating, visible practice/CTA, targeted CAD slugs and workflow lint/test commands.
- No submitted independent review was returned; no exact-head CI evidence was obtained.
- **Disposition: HOLD**, despite clean main ancestry, until required workflow checks and review are verified.

### Groot Software — PR #38
- Branch: `fix/internship-main-landmark-20261120`; compare **2 ahead / 9 behind**, one HTML file changed.
- Review comment is explicitly **Release QA HOLD**; browser/keyboard, responsive layout, navigation/footer, canonical/noindex and exact-head checks were not verified.
- **Disposition: HOLD; restack and validate.**

### Groot Software — PR #35
- Branch: `fix/readability-ux-20261109`; compare **1 ahead / 15 behind**, stylesheet-only diff.
- **Disposition: HOLD; reconcile with current main and validate.**

### Groot Software — PR #31
- Branch: `automation/internship-filter-history-20261107`; compare **25 ahead / 15 behind**, eight files including workflow, JavaScript, documentation and test scripts.
- **Disposition: HOLD; broad diff and current-main reconciliation required.**

### Forsk Technologies — PR #28
- Branch: `feature/internship-programs-landing-2026`; compare **23 ahead / 5 behind**.
- PR description identifies release blockers: confirm enquiry channel delivery, links, keyboard/responsive behavior and exact-head checks.
- **Disposition: HOLD; restack and complete release QA.**

### Forsk Technologies — PR #3
- Branch: `feat/secure-enquiry-form-system`; compare **14 ahead / 79 behind**; ten files include PHP form/security pipeline, JS/CSS, SQL, docs and tests.
- Existing review comments explicitly require durable DB success before UI success, consent checkbox/server validation and recording, exact-head CI, migrations, compatibility and synthetic DB/email smoke tests.
- **Disposition: HOLD; security/consent/persistence blockers must be addressed before merge.**

### Clever Ape Academy — PR #22
- Branch: `fix/readability-ux-20261109`; compare **1 ahead / 68 behind**, stylesheet-only.
- **Disposition: HOLD; restack and validate.**

## Merge safety decision

No PR was merged in this audit. This is deliberate: several repositories have hundreds of open/stacked PRs; branches are often stale or divergent; many PRs are explicitly Draft/HOLD; CI, review, browser, security, deployment or production checks are missing. The next pass must paginate all branch inventories and PR searches, then process one PR at a time: classify scope, inspect full diff, reconcile with current main, run exact-head tests/checks, verify review requirements, and merge only when all gates pass. Never force-push or mass-merge.

## Next actions

1. Exhaust branch pagination and PR search for repositories capped at 100 results.
2. Prioritize small, non-diverged, non-draft PRs with exact-head CI and required review evidence.
3. Restack stale/diverged PRs onto current main without force-pushing; resolve conflicts with scoped ownership.
4. Run exact-head tests and review the full diff before merging.
5. Update this audit and the central controller after every verified merge; record deployment separately.
