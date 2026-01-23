## 2024-10-24 - Offloading CPU-bound Parsing in AsyncIO
**Learning:** `BeautifulSoup` parsing is synchronous and CPU-intensive. When used directly inside an `async def` function in an `aiohttp` scraper, it blocks the event loop, preventing concurrent network requests and heartbeats.
**Action:** Wrap the parsing logic in a synchronous function and call it using `await loop.run_in_executor(None, sync_func, *args)` to offload it to a thread pool.
