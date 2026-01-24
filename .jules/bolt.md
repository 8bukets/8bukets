## 2024-05-22 - BeautifulSoup Performance: Find vs Select

**Learning:** Replacing `select_one` (CSS selectors) with `find` (direct tag lookup) in BeautifulSoup yielded a ~15% performance improvement (3.9s saved on 50 pages) in `scraper.py`. CSS selector parsing adds significant overhead in tight loops.

**Action:** Prefer `find/find_all` over `select/select_one` for simple tag/class lookups in high-frequency parsing paths.

## 2024-05-22 - AsyncIO Threads vs GIL

**Learning:** Using `asyncio.to_thread` for CPU-bound HTML parsing in a batch-processing scraper did NOT improve throughput (and slightly degraded it by ~20%) due to Python's GIL and thread switching overhead.

**Action:** Only use `to_thread` when maintaining event loop responsiveness (latency) is more critical than raw throughput, or when the task releases the GIL (e.g. numpy, I/O).
