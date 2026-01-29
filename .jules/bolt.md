## 2026-01-29 - SoupStrainer Class Matching with html.parser
**Learning:** `SoupStrainer(class_='foo')` with `html.parser` fails to match elements with multiple classes (e.g., `class="foo bar"`). Unlike `find_all`, it seems to require an exact match or strict string behavior in this context.
**Action:** Use `re.compile(r'\bfoo\b')` for the `class_` argument in `SoupStrainer` when using `html.parser` to ensure correct partial matching.
