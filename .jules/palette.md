## 2026-01-27 - [Anchor Links with Emojis]
**Learning:** Markdown headers with emojis (e.g., `## 📊 Title`) create unreliable anchor links across different renderers. Implicit slugs often strip emojis or handle them inconsistently.
**Action:** Use explicit HTML anchors (e.g., `## <a id="title"></a>📊 Title`) in generated Markdown reports to guarantee functional navigation.
# Palette's Journal

## 2024-05-22 - [ASCII Visualizations]
**Learning:** Text-based visualizations (ASCII bars) in Markdown reports significantly improve data scanability without requiring external image dependencies or complex rendering. Users can instantly see distributions (like the massive skew in categories) without parsing numbers.
**Action:** Apply this pattern to other CLI-generated reports where data distribution is key.
