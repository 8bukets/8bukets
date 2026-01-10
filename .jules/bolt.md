## 2025-05-20 - SoupStrainer for Partial Parsing
**Learning:** Using `SoupStrainer` with `BeautifulSoup` (even with `html.parser`) significantly improves performance by avoiding the creation of full DOM trees for irrelevant tags.
**Action:** When scraping large pages for specific elements, always use `SoupStrainer` to filter tags at the parsing stage.
