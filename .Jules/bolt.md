## 2026-01-19 - [Efficient Markdownify Usage]
**Learning:** `markdownify(str(soup))` serializes soup to string and re-parses it. `MarkdownConverter().convert_soup(soup)` avoids this overhead.
**Action:** Always prefer `convert_soup` when working with BeautifulSoup objects and markdownify.
