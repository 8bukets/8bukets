## 2024-12-28 - SoupStrainer with lxml Sensitivity
**Learning:** When using `SoupStrainer` with `lxml` parser, specifying attributes (like `class_`) alongside the tag name can be strict or behave unexpectedly (e.g., returning no matches if class matching logic differs from `find_all`).
**Action:** Strain by tag name only (e.g., `SoupStrainer('article')`) to reduce the parse tree significantly, then use `find_all` on the strained result to apply more complex filters (like class names) safely. This retains most of the performance benefit while maintaining robustness.
