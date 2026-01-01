## 2024-05-23 - Prevent CSV Formula Injection
**Vulnerability:** Scraper was writing user-controlled data directly to CSV without sanitization, allowing Formula Injection (CSV Injection).
**Learning:** Even internal tools generating reports can be vectors for attacks if the output is consumed by spreadsheet software.
**Prevention:** Sanitize fields starting with `=`, `+`, `-`, or `@` by prepending a single quote `'` before writing to CSV.
