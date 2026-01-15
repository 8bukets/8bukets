## 2026-01-15 - Unrestricted Pagination SSRF
**Vulnerability:** The `scrape_informatic.py` script blindly followed pagination links (`nav-previous`) without validation, allowing potential SSRF or redirection to malicious domains if the target site was compromised.
**Learning:** Even trusted target sites can have their HTML modified to include malicious links. Scrapers effectively act as a proxy and can be used to scan internal networks or access restricted local files if not constrained.
**Prevention:** Implement strict URL validation (`is_safe_pagination_url`) that enforces allowed schemes (http/https) and domains (same origin) before making any HTTP request.
