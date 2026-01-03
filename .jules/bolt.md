## 2026-01-03 - [SQLite Connection Overhead in Loops]
**Learning:** Opening and closing a SQLite connection (`sqlite3.connect`) inside a high-frequency loop (e.g., saving scraped items one by one) introduces significant overhead due to file I/O and initialization costs.
**Action:** Always reuse a persistent database connection for batched operations or sequential processing. Use `with conn:` context manager for transaction handling, and ensure the connection is explicitly closed when processing is complete. Benchmarks showed ~16-24% improvement for simple insert operations.
