## 2025-10-16 - CSV Injection Vulnerability
**Vulnerability:** User-controlled input (e.g., blog post titles) was written directly to CSV files without sanitization. An attacker could craft a title starting with `=`, `+`, `-`, or `@` to execute malicious formulas when the CSV is opened in Excel/Numbers.
**Learning:** Even internal data processing scripts (like scrapers) must treat external input as untrusted, especially when the output format (like CSV) has interpreted execution features.
**Prevention:** Always sanitize data before writing to CSV. Implemented a `sanitize_for_csv` method that prepends a single quote `'` to fields starting with dangerous characters.
