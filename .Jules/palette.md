## 2026-01-20 - Markdown Navigation Compatibility
**Learning:** Standard Markdown headers don't always generate consistent anchor IDs across different platforms (e.g., GitHub vs. local viewers). This breaks "Back to Top" links and TOC navigation.
**Action:** Always inject explicit HTML anchors (e.g., `<a name="slug"></a>`) before headers and use those for internal linking to ensure robust cross-platform compatibility.
