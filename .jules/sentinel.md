## 2026-01-04 - [SSRF Protection in Scraper]
**Vulnerability:** The scraper accepted arbitrary URLs via the `--url` argument and passed them directly to `requests.get()`. This could allow an attacker to perform Server-Side Request Forgery (SSRF) by supplying URLs pointing to internal resources (e.g., `localhost`, internal IPs) or using dangerous schemes like `file://` (though `requests` limits this by default, being explicit is better).
**Learning:** Even in CLI tools or simple scripts, input validation is crucial. Relying on the underlying library's defaults (like `requests` not handling `file://`) is insufficient defense-in-depth. Explicitly validating the scheme and checking for obvious internal targets provides a necessary layer of security.
**Prevention:** Implemented a `validate_url` method in `BlogScraper` that:
1.  Enforces `http` or `https` schemes.
2.  Blocks access to standard loopback addresses (`localhost`, `127.0.0.1`, `::1`).
3.  Ensures a valid domain/netloc exists.
This method is called before any network request is initiated.
