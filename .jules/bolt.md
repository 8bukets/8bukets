## 2026-01-07 - Database Connection Overhead
**Learning:** Opening and closing a SQLite database connection for every single row insertion (inside a loop) creates massive I/O overhead and is a major bottleneck.
**Action:** Always use a persistent database connection (passed as an argument or stored in `self`) for bulk operations or loops, and ensure proper closure using a context manager (`__enter__`/`__exit__`) or a `finally` block.

## 2026-01-07 - HTTP Session Reuse
**Learning:** Creating a new `requests.get()` call for every page in a scraper forces a new TCP (and SSL) handshake each time.
**Action:** Use `requests.Session()` to reuse the underlying TCP connection (Keep-Alive), which significantly reduces latency, especially for HTTPS sites.
