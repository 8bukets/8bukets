# Bolt's Journal

## 2026-01-30 - TextBlob Optimization
**Learning:** String concatenation in loops (O(N^2)) followed by re-parsing the huge string with TextBlob is a major bottleneck. Reusing the per-item TextBlob object for tokenization yields significant speedups (~1.7x).
**Action:** Always process text incrementally when possible instead of aggregating and re-processing.
