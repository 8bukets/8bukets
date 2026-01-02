# Bolt Journal

## 2024-05-22 - [SoupStrainer Performance]
**Learning:** Using `SoupStrainer` with `lxml` is significantly faster (~3.5x) than parsing the full DOM for specific tags.
**Action:** Always prefer `SoupStrainer` when extracting specific tags from large HTML documents.

## 2024-05-22 - [Regex vs BeautifulSoup]
**Learning:** Using Regex to extract specific HTML comments is drastically faster (~137-400x speedup) than parsing the full DOM with BeautifulSoup.
**Action:** Use Regex for simple extraction tasks where DOM parsing overhead is unnecessary.
