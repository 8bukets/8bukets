## 2026-02-03 - CSV Formula Injection Vulnerability
**Vulnerability:** The `MarkPositionScraperAsync` class saved scraped data directly to CSV format without sanitization. Maliciously crafted post titles or author names starting with `=`, `+`, `-`, or `@` could execute formulas when the CSV is opened in spreadsheet software (Excel, LibreOffice).
**Learning:** Data extracted from external websites, even trusted ones, must be treated as untrusted when exporting to rich formats like CSV where formula execution is possible.
**Prevention:** Implemented a `sanitize_for_csv` method that prepends a single quote (`'`) to any field starting with dangerous characters, neutralizing the formula.
