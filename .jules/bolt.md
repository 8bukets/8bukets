# Bolt Journal

## 2026-02-02 - SoupStrainer vs Multi-valued Classes
**Learning:** `SoupStrainer` with `class_="name"` completely ignores elements if they have multiple classes (e.g., `class="name other"`). This is different from `find_all` which matches if the class is present.
**Action:** Always use `re.compile(r'name')` when filtering by class in `SoupStrainer`, or prefer straining by tag name only and filtering by class later.
