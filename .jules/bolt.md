## 2024-03-24 - [Regex vs Built-in Methods]
**Learning:** Whitespace normalization using `' '.join(text.split())` is ~6x faster than `re.sub(r'\s+', ' ', text)` in Python 3.12. Similarly, `startswith` is ~4x faster than regex for simple prefix checks.
**Action:** Prefer built-in string methods over regex for simple string manipulations and validations. Use raw strings (`r""`) or double backslashes in docstrings to avoid `SyntaxWarning` with regex patterns.
