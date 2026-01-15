## 2026-01-15 - [SSRF Protection in Scraper]
**Vulnerability:** The `BlogScraper` accepted arbitrary URLs via CLI arguments without validation, potentially allowing Server-Side Request Forgery (SSRF) against local or private network resources.
**Learning:** Even simple CLI tools can be vectors for SSRF if they are automated or exposed via wrappers. Validating input at the boundary is crucial.
**Prevention:** Implemented a `validate_url` method that checks the URL scheme (http/https), blocks localhost explicitly, and resolves the hostname to check for private IP addresses using `ipaddress`.
