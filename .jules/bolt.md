## 2025-10-16 - Python Regex & Whitespace Optimization
**Learning:** `\s+` in Python 3 regex automatically matches non-breaking spaces (`\xa0`). Explicitly replacing `\xa0` before regex replacement is redundant and wasteful.
**Action:** Pre-compile regex as class attributes and verify unicode behavior before adding manual string replacements.
