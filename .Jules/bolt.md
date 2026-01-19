## 2026-01-19 - Generator Expressions in Counter
**Learning:** Passing a generator expression directly to `collections.Counter` is more memory-efficient than passing a list comprehension, as it avoids creating an intermediate list in memory.
**Action:** Use `Counter(gen_expr)` instead of `Counter([list_comp])` for large datasets.
