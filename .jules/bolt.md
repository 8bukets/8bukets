## 2024-05-23 - BeautifulSoup Performance with SoupStrainer
**Learning:** `SoupStrainer('article')` with `html.parser` is significantly faster (~10%) than parsing the full DOM, but `SoupStrainer` with class filtering (`SoupStrainer(class_=...)`) is slower because it inspects every tag.
**Action:** When parsing large HTML documents for specific tags (like articles), use `SoupStrainer` with specific tag names and handle auxiliary data (like pagination) with Regex or separate lightweight searches if possible.
