## 2026-01-30 - Reliable Markdown Anchors
**Learning:** Standard Markdown slugification for headers containing emojis is inconsistent across renderers (e.g., GitHub vs VSCode), breaking Table of Contents links.
**Action:** Always inject explicit HTML anchors (e.g., `<a name='slug'></a>`) immediately before the header text to ensure reliable deep linking in generated reports.
