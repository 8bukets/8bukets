## 2026-01-18 - Generator Exhaustion in Analytics
**Learning:** When optimizing list comprehensions to generators, ensure the generator is not consumed multiple times. `Counter(gen)` consumes the generator. Subsequent calls like `set(gen)` will return an empty set.
**Action:** Store the `Counter` object and use `len(counter_obj)` for unique counts instead of re-iterating.
