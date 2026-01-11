## 2026-01-11 - [Input Sanitization Strategy]
**Vulnerability:** The scraper naively extracted URLs from `href` attributes without validation, allowing `javascript:` schemes that could lead to Stored XSS.
**Learning:** In web scraping contexts, "URLs" are untrusted input. Libraries like `requests` or `BeautifulSoup` do not automatically sanitize protocols. A strict allow-list (http/https) is required.
**Prevention:** Always implement a `validate_url` helper that enforces protocol schemes before storing or processing scraped links.
