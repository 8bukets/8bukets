## 2026-02-02 - Fix CSV Injection in Scraper
**Vulnerability:** The scraper was writing untrusted input (titles, authors, etc.) directly to a CSV file. If these fields started with `=`, `+`, `-`, or `@`, opening the CSV in Excel could execute malicious formulas (CSV Injection).
**Learning:** Standard CSV writers do not automatically sanitize input against formula injection. Untrusted data must always be sanitized before being written to CSVs intended for spreadsheet software.
**Prevention:** Implement a sanitization layer that prepends a single quote `'` to any field starting with formula characters (`=`, `+`, `-`, `@`) before writing to CSV.
