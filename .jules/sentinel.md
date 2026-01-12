## 2026-01-12 - [SSRF Protection in Scraper]
**Vulnerability:** The scraper was vulnerable to Server-Side Request Forgery (SSRF) as it allowed fetching any URL scheme and connecting to local addresses.
**Learning:** `requests` follows redirects by default, potentially bypassing initial checks. Simple string matching for `localhost` is insufficient; resolving to IP is necessary to catch aliases (like `127.0.0.1`).
**Prevention:** Implement strict scheme validation (`http`/`https`), resolve hostnames to IPs to check against private ranges (`ipaddress` module), and disable automatic redirects (`allow_redirects=False`) or validate each redirect hop.
