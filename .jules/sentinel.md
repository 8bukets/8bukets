## 2024-05-22 - CSV Injection Prevention
**Vulnerability:** The scraper was writing untrusted user input directly to CSV files without sanitization. This allowed for CSV Injection (Formula Injection) where a malicious title starting with `=`, `+`, `-`, or `@` could execute arbitrary code when opened in Excel/Sheets.
**Learning:** Even simple data export formats like CSV can be vectors for code execution if they are destined for spreadsheet software. Standard `csv` libraries do not automatically sanitize for formula injection.
**Prevention:** Implemented a `sanitize_for_csv` method that prepends a single quote (`'`) to any field starting with dangerous characters (`=`, `+`, `-`, `@`). This forces the spreadsheet software to treat the field as text rather than a formula.
