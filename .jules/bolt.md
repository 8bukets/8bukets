## 2026-01-28 - SoupStrainer Performance with html.parser
**Learning:** Using `SoupStrainer('article')` with `html.parser` was measurably slower (1.5s vs 1.4s user time) than parsing the full document on a page with ~350 articles. This indicates that the overhead of the strainer logic in Python's `html.parser` implementation can outweigh the benefits of a smaller DOM tree, unlike `lxml` which is typically faster with straining.
**Action:** Always benchmark `SoupStrainer` when `lxml` is unavailable before assuming it yields a performance gain.
