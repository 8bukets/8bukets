## 2024-05-23 - BeautifulSoup SoupStrainer Optimization
**Learning:** Parsing the entire HTML tree when only specific tags are needed is a significant performance bottleneck in BeautifulSoup.
**Action:** Use `SoupStrainer` to restrict parsing to only relevant tags (e.g., `<a>`), which can reduce parsing time by ~30-40% on large pages.
