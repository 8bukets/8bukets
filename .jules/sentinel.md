## 2025-10-27 - CSV Injection in Scraper Outputs
**Vulnerability:** Scraped content (titles, authors) was exported directly to CSV files. Malicious content starting with =, +, -, or @ could execute formulas in spreadsheet software.
**Learning:** Data exported to CSV is not just text; it can be interpreted as code by spreadsheet applications.
**Prevention:** Always escape fields starting with dangerous characters by prepending a single quote (') before writing to CSV.
