## 2026-02-02 - SQLite Connection Reuse & Batching
**Learning:** Opening and closing a SQLite connection for every single insert in a loop caused significant I/O overhead, slowing down the scraper. Reusing the connection and batching commits (every 50 items) resulted in a ~32x performance improvement.
**Action:** When performing bulk database operations, always reuse the connection and implement batch committing to minimize disk I/O and transaction overhead.
