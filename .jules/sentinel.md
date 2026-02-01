## 2026-02-01 - CSV Injection in Scraper
**Vulnerability:** The scraper saved untrusted data directly to CSV files, allowing potential formula injection (CSV Injection) if the data contained special characters like `=`.
**Learning:** External data sources, even seemingly benign ones like blog post titles, must be treated as untrusted and sanitized before being written to formats that support executable content (like CSV/Excel).
**Prevention:** Always sanitize fields starting with `=`, `+`, `-`, or `@` by prepending a single quote when writing to CSV. Use a centralized sanitization method.
