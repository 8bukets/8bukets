## 2025-02-18 - CSV Injection in Scraper
**Vulnerability:** The `OracleNewsScraper` was writing scraped data directly to CSV files without sanitization. Maliciously crafted input (starting with `=`, `+`, `-`, `@`) could lead to formula injection when opened in spreadsheet software.
**Learning:** Even when scraping "trusted" sites, the data structure might contain characters that are dangerous in specific contexts like CSV/Excel. Data must always be sanitized for the target sink.
**Prevention:** Implemented `sanitize_for_csv` to prepend a single quote `'` to any field starting with dangerous characters before writing to CSV.
