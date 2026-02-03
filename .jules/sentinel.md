## 2026-02-03 - CSV Formula Injection Vulnerability
**Vulnerability:** User-controlled input (titles, authors) is written directly to CSV without sanitization. If fields start with `=`, `+`, `-`, or `@`, they could be executed as formulas in spreadsheet software.
**Learning:** External data should never be trusted when generating file formats that can execute code (like CSVs in Excel).
**Prevention:** Sanitize all fields by prepending a single quote `'` if they start with dangerous characters.
