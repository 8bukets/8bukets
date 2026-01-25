## 2024-05-23 - [SQLite Connection Overhead]
**Learning:** The scraper was opening and closing a SQLite connection for every single inserted item, causing a massive performance bottleneck (over 100x slower than persistent connection).
**Action:** When working with SQLite in this codebase, always ensure connections are persistent across the lifespan of the batch operation (e.g., in `__init__` or `run` scope) and commit in batches, rather than per-record.
