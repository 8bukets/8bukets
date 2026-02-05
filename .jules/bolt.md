## 2025-02-05 - Regex Micro-optimization
**Learning:** Pre-compiling regex patterns as class attributes (`self.RE_WHITESPACE`) was slower or neutral compared to using `re.sub()` directly in this specific context.
**Action:** Trust Python's internal regex caching for simple patterns unless profiling proves otherwise. Focus on algorithmic changes (like `SoupStrainer`) first.
