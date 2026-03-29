## 2026-01-22 - [Python Regex Whitespace]
**Learning:** Python's `\s` regex character class matches Unicode whitespace including non-breaking spaces (`\xa0`). Explicitly replacing `\xa0` before a `\s+` sub is redundant.
**Action:** Trust `\s` for unicode whitespace normalization to save string traversals.
