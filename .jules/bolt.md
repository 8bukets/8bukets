## 2024-01-11 - SoupStrainer Attribute Filtering
**Learning:** `SoupStrainer` works differently than `find_all` when filtering by attributes like `class`. It performs an exact match on the attribute value string rather than parsing it as a list of classes. For example, `SoupStrainer('article', class_='post')` fails to match `<article class="post status-publish">`.
**Action:** When optimizing with `SoupStrainer`, strain by tag name only (e.g., `SoupStrainer('article')`) to reduce the parse tree, then use `find_all` on the resulting soup to safely filter by attributes.
