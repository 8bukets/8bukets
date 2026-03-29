## 2026-01-22 - CSV Injection in Scraper
**Vulnerability:** `scraper.py` exported user-controlled data (e.g., article titles) directly to CSV without sanitization, allowing Formula Injection if opened in Excel.
**Learning:** Even in automated scrapers, data from external websites must be treated as untrusted. CSVs are not just text files; they are executable by spreadsheet software.
**Prevention:** Always sanitize fields starting with `=`, `+`, `-`, `@` by prepending a single quote `'` before writing to CSV. Use a centralized sanitization method for all CSV exports.
