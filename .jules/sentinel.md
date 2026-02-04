## 2026-02-04 - CSV Injection in Scraper Output
**Vulnerability:** `scraper.py` wrote untrusted input (titles, authors) directly to CSV files, allowing for Formula Injection (CSV Injection).
**Learning:** When generating CSVs for human consumption, any field starting with `=`, `+`, `-`, or `@` must be sanitized (e.g., by prepending `'`), even if the data seems benign. Also, verifying scraping scripts requires care to avoid overwriting production datasets.
**Prevention:** Use a dedicated sanitization helper for all CSV exports and verify scripts in a sandbox or with mocked outputs.
