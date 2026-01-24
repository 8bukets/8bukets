## 2026-01-24 - [Asyncio Blocking Operations]
**Learning:** CPU-bound operations like `BeautifulSoup` parsing block the asyncio event loop, degrading concurrency.
**Action:** Always offload CPU-intensive tasks to a thread using `asyncio.to_thread` (or `loop.run_in_executor`) in async applications.
