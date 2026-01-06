## 2024-03-24 - CSV Injection Vulnerability
**Vulnerability:** User-controlled input (scraped titles/authors) was written directly to CSV files without sanitization. If the input started with `=`, `+`, `-`, or `@`, it could be interpreted as a formula by spreadsheet software, leading to potential command execution or data exfiltration on the user's machine.
**Learning:** Even internal tools generating CSVs for analysis can be vectors for attacks if the source data (web content) is untrusted. Simple CSV writers do not automatically escape formula triggers.
**Prevention:** Implemented a `sanitize_for_csv` method that prepends a single quote `'` to any field starting with dangerous characters. This forces the spreadsheet to treat the content as a string.
