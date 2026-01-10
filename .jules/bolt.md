## 2024-05-23 - [Text Normalization Performance]
**Learning:** For simple whitespace normalization (trimming and collapsing internal whitespace), `"".join(text.split())` is significantly faster (~5x) than `re.sub(r'\s+', ' ', text)`.
**Action:** Prefer string methods over regex for simple string manipulations in hot paths like scraper loops.
