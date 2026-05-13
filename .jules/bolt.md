## 2026-02-05 - CPU-bound parsing blocking asyncio loop
**Learning:** `scraper.py` was running `BeautifulSoup` parsing (CPU-bound) directly in the `asyncio` event loop. This blocks the loop, negating the concurrency benefits of `aiohttp` as the loop cannot process other network events while parsing.
**Action:** Offloaded parsing to a `ProcessPoolExecutor` using `loop.run_in_executor` to allow truly concurrent scraping and parsing.
## 2024-05-23 - Regex Compilation Overhead
**Learning:** Python's `re` module internal caching is very effective. Explicitly compiling simple regex patterns like `\s+` into class attributes yielded negligible performance gains (1.02x) compared to just calling `re.sub` directly.
**Action:** Do not prematurely optimize regex by pre-compiling unless profiling shows a specific need or the pattern is very complex.
## 2024-05-23 - BeautifulSoup SoupStrainer with lxml Behavior
**Learning:** `SoupStrainer(class_='classname')` combined with `BeautifulSoup(..., 'lxml', parse_only=strainer)` yielded 0 results in tests, whereas `SoupStrainer('tagname')` worked correctly and provided >50% parsing speedup. `lxml`'s integration with `SoupStrainer` attribute filtering seems strict or buggy compared to `html.parser`, but tag filtering works reliably.
**Action:** When using `SoupStrainer` for performance with `lxml`, prefer straining by tag name and then filtering by attributes using `find_all` on the strained soup, rather than straining by attributes directly.
## 2025-02-03 - SoupStrainer Regex Pitfalls
**Learning:** When using `SoupStrainer` with `class_` and a regex, `\b` (word boundary) treats hyphens as boundaries. This means `r'\bpost\b'` matches `class="not-a-post"`.
**Action:** Use `r'(^|\s)word(\s|$)'` to strictly match space-separated classes in HTML attributes.

## 2025-02-03 - Blocking Event Loop
**Learning:** `BeautifulSoup` parsing is CPU-intensive and blocks the asyncio event loop if run directly in an `async` function.
**Action:** Always offload parsing to `loop.run_in_executor` (ThreadPool or ProcessPool) to maintain concurrency.
