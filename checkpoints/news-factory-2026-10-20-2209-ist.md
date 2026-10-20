# News Factory checkpoint — 20 October 2026, 22:09 IST

## Coordination
- Parent checkpoint: `checkpoints/news-factory-2026-10-20-1804-ist.md`
- Coordination branch: `ops/news-factory-20261019`
- Brand implementation branch: `content/news-factory-20261019-1410`
- This cycle implemented previously researched queue item 1. No newly discovered story is being represented as newly opened or newly released.

## Implemented
### Jaipur Engineers — AWS Cloud Credit for Research India guide
- Draft: https://github.com/satnamkhowal/jaipur-engieneers/blob/content/news-factory-20261019-1410/docs/news-factory/drafts/aws-cloud-credit-research-india-student-guide.md
- Draft commit: `7826681b3b848b376d5fa877c534504956e13ddb`
- Original graphic: https://github.com/satnamkhowal/jaipur-engieneers/blob/content/news-factory-20261019-1410/docs/news-factory/media/aws-research-credit-india-application-path.svg
- Graphic commit: `4a24e4636733b9a4ff4bdc8ff5367e6a68b7dbcd`
- Graphic: 1200×675 SVG; original educational diagram; no AWS logo or third-party artwork.
- Alt text: “AWS research credit India application path showing eligibility, proposal, review estimates, award cap and billing safeguards”.
- No video embed was added: no suitable program-specific official video with verified metadata and embedding evidence was identified.

## Verification notes
- AWS Cloud Credit for Research is an ongoing, rolling programme, not a newly opened scholarship.
- India applicants are served by Amazon Internet Services Private Limited (AISPL).
- Individual eligibility is for full-time faculty/research staff and graduate, postgraduate or PhD students at accredited research institutions. The draft does not generalise eligibility to all undergraduate/B.Tech students.
- Student requests are capped at USD 5,000 in AWS Promotional Credit, but an award is not guaranteed and is not cash.
- AWS pages currently give two review estimates: 90–120 days on the overview and 30–60 days on the application page. The draft preserves both rather than collapsing them.
- From 16 February 2026, accounts on the AWS Free Tier account plan are not eligible to apply.
- An AWS account and institution email are required; applicants should understand card/billing exposure, ineligible services, expiry and spend beyond awarded credits before enabling workloads.

## Primary sources
- Programme overview: https://aws.amazon.com/government-education/research-and-technical-computing/cloud-credit-for-research/
- FAQ: https://aws.amazon.com/government-education/research-and-technical-computing/cloud-credit-for-research/faqs/
- Application requirements: https://aws.amazon.com/government-education/research-and-technical-computing/cloud-credit-for-research/application/
- AWS Promotional Credit terms: https://aws.amazon.com/awscredits/

## Monitored tracks
- React/frontend: no new stable release or newly published security fix after the prior checkpoint; canary builds were not treated as stable.
- Node.js/backend: the announced 21 October 2026 security release batch was still future-tense; no final patched versions or CVEs were available at this checkpoint.
- AI/cloud: no additional primary-source item cleared the freshness and non-duplication threshold.

## QA and publication state
- Round-trip fetched draft blob: `365b7f6b92af75c04a044611936044faaddad70a`
- Round-trip fetched graphic blob: `1c87b988f44c904e0061bf13684ce285b2013afd`
- Draft checked for source URLs, explicit status, India eligibility, amount qualifier, date discrepancy and billing caveat.
- SVG checked for 1200×675 dimensions, `viewBox`, `title`, `desc` and descriptive alt text.
- Independent editorial/legal/financial QA: pending.
- Merge, deploy, publication and programme application: not performed.

## Counts
### This cycle
- Newly discovered verified stories: 0
- Previously verified queue items implemented: 1
- Drafts: 1
- Original graphics: 1
- Video embeds: 0
- Brand-repository commits: 2
- Central checkpoint commits: 1 (this file)
- Independent QA-ready: 0
- Live: 0

### Cumulative
- Researched: 19
- Drafted: 19
- Original graphics: 19
- GitHub commits including checkpoints: 53
- Independent QA-ready: 0
- Live: 0

## Next action
1. Independent editorial and financial-risk review of the AWS guide.
2. Recheck the Node.js security page after the announced 21 October release window for final versions and CVEs.
3. Continue primary-source monitoring without duplicating existing queue items.
