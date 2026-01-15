## 2024-01-15 - Python Loop vs List Comprehension
**Learning:** In `analytics.py`, a "single-pass" Python loop doing `Counter` updates manually was ~20% slower than multiple passes using C-optimized list comprehensions and `Counter(iterable)`.
**Action:** Prefer list comprehensions and built-in C-loops over manual Python loops for heavy data processing, even if it means iterating data multiple times, unless memory is a constraint.

## 2024-01-15 - urlparse vs String Splitting
**Learning:** `urllib.parse.urlparse` is significantly slower (5x) than manual string splitting for simple domain extraction. In a hot loop (67k calls), this caused a 50% performance degradation for the entire report generation.
**Action:** Use manual string parsing for simple URL extraction in hot paths, but ensure edge cases (like auth) are handled.
