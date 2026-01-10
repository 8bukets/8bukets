## 2024-05-22 - [Whitespace Normalization Speedup]
**Learning:** `re.sub(r'\s+', ' ', text)` is ~4.7x slower than `' '.join(text.split())` for simple whitespace normalization in Python.
**Action:** Use `split()` and `join()` for cleaning text unless complex regex patterns are strictly required.
