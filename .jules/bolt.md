## 2025-01-13 - SoupStrainer vs Class Attributes
**Learning:** SoupStrainer('tag', class_='value') does not support partial matches or multi-valued attributes like BeautifulSoup.find() does. It requires exact match or custom function. It can return 0 results silently.
**Action:** Avoid using class filtering with SoupStrainer unless sure of exact match, or use a custom function/regex.
