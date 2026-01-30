## 2026-01-30 - CSV Injection in Scraper
**Vulnerability:** Scraped content (titles, authors) was written to CSV without sanitization, allowing Formula Injection.
**Learning:** Python's csv module handles formatting but not content security. Formula injection is a distinct risk.
**Prevention:** Sanitize fields starting with =, +, -, @ by prepending a single quote.
