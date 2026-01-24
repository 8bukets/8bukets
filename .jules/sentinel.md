## 2025-02-18 - CSV Injection in Scraper Output
**Vulnerability:** The scraper was writing untrusted input (post titles, authors) directly to CSV files without sanitization. Malicious websites could inject spreadsheet formulas (starting with =, +, -, @) which would execute when an analyst opens the CSV in Excel.
**Learning:** Even "read-only" data scraping can lead to RCE on the analyst's machine if the output format (CSV) is interpreted by smart readers like Excel.
**Prevention:** Always sanitize CSV fields by prepending a single quote `'` if the field starts with dangerous characters (`=`, `+`, `-`, `@`).
