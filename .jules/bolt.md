## 2024-05-24 - SoupStrainer Attribute Filtering with lxml
**Learning:** When using `SoupStrainer` with `lxml`, filtering by attributes (e.g., `SoupStrainer('article', class_='post')`) often fails to find elements that definitely exist. However, filtering by tag only (e.g., `SoupStrainer('article')`) is reliable and still offers significant performance gains over full parsing.
**Action:** When optimizing BeautifulSoup with `lxml`, prefer tag-only `SoupStrainer` configurations unless specific attribute filtering is verified to work in the target environment.
