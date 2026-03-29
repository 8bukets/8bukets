## 2026-01-23 - CSV Injection in Scraper Output
**Vulnerability:** `scraper.py` wrote user-controlled data (titles, authors) directly to CSV files without sanitization. Malicious input starting with `=`, `+`, `-`, or `@` could execute formulas (CSV Injection) when opened in spreadsheet software.
**Learning:** CSV files are not just text; they are executable code in the context of spreadsheet applications. Direct writing without escaping is dangerous.
**Prevention:** Always sanitize fields starting with `=`, `+`, `-`, or `@` by prepending a single quote `'` when generating CSV files from untrusted data.
