## 2026-01-28 - CSV Injection in Scraper
**Vulnerability:** The scraper was writing user-controlled input directly to CSV files without sanitization, allowing for Formula Injection.
**Learning:** Scraped data can contain malicious payloads targeting data analysts' tools (like Excel).
**Prevention:** Always sanitize fields starting with `=`, `+`, `-`, or `@` by prepending a single quote `'` when exporting to CSV.
