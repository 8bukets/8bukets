## 2024-03-24 - CSV Injection in Data Scrapers
**Vulnerability:** The scraper was writing untrusted input (web content) directly to CSV files without sanitization. This allowed potential CSV Injection (Formula Injection) where malicious content starting with `=`, `+`, `-`, or `@` could execute formulas in spreadsheet software.
**Learning:** Even when scraping "passive" data, format-specific vulnerabilities like CSV injection must be considered. Data that is safe in a browser (after XSS escaping) might not be safe in a spreadsheet.
**Prevention:** Always sanitize data written to CSVs by prepending a single quote `'` to fields starting with trigger characters (`=`, `+`, `-`, `@`), forcing them to be treated as text.
