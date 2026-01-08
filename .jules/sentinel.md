## 2026-01-08 - Memory DoS and SSRF Protection in Scraper
**Vulnerability:** The scraper was vulnerable to Memory Denial of Service (DoS) because it used `requests.get()` without `stream=True`, loading unlimited response bodies into memory. It also lacked validation for URL schemes, potentially allowing SSRF via `file://` or other schemes.
**Learning:** Even internal tools need input validation. Scrapers should always treat the target server as potentially hostile (maliciously large responses). Mocking `requests` with `stream=True` requires mocking `iter_content` instead of just `.content`.
**Prevention:** Use `requests.get(stream=True)` with `iter_content` and a size limit loop. Always validate URL schemes against an allowlist (e.g., `http`, `https`).
