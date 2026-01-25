## 2024-05-22 - Asyncio Event Loop Blocking
**Learning:** Heavy DOM parsing with BeautifulSoup in `async` functions blocks the event loop, defeating the purpose of concurrency. In `scraper.py`, parsing 350+ posts per page synchronously stalled network requests.
**Action:** Wrap CPU-bound parsing logic in `asyncio.to_thread` to maintain responsiveness.
