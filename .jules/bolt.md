## 2024-05-23 - Regex Compilation Optimization
**Learning:** Pre-compiling frequent regex patterns (`re.compile`) at the module level significantly improves performance for high-frequency string operations.
**Measurement:** `is_url` execution speed improved by ~46%, and `clean_text` by ~3-6% in synthetic benchmarks.
**Action:** Always pre-compile regexes that are used inside loops or frequently called methods.
