## 2024-05-24 - CSV Injection Prevention
**Vulnerability:** The scraper was writing untrusted input (blog post titles, authors, etc.) directly into a CSV file without sanitization. If a malicious actor created a post with a title like `=cmd|' /C calc'!A0`, it could execute arbitrary code when opened in Excel.
**Learning:** Even simple data export features can introduce significant security risks if the data is consumed by rich-client applications like Excel.
**Prevention:** Always prepend a single quote `'` to any field starting with `=`, `+`, `-`, or `@` when generating CSV files.
