## 2026-01-07 - SoupStrainer vs nested tags
**Learning:** When using `SoupStrainer` with `html.parser` (the default in BS4), you MUST match parent tags if you want to find nested tags. If a parent tag is not matched by the strainer, its children are ignored and never parsed, even if they match the strainer. This is different from `find_all` which searches the whole tree.
**Action:** When optimizing scraping with `SoupStrainer`, always include the container tags in the strainer filter to ensure deep nested elements are reached.
