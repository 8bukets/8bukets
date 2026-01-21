## 2024-05-22 - Regex Compilation Optimization
**Learning:** Pre-compiling regular expressions as module-level constants in Python (`re.compile`) significantly improves performance for frequently called methods.
**Impact:** `is_url` execution speed improved by ~50% in micro-benchmarks. `clean_text` showed mixed results but is cleaner and safer.
**Action:** Use module-level `re.compile` for patterns used in loops or frequently called utility functions.
