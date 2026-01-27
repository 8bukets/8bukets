## 2026-01-27 - Regex Pre-compilation
**Learning:** Pre-compiling frequent regex patterns (especially in loops like `clean_text` called for every field) yields significant performance gains (~15-46% in micro-benchmarks).
**Action:** Always identify and pre-compile regex patterns used in hot paths or tight loops.
