## 2026-02-04 - CSV Injection in Scraper Output
**Vulnerability:** User-controlled input (titles, authors) was written directly to CSV files without sanitization, allowing Formula Injection (CSV Injection).
**Learning:** Even simple data export formats like CSV can be vectors for client-side attacks if opened in spreadsheet software. Sanitization is crucial when moving data between contexts (Web -> CSV).
**Prevention:** Always sanitize fields starting with `=`, `+`, `-`, `@` by prepending a single quote `'` before writing to CSV.
