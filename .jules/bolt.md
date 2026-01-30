## 2024-05-23 - Python GIL and Threading Pitfalls
**Learning:** Attempted to optimize CPU-bound BeautifulSoup parsing by offloading to `ThreadPoolExecutor`. This caused a performance regression because the GIL prevents parallel execution of Python bytecode. Threads only benefit I/O-bound tasks or extensions that release the GIL.
**Action:** Avoid threading for CPU-bound Python code. Focus on algorithmic efficiency (e.g., replacing CSS selectors with direct lookups, avoiding regex) or use multiprocessing if overhead permits.
