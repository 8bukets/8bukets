## 2026-01-10 - [Scraper DoS Protection Pattern]
**Vulnerability:** Scrapers utilizing `requests.get()` without size limits or timeouts expose the application to DoS attacks via memory exhaustion (zip bombs) or hanging connections.
**Learning:** `requests` downloads the entire response body into memory by default. Streaming (`stream=True`) is required to inspect `Content-Length` and accumulate bytes safely.
**Prevention:** Implement a wrapper function (like `safe_get_content`) that enforces a `MAX_RESPONSE_SIZE` (e.g., 10MB) by checking headers and iterating over content chunks, raising an exception if limits are exceeded.
