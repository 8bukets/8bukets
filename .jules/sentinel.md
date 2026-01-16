## 2024-02-14 - SSRF Protection in Web Scraper
**Vulnerability:** The scraper accepted any URL scheme (file://, ftp://) and local IP addresses, allowing potential Server-Side Request Forgery (SSRF) and local file read access.
**Learning:** Standard HTTP libraries like `requests` may support schemes other than HTTP/HTTPS or resolve to local addresses by default. Explicit validation is necessary for user-provided URLs.
**Prevention:** Implemented a `validate_url` method in `BlogScraper` to enforce an allowlist of schemes (http, https) and a blocklist of local hostnames/IPs.
