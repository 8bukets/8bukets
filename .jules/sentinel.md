## 2024-03-24 - CSV Injection Prevention
**Vulnerability:** Unsanitized user-controlled data (e.g., blog post titles, authors) written to CSV files allows for Formula Injection (CSV Injection).
**Learning:** Even simple data exports like CSVs can be vectors for attacks if spreadsheet software interprets cell contents starting with =, +, -, or @ as formulas.
**Prevention:** Sanitize all fields written to CSVs by prepending a single quote `'` if they start with dangerous characters.
