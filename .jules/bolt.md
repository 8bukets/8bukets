# Bolt's Journal

## 2024-05-23 - SoupStrainer Class Matching Behavior
**Learning:** `SoupStrainer(class_='foo')` performs an exact string match on the class attribute, unlike `find_all` which checks for token existence. For elements with multiple classes (e.g., `class="foo bar"`), `SoupStrainer` will fail to match unless a regex (e.g., `re.compile(r'\bfoo\b')`) is used.
**Action:** Always use regex for `class_` argument in `SoupStrainer` when the element might have multiple classes.
