## 2025-02-03 - SoupStrainer Regex Pitfalls
**Learning:** When using `SoupStrainer` with `class_` and a regex, `\b` (word boundary) treats hyphens as boundaries. This means `r'\bpost\b'` matches `class="not-a-post"`.
**Action:** Use `r'(^|\s)word(\s|$)'` to strictly match space-separated classes in HTML attributes.

## 2025-02-03 - Blocking Event Loop
**Learning:** `BeautifulSoup` parsing is CPU-intensive and blocks the asyncio event loop if run directly in an `async` function.
**Action:** Always offload parsing to `loop.run_in_executor` (ThreadPool or ProcessPool) to maintain concurrency.
