## 2026-01-29 - [Scraper Pagination SSRF Risk]
**Vulnerability:** Scraper followed pagination links (`href`) blindly without validation, allowing potential redirection to internal/malicious networks (SSRF).
**Learning:** Even hardcoded base URLs don't protect against SSRF if the navigation logic trusts external HTML content for the "next" URL.
**Prevention:** Always validate that extracted navigation URLs match the expected domain (strict allowlist) before requesting them.
