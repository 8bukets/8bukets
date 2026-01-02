## 2026-01-02 - SSRF Protection in Web Scraper
**Vulnerability:** The scraper blindly followed 'next page' links extracted from the DOM. A malicious or compromised target site could inject links to internal network resources (e.g., http://localhost, http://169.254.169.254), leading to Server-Side Request Forgery (SSRF).
**Learning:** Pagination links are untrusted user input. Even when scraping a "trusted" site, the content (especially links) should be treated as potentially malicious. `urlparse` combined with strict domain matching is a simple but effective control.
**Prevention:** Implemented strict domain validation in `scraper.py` using `urlparse`. The scraper now verifies that any URL it attempts to fetch matches the `netloc` of the initial base URL.
