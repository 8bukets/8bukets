## 2026-02-06 - SQLite Connection Overhead
**Learning:** Reopening SQLite connections for every insert/update is a significant performance bottleneck (N+1 connection problem). In `scraper.py`, switching to a persistent connection reduced the overhead by ~1.5x in benchmarks.
**Action:** Always verify if database connections are reused in tight loops. Implement the Context Manager pattern (`__enter__`/`__exit__`) for classes handling database resources to ensure proper lifecycle management.
