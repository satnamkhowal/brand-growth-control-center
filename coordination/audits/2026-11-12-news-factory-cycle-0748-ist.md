# News Factory cycle — 12 November 2026, 07:48 IST

**Scope:** Four non-overlapping research lanes across verified education/IT brands. This is an append-only coordination record. No main branch, live website, sitemap, redirect or production route was changed.

## 1. New verified story and draft delivery

### Forsk Coding School — Ishan Uday Special Scholarship Scheme 2026–27

- Current official NSP All-Scholarships listing shows the scheme open from **16 September 2026** with student applications through **30 November 2026**.
- UGC scheme page states **₹80,000 per year**, 10,000 slots per annum and 3–5 year tenure depending on the eligible UG programme.
- The linked official guideline and FAQ express the award as ₹8,000 per month for 10 months; they describe NER Class XII schooling, NER domicile, first-year first UG degree, regular/full-time mode, parental income below ₹4.50 lakh and state-wise merit.
- The linked detailed guideline PDF is labelled **2021**; the FAQ carries reference **1-9/2025 (SA-III)**. The article explicitly discloses those document dates and does not claim a new 2026–27 guideline was issued.
- The live NSP listing gives 15 December 2026 for defective-application and institute verification, and 31 December 2026 for DNO/SNO/MNO verification.
- Application fee is not stated in the official pages reviewed.

New original guide:
- [Forsk PR #186](https://github.com/satnamkhowal/forsk-coding-school/pull/186) — OPEN / DRAFT / UNMERGED.
- Branch: `news-factory/ishan-uday-2026-27-ner-20261112-0748`, based on Forsk main `a690ef725029e8c7f96b6148e9012f82a481bd6d`.
- Two files only: 2,430-word Markdown article and JSON provenance/SEO metadata.
- Read-back verified; front matter present; metadata JSON parses; official source URLs present; compare is 2 commits ahead / 0 behind main.
- GitHub create response initially reported mergeable=false. Do not treat the draft as merge-approved; the compare result only establishes that it is not behind main.
- No CI status was returned. Independent editorial/fact QA remains pending.
- No article has been merged, published or submitted as a student application.

Primary sources:
- https://scholarships.gov.in/All-Scholarships
- https://scholarships.gov.in/Students
- https://www.ugc.gov.in/Scholarships/stu_Scholarship5
- https://scholarships.gov.in/public/schemeGuidelines/Guidelines_ISHAN%20UDAY_2324.pdf
- https://scholarships.gov.in/public/FAQ/FAQ_Ishanuday.pdf

## 2. Student programmes and opportunities — ownership preserved

- Google Student Researcher 2027: official Google Careers search result currently lists India / Remote eligible, currently enrolled Bachelor's/Master's/PhD applicants in specified research disciplines, relevant CS-area experience, rolling review and **4 December 2026** deadline. Stipend is not disclosed. Existing owner: [Forsk #146](https://github.com/satnamkhowal/forsk-coding-school/pull/146). The direct page renderer returned a generic jobs-search shell during open, but the exact official Google Careers search result still exposed the full role listing; use the official application URL and recheck before action.
- Sage IT India Scholarship: sponsor page currently lists ₹50,000, age 17–30, recognised Indian college/university enrolment, 1,000–1,500-word individual unpublished entry, no entry fee and **15 November 2026** deadline. Existing owner: [Forsk #184](https://github.com/satnamkhowal/forsk-coding-school/pull/184).
- NMMSS: current NSP All-Scholarships page lists student deadline **15 November 2026**. Existing owner: [Forsk #173](https://github.com/satnamkhowal/forsk-coding-school/pull/173).
- PM YASASVI Top Class Education in Schools: current NSP listing shows the scheme open through **30 November 2026**, but the separate NSP Student Announcements page says fresh applications from **Rajasthan, Keralam and Karnataka** cannot yet be submitted and those students must wait. Existing owner: [Forsk #156](https://github.com/satnamkhowal/forsk-coding-school/pull/156). Do not tell Rajasthan students the portal is currently accepting their fresh applications.
- PM Scholarship Scheme for CAPF/Assam Rifles and eligible State Police wards: Jaipur already owns the new guide in [Jaipur Engineers PR #47](https://github.com/satnamkhowal/jaipurengineers.com/pull/47); no duplicate.
- Existing AICTE, SDEF, VSSC, NeGD, Bharti Airtel, Honeywell and other programme owners were preserved. No new open-program claim was made from unverified technical-internship PDFs or conflicting/old deadlines.

## 3. React / frontend

- React official blog still lists React 19.3 (9 September 2026) as the latest feature announcement.
- Visible stable React patch tags remain 19.3.1, 19.2.9, 19.1.10 and 19.0.9 (14 October 2026); no new November stable core release was found.
- Current React Server Components advisory GHSA-xqc2-xf4c-x3h3 is dated 14 October 2026 and lists CVE-2026-126187, Critical, with patched package versions 19.0.9, 19.1.10, 19.2.9 and 19.3.1. This is not a new November disclosure. Existing [Forsk #145](https://github.com/satnamkhowal/forsk-coding-school/pull/145) already received the 07:03 IST correction.
- React Native release overview lists 0.88.x as Active and 0.89.x as Future, planned for 7 December 2026. RC/nightly channels are not production channels. Existing [Groot #644](https://github.com/satnamkhowal/grootacademy.com/pull/644) remains owner.

Sources:
- https://react.dev/blog
- https://github.com/react/react/releases
- https://github.com/react/react/security/advisories/GHSA-xqc2-xf4c-x3h3
- https://reactnative.dev/releases/overview

## 4. Node.js / backend security

Official 11 November 2026 security releases are confirmed:
- Node.js 22.x: **22.23.5**
- Node.js 24.x: **24.22.3**
- Node.js 26.x: **26.13.1**

The release pages list HIGH, MEDIUM and LOW fixes across HTTP/2, TLS, HTTPS, HTTP, permissions and dependencies. CVE-2026-126051 (remotely reachable TLS server crash) is listed in 24.x and 26.x, not in the 22.23.5 page. The 22.x/24.x/26.x patches are already owned by [Mango #143](https://github.com/satnamkhowal/mangoengineers.com/pull/143); Groot [#650](https://github.com/satnamkhowal/grootacademy.com/pull/650) separately owns the Node.js 27 Alpha/V8 learning guide. No duplicate article was created.

Sources:
- https://nodejs.org/en/blog/release/v22.23.5
- https://nodejs.org/en/blog/release/v24.22.3
- https://nodejs.org/en/blog/release/v26.13.1
- https://nodejs.org/en/blog

## 5. AI / Cloud / developer news

- GitHub's November changelog includes Issue Types/Fields for personal accounts (11 November), Enterprise Copilot seat-management API (10 November), Gemini 4 Carbon in Copilot (10 November), C++/MSBuild auto-configuration (10 November), Dependabot inactive-repository alert policy (10 November) and Claude Fable 5.2 in Copilot (9 November).
- Anthropic announced Claude Fable 5.2 and Claude Mythos 5.2 on 9 November.
- These topics are already assigned across existing Forsk #159/#165/#168/#171/#176/#182/#185 and other current Mango/Groot PRs. No duplicate article was created.
- No additional fresh, sufficiently verified and unowned AI/Cloud story was selected.

Sources:
- https://github.blog/changelog/month/11-2026/
- https://www.anthropic.com/news/announcements

## 6. Repository and coordination review

- **Mango Engineers** — private canonical `satnamkhowal/mangoengineers.com`; README, agent-start instructions, task board, work log, integration queue and open PR inventory read. Node security remains with #143. No Mango write.
- **Groot Academy** — private canonical `satnamkhowal/grootacademy.com`; root README and current open PR inventory reviewed. Existing #644, #650, #653, #655 and other owners preserved. Root README is minimal; no source write.
- **Forsk Coding School** — private canonical `satnamkhowal/forsk-coding-school`; README.txt, open PR inventory and News Factory draft path conventions reviewed. New isolated draft #186 only.
- **Jaipur Engineers** — exact canonical website repository confirmed as private `satnamkhowal/jaipurengineers.com`. Root README.md, README.txt and AGENTS.md were not found. Current PR inventory reviewed: #47 PM Scholarship CAPF/Assam Rifles/State Police, #46 Honeywell, #45 Bharti Airtel, #44 NITI Aayog, #43 readability, #41 enquiry/batch handoff and #27 social. No write.
- **Forsk Technologies** — public `satnamkhowal/forsktechnologies.com` README identifies a converted static theme/demo deliverable, warns that contact information and promotional claims must be replaced, and says theme/library licensing remains with original owners. No News Factory write.
- **CadMate India** — private `satnamkhowal/cadmateindia.com` README confirms CAD/BIM/engineering-design training positioning; no open PRs returned. No current source-backed News Factory story selected; no write.
- **Groot Software** and **Clever Ape Academy** — canonical website repository not resolved in the current installed-repository search; no writes.
- Central Control Center README lists eight brands but its current control board still has only Jaipur, Central and Forsk rows. Mango/Groot ownership rows remain absent; no controller-owned board edit was made.

## 7. Central coordination status

- Reused existing central News Factory PR [#19](https://github.com/satnamkhowal/brand-growth-control-center/pull/19) and branch `ops/news-factory-cycle-20261109-2209`.
- Before this checkpoint, central branch compare was **113 ahead / 4 behind** main `80c75e28734ce22831e93d9f431f4c15ccad0f6c`, status diverged. This run did not rebase or merge it.
- Appended this run as a new audit file; no central main/control-board change.

## 8. Production ledger — this run only

| Stage | Delta |
|---|---:|
| Non-overlapping research tracks | 4 |
| New verified unowned story selected | 1 |
| Original English article drafts | 1 |
| New Draft PRs | 1 |
| New graphics | 0 |
| Optimized image derivatives | 0 |
| Verified YouTube embeds | 0 |
| Independent QA-ready increment | 0 |
| Live/published increment | 0 |
| Existing-owner status comments | 0 |

**Next actions:** independent editorial/fact QA of Forsk #186; recheck the current NSP Ishan Uday listing and any updated 2026–27 guideline before publication handoff; recheck Sage IT and NMMSS before 15 November; preserve existing React, Node and AI/Cloud owners. No merge, deployment, application submission or live publication in this cycle.
