## 2026-01-23 - Python Regex Optimization
**Learning:** Python 3's regex `\s` character class matches non-breaking spaces (`\xa0`). Explicit string replacement `text.replace('\xa0', ' ')` before regex substitution is redundant and adds unnecessary string allocation overhead.
**Action:** Use pre-compiled `re.compile(r'\s+')` and skip explicit `\xa0` replacement for cleaner and slightly faster code.
