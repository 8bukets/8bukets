## 2025-10-17 - BeautifulSoup Performance Optimization

**Learning:** When using BeautifulSoup for scraping, parsing the entire DOM tree is unnecessary if you only need specific tags. Using `SoupStrainer` to whitelist tags (e.g., `<a>`) can drastically reduce parsing time (observed ~1.75x speedup). Additionally, for whitespace normalization, `re.sub` is significantly slower (5.4x) than `' '.join(text.split())` in hot loops.

**Action:** Always evaluate if full DOM parsing is required. Use `SoupStrainer` for targeted extraction. Prefer built-in string methods over regex for simple transformations like whitespace normalization. Verify that `SoupStrainer` configuration includes children if nested content is needed (it does by default).
