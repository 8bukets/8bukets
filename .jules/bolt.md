## 2026-01-31 - [AsyncIO Blocking Operations]
**Learning:** CPU-bound operations like BeautifulSoup parsing inside `async` functions block the event loop, defeating the purpose of concurrency.
**Action:** Use `asyncio.to_thread` to offload heavy parsing logic to a separate thread, keeping the main loop responsive.
