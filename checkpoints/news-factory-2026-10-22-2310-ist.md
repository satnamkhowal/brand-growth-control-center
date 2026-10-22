# News Factory checkpoint — 22 October 2026, 23:10 IST

## Coordination
- Parent checkpoint: `checkpoints/news-factory-2026-10-21-0908-ist.md`
- Coordination branch: `ops/news-factory-20261019`
- Brand implementation branch: `content/news-factory-20261019-1410`
- Repositories and existing queue were read before writes.
- No merge, deployment or publication was performed.

## Accepted story 1 — Groot Academy
### Node.js October 2026 security releases
- Official release date: 21 October 2026.
- Fixed versions: Node.js 26.12.1 Current, 24.22.1 Krypton LTS, 22.23.4 Jod LTS.
- Final advisory: https://nodejs.org/en/blog/vulnerability/october-2026-security-releases
- Draft: https://github.com/satnamkhowal/groot-academy/blob/content/news-factory-20261019-1410/docs/news-factory/drafts/nodejs-october-2026-security-releases-india.md
- Original SVG: https://github.com/satnamkhowal/groot-academy/blob/content/news-factory-20261019-1410/docs/news-factory/media/nodejs-october-2026-security-upgrade-path.svg
- Draft commit: `2bb52bece0cda17d21ac56e1f117e2faf0aa2364`
- Graphic commit: `73b9b593af9bd4c304aebf9946c948c2cdbaf027`
- Initial QA-state commit: `ad04768318e3d0d1e25226298ec72f6ea92db6ad`
- Final-advisory correction commit: `edc90226018e226a1b34ea36c568c2c687c452ff`
- Re-QA state commit: `d411e38b339f76ed8451192979dc4a97256cb40a`
- Final draft blob: `ea3ff6e41e122ec069965cc819016c6caa4613f0`
- Status: independently QA-ready; not live.

The final Node.js advisory superseded the initial release-note presentation for severity and affected-line mapping. The draft now correctly records `CVE-2026-106072` as Medium and affecting 26.x, 24.x and 22.x.

## Accepted story 2 — Forsk Coding School
### Google Cloud Agent Compute Engine preview explainer
- Official publication/event date: 22 October 2026 at AGNTCon + MCPCon.
- Availability: preview targeted for the coming months; not GA and not yet announced as public preview.
- India status: no India-specific availability or region statement.
- Pricing: no public list price; the technical article says customers will not pay for idle VMs, but this is not a complete pricing schedule.
- Agent Substrate is a separate open-source runtime available to try on GKE now.
- Announcement: https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance
- Technical source: https://cloud.google.com/blog/topics/ai-infrastructure/agent-compute-engine-deep-dive
- Draft: https://github.com/satnamkhowal/forsk-coding-school/blob/content/news-factory-20261019-1410/docs/news-factory/drafts/google-agent-compute-engine-preview-india.md
- Original SVG: https://github.com/satnamkhowal/forsk-coding-school/blob/content/news-factory-20261019-1410/docs/news-factory/media/google-agent-compute-engine-learning-stack.svg
- Draft commit: `35bc727d9c7fd5eeec01ef8c320d09d4c24e2f17`
- Graphic commit: `9d4d3b6a5164fe960c868d5490a2e3497f5e86ad`
- QA-state commit: `c9a8e3f1dc3c55d221f571fe58878f718caf0bae`
- Final draft blob: `0659e156f17ce978f0ecb0d6b882fbfa02439929`
- Status: independently QA-ready; not live.

## Independent QA
Independent re-review passed both drafts and graphics:
- exact Node.js fixed versions, CVE severity and affected maintained lines;
- Google publication date, pre-preview language, no India/region/pricing overclaim;
- original SEO/AEO structure and distinct brand angles;
- SVG dimensions 1200×675, accessibility metadata and no third-party logos;
- publication status remains not-live and institutional/legal review remains pending.

## Other monitored tracks
- Student/developer programmes: no qualifying fresh opportunity with a verifiable publication/update date after the prior cutoff. Amazon India SDE I Intern 2027 is open but has no visible publication/update date or deadline, so it was not reported as newly opened.
- React/frontend: no qualifying stable release or security advisory after the cutoff; prereleases excluded.
- Node.js/backend: no release newer than 26.12.1/24.22.1/22.23.4; Express, NestJS and npm also had no newer qualifying release/advisory.
- Other AI/cloud: OpenAI–Uber is an enterprise deployment story rather than a new public product, so no duplicate draft was added.

## Media and video
- New original graphics: 2.
- Licensed third-party graphics downloaded: 0.
- Video embeds added: 0. No announcement-specific video with verified ID and confirmed embed availability was used.

## Counts
### Since the parent checkpoint
- Newly researched stories accepted: 2
- New drafts: 2
- New original graphics: 2
- Corrected existing drafts: 1
- Newly independent QA-ready: 2
- Brand-repository commits: 8
- Central checkpoint commits: 1 (this file)
- Newly live: 0

### Cumulative
- Researched: 21
- Drafted: 21
- Original graphics: 21
- GitHub commits including checkpoints: 73
- Independent QA-ready: 6
- Live: 0

## Next action
1. Institutional/legal review of the six QA-ready guides.
2. Re-check Agent Compute Engine preview opening, India regions and pricing before publication.
3. Continue primary-source monitoring without treating undated job listings, prereleases or event dates as new openings.
