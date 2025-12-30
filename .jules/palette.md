## 2025-12-30 - [CLI Status Visibility]
**Learning:** Python's `len()` counts characters, not visual width. Emojis (e.g., 🚀) often take up 2 columns in terminals but `len()` reports 1 or 2 depending on the python version and emoji. This causes misalignment in ASCII borders if not handled.
**Action:** When calculating padding for CLI tables, use a library like `wcwidth` if available, or manually adjust for known double-width characters if dependencies are restricted.
