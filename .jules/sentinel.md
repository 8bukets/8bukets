## 2024-03-25 - Prevented XSS via URL Scheme Validation
**Vulnerability:** The scraper naively joined relative URLs with the base URL, allowing `javascript:` schemes to bypass filters and be saved to output files.
**Learning:** `urljoin` does not validate schemes. String-based filters (like checking for `/news/`) can be bypassed by comments in malicious payloads (e.g., `javascript:/* /news/ */`).
**Prevention:** Always parse the resolved URL using `urlparse` and explicitly allow-list schemes (`http`, `https`) before processing or storing the link.
