## 2026-01-12 - [DB Transaction Bottleneck]
**Learning:** SQLite disk I/O with `commit()` is a massive bottleneck if called inside a loop. The overhead of fsync per-insert was 63x slower than batching.
**Action:** Always batch database inserts/updates within a single transaction scope, committing only at logical checkpoints (e.g., per page or per session), and reuse the connection object.
