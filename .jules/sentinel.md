## 2024-05-23 - [Availability] Unbounded Scraping Requests
**Vulnerability:** The scraper lacked a timeout for HTTP requests and did not limit the size of downloaded responses.
**Learning:** `requests.get()` in Python does not have a default timeout, meaning a connection can hang indefinitely, causing a Denial of Service for the worker process. Also, downloading without a size limit can lead to Memory DoS.
**Prevention:** Always set `timeout=...` in `requests` calls and check `Content-Length` or use `stream=True` with a chunk limit for untrusted URLs.
