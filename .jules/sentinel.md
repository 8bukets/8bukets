## 2026-01-24 - CSV Injection in Scraper
**Vulnerability:** User-controlled content (post titles, authors, categories) was written directly to CSV files without sanitization. This allowed CSV Injection (Formula Injection) where strings starting with `=`, `+`, `-`, or `@` could be executed as formulas in spreadsheet software.
**Learning:** Even when scraping "static" content, if the output format is CSV, the data must be treated as untrusted and sanitized to prevent client-side injection attacks.
**Prevention:** Always sanitize fields starting with dangerous characters by prepending a single quote `'` before writing to CSV. Implemented `sanitize_for_csv` helper method.
