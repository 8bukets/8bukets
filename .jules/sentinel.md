## 2026-01-15 - Uncontrolled Resource Consumption (DoS)
**Vulnerability:** The scraper used `await response.text()` which loads the entire response body into memory. A malicious or misconfigured server returning a massive file (e.g., 10GB) could cause the application to crash due to memory exhaustion (OOM).
**Learning:** `aiohttp`'s convenience methods like `.text()` and `.read()` are unsafe for untrusted or potentially large resources. Checking `Content-Length` is necessary but not sufficient (it can be missing or faked).
**Prevention:** Always use streaming (chunked reading) when fetching external resources. Implement a strict size limit and abort the connection if the limit is exceeded.
