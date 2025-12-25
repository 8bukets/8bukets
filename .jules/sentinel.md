# Sentinel Journal

## 2023-10-27 - [CSV Injection in Scraper]
**Vulnerability:** Scraper was saving user-controlled content (titles, authors) directly to CSV without sanitization. Malicious input starting with =, +, -, @ could execute formulas in Excel.
**Learning:** Even when scraping trusted sites, data can be manipulated. Always sanitize data before exporting to formats that interpret content (like CSV/Excel).
**Prevention:** Implemented sanitize_for_csv to quote dangerous characters.
