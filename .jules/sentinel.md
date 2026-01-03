## 2024-10-27 - CSV Formula Injection Vulnerability
**Vulnerability:** User-controlled input (like post titles or author names) was being written directly to CSV files without sanitization. If these fields started with special characters like `=`, `+`, `-`, or `@`, spreadsheet software would interpret them as formulas, potentially executing arbitrary commands or leaking data.
**Learning:** Even when scraping "public" data, if that data is viewed in a rich client like Excel, it can become an attack vector. Always treat data destined for CSV as potentially malicious.
**Prevention:** Implemented a `sanitize_for_csv` method that prepends a single quote (`'`) to any field starting with dangerous characters, forcing the spreadsheet to treat it as a literal string.
