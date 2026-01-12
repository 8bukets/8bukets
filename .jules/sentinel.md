## 2024-05-24 - [Unbounded Network Requests]
**Vulnerability:** Found `requests.get()` call in `scrape_informatic.py` without a `timeout` parameter.
**Learning:** Even when using `HTTPAdapter` with retries, the underlying `get` request can hang indefinitely if the server accepts the connection but sends no data. This is a potential DoS vector.
**Prevention:** Always enforce a `timeout` on all network requests (e.g., `requests.get(url, timeout=10)`). Use linters or static analysis to catch missing timeouts.
