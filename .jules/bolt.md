## 2025-12-27 - [String Concatenation in Loops]
**Learning:** String concatenation using `+=` in a loop is $O(N^2)$ in Python because strings are immutable. This becomes a significant bottleneck when processing large datasets of text.
**Action:** Use `list.append()` inside the loop and then `' '.join(list)` at the end, which is $O(N)$.
