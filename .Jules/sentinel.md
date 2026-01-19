## 2025-10-16 - CSV Injection Mitigation
**Vulnerability:** Scraped data (titles, authors, etc.) was being written directly to CSV files without sanitization. If a malicious website contained a title starting with `=`, `+`, `-`, or `@`, it could execute arbitrary formulas in the spreadsheet software of the user viewing the report (CSV Injection).
**Learning:** Data exported to CSVs is not just text; it can be executable code in the context of spreadsheet applications. Trusting scraped content implicitly is dangerous.
**Prevention:** Always sanitize fields before writing to CSV. A common and effective method is to prepend a single quote `'` to any field starting with the dangerous characters (`=`, `+`, `-`, `@`).
