## 2026-01-23 - SQLite Batching Optimization
**Learning:** Committing every row in SQLite is extremely slow due to filesystem syncing overhead. Batching commits (e.g., per page or every N items) yields 100x performance improvement.
**Action:** Always use shared connections and batch commits when performing bulk inserts in SQLite.
