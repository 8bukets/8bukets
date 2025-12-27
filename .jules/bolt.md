## 2024-03-24 - Efficient String Whitespace Normalization
**Learning:** For simple whitespace normalization (replacing all whitespace sequences with a single space), `str.split()` followed by `' '.join()` is significantly faster (~5x) than `re.sub(r'\s+', ' ', text)`.
**Action:** Prefer `join(text.split())` over regex for whitespace normalization when no other regex features are needed.
