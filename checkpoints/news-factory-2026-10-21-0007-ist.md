# News Factory checkpoint — 21 October 2026, 00:07 IST

## Coordination
- Parent checkpoint: `checkpoints/news-factory-2026-10-20-2209-ist.md`
- Coordination branch: `ops/news-factory-20261019`
- Brand implementation branch: `content/news-factory-20261019-1410`
- No new release or programme cleared the freshness and duplication gate in this cycle.
- The cycle completed the pending independent QA action for the existing Jaipur Engineers AWS guide.

## Independent QA outcome
### Jaipur Engineers — AWS Cloud Credit for Research India guide
- Status: independently QA-ready; not live.
- Draft: https://github.com/satnamkhowal/jaipur-engieneers/blob/content/news-factory-20261019-1410/docs/news-factory/drafts/aws-cloud-credit-research-india-student-guide.md
- Graphic: https://github.com/satnamkhowal/jaipur-engieneers/blob/content/news-factory-20261019-1410/docs/news-factory/media/aws-research-credit-india-application-path.svg
- Draft correction commit: `16e18208f478b752a8023730d60f9386ebb67d69`
- SVG correction commit: `73dc91d3e5de2f1cf2688acea3a41748c675923c`
- QA-state commit: `738cb2f4d2406ad42e56666822181c287075d96f`
- Final draft blob: `dda3473223c09c814590293d302bfb8d7d9fe719`
- Final SVG blob: `0cd68905340845ea2d89e1b4a02d81361b0e1ba3`

## Corrections made
1. Preserved the official expiry-start discrepancy:
   - application page: one year from application to the account;
   - Promotional Credit Terms updated 24 September 2026: one year from the earlier of receiving the code or AWS depositing the credit.
   The guide now tells applicants to follow the Terms and the specific account/award expiry.
2. Replaced overbroad “Free Tier accounts” wording with “accounts on the Free Tier account plan.”
3. Added the limited AWS-authorized sharing exception within an AWS Organization to the transfer warning.
4. Corrected the SVG warning to “Free Tier plan accounts.”

## Independent QA checks passed
- India/AISPL applicability and applicant roles
- USD 5,000 student request cap, non-guarantee and non-cash status
- 90–120 versus 30–60 day review discrepancy
- account/card/billing/tax/ineligible-service safeguards
- rolling status and absence of a stated deadline
- source-date language and close-paraphrase review
- SEO/AEO structure
- original 1200×675 SVG, viewBox, title, description and ARIA metadata

Institutional and legal review remain pending. No merge, deployment, publication, AWS account creation or application was performed.

## Monitored tracks
- Programmes: no new or status-changed India-relevant item after the previous cutoff.
- React/frontend: no new stable release or security advisory; canary/RC builds excluded.
- Node.js/backend: the announced 21 October security batch is still not published. Official advisory remains future tense; patched versions and CVEs are absent.
- AI/cloud: no item could be proven newer than the prior checkpoint.

## Counts
### This cycle
- Newly researched stories accepted: 0
- New drafts: 0
- New graphics: 0
- Corrected existing drafts: 1
- Corrected existing graphics: 1
- Brand-repository commits: 3
- Central checkpoint commits: 1 (this file)
- Newly independent QA-ready: 1
- Newly live: 0

### Cumulative
- Researched: 19
- Drafted: 19
- Original graphics: 19
- GitHub commits including checkpoints: 57
- Independent QA-ready: 1
- Live: 0

## Next action
1. Institutional/legal review of the AWS guide before any publication decision.
2. Recheck the Node.js security advisory later on 21 October for final versions and CVEs.
3. Continue primary-source monitoring without converting date-only pages into hourly “new” claims.
