## 2024-03-22 - CSV Injection Mitigation
**Vulnerability:** Scraper wrote untrusted user input directly to CSV files, allowing malicious inputs (e.g., `=1+1`) to be executed as formulas in Excel.
**Learning:** Even simple data export formats like CSV have injection risks. Libraries like `csv` in Python do not automatically sanitize for formula injection (CSV Injection).
**Prevention:** Always sanitize untrusted input before writing to CSV. Prepend a single quote `'` to fields starting with `=`, `+`, `-`, or `@`.
