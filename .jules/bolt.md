## 2025-02-03 - SoupStrainer Class Matching
**Learning:** `SoupStrainer` with `class_` string argument behaves differently than `find_all`. It requires exact match for the attribute value, failing on multi-valued classes unless a regex is used.
**Action:** Always use `re.compile(r'\bword\b')` when using `SoupStrainer` with classes to ensure it matches like `find_all`.

## 2025-02-03 - Asyncio CPU Bottleneck
**Learning:** Heavy HTML parsing (`BeautifulSoup`) blocks the asyncio event loop, negating concurrency benefits. `ThreadPoolExecutor` doesn't help due to GIL. `ProcessPoolExecutor` works but requires picklable (module-level) functions.
**Action:** Refactor heavy parsing logic into standalone module-level functions and offload to `ProcessPoolExecutor` using `loop.run_in_executor`.
