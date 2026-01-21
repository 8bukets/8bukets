## 2025-02-18 - [Regex Compilation in Loops]
**Learning:** Compiling regex patterns (e.g., `re.compile`) outside of loops yielded a ~30% performance improvement for repeated date extraction, compared to calling `re.search` inside the loop.
**Action:** Always pre-compile regex patterns as module-level constants when they are used in hot loops or frequently called methods.
