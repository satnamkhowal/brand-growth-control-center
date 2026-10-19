# All Brands News Factory Checkpoint — 2026-10-19 20:09 IST

Status: RESEARCHED + DRAFTED, NOT INDEPENDENTLY APPROVED, NOT MERGED, NOT DEPLOYED, NOT LIVE

Parent checkpoint: `checkpoints/news-factory-2026-10-19-1918-ist.md`

## Coordination review

- Latest central checkpoint fetched before implementation.
- Recent activity reviewed for Mango Engineers, Groot Academy, Forsk Coding School and Jaipur Engineers.
- Duplicate search for Kiro Students across all four brand repositories and central coordination returned no matching story.
- Existing brand branch reused: `content/news-factory-20261019-1410`.
- Existing central branch reused: `ops/news-factory-20261019`.

## New verified student/developer program coverage

### Kiro Students

- Original launch date: 2026-03-18
- University expansion announcement: 2026-09-14
- Current application status: Student verification available for listed eligible universities when checked on 2026-10-19
- Benefit: 1,000 credits per month for 12 months
- Cost: No cost and no credit card for successfully verified students
- Age: 18 or older
- Verification: University-affiliated email and SheerID
- Deadline: No fixed closing date stated on the official page
- Monthly rules: Credits do not roll over; add-on credits are not available
- End of benefit: Account moves to the regular Kiro free tier after one year
- India finding: No Indian university appeared in the current published eligible-school list. India-based students should not be described as generally eligible.
- Missing-school path: The official page allows students to request that their university be added.
- Official current page: https://kiro.dev/students/
- Official launch post: https://kiro.dev/blog/introducing-kiro-students-tier/
- AWS expansion report: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-openai-gpt-6-astra-on-amazon-bedrock-amazon-quick-desktop-ga-kiro-for-students-and-more-september-14-2026/
- Official pricing: https://kiro.dev/pricing/

## New implementation

| Brand | Repository | Draft | Media | State |
| --- | --- | --- | --- | --- |
| Forsk Coding School | satnamkhowal/forsk-coding-school | `docs/news-factory/drafts/kiro-students-free-year-india-eligibility.md` | `docs/news-factory/media/kiro-students-india-eligibility.svg` | RESEARCHED_DRAFT |

Media record:

- Type: Original SVG eligibility explainer
- Dimensions: 1200×675
- Rights: Copyright Forsk Coding School; no Kiro or AWS logo and no third-party artwork
- Attribution: Original Forsk Coding School editorial graphic
- Repository path: `docs/news-factory/media/kiro-students-india-eligibility.svg`
- Alt text: Kiro Students eligibility checklist showing one thousand monthly credits and India university limitation
- Video: None. No program-specific official YouTube video with verified embed availability was found.

## Verification and QA

- Article and SVG fetched back after commit.
- No conflict markers found.
- Current eligible-school list inspected; no Indian institution found.
- Age, email, SheerID, credit amount, duration, no-rollover and no-add-on rules checked against the official student page.
- The article distinguishes credits from cash, stipend, scholarship or internship funding.
- The program is not presented as newly launched; March launch and September expansion dates are separate.
- This is internal second-pass QA only. Independent editorial approval is still required.

## Monitored tracks

- Google/student programs: No new official GSoC 2027 program page or application timeline was found; no speculative article created.
- React/frontend: No new official October release or security advisory found.
- Node.js/backend: The 21 October 2026 security release remains scheduled; patched versions and CVEs are not yet available.
- AI/cloud/developer: Kiro Students was selected because the current benefit and a critical India-eligibility limitation could be verified.

## Counts

### This cycle

- New verified stories: 1
- New English drafts: 1
- New original graphics: 1
- Brand commits: 2
- Central checkpoint commits: 1
- Verified YouTube embeds: 0
- Independently QA-ready: 0
- Live: 0

### Cumulative batch

- Researched stories: 9
- Drafted articles: 9
- Original SVG graphics: 9
- GitHub commits including coordination checkpoints: 22
- Independently QA-ready articles: 0
- Live articles: 0

## Next actions

1. Re-check the Kiro eligible-school list before publication and monitor for Indian university additions.
2. Independently review the India wording and student-verification claims.
3. Add CMS schema and internal links only after confirming Forsk's target content model.
4. Re-check the Node.js security advisory on or after 21 October 2026.
5. Obtain explicit approval before merge, deployment or publication.
