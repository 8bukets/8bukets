## 2026-01-14 - Scraper SSRF Vulnerability
**Vulnerability:** The `BlogScraper` blindly fetched URLs found in the `next_page` link without validating the domain or scheme, allowing potential Server-Side Request Forgery (SSRF) if the target site linked to internal or malicious URLs.
**Learning:** Scrapers that recursively follow links must validate that those links belong to the expected domain and use safe protocols (http/https). Trusting external content to provide safe URLs is a risk.
**Prevention:** Implement strict URL validation in the fetching logic. Whitelist allowed domains (e.g., the base URL's domain) and schemes.
