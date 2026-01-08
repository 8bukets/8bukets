## 2024-05-24 - CSV Injection Vulnerability
**Vulnerability:** The scraper was writing user-controlled data directly to CSV files without sanitization. This allows malicious actors to inject spreadsheet formulas (starting with =, +, -, @) which could execute arbitrary commands when opened in Excel/Sheets.
**Learning:** Always treat data destined for CSV files as untrusted. Even simple text fields can be dangerous if they start with specific characters.
**Prevention:** Sanitize all fields before writing to CSV by prepending a single quote (') to any value starting with =, +, -, or @.
