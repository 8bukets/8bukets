## 2024-03-25 - Prevented CSV Injection (Formula Injection)
**Vulnerability:** User-controlled data (scraped titles, authors, etc.) was being written directly to CSV files without sanitization. If a field started with `=`, `+`, `-`, or `@`, spreadsheet software (Excel, LibreOffice) would execute it as a formula, potentially leading to data exfiltration or command execution.
**Learning:** Even internal data scraping tools need output encoding. When generating CSVs that might be opened by humans in spreadsheet software, always escape fields that could be interpreted as formulas.
**Prevention:** Implemented a `sanitize_for_csv` method that prepends a single quote `'` to any field starting with dangerous characters (`=`, `+`, `-`, `@`).
