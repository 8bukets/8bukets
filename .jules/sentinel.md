## 2024-05-22 - [Scraper DoS Protection]
**Vulnerability:** The `scraper.py` script was vulnerable to Denial of Service (DoS) attacks via memory exhaustion because it used `await response.text()` to read full response bodies into memory without any size limit.
**Learning:** `aiohttp`'s `response.text()` reads the entire body. For untrusted or potentially large resources, one must check `Content-Length` headers and/or stream the response using `response.content.iter_chunked()` to enforce a maximum size limit.
**Prevention:** Always implement size limits when fetching external resources. Use streaming response processing instead of loading full bodies into memory for unbounded data sources.
