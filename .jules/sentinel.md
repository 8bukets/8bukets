## 2024-05-23 - [CSV Injection Vulnerability in Scraper]
**Vulnerability:** The scraper was writing scraped titles and other fields directly to a CSV file without sanitization. This allowed for CSV Injection (Formula Injection) where malicious content (starting with =, +, -, @) could execute commands when the CSV is opened in spreadsheet software.
**Learning:** Even when scraping "trusted" sites, data should be treated as untrusted before exporting to formats that interpret formulas (like CSV/Excel).
**Prevention:** Sanitize all fields starting with dangerous characters by prepending a single quote (') before writing to CSV.
