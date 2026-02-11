## 2026-02-06 - CSV Injection Vulnerability
**Vulnerability:** The scraper was exporting data to CSV without sanitizing fields. Malicious input starting with `=`, `+`, `-`, or `@` could be executed as formulas in Excel.
**Learning:** Always sanitize user-controlled input before writing to CSV files, especially if they might be opened in spreadsheet software.
**Prevention:** Prepend a single quote `'` to fields starting with dangerous characters.
