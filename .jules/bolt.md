## 2024-05-23 - [SoupStrainer vs Full Parse]
**Learning:** `SoupStrainer` with `html.parser` yields a ~2x performance improvement (reducing parsing time by ~50%) by parsing only specific tags (e.g., `<article>`) when the document contains significant non-target content.
**Action:** Always prefer `SoupStrainer` when scraping specific elements from large HTML documents, especially if `lxml` is unavailable.
