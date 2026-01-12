## 2024-03-24 - CSV Formula Injection
**Vulnerability:** The scraper was writing user-controlled input (from scraped websites) directly to a CSV file without sanitization. Malicious titles or authors starting with `=`, `+`, `-`, or `@` could execute arbitrary formulas in spreadsheet software (Formula Injection).
**Learning:** CSV files are not just text files; they are executable when opened in spreadsheet applications. Input validation must account for context-specific vulnerabilities like DDE/DCOM execution in Excel.
**Prevention:** Sanitize all fields written to CSV by prepending a single quote `'` if they start with dangerous characters (`=`, `+`, `-`, `@`). This forces the spreadsheet to treat the content as a string literal.
