## 2024-03-24 - SoupStrainer Optimization
**Learning:** `BeautifulSoup` parses the entire document by default, which is wasteful when we only need specific tags. `SoupStrainer` allows parsing only specific parts of the DOM, significantly reducing CPU usage and time.
**Action:** Use `SoupStrainer` when only a subset of tags is needed.
