## 2026-01-19 - [Optimizing `requests` with `Session`]
**Learning:** Instantiating a new `requests.get` call for every URL in a scraping loop is inefficient because it establishes a new TCP connection (and SSL handshake) for each request.
**Action:** Use `requests.Session()` to enable connection pooling (Keep-Alive). This persists the connection to the host, significantly reducing latency for subsequent requests to the same domain. In unit tests, this requires mocking `session.get` on the instance rather than patching `requests.get`.
