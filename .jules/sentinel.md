## 2026-01-21 - Markdown Injection in Reports
**Vulnerability:** User-controlled content from scraped websites was directly embedded into Markdown reports without sanitization. This could allow malicious websites to break the report structure (tables) or inject malicious content (Stored XSS if rendered to HTML).
**Learning:** Even internal reports generated from external data must be treated as untrusted. Markdown has special characters that can be abused.
**Prevention:** Implemented `sanitize_for_markdown` and `sanitize_url` in `agents/security_utils.py` and applied them in `report_generator.py` to escape special characters and sanitize URLs.
