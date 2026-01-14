## 2024-05-24 - Text Processing Optimizations
**Learning:** `str.split()` combined with `str.join()` is significantly faster (~5x) than `re.sub()` for normalizing whitespace in Python. Similarly, `str.startswith()` is faster (~3x) than `re.match()` for simple prefix checks.
**Action:** Prefer built-in string methods over regex for simple string manipulations and checks in performance-critical loops.
