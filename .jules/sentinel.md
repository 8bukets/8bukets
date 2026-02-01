# Sentinel Journal

## 2024-05-22 - CSV Injection Vulnerability in Scraper Output
**Vulnerability:** User-controlled input (Post titles, Authors, Categories) was written directly to CSV files without sanitization. If a malicious user created a post with a title starting with `=`, `+`, `-`, or `@`, it could execute formulas when the CSV is opened in spreadsheet software (like Excel), potentially leading to data exfiltration or arbitrary code execution on the analyst's machine.
**Learning:** Even "read-only" data scraping can be dangerous if the output format (CSV) interprets certain characters as executable code. Trusting that scraped content is "passive" text is a mistake when bridging to rich-client applications like Excel.
**Prevention:** Always sanitize data before writing to CSV. Prepend a single quote `'` to any field starting with formula triggers (`=`, `+`, `-`, `@`) to force the spreadsheet to treat it as a string literal.
