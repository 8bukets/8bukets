## 2026-01-28 - Unvalidated Pagination & Missing Timeouts
**Vulnerability:** The scraper blindly followed pagination links from the scraped page content, which could lead to SSRF or Open Redirect if the target site is compromised or malicious. It also lacked request timeouts.
**Learning:** Scrapers must treat all content from the target site as untrusted input, including navigation links.
**Prevention:** Implement `is_safe_url` validation for any URL extracted from content before requesting it. Always set explicit timeouts on `requests` calls.
