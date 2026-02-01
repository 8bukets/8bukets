## 2026-02-01 - Python Generator vs List Comprehension
**Learning:** Replacing list comprehensions with generator expressions in `Counter()` constructor avoids creating intermediate lists, saving memory and offering slight performance improvement (~5-6%) for aggregation tasks. Manual loops in Python are often slower than C-optimized list operations (`extend`), so generators provide a good balance of single-pass efficiency and C-speed iteration.
**Action:** Prefer `Counter(generator)` over `Counter(list_comp)` or manual loop aggregation for analytics tasks involving large datasets.
