## 2026-01-18 - Async SSRF Protection
**Vulnerability:** The `scraper.py` blindly accepted URLs for fetching, making it vulnerable to Server-Side Request Forgery (SSRF) where it could be used to scan internal network resources (e.g., localhost ports).
**Learning:** In async Python (`aiohttp`), DNS resolution happens implicitly. To prevent SSRF, we must explicitly resolve the hostname using `loop.getaddrinfo` and validate the resulting IP address against private/loopback ranges using the `ipaddress` module *before* making the request.
**Prevention:** Always validate user-provided or external URLs using an `is_safe_url` helper that enforces HTTP/HTTPS schemes and blocks private/loopback IP addresses by pre-resolving the hostname.
