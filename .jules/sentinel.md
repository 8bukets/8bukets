## 2026-01-05 - SSRF in Web Scraper
**Vulnerability:** The `BlogScraper` blindly followed "Next Page" links found in scraped HTML content. If a scraped page contained a link to an internal or malicious domain (e.g., `http://localhost:8080/admin`), the scraper would make a GET request to it, potentially exposing internal services (SSRF).
**Learning:** Web scrapers that follow links must treat those links as untrusted user input. Standard libraries like `requests` will follow redirects and fetch whatever URL is provided, so explicit validation is needed.
**Prevention:** Validate the domain of any URL extracted from content before fetching it. Ensure it matches the expected domain (or a whitelist) using `urllib.parse.urlparse(url).netloc`.
