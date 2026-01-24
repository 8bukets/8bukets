## 2024-05-22 - Asyncio Event Loop Blocking
**Learning:** `BeautifulSoup` parsing is synchronous and CPU-bound. Calling it directly within an `async def` function blocks the asyncio event loop, preventing concurrent network requests even if `aiohttp` is used.
**Action:** Use `asyncio.to_thread` (Python 3.9+) to offload CPU-bound parsing to a separate thread, keeping the event loop free for I/O operations.
