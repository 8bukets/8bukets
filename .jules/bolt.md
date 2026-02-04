## 2024-05-22 - Asyncio CPU Bottleneck
**Learning:** Asyncio functions that perform heavy CPU operations (like BeautifulSoup parsing) block the event loop, defeating the purpose of async I/O.
**Action:** Offload CPU-bound tasks to `ProcessPoolExecutor` using `loop.run_in_executor` and ensure functions are pickleable (pure functions, top-level).
