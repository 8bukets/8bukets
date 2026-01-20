## 2025-10-16 - [CSV Injection (Formula Injection) in Scraper]
**Vulnerability:** User-controlled input (scraped data) was written directly to CSV files without sanitization. Fields starting with `=`, `+`, `-`, or `@` could be interpreted as formulas by spreadsheet software, leading to potential command execution or data exfiltration.
**Learning:** Even internal data scraping tools need output encoding/sanitization if the artifacts (CSVs) are intended for human consumption via spreadsheet applications.
**Prevention:** Always sanitize data written to CSVs by prepending a single quote `'` to fields starting with trigger characters (`=`, `+`, `-`, `@`).
