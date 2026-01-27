## 2026-01-27 - SoupStrainer Attribute Filtering Gotcha
**Learning:** `SoupStrainer('tag', class_='value')` with `html.parser` may fail to match elements where 'value' is just one of multiple classes (exact match vs contains). It's safer to strain by tag name only and filter attributes later.
**Action:** Use `SoupStrainer('tag')` and then `soup.find_all('tag', class_='value')` for reliable partial parsing.
