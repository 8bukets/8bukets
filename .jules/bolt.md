## 2025-12-28 - [String Concatenation in Loops]
**Learning:** Python strings are immutable. Using `+=` to concatenate strings inside a loop (especially large texts like blog content) creates a new string object in every iteration, leading to O(N^2) complexity.
**Action:** Use a list to collect strings and `"".join(list)` at the end, or processing data incrementally (e.g. via `Counter.update()`) to avoid holding the massive concatenated string in memory.
