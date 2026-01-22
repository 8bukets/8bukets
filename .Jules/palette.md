## 2026-01-22 - Markdown Header Anchors with Emojis
**Learning:** Standard Markdown auto-generated links fail when headers contain emojis (e.g., `## 🏥 Health`). This breaks Table of Contents navigation.
**Action:** Always place explicit HTML anchors inline within the header text (e.g., `## <a id="health"></a>🏥 Health`) and link to the ID in the Table of Contents.
