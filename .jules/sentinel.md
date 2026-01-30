# Sentinel Journal 🛡️

This journal records critical security learnings and vulnerability patterns found in the codebase.

## 2026-01-30 - Unvalidated Pagination SSRF
**Vulnerability:** The `scrape_informatic.py` script blindly followed `href` attributes in pagination links without validating the domain, allowing potential SSRF if the target site returned malicious links.
**Learning:** Web scrapers often trust the structure of the site they scrape, but `href` attributes are untrusted input. `requests` will follow absolute URLs to any domain.
**Prevention:** Always validate extracted URLs against an allowlist of domains before fetching. Use `urljoin` to handle relative paths correctly and `urlparse` to check the `netloc`.
