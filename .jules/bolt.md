## 2024-05-23 - BeautifulSoup SoupStrainer Behavior
**Learning:** `SoupStrainer` is stricter than `find_all` when matching attributes with strings. While `find_all(class_='post')` matches "post category-tech", `SoupStrainer(class_='post')` does not. It requires regex (e.g., `re.compile(r'\bpost\b')`) to perform partial/word matches on attributes.
**Action:** When using `SoupStrainer` for performance, always verify attribute matching logic with regex if the attribute value is a list (like class names).

## 2024-05-23 - Asyncio Blocking with BeautifulSoup
**Learning:** `BeautifulSoup` parsing is CPU-intensive and blocks the `asyncio` event loop. On pages with large HTML (simulated 5000 repetitions), parsing time can dominate. Offloading to `SoupStrainer` reduced parsing time by ~3x (14s to 5s in simulation).
**Action:** Use `SoupStrainer` to parse only relevant sections of large HTML documents in async scrapers to minimize blocking time.
