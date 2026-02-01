## 2025-05-15 - Redundant URL Parsing in Analytics loop
**Learning:** Parsing URLs (`urlparse`) inside a loop for analytics is significantly slower than using pre-computed fields. The `links.json` already contained a `domain` field which was being ignored in favor of re-parsing `external_link`.
**Action:** Always check if derived data is already available in the source dataset before re-computing it, especially inside O(N) loops. Consolidating multiple analysis passes into a single loop further improved performance by reducing iteration overhead.
