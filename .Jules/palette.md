# Palette's Journal - Critical Learnings Only

## 2026-01-19 - CLI & Report UX
**Learning:** CLI applications that double-log messages cause significant cognitive load and feel "unpolished". Similarly, generating reports that crash on partial data failures (common in scraping) creates a "fragile" user experience.
**Action:** Ensure centralized logging configuration to avoid propagation duplication. Always use defensive coding (`.get()` with defaults) when generating reports from unpredictable agent outputs.
