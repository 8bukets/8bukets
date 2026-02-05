## 2025-02-21 - [CSV Injection Vulnerability in Scraper]
**Vulnerability:** The scraper was taking user-controlled content (titles, authors, etc.) and writing it directly to a CSV file. Malicious input starting with =, +, -, or @ could execute formulas in spreadsheet software (Formula Injection).
**Learning:** Even when scraping a "trusted" site, the content might be manipulated or contain patterns that are dangerous in specific output formats like CSV. Always sanitize data at the boundary of the output format.
**Prevention:** Implemented a `sanitize_for_csv` method that prepends a single quote `'` to fields starting with dangerous characters, treating them as text literals.
