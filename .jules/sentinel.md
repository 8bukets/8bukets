## 2024-05-23 - [CSV Formula Injection Risk]
**Vulnerability:** The scraper writes user-controlled data (scraped titles, authors) directly to CSV files without sanitization. If these fields start with `=`, `+`, `-`, or `@`, spreadsheet software like Excel may execute them as formulas (CSV Injection).
**Learning:** Even simple data export features can introduce security risks if the consumption environment (Excel) interprets data as code.
**Prevention:** Sanitize all fields written to CSV by prepending a single quote `'` if they start with dangerous characters.
