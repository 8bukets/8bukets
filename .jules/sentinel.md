## 2026-01-25 - CSV Injection Vulnerability in Scraper
**Vulnerability:** User-controlled data (titles, authors) starting with `=`, `+`, `-`, `@` was written directly to CSV, allowing formula injection.
**Learning:** Scraping external content and exporting to CSV without sanitization creates a risk if the output is opened in spreadsheet software.
**Prevention:** Prepend a single quote `'` to any field starting with these characters to force them to be treated as text.
