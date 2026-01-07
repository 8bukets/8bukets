## 2024-02-14 - [SoupStrainer Optimization]
**Learning:** Parsing the entire DOM tree with `BeautifulSoup` when only a specific subset of tags is needed is wasteful. `SoupStrainer` can significantly reduce memory usage and parsing time by telling the parser to only process specific tags.
**Action:** When scraping large pages where only a small part of the content is relevant (e.g., `<article>` tags in a blog list), use `SoupStrainer` to restrict the parser's focus. This is especially effective with `html.parser`.
