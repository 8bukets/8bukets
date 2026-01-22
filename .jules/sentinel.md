## 2026-01-22 - [Scraper URL Validation]
**Vulnerability:** Scrapers using `urljoin` without scheme validation can allow `javascript:` or other malicious schemes if the source HTML is compromised or malicious.
**Learning:** `urljoin` resolves relative URLs against the base, but if the relative URL is actually absolute with a different scheme (like `javascript:`), it takes precedence.
**Prevention:** Always validate the scheme of extracted URLs is `http` or `https` before processing or storing them.
