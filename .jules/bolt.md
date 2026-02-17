## 2025-02-12 - SoupStrainer Class Matching
**Learning:** `SoupStrainer('tag', class_='classname')` performs an exact string match on the `class` attribute of the HTML tag. It does NOT check if 'classname' is present in the list of classes (like `find_all` does). This causes it to fail silently (filter out everything) when tags have multiple classes (e.g., `<article class="classname otherclass">`).
**Action:** Always use `re.compile(r'\bclassname\b')` when filtering by class with `SoupStrainer` if the element might have multiple classes.

## 2025-02-12 - Whitespace Cleaning Performance
**Learning:** `re.sub(r'\s+', ' ', text).strip()` is significantly slower (5x) than `" ".join(text.split())` for standard whitespace normalization in Python.
**Action:** Prefer `split()` and `join()` for simple whitespace normalization tasks.
