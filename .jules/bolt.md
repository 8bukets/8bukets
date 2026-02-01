## 2024-05-22 - BeautifulSoup Performance Optimizations
**Learning:** `asyncio.to_thread` provides no benefit for CPU-bound tasks that hold the GIL (like `BeautifulSoup` parsing) and can cause regressions due to thread overhead and context switching.
**Action:** For GIL-bound parsing tasks, optimize the parsing logic itself (e.g., using `SoupStrainer`) or use `multiprocessing` instead of threading.

## 2024-05-22 - SoupStrainer Behavior
**Learning:** `SoupStrainer` with `class_` argument may not strictly match multi-valued class attributes (e.g., `class="post category-tech"`) the same way `find_all` does.
**Action:** Use `SoupStrainer('tag_name')` for broader filtering or compiled regex for robust attribute matching when optimizing parsing.
