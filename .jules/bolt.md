## 2025-01-29 - [Optimizing Hidden Content Extraction]
**Learning:** Using `re.findall` (or `re.search`) to extract specific content from HTML comments is orders of magnitude faster (~137x speedup observed) than parsing the entire page with BeautifulSoup just to find those comments.
**Action:** When the target content is embedded in a specific pattern (like a comment or script tag) and does not require full DOM traversal to locate, prefer Regex for the initial extraction step, then use BeautifulSoup on the extracted fragment if necessary.
