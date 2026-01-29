## 2026-01-29 - Stored XSS via Scraper
**Vulnerability:** The scraper was extracting raw URLs (`href` attributes) and saving them to the database without validation. These URLs were later used in Markdown reports. A malicious site could inject `javascript:alert(1)` links which, when rendered in Markdown, became clickable XSS vectors.
**Learning:** Scraping external content is equivalent to accepting user input. Trusting `href` attributes blindly assumes the source is benign, which defeats the purpose of a security boundary.
**Prevention:** Always sanitize scraped data. For URLs, strictly whitelist protocols (`http`, `https`) before storage. Treat all external data as untrusted.
