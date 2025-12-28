## 2025-02-18 - SoupStrainer Partial Parsing
**Learning:** `SoupStrainer('a', href=True)` with `lxml` is a highly effective optimization for scraping link-heavy pages. Crucially, it preserves the `<a>` tag *and its descendants* (like `<h3>`, `<span>`), allowing for context-aware extraction within the link, whereas straining by parent containers can sometimes yield incomplete trees if not careful.
**Action:** Prefer `SoupStrainer` on specific target tags (like `a` or `article`) over full page parsing when only a subset of data is needed, but always verify child element preservation.
