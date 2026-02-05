## 2026-02-05 - Offloading CPU-bound tasks in Asyncio (Rejected)
**Learning:** While `ProcessPoolExecutor` is correct for CPU-bound tasks in asyncio, using it for a single-page scrape introduces unnecessary overhead (process spawning, IPC) that outweighs the benefits.
**Action:** Only use multiprocessing when the workload is large enough (e.g., multiple concurrent pages) to justify the overhead. For smaller tasks, look for algorithmic optimizations first.

## 2026-02-05 - Optimizing BeautifulSoup with SoupStrainer
**Learning:** `BeautifulSoup` parses the entire DOM by default. `SoupStrainer` allows parsing only specific tags (e.g., `<a>`), which drastically reduces parsing time and memory usage.
**Action:** Use `SoupStrainer` in `BeautifulSoup` constructor when extracting specific elements from large documents.
