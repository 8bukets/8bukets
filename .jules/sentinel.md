## 2026-02-05 - Markdown Table Injection and XSS via Unsanitized Input
**Vulnerability:** `analytics.py` generated Markdown reports by directly concatenating user-controlled strings (domain names, categories) into table rows. Malicious input containing `|` characters broke the table structure, and input containing HTML tags could lead to XSS if rendered in a browser.
**Learning:** Even in offline report generation, output encoding is critical. Markdown is structured text; injecting control characters like `|` compromises integrity.
**Prevention:** Always sanitize data before inserting it into structured formats (HTML, Markdown, SQL, JSON, etc.). Implemented `escape_markdown` helper.
