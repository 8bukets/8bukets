## 2026-02-01 - Fix CSV Injection in Scraper
**Vulnerability:** `scraper.py` was writing untrusted user input directly to CSV files, allowing for CSV injection (formula injection) if fields started with `=`, `+`, `-`, or `@`.
**Learning:** Data extracted from websites should always be treated as untrusted, even if it looks benign. CSVs are executable formats in many contexts (Excel, LibreOffice).
**Prevention:** Always sanitize data before writing to CSVs by prepending a single quote `'` to fields starting with dangerous characters.
