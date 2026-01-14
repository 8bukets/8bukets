## 2024-05-22 - CSV Injection Prevention
**Vulnerability:** User-controlled input (e.g., article titles) written directly to CSV files without sanitization.
**Learning:** Even "read-only" data scraping can be dangerous if the output format (CSV) is interpreted by other tools (Excel) as executable code (formulas).
**Prevention:** Sanitized all CSV output by prepending `'` to fields starting with `=`, `+`, `-`, or `@` to force them to be treated as strings.
