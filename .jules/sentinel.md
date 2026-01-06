## 2024-02-14 - CSV Injection Vulnerability Pattern
**Vulnerability:** The scraper was writing user-controlled input (from external websites) directly to CSV files without sanitization. Malicious titles starting with `=`, `+`, `-`, or `@` could execute formulas in spreadsheet software.
**Learning:** Any application that exports untrusted data to CSV/Excel formats must consider "CSV Injection" (or Formula Injection) as a critical risk, even if the data source (like a blog) seems semi-trusted.
**Prevention:** Always sanitize strings before writing to CSV by prepending a single quote `'` if the string starts with formula-triggering characters.
