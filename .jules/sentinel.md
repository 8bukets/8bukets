# Sentinel Journal

## 2026-01-28 - SSRF in Scraper
**Vulnerability:** The scraper utility accepted arbitrary URLs via CLI arguments without validation, allowing potential access to internal network resources (SSRF).
**Learning:** Even client-side or CLI tools can be vectors for SSRF if they are automated or exposed via other interfaces (like the scheduler).
**Prevention:** Always validate user-supplied URLs to ensure they point to public, expected schemes (HTTP/S) and do not resolve to private/local IP addresses before making requests.
