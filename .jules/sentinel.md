## 2024-05-23 - Denial of Service via Unbounded Response Download
**Vulnerability:** The scraper used `await response.text()` which loads the entire response body into memory without checking its size. A malicious or compromised server could return a multi-gigabyte response, crashing the application (Memory DoS).
**Learning:** `aiohttp`'s `response.text()` is convenient but risky for untrusted input. Always use streaming for network responses when size is not guaranteed.
**Prevention:** Use `response.content.iter_chunked()` with a counter to enforce a strict byte limit (e.g., 10MB) on all downloads. Check `Content-Length` header first as an optimization.
