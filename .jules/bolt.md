# Bolt's Journal

## 2025-10-25 - Initial Setup
**Learning:** Initialized Bolt's journal for performance tracking.
**Action:** Will document critical performance learnings here.

## 2025-10-25 - Regex vs. String Search for HTML Comments
**Learning:** Using regex to extract content from HTML comments (specifically `<!-- ... -->`) is fraught with edge cases, especially when multiple comments exist. `re.DOTALL` combined with non-greedy matchers can easily overshoot or match the wrong comment boundaries if not carefully anchored. Simple string searching (`find`, `rfind`, slicing) is not only significantly faster (O(N) vs complex regex state machine) but also more robust for extracting content between known delimiters.
**Action:** Prefer primitive string operations over regex for extracting content between known delimiters when full DOM parsing is too slow.
