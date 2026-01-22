## 2024-01-22 - [SQLite Transaction Overhead]
**Learning:** SQLite connection/commit overhead per row is significant (measured ~370x slowdown vs batched).
**Action:** Always reuse DB connections and batch commits when processing bulk data in scrapers.
