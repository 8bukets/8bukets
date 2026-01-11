## 2025-01-11 - Whitespace Normalization Performance
**Learning:** Python's `re.sub(r'\s+', ' ', text)` is significantly slower (6x) than `' '.join(text.split())` for normalizing whitespace.
**Action:** Use `' '.join(text.split())` for simple whitespace normalization tasks in Python.
