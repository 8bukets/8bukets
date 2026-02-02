## 2026-02-02 - Sliding Window vs Batching
**Learning:** For IO-bound scraping tasks with variable response times (simulated or real), batching with `asyncio.gather` leads to straggler issues where the entire batch waits for the slowest request.
**Action:** Use a sliding window approach with `asyncio.wait(return_when=asyncio.FIRST_COMPLETED)` to maintain constant concurrency and maximize throughput.
