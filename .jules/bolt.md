## 2026-01-20 - Generator Exhaustion in Analytics
**Learning:** When optimizing list comprehensions to generators for memory efficiency (e.g., passing to `Counter`), remember that the generator is consumed. Subsequent operations like `len(set(generator))` will fail (return 0 or empty) because the generator is already exhausted.
**Action:** When using `Counter(generator)`, keep the `Counter` object reference if you need statistics like "total unique items" (`len(counter_instance)`), instead of trying to iterate the generator again.
