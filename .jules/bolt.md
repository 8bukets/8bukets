## 2025-01-12 - BeautifulSoup Optimization Limitations
**Learning:** `SoupStrainer` with `lxml` parser may not yield performance benefits for all HTML structures, especially if the overhead of creating the strainer outweighs the parsing skip. In some cases, `lxml` is already fast enough that filtering adds net overhead.
**Action:** Always benchmark `SoupStrainer` on representative data before committing to it. Fallback to simpler string manipulation or full parsing if gains are negligible.

## 2025-01-12 - String Optimization
**Learning:** `re.sub` for whitespace normalization is significantly slower (~5x) than `' '.join(text.split())` in Python.
**Action:** Prefer `split()` and `join()` for simple whitespace cleaning.
