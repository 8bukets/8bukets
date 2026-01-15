## 2025-05-14 - String Whitespace Normalization Performance
**Learning:** Using `' '.join(text.split())` is approximately 6x faster than `re.sub(r'\s+', ' ', text).strip()` for normalizing whitespace in Python strings. It also correctly handles non-breaking spaces (`\xa0`) without explicit replacement.
**Action:** Prefer `split().join()` over regex for simple whitespace normalization in high-throughput text processing paths.
