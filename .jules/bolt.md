## 2024-05-23 - BeautifulSoup Parsing Performance
**Learning:** `SoupStrainer` with regex class matching provides negligible speedup (1.03x) vs full parsing when the target elements (articles) contain the bulk of the page content. The overhead of regex matching in Python likely offsets the parsing savings.
**Action:** Focus on optimizing the traversal loop (`find` vs `select_one`) and string operations (compiled regex, `startswith`) which yielded a combined ~1.2x - 2x improvement on specific components.
