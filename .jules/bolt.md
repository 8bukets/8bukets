## 2025-02-18 - SoupStrainer with Multi-valued Classes
**Learning:** `SoupStrainer(class_='post')` performs an exact string match and fails on elements with multiple classes (e.g., `class="post type-post..."`). It does not behave like `find_all(class_='post')` which matches any class in the list.
**Action:** Always use a regex (e.g., `re.compile(r'\bpost\b')`) when using `SoupStrainer` to filter by class if the element might have multiple classes.
