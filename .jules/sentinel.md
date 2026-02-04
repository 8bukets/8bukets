## 2025-02-18 - [CRITICAL] CSV Injection in Scraper
**Vulnerability:** Scraper data was written directly to CSV without sanitization, allowing Formula Injection (CSV Injection) if the scraped content contained `=`, `+`, `-`, or `@`.
**Learning:** Even when scraping "passive" content like blog posts, the data can be malicious if exported to formats like CSV/Excel that execute formulas.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending a single quote `'` to fields starting with dangerous characters.
