## 2024-03-24 - [Regex Performance in Python 3]
**Learning:** In Python 3, the `\s` regex character class matches Unicode whitespace, including non-breaking spaces (`\xa0`). Explicitly replacing `\xa0` with `replace()` before using `re.sub(r'\s+', ...)` is redundant and adds unnecessary string allocation overhead.
**Action:** When normalizing whitespace in Python 3, rely on `re.sub(r'\s+', ' ', text)` directly (preferably with a pre-compiled pattern) instead of chaining string replacements for specific whitespace characters.
