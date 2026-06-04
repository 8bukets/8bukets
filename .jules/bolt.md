## 2025-01-27 - Regex Extraction for Hidden Comments
**Learning:** Using regex (`re.finditer`) to extract large hidden HTML comments containing specific substrings is significantly faster (~50x) than parsing the entire DOM with `BeautifulSoup`, especially when the target content is buried in a comment block.
**Action:** When scraping sites that embed content in comments (e.g., lazy-loading placeholders), prioritize regex extraction for the initial step, but always include a robust fallback (e.g., full DOM parsing) to handle edge cases where regex might fail.
## 2025-10-27 - [Initial Performance Assessment]
**Learning:** `analytics.py` re-parses URLs for domain extraction despite `scraper.py` already providing a pre-computed `domain` field in `links.json`.
**Action:** Always check if upstream data sources (like scrapers or APIs) already provide processed fields before computing them again in downstream consumers.
