# Bolt's Journal

## 2026-01-26 - CPU-bound tasks in AsyncIO
**Learning:** Async functions (`async def`) that perform heavy CPU-bound operations (like BeautifulSoup parsing) block the entire asyncio event loop, defeating the purpose of concurrency.
**Action:** Offload CPU-intensive tasks to threads using `asyncio.to_thread` to keep the event loop responsive.
