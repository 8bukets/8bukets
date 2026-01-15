## 2024-05-24 - [Python String Processing Optimization]
**Learning:** `str.split()` combined with `' '.join()` is significantly faster (4-6x) than `re.sub(r'\s+', ' ', text)` for whitespace normalization in Python, and correctly handles unicode non-breaking spaces.
**Action:** Prefer `split()` and `join()` over regex for simple whitespace normalization in hot paths.

## 2024-05-24 - [Python String Prefix Checking]
**Learning:** `str.startswith()` with a tuple is significantly faster (4x) than `re.match()` for checking simple string prefixes.
**Action:** Use `startswith()` instead of regex for prefix checking.
