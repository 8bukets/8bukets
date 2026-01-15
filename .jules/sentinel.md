# Sentinel's Journal

## 2026-01-15 - CSV Injection in Scraper Output
**Vulnerability:** `scraper.py` wrote scraped content directly to CSV files without sanitization. Malicious titles starting with `=`, `@`, etc. could execute formulas in spreadsheet software.
**Learning:** Even "read-only" data scraping can introduce vulnerabilities if the output format (CSV) interprets specific characters as executable code.
**Prevention:** Always sanitize data before writing to CSV by prepending `'` to fields starting with `=`, `+`, `-`, `@`.
