## 2026-01-31 - CSV Injection in Scraper
**Vulnerability:** The scraper wrote untrusted data (titles, dates, etc.) directly to a CSV file without sanitization. Malicious titles starting with `=`, `+`, `-`, or `@` could execute formulas when opened in spreadsheet software.
**Learning:** Even simple data export features can introduce vulnerabilities if the format (like CSV) interprets special characters as executable instructions.
**Prevention:** Always sanitize data before writing to CSV. Prepending a single quote `'` to fields starting with dangerous characters is a standard mitigation.
