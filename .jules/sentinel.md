## 2026-01-15 - CSV Injection in Scraper Data
**Vulnerability:** Scraped data (titles, authors) was written directly to CSV without sanitization, allowing malicious formulas (starting with =, +, -, @) to be executed by spreadsheet software.
**Learning:** External data sources, even 'passive' ones like web scraping, must be treated as untrusted user input when generating file formats that have executable capabilities like CSV (Excel).
**Prevention:** Implemented a `sanitize_for_csv` method that prepends a single quote to fields starting with dangerous characters.
