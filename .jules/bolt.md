## 2024-12-26 - [Regex vs String Methods]
**Learning:** Python's native string methods (`str.split()`, `str.join()`, `str.startswith()`) are significantly faster (5x+) than `re` for simple whitespace normalization and prefix checking.
**Action:** Replace `re.sub(r'\s+', ' ', text).strip()` with `" ".join(text.split())` and `re.match(r'^prefix', text)` with `text.startswith('prefix')` whenever pattern complexity is low.
