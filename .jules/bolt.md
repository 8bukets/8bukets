## 2025-01-16 - Single Pass vs List Comprehension in Python
**Learning:** Converting multiple list comprehensions into a single explicit for-loop in Python can degrade performance. Python's list comprehensions and `Counter(iterable)` are highly optimized in C. An explicit Python loop incurs interpreter overhead that outweighs the benefit of reducing iteration passes for simple operations.
**Action:** Prefer list comprehensions and built-in iterators over explicit loops for data aggregation in Python.
