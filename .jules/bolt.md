## 2026-01-22 - [Python Regex Performance]
**Learning:** Python's `re` module compiles patterns, but pre-compiling them as class attributes avoids re-compilation overhead in loops (~6-50% speedup). Also, `\s` matches non-breaking spaces (`\xa0`), making explicit replacement redundant.
**Action:** Always pre-compile regexes used in hot loops and check character class coverage.
