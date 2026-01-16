# Sentinel's Journal

## 2025-02-14 - Missing URL Validation in Scraper
**Vulnerability:** The scraper lacked validation for URL schemes and domains, which could allow SSRF or processing of malicious links if the source page contained absolute URLs pointing to attacker-controlled sites.
**Learning:** Even when scraping a specific site, relying on `urljoin` and string filtering is insufficient. Explicit validation of schemes and domains is necessary to ensure data integrity and security, especially when data is consumed by downstream agents.
**Prevention:** Implement a strict `validate_url` method that checks for allowed schemes (http/https) and authorized domains (e.g., oracle.com) before fetching or storing URLs.
