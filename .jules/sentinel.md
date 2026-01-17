# Sentinel Journal

## 2024-05-24 - CSV Injection in Scraper Data
**Vulnerability:** Scraper was saving untrusted external data directly to CSV without sanitization. Malicious titles starting with `=`, `+`, `-`, `@` could execute formulas in Excel (CSV Injection).
**Learning:** Even "read-only" scrapers can vector attacks to analysts who open the data. `csv.writer` does not sanitize for Excel formulas by default.
**Prevention:** Sanitized all fields in `save_data` by prepending `'` if they start with dangerous characters. Added `sanitize_for_csv` helper.
