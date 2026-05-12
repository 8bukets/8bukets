<<<<<<< bolt-scraper-optimization-8033040251280167060
## 2025-01-27 - BeautifulSoup SoupStrainer Behavior
**Learning:** `SoupStrainer(tag, class_='value')` may behave differently than `find_all` regarding partial matches or multiple classes. It is safer to strain by tag name only (e.g. `SoupStrainer('article')`) and then filter attributes using `find_all` on the resulting soup.
**Action:** When optimizing BeautifulSoup parsing with `SoupStrainer`, verify attribute filtering behavior or stick to tag-based straining followed by attribute filtering.
=======
## 2026-02-06 - Avoid Redundant URL Parsing
**Learning:** URL parsing using `urllib.parse` adds up when processing thousands of records. Using a pre-computed `domain` field from the dataset reduced execution time by ~63% (from 10.6ms to 3.9ms per 1000 runs) in `analytics.py`.
**Action:** Always verify if required metadata (like domains) is already present in the source data before implementing parsing logic.
>>>>>>> analytics-single-pass-optimization-8605272393071134080
