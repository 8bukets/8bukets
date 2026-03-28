## 2025-02-18 - CSV Injection in Scraper Output
**Vulnerability:** The scraper exported data directly to CSV format without sanitizing fields. Maliciously crafted input (starting with =, +, -, @) could execute formulas when opened in spreadsheet software (Excel/LibreOffice).
**Learning:** Data extracted from web sources, even if simple text like titles or author names, must be treated as untrusted. When converting to CSV, special characters that trigger formulas must be escaped.
**Prevention:** Implement a sanitization layer for all CSV exports that prepends a single quote `'` to any field starting with `=, +, -, @`.
