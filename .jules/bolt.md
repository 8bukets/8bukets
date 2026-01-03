## 2024-05-23 - BeautifulSoup SoupStrainer Optimization
**Learning:** Parsing the entire HTML document with `BeautifulSoup` when only specific tags are needed is inefficient. Using `SoupStrainer` with `html.parser` allows parsing only relevant parts of the document, reducing the overhead of building the full DOM tree.
**Action:** When scraping large pages where only specific sections are needed, always use `SoupStrainer` to limit the scope of parsing.
