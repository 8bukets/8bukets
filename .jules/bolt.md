## 2024-05-22 - Regex Pre-compilation in Scraper
**Learning:** Pre-compiling regex patterns (`re.compile`) in `scraper.py` reduced `clean_text` execution time by ~17% and `is_url` by ~50% in micro-benchmarks. Explicitly replacing `\xa0` is redundant when using `\s` in regex.
**Action:** Always pre-compile regex patterns at the module level when they are used in tight loops or frequently called methods.
