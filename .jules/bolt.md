## 2024-05-22 - Regex Compilation Optimization
**Learning:** Pre-compiling frequent regex patterns as module-level constants significantly improves performance for high-frequency string operations.
**Action:** In `scraper.py`, `clean_text` saw a ~7% speedup and `is_url` saw a ~50% speedup by moving `re.sub` and `re.match` compilation outside the function calls. Always verify with `timeit` benchmarks.
