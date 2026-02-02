## 2026-02-02 - Threading vs Multiprocessing for BeautifulSoup
**Learning:** ThreadPoolExecutor caused a 4x slowdown (7s -> 31s) when parsing with BeautifulSoup/lxml, likely due to GIL contention or lock contention in lxml, whereas ProcessPoolExecutor provided a 3x speedup (2.5s).
**Action:** Always prefer ProcessPoolExecutor for CPU-bound parsing tasks in Python, even if libraries like lxml claim to release GIL.
