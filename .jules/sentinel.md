## 2026-01-20 - Unchecked Scraper URL Traversal
**Vulnerability:** The `BlogScraper` was susceptible to SSRF because it blindly fetched URLs extracted from HTML content (`get_next_page`) without validation, allowing potential access to local/private network resources if a target site was compromised or malicious.
**Learning:** Scrapers often trust the "next page" links implicitly, but these are untrusted inputs. `requests` does not block local schemes or private IPs by default.
**Prevention:** Implement strict URL scheme validation (allowlist `http`/`https`) and consider DNS resolution checks for private IPs for any URL derived from scraped content before fetching.
