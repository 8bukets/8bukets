## 2026-02-03 - SQLite Connection Reuse
**Learning:** Reusing a single SQLite connection and batching commits per page (vs per item) reduced DB overhead by >300x in micro-benchmarks.
**Action:** Always verify DB connection lifecycles in loop-heavy operations. Prefer persistent connections and batched transactions.
