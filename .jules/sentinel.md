## 2026-01-19 - Markdown Injection in Analytics Reports
**Vulnerability:** `analytics.py` generated `REPORT.md` by directly interpolating user-controlled data (domains, categories, authors) into Markdown tables, allowing for table structure breakage (via pipes) and Stored XSS (via HTML injection).
**Learning:** When generating Markdown programmatically, simply escaping HTML is insufficient; Markdown-specific delimiters like pipes `|` must also be escaped. Additionally, backslashes must be escaped *before* pipes to prevent escape character injection.
**Prevention:** Use a robust sanitization function that escapes HTML entities, escapes backslashes, and escapes pipes when inserting untrusted data into Markdown tables.
