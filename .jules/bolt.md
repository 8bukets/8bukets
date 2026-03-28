## 2026-02-02 - AsyncIO CPU Blocking
**Learning:** Even with the GIL, offloading CPU-bound tasks (like BeautifulSoup parsing) to `loop.run_in_executor` significantly improves throughput in `asyncio` applications by preventing the event loop from being blocked.
**Action:** When mixing async I/O with heavy CPU processing (like HTML parsing), always offload the CPU work to a thread or process pool.
