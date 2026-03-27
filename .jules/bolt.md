## 2024-05-22 - SoupStrainer with lxml and Classes
**Learning:** `SoupStrainer(class_='foo')` works intuitively with `find_all` but behaves differently when used as `parse_only` with `lxml`. Specifically, partial class matching fails unless explicitly defined with regex in `attrs`. `SoupStrainer('article', attrs={'class': re.compile(r'\bpost\b')})` was required to match `<article class="post type-post">`.
**Action:** When using `SoupStrainer` for performance, always verify it actually matches elements (it can silently return empty soup) and use regex for robust class matching.
