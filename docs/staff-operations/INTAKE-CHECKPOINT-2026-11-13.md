# Private staff-operations intake checkpoint — 2026-11-13

**Purpose:** Public, non-personal operational checkpoint for the Groot Academy / Forsk Coding School management system. Source records are stored outside the public repository.

## Verified pilot state
- **1** student fee-receipt entry transcribed to a private register and native Google Sheet; payment bank reconciliation remains pending.
- **1** staff attendance entry submitted via photo and self-declared as present/late.
- The photo-submission timestamp is stored separately from actual arrival, which is **unknown**.
- Staff name/role came from the submitter's declaration. Face recognition and verified account association have **not** been performed.
- **1** image evidence item stored in restricted Google Drive; permissions checked and only the owner was listed.
- Native Google Sheet created with tabs for fee receipts, students, student attendance, staff, staff attendance, evidence index, audit log, and instructions.
- Separate private offline workbook and image-evidence bundle were generated for owner retrieval.
- **0** staff photos, student names, phone numbers, receipts, links to private records, or other personal data committed to this public repository.

## Still required before accepting live production attendance
1. Verified sign-in per employee, role-based access and organization boundaries.
2. Official late/present rules, shift timetable and handling of authorized self-attendance.
3. Automatic OCR/image extraction pipeline with a review queue.
4. Server-side append-only audit trail, duplicate detection, tamper-resistant attendance ledger and edit restrictions.
5. Secure photo retention, backups, restore tests and explicit access/retention policy.
6. Verified integration with cloud records so a chat submission does not depend on an individual assistant run.

## Public-repo policy
Do not upload personal attendance data or selfies to GitHub. This file is a coordination status report, not the authoritative attendance ledger.

Status: pilot entries logged, secure cloud persistence established for the first entries; automated and enforceably locked attendance system is **not yet implemented**.
