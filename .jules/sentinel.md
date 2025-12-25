## 2024-05-22 - CSV Injection Prevention
**Vulnerability:** Scraped data was written directly to CSV files without sanitization, allowing for potential CSV/Formula Injection if the scraped content contained characters like '=', '+', '-', or '@'.
**Learning:** Even when data is scraped from a 'trusted' source, it should be treated as untrusted when exporting to formats like CSV that have executable capabilities in spreadsheet software.
**Prevention:** Implemented a `sanitize_for_csv` method that prepends a single quote (') to any field starting with dangerous characters before writing to CSV.
