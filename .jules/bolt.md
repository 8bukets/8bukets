## 2026-02-03 - [SoupStrainer & ProcessPool]
**Learning:** `SoupStrainer(class_='post')` fails on multi-valued classes (e.g., `post category-tech`). Use `re.compile(r'\bpost\b')`. Also, CPU-bound parsing blocks asyncio loop; offloading to `ProcessPoolExecutor` gave 8x speedup.
**Action:** Always verify `SoupStrainer` with regex for class matching. Offload heavy parsing in async apps.
