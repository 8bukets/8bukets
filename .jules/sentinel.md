## 2026-01-26 - [Scraper URL Validation]
**Vulnerability:** Scraper was accepting arbitrary URL schemes (javascript:, data:) which could lead to Stored XSS in reports.
**Learning:** Always validate and sanitize data at the point of entry (scraping), especially when that data is later used in formats prone to injection (Markdown/HTML).
**Prevention:** Implemented strict whitelist validation for URL schemes (http/https) in the scraper.
