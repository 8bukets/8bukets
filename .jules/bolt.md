## 2026-01-23 - Asyncio CPU Blocking
**Learning:** In async Python applications, CPU-bound tasks like BeautifulSoup parsing block the event loop, effectively sequentializing concurrent network requests. `ThreadPoolExecutor` does not solve this due to the GIL.
**Action:** Use `ProcessPoolExecutor` via `loop.run_in_executor` for CPU-intensive work, and ensure target functions are picklable (module-level, not instance methods).
