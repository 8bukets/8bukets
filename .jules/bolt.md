## 2026-02-02 - SoupStrainer Regex Requirement
**Learning:** `SoupStrainer` performs exact string matching on class attributes by default. For elements with multiple classes (e.g., `class="post post-123 type-post"`), passing `class_='post'` fails to match because it expects the entire class string to be 'post'.
**Action:** Use `re.compile(r'\bclassname\b')` when using `SoupStrainer` to match a specific class within a multi-valued class attribute.
