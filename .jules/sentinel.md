## 2026-02-06 - [SSRF in Scraper]
**Vulnerability:** Unrestricted URL input in `scraper.py` allowed scraping of local services (SSRF) via CLI arguments.
**Learning:** `requests.get` will fetch any URL provided, including `localhost` or private IPs, and follows redirects by default. Validating only the scheme is insufficient for SSRF protection.
**Prevention:** Implement strict input validation using `urllib.parse` and `ipaddress` to check for schemes (http/https only) and reject private/loopback IP addresses. Note that complete protection against DNS rebinding requires lower-level network control or disabling redirects.
