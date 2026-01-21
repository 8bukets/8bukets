## 2025-01-21 - Python Regex Optimization
**Learning:** In Python 3, the `\s` regex character class matches Unicode whitespace, including `\xa0` (non-breaking space). Explicitly replacing `\xa0` before running a regex substitution for whitespace is redundant and adds unnecessary string traversal overhead.
**Action:** When cleaning text, rely on pre-compiled regex patterns with `\s+` to handle all whitespace normalization in a single pass.
