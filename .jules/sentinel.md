## 2024-05-21 - CSV Injection Prevention
**Vulnerability:** User-controlled data (titles, authors) was written directly to CSV files, allowing Formula Injection (CWE-1236).
**Learning:** Standard Python `csv` library does not sanitize fields starting with `=`, `+`, `-`, `@` which are interpreted as formulas by spreadsheet software.
**Prevention:** Implement a sanitization layer that prepends a single quote `'` to any field starting with these characters before writing to CSV. Added `sanitize_csv_field` helper in scraper.
