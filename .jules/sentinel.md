## 2024-05-23 - CSV Injection in Scraper
**Vulnerability:** The scraper was writing untrusted data (article titles, authors, etc.) directly into CSV files without sanitization. If a website contained an article title starting with `=, +, -, @`, it could trigger formula execution when opened in Excel (CSV Injection).
**Learning:** Even simple data export formats like CSV can be vectors for attacks if the consuming application (Excel) interprets the data as code.
**Prevention:** Always escape fields starting with `=, +, -, @` by prepending a single quote `'` when generating CSVs.
