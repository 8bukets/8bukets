## 2024-05-23 - [Initial Sentinel Journal]
**Vulnerability:** Missing security journal.
**Learning:** Security learnings need a dedicated place to live to prevent knowledge loss.
**Prevention:** Created this file.

## 2026-01-22 - [Fixed SSRF in Scraper]
**Vulnerability:** The `fetch_page` method in `scraper.py` blindly requested any URL, including `file://` or other schemes, allowing potential Server-Side Request Forgery or local file disclosure.
**Learning:** Python's `requests` library might support schemes other than HTTP/HTTPS depending on adapters, and lack of input validation on scraped URLs can lead to the scraper acting as a proxy for malicious requests.
**Prevention:** Added `validate_url` to enforce `http` or `https` schemes before making requests.
