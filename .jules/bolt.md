## 2024-05-22 - BeautifulSoup Parsing Concurrency
**Learning:** `BeautifulSoup` parsing is CPU-bound and significantly blocks the asyncio event loop. Using `SoupStrainer` alone provides minimal speedup (~3%) on this site's HTML, but offloading parsing to a `ProcessPoolExecutor` provided a ~3x improvement in throughput by allowing network I/O to overlap with CPU-intensive parsing.
**Action:** Always offload CPU-bound HTML parsing to `ProcessPoolExecutor` when scraping concurrently, and prefer `SoupStrainer` to minimize data passing overhead.
