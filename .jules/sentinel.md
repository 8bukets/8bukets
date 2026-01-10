## 2026-01-10 - [SSRF Risk in URL Input]
**Vulnerability:** The scraper accepted any URL scheme (e.g., `file://`), which could allow reading local files or accessing internal services if the underlying library supported it.
**Learning:** Even in CLI tools, validating input is crucial for defense-in-depth, especially if the code might be reused in a web service later.
**Prevention:** Always use `urllib.parse` to whitelist allowed schemes (`http`, `https`) before making network requests.
