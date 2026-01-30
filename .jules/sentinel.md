## 2026-01-30 - CSV Injection in Scraper
**Vulnerability:** The scraper saved untrusted input (titles, authors) directly to CSV, allowing Formula Injection (CSV Injection) if the text started with `=`, `+`, `-`, or `@`.
**Learning:** Even simple data export formats like CSV can be vectors for attacks if opened in spreadsheet software. Untrusted input must always be sanitized before export.
**Prevention:** Sanitized all CSV fields by prepending a single quote `'` to dangerous characters.
