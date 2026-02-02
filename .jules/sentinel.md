## 2024-05-22 - CSV Injection in Scraper
**Vulnerability:** `scraper.py` was writing unsanitized input (titles, authors) directly to CSV, allowing formula injection.
**Learning:** CSVs generated from external input must be sanitized against formula injection (`=`, `+`, `-`, `@`).
**Prevention:** Use a `sanitize_csv_field` helper to prepend `'` to risky fields.
