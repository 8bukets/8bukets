## 2025-05-21 - Regex vs BeautifulSoup for Comment Extraction
**Learning:** Using Regex to extract specific HTML comments is drastically faster (~400x speedup observed) than parsing the full DOM with BeautifulSoup, especially when the target content is embedded within comments.
**Action:** Use regex (e.g., re.finditer) for initial extraction of comment-wrapped content before parsing the inner HTML with BeautifulSoup.
