## 2024-03-21 - [Regex vs String Methods Performance]
**Learning:** Python's `str.split()` combined with `str.join()` is significantly faster (~80% in this case) than `re.sub(r'\s+', ' ', ...)` for normalizing whitespace, even when the regex is compiled. This is because `split()` is highly optimized in C and avoids the regex engine overhead entirely for this common pattern.
**Action:** Prefer ` " ".join(text.split())` over regex for simple whitespace normalization in tight loops.

## 2024-03-21 - [Regex Compilation]
**Learning:** Pre-compiling regex patterns using `re.compile()` provides a measurable performance boost (~50% for simple matches) compared to using module-level functions like `re.match()` inside a loop, as it avoids repeated cache lookups and compilation checks.
**Action:** Always pre-compile regex patterns as module-level constants or class attributes when they are used in loops or frequently called methods.
