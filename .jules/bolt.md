## 2024-05-22 - SoupStrainer vs find_all class matching
**Learning:** `SoupStrainer(class_='foo')` performs an exact string match on the `class` attribute, whereas `soup.find_all(class_='foo')` checks if 'foo' is present in the class list (CSS-style). This means `SoupStrainer` will miss `<div class="foo bar">`.
**Action:** When using `SoupStrainer` for optimization, prefer straining by tag name only (e.g., `SoupStrainer('div')`) and let `find_all` handle the precise class filtering on the resulting soup, or ensure exact attribute matches.
