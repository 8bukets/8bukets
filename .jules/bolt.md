## 2026-02-05 - CPU-bound parsing blocking asyncio loop
**Learning:** `scraper.py` was running `BeautifulSoup` parsing (CPU-bound) directly in the `asyncio` event loop. This blocks the loop, negating the concurrency benefits of `aiohttp` as the loop cannot process other network events while parsing.
**Action:** Offloaded parsing to a `ProcessPoolExecutor` using `loop.run_in_executor` to allow truly concurrent scraping and parsing.
