## 2025-01-19 - Regex Compilation in Scrapers
**Learning:** Compiling regex patterns (`re.compile`) at the module level provided a ~50% speedup for simple URL validation checks (`is_url`) and ~6% for text cleaning (`clean_text`) in the scraper. However, replacing `str.replace` with string slicing for category extraction yielded negligible gains, confirming that built-in string methods are highly optimized.
**Action:** Always compile regex patterns used in tight loops or frequently called helper methods in scrapers.
