## 2024-05-23 - CSV Injection in Scraper Export
**Vulnerability:** `scraper.py` exported user-controlled data (titles, authors, etc.) directly to CSV without sanitization.
**Learning:** Even when scraping "trusted" sites, content can be manipulated or contain characters that trigger CSV injection (Formula Injection) in spreadsheet software.
**Prevention:** Implement a `sanitize_for_csv` method that escapes characters `=`, `+`, `-`, `@` by prepending a single quote `'`.
