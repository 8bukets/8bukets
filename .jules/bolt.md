## 2026-01-26 - SQLite Connection Reuse
**Learning:** The scraper was opening and closing a SQLite connection for every single record processed, causing significant I/O overhead (N connections for N items).
**Action:** Ensure database connections are established once at the start of the batch process and closed at the end, reusing the same connection for all operations.
