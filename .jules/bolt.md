## 2025-01-14 - SoupStrainer vs WordPress Classes
**Learning:** `SoupStrainer(class_='post')` fails to find `<article class="post type-post ...">` elements because it seems to require exact match or strict class handling, returning 0 results.
**Action:** When filtering tags with multiple classes using `SoupStrainer`, rely on `SoupStrainer(tag_name)` and filter by class in the `find_all` step, or implement a custom function for the strainer. For WordPress sites, avoid strict class straining.
