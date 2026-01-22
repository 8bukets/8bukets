## 2024-05-23 - [Python Regex Whitespace]
**Learning:** Python's regex `\s` character class matches Unicode whitespace (including `\xa0` non-breaking space) by default in Python 3.
**Action:** Remove redundant `str.replace('\xa0', ' ')` calls when using `re.sub(r'\s+', ...)` to avoid unnecessary string allocations and passes.