## 2025-02-06 - Regex Recompilation in Scraper
**Learning:** `scraper.py` was re-compiling regexes (`re.match`, `re.sub`) inside frequently called methods (`clean_text`, `is_url`). While Python caches recent regexes, explicit pre-compilation removes lookup overhead and clarifies intent.
**Action:** Use class-level pre-compiled regex constants (`re.compile`) for patterns used in loops or high-frequency methods.
