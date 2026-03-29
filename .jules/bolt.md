## 2026-01-26 - [Regex vs BeautifulSoup for Comment Extraction]
**Learning:** Parsing a full HTML document with `BeautifulSoup` just to extract a specific comment block is extremely inefficient. Using `re.finditer` with `re.DOTALL` to locate the comment provided a ~268x speedup.
**Action:** When extracting simple text blocks or comments from large documents, prefer regex over full DOM parsing, but handle edge cases (newlines, nested structures) carefully.
