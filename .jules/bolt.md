## 2026-02-03 - SoupStrainer class matching quirk
**Learning:** `SoupStrainer` with `class_` argument does not perform partial matching or handle multi-valued class attributes (like `class="post extra"`) as flexibly as `find_all`. It often requires exact match or explicit regex.
**Action:** Always use `re.compile(r'\bclassname\b')` when using `SoupStrainer` to filter by class to ensure robust matching.
