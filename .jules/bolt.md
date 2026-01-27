## 2025-01-27 - Regex Extraction for Hidden Comments
**Learning:** Using regex (`re.finditer`) to extract large hidden HTML comments containing specific substrings is significantly faster (~50x) than parsing the entire DOM with `BeautifulSoup`, especially when the target content is buried in a comment block.
**Action:** When scraping sites that embed content in comments (e.g., lazy-loading placeholders), prioritize regex extraction for the initial step, but always include a robust fallback (e.g., full DOM parsing) to handle edge cases where regex might fail.
