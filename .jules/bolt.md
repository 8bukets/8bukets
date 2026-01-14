## 2024-05-22 - Persistent SQLite Connection & Requests Session
**Learning:** Reopening a SQLite connection and creating a new HTTP connection for every item in a loop adds significant overhead (approx 20% in local benchmarks, likely more with real network latency).
**Action:** Always initialize `requests.Session()` and `sqlite3.connect()` in `__init__` for scrapers processing multiple items, and ensure a `close()` method exists for cleanup.
