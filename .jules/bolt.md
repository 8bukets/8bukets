## 2024-05-23 - BeautifulSoup Performance: select vs find
**Learning:** `soup.select_one()` (CSS selectors) is significantly slower than `soup.find()` for simple lookups (tag + class), but `find(class_="a b")` is brittle for multi-class matching as it relies on string order (unless used as a filter).
**Action:** Use `find()` for simple lookups (e.g., `find('h1', class_='title')`). Stick to `select_one()` for complex or multi-class selectors (e.g., `.author.vcard`) unless you can robustly verify class order or use a lambda filter.

## 2024-05-23 - Async Scraper Blocking
**Learning:** Even in `asyncio` code, synchronous CPU-bound operations (like parsing large HTML with BeautifulSoup) block the event loop, stopping all other concurrent network tasks.
**Action:** Always offload heavy parsing to a thread executor using `loop.run_in_executor(None, func, *args)` to maintain high concurrency.
