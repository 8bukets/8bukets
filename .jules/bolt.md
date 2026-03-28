## 2024-05-22 - [Python String Processing Optimization]
**Learning:** For simple whitespace normalization, `' '.join(text.split())` is ~5x faster than `re.sub(r'\s+', ' ', text).strip()` and correctly handles non-breaking spaces without explicit replacement. For prefix checking, `str.startswith()` is ~3x faster than `re.match()`.
**Action:** Prefer native string methods over regex for simple text cleaning and validation tasks in high-frequency loops (like scraping parsers).
