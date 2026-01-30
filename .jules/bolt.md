## 2026-01-30 - SQLite Batch Commits & Persistent Connections
**Learning:** Opening a new SQLite connection and committing for every single record insertion creates massive overhead. In a scraping loop, this resulted in >100x performance penalty (2.2s vs 0.02s for 1000 inserts).
**Action:** Use a persistent database connection for the duration of the process and batch commits (e.g., after processing a full page of results) rather than after every row.
