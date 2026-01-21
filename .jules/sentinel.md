## 2026-01-21 - [CSV Injection in Data Exports]
**Vulnerability:** User-controlled data (titles, authors) was written directly to CSV files without sanitization, allowing Formula Injection (CSV Injection).
**Learning:** Any application generating CSV files for user consumption (opening in Excel/Sheets) must treat fields starting with `=`, `+`, `-`, `@` as dangerous.
**Prevention:** Implemented `sanitize_for_csv` method in the scraper to prepend `'` to dangerous fields. Future CSV exports must verify this sanitization.
