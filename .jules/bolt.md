## 2026-01-22 - [Optimizing BeautifulSoup to Markdown Conversion]
**Learning:** Converting a BeautifulSoup Tag to a string (`str(tag)`) and then passing it to `markdownify` forces a redundant re-parsing of the HTML. The `markdownify` library provides `MarkdownConverter` which can process a soup object directly via `convert_soup`.
**Action:** When using `markdownify` on a BeautifulSoup object, instantiate `MarkdownConverter` once and call `convert_soup(tag)` directly. This avoids serialization/deserialization overhead and sped up parsing by ~4x.
