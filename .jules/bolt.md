## 2024-05-22 - [Blocking CPU Work in Async Loop]
**Learning:** Performing heavy CPU-bound tasks (like parsing HTML with BeautifulSoup) inside an `async def` function without awaiting effectively blocks the event loop, negating the benefits of concurrency.
**Action:** Offload CPU-bound tasks to a thread using `asyncio.to_thread` to keep the event loop responsive.
