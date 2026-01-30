## 2026-01-30 - [Regex vs String Methods for Whitespace Normalization]
**Learning:** Using `" ".join(text.split())` is ~6x faster than `re.sub(r'\s+', ' ', text).strip()` for normalizing whitespace in Python, even with `\xa0` characters.
**Action:** Prefer string methods over regex for simple whitespace cleaning in hot paths.
