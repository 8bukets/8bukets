## 2025-02-18 - BeautifulSoup vs Regex for Comment Extraction
**Learning:** `BeautifulSoup` parses the entire HTML tree even when just searching for comments. For large pages where the target data is inside a specific comment, this is extremely inefficient.
**Action:** Use `re.findall(r'<!--(.*?)-->', html, re.DOTALL)` to extract comments first, then parse only the relevant fragment. This yielded a ~95x speedup.
