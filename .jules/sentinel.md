## 2025-01-26 - CSV Injection Vulnerability in Data Export
**Vulnerability:** The scraper was writing untrusted user input directly to CSV files without sanitization. Malicious input starting with `=`, `+`, `-`, or `@` could trigger formula execution in spreadsheet software (CSV Injection).
**Learning:** `csv.writer` does not automatically sanitize fields against formula injection, only delimiter escaping.
**Prevention:** Always sanitize data before writing to CSV by prepending a single quote `'` to fields starting with dangerous characters.
