## 2024-12-26 - CSV Injection / Formula Injection
**Vulnerability:** The scraper was writing user-controlled input (post titles, authors, etc.) directly into a CSV file. If a scraped field started with `=`, `+`, `-`, or `@`, it could be interpreted as a formula by spreadsheet applications (Excel, Google Sheets) when opened by a user.
**Learning:** Even when scraping "trusted" sites, the data structure (CSV) itself introduces vulnerabilities based on how *consumers* of that data (spreadsheet apps) interpret it. Input sanitization must consider the *destination* format's quirks.
**Prevention:** Sanitized all fields before writing to CSV by prepending a single quote `'` if the field starts with dangerous characters (`=`, `+`, `-`, `@`).
