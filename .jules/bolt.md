## 2025-02-18 - [SoupStrainer Efficiency]
**Learning:** `SoupStrainer` optimization in BeautifulSoup is context-dependent. It can be slower than full parsing on small/clean HTML due to overhead, but provides significant gains (e.g., ~50%) on real-world "noisy" HTML with deep structures.
**Action:** Always verify `SoupStrainer` impact with realistic data (with noise) rather than minimal synthetic examples.
