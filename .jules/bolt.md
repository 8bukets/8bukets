## 2024-05-22 - [Asyncio CPU Bottleneck]
**Learning:** `BeautifulSoup` parsing is CPU-bound and blocks the `asyncio` event loop, significantly reducing concurrent network request throughput in scrapers.
**Action:** Always offload CPU-intensive parsing to a `ProcessPoolExecutor` using `loop.run_in_executor` to keep the event loop responsive.
