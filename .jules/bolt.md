## 2026-01-29 - [SoupStrainer strictness]
**Learning:** `SoupStrainer` with `class_` argument can be too strict or behave inconsistently with multi-valued class attributes compared to `find_all`. Straining by tag name and filtering by class later is more robust.
**Action:** Use `SoupStrainer(tag_name)` to reduce parsing overhead, then use `find_all` for specific attribute filtering.
