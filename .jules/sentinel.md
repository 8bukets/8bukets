## 2026-01-16 - CSV Injection Risks in Exports
**Vulnerability:** The scraper was exporting user-controlled data (titles, authors) directly to CSV without sanitization, allowing Formula Injection (CSV Injection).
**Learning:** Any data starting with `=`, `+`, `-`, or `@` can be interpreted as a formula by spreadsheet software, leading to potential code execution.
**Prevention:** Always sanitize CSV fields by prepending a single quote `'` to values starting with these characters.
