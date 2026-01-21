## 2025-12-13 - [Python Regex Whitespace Optimization]
**Learning:** Python's `\s` regex character class matches `\xa0` (non-breaking space). Explicitly replacing `\xa0` before using a regex like `\s+` is redundant and adds unnecessary string allocation overhead.
**Action:** When cleaning whitespace using regex in Python, rely on `\s` to handle non-breaking spaces and pre-compile the regex pattern for frequent calls.
