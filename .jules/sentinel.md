## 2026-01-17 - SSRF in Scraper Pagination
**Vulnerability:** The web scraper blindly trusted the `href` in the "Next Page" link, allowing it to be redirected to internal network resources (SSRF).
**Learning:** Scrapers must treat all extracted links as untrusted input, even from seemingly safe sites, as they can be compromised or manipulated.
**Prevention:** Implement strict `is_safe_url` validation that checks URL schemes and blocks private/loopback IP addresses before fetching any extracted link.
