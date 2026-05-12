## 2024-05-23 - BeautifulSoup SoupStrainer with lxml Behavior
**Learning:** `SoupStrainer(class_='classname')` combined with `BeautifulSoup(..., 'lxml', parse_only=strainer)` yielded 0 results in tests, whereas `SoupStrainer('tagname')` worked correctly and provided >50% parsing speedup. `lxml`'s integration with `SoupStrainer` attribute filtering seems strict or buggy compared to `html.parser`, but tag filtering works reliably.
**Action:** When using `SoupStrainer` for performance with `lxml`, prefer straining by tag name and then filtering by attributes using `find_all` on the strained soup, rather than straining by attributes directly.
## 2025-02-03 - SoupStrainer Regex Pitfalls
**Learning:** When using `SoupStrainer` with `class_` and a regex, `\b` (word boundary) treats hyphens as boundaries. This means `r'\bpost\b'` matches `class="not-a-post"`.
**Action:** Use `r'(^|\s)word(\s|$)'` to strictly match space-separated classes in HTML attributes.

## 2025-02-03 - Blocking Event Loop
**Learning:** `BeautifulSoup` parsing is CPU-intensive and blocks the asyncio event loop if run directly in an `async` function.
**Action:** Always offload parsing to `loop.run_in_executor` (ThreadPool or ProcessPool) to maintain concurrency.
