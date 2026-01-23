## 2026-01-23 - CSV Injection in Scraper Output
**Vulnerability:** `scraper.py` wrote user-controlled fields (like title, author) directly to a CSV file without sanitization. Malicious titles starting with `=`, `+`, `-`, or `@` could execute arbitrary formulas/commands when opened in Excel.
**Learning:** Even in automated backend scripts, output formats like CSV can be vectors for client-side attacks if they are consumed by humans in vulnerable software (like Excel).
**Prevention:** Always sanitize fields starting with special characters (`=`, `+`, `-`, `@`) by prepending a single quote `'` when writing to CSVs.
