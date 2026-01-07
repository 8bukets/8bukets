## 2025-12-25 - [SSRF Protection in Scraper]
**Vulnerability:** The scraper accepted any URL via CLI arguments, potentially allowing access to internal network resources (SSRF) or local files (if scheme not checked).
**Learning:** `requests` library is powerful but naive; it will fetch whatever you tell it to. Simple scheme validation prevents whole classes of attacks (file://).
**Prevention:** Validate URL scheme (http/s only) and block localhost access before making the request.
