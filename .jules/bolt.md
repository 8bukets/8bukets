## 2024-05-23 - [CPU-Bound Tasks Block Async Event Loop]
**Learning:** In `scraper.py`, synchronous BeautifulSoup parsing inside async functions blocked the event loop, negating concurrency benefits.
**Action:** Offload CPU-bound tasks to `ProcessPoolExecutor` and ensure worker functions are module-level (picklable).
