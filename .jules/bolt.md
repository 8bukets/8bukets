## 2025-01-27 - BeautifulSoup Optimization Strategy
**Learning:** `SoupStrainer` with `html.parser` provides significant (~40%) performance improvement for large HTML documents when only specific tags (like `<a>`) are needed, even without `lxml`.
**Action:** Prioritize `SoupStrainer` for scraping tasks where the target data is sparse relative to the document size, and always offload parsing to threads (`asyncio.to_thread`) to keep the event loop responsive.
