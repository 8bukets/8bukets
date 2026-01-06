## Sentinel Journal

## 2026-01-06 - Protocol Validation in Scraper
**Vulnerability:** The scraper accepted any URL scheme (e.g., `javascript:`, `file:`) extracted from the target page, creating risks of stored XSS (in CSV/JSON outputs) and SSRF.
**Learning:** Even when using robust libraries like `aiohttp`, the logic extracting and storing URLs must explicitly validate protocols to ensure data integrity and safety.
**Prevention:** Enforced strict `http` and `https` protocol validation in `scraper.py` using `urllib.parse.urlparse`.
