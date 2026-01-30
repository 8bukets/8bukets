## 2026-01-30 - [CPU-Bound Blocking in Async Scraper]
**Learning:** BeautifulSoup parsing is a CPU-bound operation that blocks the asyncio event loop. Even with aiohttp for concurrent fetching, the scraping throughput is limited by the parsing speed if run in the main thread.
**Action:** Always offload CPU-intensive parsing (like BeautifulSoup or complex regex) to a thread pool executor using loop.run_in_executor in asyncio applications.
