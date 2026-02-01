## 2026-02-01 - Fix Markdown Injection in Analytics Report
**Vulnerability:** `analytics.py` was susceptible to Markdown Injection and Stored XSS because it inserted untrusted data (domains, categories, authors) directly into Markdown tables and lists without sanitization.
**Learning:** Even in internal reporting tools, untrusted data must be sanitized before rendering. Markdown tables are easily broken by pipe characters `|`, and some Markdown viewers execute HTML, leading to XSS.
**Prevention:** Always sanitize data destined for Markdown reports. Escape HTML characters using `html.escape()` and escape table delimiters (pipes) with backslashes.
