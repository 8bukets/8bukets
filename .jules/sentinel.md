## 2024-03-25 - CSV Injection Fix
**Vulnerability:** The scraper was writing untrusted input (titles, authors, etc.) directly to CSV files without sanitization. If a field started with `=`, `+`, `-`, or `@`, it could be interpreted as a formula by spreadsheet software (Excel, LibreOffice), leading to potential code execution (CSV Injection).
**Learning:** Even internal tools that generate CSVs need to assume the output will be opened by humans in vulnerable software. The "trust boundary" extends to the tools used to view the data.
**Prevention:** Always escape fields starting with formula characters (`=`, `+`, `-`, `@`) by prepending a single quote `'` when generating CSV files from untrusted data.
