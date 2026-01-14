## 2024-05-23 - BeautifulSoup Performance
**Learning:** `SoupStrainer` with `class_` argument requires exact class matches or custom logic; it may silently return zero results if target elements have multiple classes (e.g., `<article class="post sticky">`) and only one is specified.
**Action:** When optimizing BeautifulSoup with `SoupStrainer`, avoid using `re.compile` for attribute matching as it introduces significant overhead; instead, strain by tag name (e.g., `SoupStrainer('article')`) and filter by attributes on the resulting object using `find_all`.

## 2024-05-23 - Python String Performance
**Learning:** Whitespace normalization in Python using `' '.join(text.split())` is approximately 5x faster than using `re.sub(r'\s+', ' ', text)`.
**Action:** Replace `re.sub` whitespace cleaning with `split()`/`join()` in performance-critical loops.
