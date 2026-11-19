# Staff Operations Control Center — MVP Plan

Status: proposed architecture and first intake workflow (2026-11-13).
Brands: Groot Academy and Forsk Coding School.

## Privacy boundary (mandatory)
This repository is **public** and must contain **no student names, mobile numbers, photos, receipts, signatures, staff personal email, fee transaction details, attendance records, or private Google Sheet links**. Do not put sensitive data in Git commits, PRs, issues, Actions logs, or example fixtures. If accidentally committed, quarantine and coordinate secure history purge.

## Intake workflow
1. Authenticated authorized staff enters a role-based portal on their own account.
2. Staff chooses brand, selects "Fee Receipt", "Attendance" or "Staff document", and uploads one image.
3. Preserve original image in restricted cloud object storage; generate a SHA-256 checksum, uploader identity, upload time, and evidence ID.
4. OCR extracts printed/handwritten fields into a structured draft. Store per-field confidence and whether the field comes from a receipt or from an authenticated staff statement.
5. Validate required fields, course/teacher consistency, and uniqueness (brand + receipt number + date). Flag ambiguous handwriting for review and require a reviewer for correction.
6. Store authoritative transaction in private database with immutable append-only audit history; update the staff-facing Google Sheets reporting view with narrow access.
7. "Received" is not "bank reconciled." Match bank/UPI references separately. Prevent duplicates, offer authorized reversal rather than deleting receipts.
8. A class start date never automatically marks attendance. Attendance requires separate dated proof.
9. Confirm success with a record ID, review status, and any missing field, never exposing other students' details.

## Data model
- organizations(id, brand, status)
- staff(id, auth_subject, roles_by_org, verified_email, status)
- students(id, org_id, name, verified_contacts, enrollment_status)
- enrollments(id, student_id, org_id, course, subject, teacher_id, start_date)
- receipts(id, org_id, receipt_no, receipt_date, student_id, amount_paise, currency, payment_method, collected_by_staff_id, bank_match_status, evidence_id, review_status)
- attendance(id, org_id, student_id, class_id, date, status, submitted_by, evidence_id, reviewed_by)
- evidence(id, org_id, storage_key, checksum, mime_type, created_by, captured_at, retention_policy)
- audit_events(id, actor_id, action, object_type, object_id, timestamp, before_hash, after_hash, review_reason)

## MVP screens
- Staff login, Submit Receipt, Submit Attendance, My Submissions
- Finance reconciliation and duplicate check
- Admin review queue and correction log
- Management summary per brand, date, staff, outstanding fees and attendance

## Security and operations
- Private storage/database, encrypted at rest and in transit; server-side authorization, organization-scoped access, least privilege, MFA for finance/admin.
- Never trust a typed display name as staff authentication. Shared ChatGPT conversations are a convenience for intake, not a reliable shared database or role-based access-control boundary.
- Backups, restore drill, retention/deletion policy, consent and access logs, automated quality checks, failed job retries, idempotent ingestion, and no public upload URLs.
- Avoid biometric face identification; uploaded staff photos are optional profile photos stored only with informed consent, not automatic face-attendance proof.
- Create credentials outside GitHub; store only environment variable names in the code repository.

## First intake checkpoint
- One image-based fee receipt was supplied in a private chat on 2026-11-13.
- A separate private workbook was generated locally and requires transfer into an access-controlled destination. No identifying details copied into this public repository.
- Google Sheets cloud import has **not** succeeded; do not mark cloud persistence or automatic intake as operational.
- Next: provision private storage and database, verified staff accounts, secure Sheets reporting, and test duplicate detection + OCR review end to end.

## Acceptance criteria
- Authorized staff can upload a receipt in under one minute.
- No student or staff information is visible to unauthorized brand members.
- Incomplete handwriting never creates fabricated data; review workflow is explicit.
- Transaction cannot be silently duplicated or overwritten.
- Every edit is attributed to a verified actor with timestamp and reason.
- Management dashboard totals agree with reconciled ledger.
