## 2025-01-27 - BeautifulSoup SoupStrainer Behavior
**Learning:** `SoupStrainer(tag, class_='value')` may behave differently than `find_all` regarding partial matches or multiple classes. It is safer to strain by tag name only (e.g. `SoupStrainer('article')`) and then filter attributes using `find_all` on the resulting soup.
**Action:** When optimizing BeautifulSoup parsing with `SoupStrainer`, verify attribute filtering behavior or stick to tag-based straining followed by attribute filtering.
