## 2025-02-18 - Critical Learning: Async Event Loop Blocking
**Learning:** CPU-bound operations like BeautifulSoup parsing inside an async function block the event loop, preventing concurrent network requests.
**Action:** Offload CPU-intensive tasks to a separate thread using `asyncio.to_thread` to keep the event loop responsive.
