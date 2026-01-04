## 2025-02-18 - CSV Injection Vulnerability
**Vulnerability:** The `scraper.py` script was writing scraped data directly to a CSV file without sanitization. If the scraped content (e.g., titles, dates) began with characters like `=`, `+`, `-`, or `@`, spreadsheet applications (like Excel) would interpret them as formulas, potentially executing arbitrary code.
**Learning:** Even when scraping "safe" websites, the data should be treated as untrusted, especially when exporting to formats like CSV that have executable features.
**Prevention:** Sanitized all fields before writing to CSV by prepending a single quote `'` to any field starting with dangerous characters. This forces the spreadsheet software to treat the content as text.
