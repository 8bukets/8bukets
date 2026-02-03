## 2026-02-03 - CSV Injection in Scraper
**Vulnerability:** The scraper was writing untrusted data (titles, authors, etc.) directly to CSV files without sanitization, allowing for Formula Injection if the data contained special characters like `=`, `+`, `-`, `@`.
**Learning:** Even when scraping "trusted" sites, data should be treated as untrusted. CSVs are particularly vulnerable to formula execution in spreadsheet software.
**Prevention:** Always sanitize data before writing to CSV by prepending a single quote `'` to fields starting with dangerous characters.
