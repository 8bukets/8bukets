## 2025-01-18 - Report Navigation & Scannability
**Learning:** Generated Markdown reports become difficult to navigate as they grow. Adding a Table of Contents with explicit HTML anchors ensures reliable deep linking across different Markdown viewers (GitHub, VS Code, etc.), which standard auto-generated anchors sometimes fail at. Emojis in headers significantly improve the ability to scan distinct sections.
**Action:** Always include a TOC and "Back to Top" links for generated Markdown reports exceeding one page. Use explicit `<a>` tags for anchors. Use semantic emojis for section headers.
