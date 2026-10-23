# Brand Growth Control Center

Central coordination hub for eight brands and their authorized workstreams.

## Operating rules

- One owner per task; no duplicate implementation.
- Record the repository, priority, validation, deployment state, and next action.
- Never mark work as complete without a verifiable link or test result.
- Use this repository for coordination only; implementation remains in each brand's source repository.

## Brands

1. Jaipur Engineers
2. Mango Engineers
3. Forsk Coding School
4. Groot Academy
5. Clever Ape Academy
6. CadMate India
7. Groot Software
8. Forsk Technologies

## Current control board

| Priority | Brand | Owner | Status | Evidence / next action |
| --- | --- | --- | --- | --- |
| P0 | Jaipur Engineers | Account 1 / Master Supervisor | In review | Validate the existing enquiry-form change and confirm production deployment. |
| P0 | Central coordination | Account 1 / Master Supervisor | Active | Add each brand repository, access status, and active task after verification. |
| P0 | Forsk Coding School | Forsk implementation / Central Controller | In review | [2026-10-23 work log + continuation prompt](documents/forsk-coding-school/WORK-LOG-2026-10-23.md): alumni PR #39 merged to code; trainers PR #38 still open; events hub branch and brochure/SEO QA pending. |

## Update format

For every change, add: brand, repository, owner, priority, status, changed files or URLs, pull request, test result, deployment status, blocker, and next action.

## Public Google Business Profile inventory

The [Jaipur GBP listings registry](data/gbp-listings.json) tracks user-submitted Google Maps business profiles for centralized audit. The first batch (2026-10-20) records three astrology listings: Advance jyotish (website not listed), Astrologer Amit Sharma (Google Maps lists `famouspanditindia.com`; website reachability still unverified), and Astrologer Peeyush Vashisth (website not listed).

**Important:** These are public listing snapshots, not proof of ownership or linked management access. Verify business/domain authorization before making GBP edits. Keep implementation in the relevant brand's own repository and record evidence of any live changes.

## Company registration inventory

The [company registration inventory](data/company-registrations.json) records verified business-registration facts needed for centralized coordination. It deliberately excludes contact details, full addresses, and other data not needed for that purpose. See the accompanying [provenance log](data/company-registration-provenance.md) for source and verification boundaries. Searchable, privacy-redacted source copies are organized under [documents/](documents/).
