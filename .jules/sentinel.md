## 2026-01-28 - CSV Injection in Scraper Output
**Vulnerability:** The scraper was writing unsanitized user-controlled input (article titles, authors, etc.) directly to CSV files. This could allow CSV Injection (Formula Injection) where malicious website content starting with `=`, `+`, `-`, or `@` could execute arbitrary formulas or commands when opened in spreadsheet software.
**Learning:** Even internal data processing tools like scrapers need output encoding/sanitization if their output (CSV) is consumed by users in rich client applications (Excel). Trusting scraped content is dangerous.
**Prevention:** Always sanitize data written to CSV files by prepending a single quote `'` to fields starting with dangerous characters (`=`, `+`, `-`, `@`).
