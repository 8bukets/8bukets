## 2026-01-15 - SQLite Connection Overhead
**Learning:** Reopening SQLite connections for every single insert operation in a loop significantly degrades performance (approx 35% overhead in this case).
**Action:** Always verify if a database connection can be reused across multiple operations, especially within loops, and implement a persistent connection pattern or context manager at a higher level.
