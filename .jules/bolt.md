# Bolt's Journal

## 2026-01-16 - [Async IO Blocking]
**Learning:** In `scraper.py`, the `parse_page` function uses `BeautifulSoup`, which is a CPU-bound synchronous operation. Even though it's defined as `async def`, it blocks the event loop because it contains no `await` points during the parsing phase. This prevents the `aiohttp` event loop from efficiently handling other concurrent network requests while one page is being parsed.
**Action:** Offload CPU-bound tasks like HTML parsing to a thread pool using `loop.run_in_executor` to keep the asyncio event loop responsive.
