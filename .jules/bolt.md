## 2026-01-29 - BeautifulSoup SoupStrainer Trade-offs
**Learning:** Using `SoupStrainer('article')` with `html.parser` improves performance by ~7% on noisy pages, but it excludes pagination links if they are outside the strained tags. Combining `SoupStrainer` for content with Regex for structure-specific links (like pagination) is a viable hybrid strategy when `lxml` is unavailable.
**Action:** When optimizing BS4 scraping without `lxml`, prefer `SoupStrainer` for the main content and Regex for isolated metadata/navigation links to avoid full DOM parsing.
