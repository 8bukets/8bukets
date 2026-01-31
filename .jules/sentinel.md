# Sentinel Journal

This journal records critical security learnings, vulnerabilities found, and prevention strategies.

## 2026-01-31 - Scraper SSRF Vulnerability via Pagination

**Vulnerability:** The `scrape_informatic.py` scraper extracted the "Previous" page URL from the HTML and followed it immediately without validation. An attacker could inject a malicious link (pointing to internal network or other sensitive targets) into the pagination element, causing the server to perform an arbitrary GET request (SSRF).

**Learning:** Automated scrapers that follow links must treat extracted URLs as untrusted user input. Even "official" navigation elements like pagination can be compromised or spoofed.

**Prevention:** Implement strict URL validation (`is_safe_url`) before making any request. Validate the URL scheme (http/https only) and ensure the domain matches an allowlist (in this case, the `BASE_URL` domain).
