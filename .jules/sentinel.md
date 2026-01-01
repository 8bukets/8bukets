## 2024-05-23 - Prevent CSV Formula Injection
**Vulnerability:** User-controlled data (scraped titles, authors, etc.) was being written directly to CSV files without sanitization. If a field started with `=`, `+`, `-`, or `@`, it could be interpreted as a malicious formula by spreadsheet software.
**Learning:** Even internal tools that generate CSVs are vulnerable if the output is consumed by users in spreadsheet applications. Scraping targets are untrusted inputs.
**Prevention:** Sanitize all fields before writing to CSV by prepending a single quote `'` if the value starts with dangerous characters.
