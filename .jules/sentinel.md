## 2026-02-01 - SSRF in BlogScraper
**Vulnerability:** The `BlogScraper` accepted arbitrary URLs via CLI arguments, allowing an attacker to probe internal network services (SSRF) if deployed as a service.
**Learning:** `requests` library follows redirects and resolves DNS automatically, making it easy to accidentally expose internal resources. Standard library `socket` and `ipaddress` can be used to validate the target before fetching.
**Prevention:** Implement `is_safe_url` validation that checks the URL scheme (must be http/s) and resolves the hostname to ensure it is not a private/reserved IP address.
