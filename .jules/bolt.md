## 2024-05-22 - [Async Event Loop Blocking]
**Learning:** CPU-bound operations like BeautifulSoup parsing inside an `async def` function block the event loop, negating the benefits of concurrency. Even if labeled `async`, the code runs synchronously unless awaited.
**Action:** Offload heavy parsing logic to `loop.run_in_executor` to keep the event loop responsive.

## 2024-05-22 - [Regex vs String Methods]
**Learning:** `str.split().join()` and `str.startswith()` are ~4x faster than equivalent compiled regexes for simple whitespace normalization and prefix checking.
**Action:** Prefer built-in string methods over `re` module when complex pattern matching is not required.
