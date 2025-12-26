## 2025-12-26 - Protocol-Relative URL Vulnerability in Scraper
**Vulnerability:** The scraper used `urljoin` without validating the resulting domain or scheme. This allowed a malicious page to inject links like `//evil.com/news/announcement/google-cloud` which `urljoin` resolves to `https://evil.com/news/announcement/google-cloud`. The scraper would then accept this as a valid link because it contained the required path substrings.
**Learning:** `urljoin` correctly handles protocol-relative URLs by resolving them against the base scheme, but this means the domain changes. Simple path checks are insufficient when the domain can change.
**Prevention:** Always validate `urlparse(full_url).netloc` and `urlparse(full_url).scheme` after using `urljoin` when scraping external content.
