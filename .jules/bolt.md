## 2026-01-30 - [Asyncio Blocking Operations]
**Learning:** `BeautifulSoup` parsing is a CPU-bound blocking operation that stalls the asyncio event loop, significantly impacting concurrency in the scraper.
**Action:** Always offload `BeautifulSoup` parsing (and other CPU-intensive tasks) to a thread executor using `loop.run_in_executor` in async contexts.
