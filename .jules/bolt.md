## 2025-01-18 - [Asyncio Blocking by BeautifulSoup]
**Learning:** The `scraper.py` used `BeautifulSoup` parsing (CPU-bound) directly inside `async` methods. This blocked the asyncio event loop (~660ms/page), negating the benefits of concurrency and potentially stalling other tasks (like heartbeats or other agents).
**Action:** Offload all CPU-intensive parsing to `concurrent.futures.ProcessPoolExecutor`. Ensure parsed functions are pure (top-level or static) to be picklable.
