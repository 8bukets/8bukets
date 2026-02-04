## 2026-02-04 - Fix CSV Injection in Scraper
**Vulnerability:** The scraper saved untrusted input (e.g. titles, authors) directly to CSV files. If these fields started with special characters like `=`, `@`, `+`, or `-`, they could be interpreted as formulas by spreadsheet software (Excel, LibreOffice), potentially leading to code execution (CSV Injection).
**Learning:** Even when scraping "static" sites, data can be crafted to exploit client-side tools used to view the data. Trusting the source content to be "safe" for all output formats is a mistake.
**Prevention:** Always sanitize data before exporting to CSV. Specifically, prepend a single quote `'` to fields starting with formula triggers (`=`, `@`, `+`, `-`) to force them to be treated as text.
