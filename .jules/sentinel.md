## 2024-05-22 - CSV Injection Vulnerability in Scraper
**Vulnerability:** The scraper was writing untrusted user input (titles, authors, categories) directly to a CSV file without sanitization. This allows for CSV Injection (Excel Macro Injection) where malicious input starting with =, +, -, or @ could execute arbitrary formulas or commands when opened in Excel.
**Learning:** Even when scraping "safe" blogs, the content can be manipulated or contain payloads that target data analysts. Always assume external data is hostile.
**Prevention:** Sanitize all fields written to CSV by prepending a single quote `'` if they start with dangerous characters. This forces Excel to treat the cell as text.
