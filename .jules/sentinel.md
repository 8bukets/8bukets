## 2026-01-29 - CSV Injection in Scraper
**Vulnerability:** The scraper was writing untrusted input (titles, authors, etc.) directly to CSV files without sanitization, allowing for potential Formula Injection.
**Learning:** Even when scraping a 'known' site, the content can be manipulated or contain malicious data. CSVs are often treated as trusted data by spreadsheet software.
**Prevention:** Always sanitize fields starting with `=`, `+`, `-`, or `@` by prepending a single quote `'` when writing to CSV.
