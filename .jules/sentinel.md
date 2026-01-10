## 2025-05-18 - [Preventing Unbounded Resource Consumption (DoS)]
**Vulnerability:** The application originally read entire HTTP responses into memory without a size limit. This exposed it to Denial of Service (DoS) attacks via memory exhaustion if a server returned a massive payload (e.g., a "zip bomb" or infinite stream).
**Learning:** `aiohttp`'s `response.text()` reads the full body. For untrusted URLs, it is critical to enforce a maximum download size.
**Prevention:** Implemented a `MAX_SIZE` (10MB) limit in `fetch_page`. It checks `Content-Length` header (safely) and then reads the body in chunks (or uses `read(n)`) to ensure the limit is not exceeded before decoding.
