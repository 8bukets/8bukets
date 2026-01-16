## 2026-01-16 - [Loop Invariant Hoisting in Scraping Logic]
**Learning:** Even simple standard library calls like `urlparse()` can become bottlenecks when called thousands of times inside nested loops. In `scrape_informatic.py`, `urlparse(base_url)` was called for every single link on every page.
**Action:** Always identify loop invariants (values that don't change within the loop) and hoist them out. Pre-calculate values like `netloc` if they are constant for the duration of the loop.
