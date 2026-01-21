## 2024-10-26 - Python Regex \s matches NBSP
**Learning:** In Python 3, the regex pattern `\s` matches Unicode whitespace characters, including non-breaking spaces (`\xa0`). Explicitly replacing `\xa0` before using `\s` is redundant and slower.
**Action:** Remove `text.replace('\xa0', ' ')` when using `re.sub(r'\s+', ...)` or similar patterns.
