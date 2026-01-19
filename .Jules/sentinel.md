## 2026-01-19 - Stored XSS in Scraper
**Vulnerability:** The scraper extracted `href` attributes directly from HTML and stored them in the database without validation. Malicious sites could inject `javascript:` or `data:` URIs, leading to Stored XSS when these links are rendered in reports.
**Learning:** Scrapers trusting external content structure (like `href`) can be a vector for XSS if the data is later rendered in a context that executes scripts (like HTML reports).
**Prevention:** Always validate extracted URLs against an allowlist of schemes (`http`, `https`) before storage.
