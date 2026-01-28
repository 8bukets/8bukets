## 2026-01-28 - [Scraper Connection Reuse]
**Learning:** The scraper was opening and closing SQLite connections for every single item inside a loop (N+1 connection issue), causing significant I/O overhead.
**Action:** Always initialize DB connections (and HTTP sessions) once at the start of the scraper and reuse them, ensuring proper cleanup with `try...finally` or context managers.
