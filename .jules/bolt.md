## 2026-02-04 - CPU Blocking in Asyncio
**Learning:** `BeautifulSoup` parsing is synchronous and CPU-bound. When running inside an `asyncio` event loop, it blocks the loop, preventing other concurrent network requests from proceeding.
**Action:** Offload CPU-bound tasks like HTML parsing to a `ProcessPoolExecutor` using `loop.run_in_executor` to maintain high concurrency.
