## 2026-01-31 - Markdown Injection in Analytics
**Vulnerability:** User-controlled data (categories, domains) was directly inserted into Markdown tables in `analytics.py`, allowing table structure breakage and potential XSS via HTML injection.
**Learning:** `analytics.py` lacked output encoding for Markdown generation.
**Prevention:** Implemented `sanitize_markdown` function to escape pipe characters (`|`), HTML tags (`<`, `>`), and brackets (`[`, `]`) before rendering to Markdown.
