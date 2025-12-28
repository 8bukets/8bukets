## 2024-05-23 - BeautifulSoup SoupStrainer Behavior
**Learning:** When using `SoupStrainer` with `html.parser` in BeautifulSoup, matching a parent tag (e.g., `article`) preserves its entire subtree, including all child tags (e.g., `h2`, `p`, `a`), contrary to the assumption that children must be explicitly listed.
**Action:** Use `SoupStrainer` confidently to filter by parent container to significantly reduce parsing time (30-40%) without losing child data.

## 2024-05-23 - Python Text Normalization
**Learning:** Python's `str.split()` automatically treats non-breaking spaces (`\xa0`) as whitespace, making explicit replacement logic redundant. ` " ".join(text.split())` is ~5-6x faster than regex-based `re.sub(r'\s+', ' ', text).strip()`.
**Action:** Prefer `split().join()` over regex for simple whitespace normalization.
