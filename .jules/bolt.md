## 2024-05-22 - [Blocking Parsing in Async Scraper]
**Learning:** `BeautifulSoup` parsing is CPU-bound and blocks the `asyncio` event loop, causing a 3x slowdown in concurrent scraping throughput.
**Action:** Always offload CPU-intensive tasks like HTML parsing to a `ProcessPoolExecutor` in async applications to maintain loop responsiveness.
