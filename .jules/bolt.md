## 2024-05-23 - [SQLite Batch Commits]
**Learning:** SQLite transactions are expensive. Committing after every INSERT in a loop (O(N) commits) kills performance due to frequent disk syncs.
**Action:** Reuse a single database connection and batch commits (e.g., once per page or chunk) to achieve massive speedups (observed ~340x).
