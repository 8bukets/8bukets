## 2025-12-29 - [Scraper Performance Optimization]
**Learning:** Establishing new TCP/SSL connections (requests) and opening new SQLite file handles for every iteration in a loop are significant performance bottlenecks.
**Action:** Use `requests.Session()` for HTTP Keep-Alive and reuse a single SQLite connection object across the loop iteration to minimize I/O overhead.
