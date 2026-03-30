## 2024-05-23 - CSV Injection Vulnerability
**Vulnerability:** Scraper data was written directly to CSV without sanitization, allowing Formula Injection (CSV Injection) via fields starting with `=`, `+`, `-`, or `@`.
**Learning:** Scraped data is untrusted user input. Even if it looks like "just text", specific characters can trigger execution in spreadsheet software.
**Prevention:** Always sanitize data before writing to CSV. Prepend a single quote `'` to fields starting with dangerous characters to force them to be treated as strings.
