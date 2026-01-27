## 2026-01-27 - Handling Emojis in Markdown Headers
**Learning:** Standard Markdown renderers often strip emojis or handle them inconsistently in auto-generated anchor links. To ensure ToC links work reliably, manually verify that anchor links target text-only slugs (e.g., `#general-statistics` instead of `#📊-general-statistics`).
**Action:** When adding emojis to headers, always verify the resulting anchor slug matches the link target.
