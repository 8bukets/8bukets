## 2026-01-31 - [Blocking Operations in Async Code]
**Learning:** `BeautifulSoup` parsing is CPU-bound and blocks the `asyncio` event loop. Wrapping it in `asyncio.to_thread` improved responsiveness from a 25s block to negligible delays (<0.25s) for large payloads.
**Action:** Always offload CPU-bound tasks (parsing, image processing) to threads when working in an async environment to maintain event loop liveness.
