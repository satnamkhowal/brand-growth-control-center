# Jaipur internship SEO cluster and first-party lead capture — implementation specification

Status: implementation plan, NOT deployed or approved for publishing.

## Editorial and search-intent architecture

Create **original, brand-specific** articles with meaningful differences in examples, audience and company role. Do not publish cloned "best" lists across domains. Each domain gets one primary landing URL per intent, supporting long-tail guides and carefully chosen internal links. Inventory existing URLs, sitemap and Search Console before choosing canonicals.

| Search intent | Editorial landing-page family | Content differentiation |
| --- | --- | --- |
| best full stack internship companies in Jaipur | comparison/selection guide | explicit affiliation disclosure; objective criteria; never claim independent ranking |
| full stack web development internship in Jaipur | programme/skills page | React, APIs, SQL/NoSQL, deployment, portfolio |
| data science internship in Jaipur | programme/skills page | Python, statistics, reproducibility, evaluation |
| data analytics internship in Jaipur | programme/skills page | SQL, Excel, Power BI, stakeholder reporting |
| AI/ML internship in Jaipur | programme/skills page | model validation, data governance, privacy |
| Java/Python development internship | programme/skills page | backend engineering and tests |
| cloud/DevOps internship | programme/skills page | CI, Docker, monitoring, security |
| cyber security internship | programme/skills page | defensive labs and responsible disclosure |
| UI/UX internship | programme/skills page | research, accessibility, prototyping |
| digital marketing internship | programme/skills page | GA4, Search Console, SEO measurement |

Brand positioning: Forsk Coding School / Groot Academy / Mango Engineers / Jaipur Engineers / Clever Ape Academy are education-focused; Forsk Technologies / Groot Software and any independently verified Talda Software business are company/service-oriented. Verify each organisation's legal/brand facts and live internship offering before publishing a claim. **Talda Software URL, ownership and Google Business Profile not yet verified; no fabricated link.**

Each editorial page should provide independently useful guidance, verified programme terms, comparison criteria, clear affiliate ownership disclosure, author/review dates and 2–4 relevant contextual cross-brand links. Do not create artificial link rings, keyword-stuffed anchors, fabricated testimonials, ratings, job openings, stipend or placement claims. Google Maps links must come from verified business profiles and verified branches; short URLs are optional.

## Lead form contract — each brand owns its data

Every internship landing page should include its own first-party form, branded consent and handler on that brand's domain. **Never post leads to a different brand by default.** If lead sharing between affiliates is proposed, obtain explicit separate opt-in and document recipients and retention.

Fields: full name (required), phone (required), email (optional), internship track (required), preferred location/mode (optional), message (optional), explicit consent checkbox (required), hidden honeypot, CSRF token, server-controlled brand/page/UTM attribution (validate/allowlist).

Handler: POST only; enforce origin/CSRF, per-IP and per-session rate limits, input length/type checks, anti-spam, safe redirects, no header injection, and privacy-preserving structured error responses. Return a stable submission ID and only show success after durable storage. **Use prepared statements** and a least-privilege database account. No secrets or student records in Git. Encrypt transport and restrict DB backups/access.

Suggested schema: leads(id UUID/ULID PK, brand_id, landing_page, track, full_name, phone, email, preferred_mode, message, consent_version, consent_at, created_at, status); lead_events(id, lead_id, event_type, created_at); notification_outbox(id, lead_id, recipient_role, attempt_count, next_attempt_at, status). Never store raw IP unless explicitly necessary, documented and retention-limited. Apply access control, deletion requests, retention limits and audit trails.

Write the lead and notification-outbox row in one DB transaction. A worker/cron sends branded SMTP notifications from the relevant domain with retries; failed mail must not silently discard a saved lead. Do not use unverified PHP mail delivery as the sole storage mechanism. Do not email sensitive details unnecessarily. Configure SPF/DKIM/DMARC and monitor delivery. Admin panel requires authentication and scoped access by brand.

## Existing code audit required before integration

- Mango Engineers has a mail.php form handler that sends mail but does not currently establish database persistence; its repo records a production PHP/runtime drift blocker. Preserve existing consent and routing while migrating.
- Groot Software has lead.php with filesystem storage and mail attempts; confirm its actual persistence and hosting before altering it.
- Other brands: inspect real framework, handlers, data stores and CI before selecting PHP/process.php or API endpoints; do not assume every site runs PHP.
- Implement one brand as a reviewed pilot, with database migration, SMTP config, idempotency, consent copy and automated integration tests, before replication.
- Do not publish or merge if required independent approvals, branch protections, security tests or production deployment checks are missing.

## Acceptance criteria

1. Landing page unique and canonical; no competing duplicate route.
2. Valid/invalid/spam/rate-limit/CSRF/DB-failure/mail-failure tests pass.
3. Successful test submission appears in the correct brand database, not another brand.
4. Notification arrives in the brand's authorized inbox, without exposing PII in logs.
5. Mobile, keyboard and screen-reader form checks pass.
6. Map URL, contact details and affiliate claims verified by owner.
7. Required CI, code review and protections satisfied.
8. Merge commit and actual live deployment reported separately; live form verified only with an authorized synthetic test.
