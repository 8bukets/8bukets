## 2025-10-16 - CSV Injection (Formula Injection)
**Vulnerability:** User-controlled input (like article titles or authors) that starts with `=`, `+`, `-`, or `@` was written directly to CSV files without sanitization. This allows malicious data to execute formulas (e.g., cmd execution) when the CSV is opened in spreadsheet software like Excel.
**Learning:** Even when scraping "trusted" sites, data should be treated as untrusted. CSVs are not just text files; they are executable formats for spreadsheet applications.
**Prevention:** Always prepend a single quote `'` to any field starting with risky characters before writing to CSV. This forces the application to treat the cell as a string literal.
