## 2026-01-23 - CSV Injection Vulnerability
**Vulnerability:** Scraper data (Titles, Authors, etc.) was written directly to CSV without sanitization, allowing potential Formula Injection (CSV Injection) if the scraped content contained `=`, `+`, `-`, or `@`.
**Learning:** Python's standard `csv` module does not automatically sanitize data for formula injection. Explicit sanitization is required when dealing with user-controlled or external content.
**Prevention:** Implement a sanitization layer that prefixes unsafe characters with `'` before writing to CSV.
