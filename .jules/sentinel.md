## 2026-01-31 - CSV Injection in Web Scraper
**Vulnerability:** Scraped data (titles, authors, categories) was written directly to CSV without sanitization. Malicious websites could host content starting with `=`, `+`, `-`, or `@` to trigger arbitrary code execution in spreadsheet software like Excel.
**Learning:** Even "passive" data collection can introduce vulnerabilities if the export format (CSV) is interpreted by rich client applications. Always treat scraped content as untrusted user input.
**Prevention:** Implement a sanitization layer for CSV exports that detects formula triggers (fields starting with `=`, `+`, `-`, `@`) and neutralizes them by prepending a single quote (`'`).
