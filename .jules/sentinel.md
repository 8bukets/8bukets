## 2026-01-15 - CSV Injection (Formula Injection)
**Vulnerability:** User-controlled input (titles, authors) starting with `=`, `@`, `+`, or `-` was written directly to CSV files without sanitization.
**Learning:** Even internal data collection tools (scrapers) can introduce vulnerabilities if the output is consumed by spreadsheet software (Excel/Sheets), which executes formulas.
**Prevention:** Always sanitize data written to CSVs by prepending a single quote `'` to fields starting with dangerous characters.
