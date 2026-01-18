## 2026-01-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The scraper accepted arbitrary URLs via the `--url` argument and fetched them without validation, allowing access to internal network resources (SSRF).
**Learning:** `requests.get` will happily fetch internal IPs or localhost if asked. Standard URL parsing isn't enough; DNS resolution and IP checking are required.
**Prevention:** Implemented `is_safe_url` helper that resolves the hostname and checks against private/loopback/reserved IP ranges before fetching.
