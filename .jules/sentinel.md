## 2025-02-17 - CSV Injection in Scraper
**Vulnerability:** The scraper was exporting user-controlled data (titles, authors) directly to CSV without sanitization, allowing Formula Injection (CSV Injection).
**Learning:** Python's `csv` module does not automatically escape characters that start formulas (like `=`, `+`, `-`, `@`) which are interpreted by spreadsheet software.
**Prevention:** Always sanitize untrusted input before writing to CSV by prepending a single quote `'` to fields starting with dangerous characters.
