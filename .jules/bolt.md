## 2026-01-17 - Memory Efficient Counting
**Learning:** Using `Counter(list_comp)` creates an intermediate list in memory. For large datasets, this doubles memory usage for that collection.
**Action:** Use `Counter(generator_expression)` or `Counter(itertools.chain.from_iterable(...))` to consume items lazily.
