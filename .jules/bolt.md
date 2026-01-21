## 2024-05-23 - [Database Connection Reuse]
**Learning:** Opening and closing a SQLite connection inside a loop (O(N)) significantly impacts performance due to repeated file I/O and locking overhead.
**Action:** Always maintain a persistent database connection for batch operations, opening it once at the start and closing it at the end.
