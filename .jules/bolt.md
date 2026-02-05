## 2025-05-23 - [Regex vs BeautifulSoup for Comment Extraction]
**Learning:** Extracting specific HTML comments using `re.findall` is significantly faster (~78x in this case) than parsing the full DOM with `BeautifulSoup` just to find a comment.
**Action:** When targeting content hidden in comments, especially on large pages, consider using regex to extract the comment string before parsing the inner HTML with BeautifulSoup.
