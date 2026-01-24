## 2026-01-24 - Offloading CPU-bound tasks in AsyncIO
**Learning:** AsyncIO event loop is blocked by CPU-bound operations like BeautifulSoup parsing. Wrapping them in `asyncio.to_thread` prevents this blocking and allows other concurrent network requests to proceed.
**Action:** Always offload heavy parsing logic to threads using `asyncio.to_thread` in async scrapers.
