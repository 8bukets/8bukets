## 2024-05-23 - Prevented CSV Formula Injection
**Vulnerability:** The scraper was writing unsanitized content directly to CSV files. Malicious website titles or authors starting with `=`, `@`, `+`, or `-` could execute arbitrary commands or formulas if the CSV was opened in spreadsheet software like Excel.
**Learning:** CSV files are not just plain text; they are interpreted by spreadsheet applications which can execute code. Trusting external input in CSV generation is a security risk.
**Prevention:** Implemented a `sanitize_for_csv` method that prepends a single quote `'` to any field starting with dangerous characters, forcing the application to treat the field as a string literal.
