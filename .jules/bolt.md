## 2024-05-22 - [Python String Methods vs Regex]
**Learning:** For simple whitespace normalization and prefix checking, Python's native string methods (`split().join()` and `startswith()`) are significantly faster (2x-5x) than precompiled regexes.
**Action:** Prefer `text.startswith(...)` over `re.match('^...')` and `' '.join(text.split())` over `re.sub(r'\s+', ' ', text)` in high-frequency loops (like scraping parsers).
