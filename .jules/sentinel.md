# Sentinel's Security Journal

## 2026-01-17 - Unrestricted URL Fetching (SSRF)
**Vulnerability:** The `scraper.py` script blindly accepts URLs and fetches them using `requests.get()` without validation. This allows Server-Side Request Forgery (SSRF) where the scraper could be directed to access internal network resources (localhost, metadata services).
**Learning:** Scrapers acting on external data must treat target URLs as untrusted input. Redirects and initial URLs must be validated against a whitelist of allowed protocols (http/https) and a blacklist of internal IP ranges.
**Prevention:** Implement a `is_safe_url` validator that parses URLs, checks schemes, and validates hostnames before making any network requests.
