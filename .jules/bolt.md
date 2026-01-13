# Bolt's Journal

## 2025-05-23 - BeautifulSoup SoupStrainer Optimization
**Learning:** `SoupStrainer` can improve parsing performance by filtering tags before full parsing. However, its effectiveness is context-dependent and works best on large, noisy documents. It is important to implement a fallback mechanism if the strained result is unexpectedly empty to ensure robustness against HTML structure changes.
**Action:** Always verify `SoupStrainer` performance with benchmarks on representative data and include a fallback strategy.
