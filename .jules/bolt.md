## 2025-05-18 - [Optimizing HTML Comment Extraction]
**Learning:** Parsing a full HTML page with `BeautifulSoup` (even with `html.parser`) just to extract content hidden inside comments is extremely inefficient (O(N) on DOM size).
**Action:** Use Regex `re.compile(r'<!--(.*?)-->', re.DOTALL)` to find comments in the raw HTML string first. This treats the HTML as a flat string and avoids the overhead of building the DOM tree, resulting in a ~1000x speedup for this specific task. Only parse the extracted inner HTML with BeautifulSoup.
