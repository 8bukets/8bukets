## 2026-01-29 - [Dynamic Navigation in Static Reports]
**Learning:** When generating static reports (like Markdown) with navigation (TOC), conditional content blocks can lead to broken links if the TOC isn't equally conditional.
**Action:** Always wrap TOC entries in the same boolean checks used for the content sections they link to.
