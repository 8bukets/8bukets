## 2024-12-26 - CSV Injection in Scraper
**Vulnerability:** The scraper wrote untrusted external data (post titles, authors, etc.) directly to a CSV file. Malicious input starting with =, +, -, @ could execute formulas in Excel/Calc (CSV Injection).
**Learning:** Even simple data collection scripts can introduce client-side vulnerabilities if output formats like CSV are not handled defensively.
**Prevention:** Always sanitize fields starting with dangerous characters by prepending a single quote (') when writing to CSV.
