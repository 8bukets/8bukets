# Palette's Journal - UX & Accessibility Learnings

This journal records critical insights about User Experience and Accessibility patterns in this codebase.

## Format
`## YYYY-MM-DD - [Title]`
`**Learning:** [Insight]`
`**Action:** [Application]`

---

## 2026-01-19 - Navigable Markdown Reports
**Learning:** Generated Markdown reports often lack navigation, making them hard to consume. Adding a Table of Contents and "Back to Top" anchors transforms a static dump into a usable document.
**Action:** Include explicit HTML anchors (<a name='slug'></a>) and TOC in all generated Markdown reports.
