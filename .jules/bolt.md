# Bolt's Journal

## 2025-02-12 - [Regex Pre-compilation in Python]
**Learning:** Pre-compiling regex patterns in Python (`re.compile`) and storing them as class attributes can significantly reduce overhead in tight loops compared to repeated `re.match` or `re.sub` calls, which invoke the internal cache lookup.
**Action:** When using regex in frequent method calls (like parsing logic), always pre-compile the patterns.
