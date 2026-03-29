## 2026-01-26 - SoupStrainer & Async Offloading
**Learning:** `BeautifulSoup` parsing is CPU-bound and blocks the `asyncio` event loop, significantly degrading concurrency. `SoupStrainer` can reduce parsing time by 15-20% but the biggest win is offloading parsing to a thread.
**Action:** Always offload CPU-intensive parsing to `asyncio.to_thread` in async scrapers and use `SoupStrainer` when only specific tags are needed.
