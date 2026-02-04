## 2025-02-04 - CPU-bound tasks in AsyncIO
**Learning:** `BeautifulSoup` parsing can take ~0.7s+ per page for complex HTML. Running this directly in an `asyncio` loop blocks the event loop, negating the benefits of concurrent network requests.
**Action:** Always offload CPU-intensive parsing to `ProcessPoolExecutor` when using `asyncio` for scraping, to maintain event loop responsiveness.
