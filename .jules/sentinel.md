# Sentinel Journal

## 2025-12-27 - Markdown Injection & Stored XSS in Reports
**Vulnerability:** Scraped data (titles, URLs, changed values) was written directly into Markdown tables in `report_generator.py`. This allowed table structure breakage via pipe characters (`|`) and Stored XSS via `javascript:` links if the report was rendered to HTML.
**Learning:** Generating Markdown or HTML reports from untrusted/scraped data requires strict sanitization, just like SQL or HTML rendering. Markdown tables are fragile and easily broken by raw input.
**Prevention:** Implemented `sanitize_markdown_cell` (escapes pipes to `&#124;`) and `sanitize_url` (blocks `javascript:`) functions. Applied these to all user-controlled inputs in the report generation logic.
