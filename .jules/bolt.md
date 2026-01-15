## 2025-01-29 - String Cleaning Optimization
**Learning:** `re.sub(r'\s+', ' ', text)` is significantly slower (~5x) than `' '.join(text.split())` for normalizing whitespace in Python. `str.split()` also handles non-breaking spaces (`\xa0`) automatically, making explicit replacement redundant.
**Action:** Use `' '.join(text.split())` for whitespace normalization when no other complex regex patterns are needed.
