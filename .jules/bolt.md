## 2026-01-23 - [Python Regex Caching vs Compilation]
**Learning:** Python's `re` module internally caches compiled patterns, so explicit `re.compile` may not yield significant speedups for simple calls unless the cache is thrashing. However, combining compilation with removing redundant string operations (like `replace` for `\xa0` when `\s` already covers it) yields measurable gains.
**Action:** When optimizing regex, focus on logic simplification and removing redundant passes first, then pre-compile for cleanliness and slight edge in tight loops.
