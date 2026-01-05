## 2024-02-14 - CSV Injection in Scraper Output
**Vulnerability:** The scraper writes user-controlled content (e.g., post titles, authors) directly to a CSV file. If a field starts with characters like `=`, `+`, `-`, or `@`, it could be interpreted as a formula by spreadsheet software (Excel, LibreOffice), potentially leading to code execution (CSV Injection).
**Learning:** Even when scraping "static" sites, content can be malicious. Generating CSV files for user consumption requires sanitizing fields to prevent formula injection.
**Prevention:** Prefix any field starting with `=`, `+`, `-`, or `@` with a single quote `'` to force it to be treated as text.
