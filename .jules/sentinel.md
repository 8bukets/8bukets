## 2024-05-22 - CSV Injection Vulnerability
**Vulnerability:** User-controlled input (titles, authors, etc.) starting with `=`, `+`, `-`, or `@` was written directly to CSV files without sanitization. This allows malicious formulas to be executed when the CSV is opened in spreadsheet software (Excel, LibreOffice).
**Learning:** Standard CSV libraries (like Python's `csv` module) do not automatically sanitize against formula injection. They only handle delimiter escaping.
**Prevention:** Always prepend a single quote `'` to fields starting with dangerous characters (`=`, `+`, `-`, `@`) before writing to CSV.
