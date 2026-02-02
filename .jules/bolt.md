## 2025-05-18 - Regex vs DOM Parse for Comment Extraction
**Learning:** `BeautifulSoup` parses the entire HTML document structure, which is expensive. When extracting a specific block wrapped in comments, using regex to find that block first and *then* parsing only that fragment is significantly faster (~80x speedup observed).
**Action:** Always consider regex pre-filtering when targeting isolated content blocks (like comments or embedded JSON) within large HTML documents to skip full DOM parsing overhead.
