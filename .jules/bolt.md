## 2024-05-22 - [Offloading CPU-bound tasks in AsyncIO]
**Learning:** Offloading `BeautifulSoup` parsing to `asyncio.to_thread` is essential to prevent blocking the event loop, even if micro-benchmarks on small batches show mixed results due to thread overhead.
**Action:** Always verify if `async` functions are actually non-blocking. If they perform heavy CPU work (like parsing large HTML), they should be offloaded to threads or processes to maintain loop responsiveness.
