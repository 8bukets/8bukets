## 2026-02-04 - Reuse SQLite Connection
**Learning:** Reusing a single SQLite connection across many operations provides a measurable performance boost (~5-14% locally) but introduces transaction management risks. A failed operation can leave a transaction open, contaminating subsequent operations if `conn.rollback()` is not explicitly called.
**Action:** When reusing DB connections, always ensure `rollback()` is called in the exception handler to reset the transaction state.
