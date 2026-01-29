## 2025-02-18 - Regex vs Split/Join for whitespace
**Learning:** `str.split().join()` is ~6x faster than `re.sub(r'\s+')` for whitespace normalization in Python and correctly handles `\xa0` (non-breaking space).
**Action:** Prefer `split().join()` for simple whitespace cleaning in hot paths.
