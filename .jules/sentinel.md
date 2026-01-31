# Sentinel Journal

## 2026-01-31 - CSV Injection in Scraper Output
**Vulnerability:** User-controlled input scraped from websites was written directly to CSV files without sanitization. This allows malicious actors to inject formulas (starting with =, +, -, @) that execute when the CSV is opened in Excel.
**Learning:** Even "read-only" data from external sources must be treated as untrusted when exporting to formats with executable capabilities like CSV (Excel).
**Prevention:** Always sanitize fields starting with `=`, `+`, `-`, or `@` by prepending a single quote `'` before writing to CSV.
