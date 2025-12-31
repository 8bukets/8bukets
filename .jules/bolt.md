## 2025-12-31 - Parsing Performance Optimization
**Learning:** Using `SoupStrainer` with `lxml` provides significant speedup (~24% observed) for targeted extraction in large HTML documents, but necessitates handling potential parser unavailability (fallback to `html.parser`).
**Action:** Always prefer `SoupStrainer` + `lxml` for partial parsing tasks, wrapped in dynamic parser selection logic.
