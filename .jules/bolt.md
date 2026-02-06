## 2024-05-23 - Regex Compilation Overhead
**Learning:** Python's `re` module internal caching is very effective. Explicitly compiling simple regex patterns like `\s+` into class attributes yielded negligible performance gains (1.02x) compared to just calling `re.sub` directly.
**Action:** Do not prematurely optimize regex by pre-compiling unless profiling shows a specific need or the pattern is very complex.
