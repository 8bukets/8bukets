# Bolt's Journal

## 2024-05-22 - [SoupStrainer for Parsing Efficiency]
**Learning:** Using `SoupStrainer` with `html.parser` provided a ~2.3-2.6x speedup compared to full DOM parsing in `scraper.py`. It allows parsing only the specific parts of the document needed (e.g., specific tags or classes), significantly reducing overhead.
**Action:** When scraping specific elements from large HTML documents, always consider `SoupStrainer` to avoid parsing the entire tree.

## 2024-05-22 - [Regex Compilation]
**Learning:** Regex patterns used in loops or frequent function calls should be pre-compiled at the module or class level. This avoids the overhead of recompiling the pattern every time the function is called.
**Action:** Move regex patterns to class-level constants or module-level variables.
