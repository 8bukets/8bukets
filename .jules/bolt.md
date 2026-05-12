## 2026-01-27 - [Sequential Agent Bottleneck]
**Learning:** The `AgentOrchestrator` runs agents sequentially by default. `ResearcherAgent` and `CuriosityAgent` are IO-bound (network requests), causing significant delays. `AnalystAgent` and `MonetizationAgent` are fast but block downstream dependent agents.
**Action:** Use `ThreadPoolExecutor` to parallelize independent agents and carefully manage dependencies (Analyst -> Intelligence) to maximize concurrency. This pattern should be applied to future agent additions.
## 2026-02-06 - SQLite Connection Overhead
**Learning:** Reopening SQLite connections for every insert/update is a significant performance bottleneck (N+1 connection problem). In `scraper.py`, switching to a persistent connection reduced the overhead by ~1.5x in benchmarks.
**Action:** Always verify if database connections are reused in tight loops. Implement the Context Manager pattern (`__enter__`/`__exit__`) for classes handling database resources to ensure proper lifecycle management.
## 2026-02-04 - Reuse SQLite Connection
**Learning:** Reusing a single SQLite connection across many operations provides a measurable performance boost (~5-14% locally) but introduces transaction management risks. A failed operation can leave a transaction open, contaminating subsequent operations if `conn.rollback()` is not explicitly called.
**Action:** When reusing DB connections, always ensure `rollback()` is called in the exception handler to reset the transaction state.
