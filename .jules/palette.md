## 2026-02-01 - Reliable Markdown Linking with Emojis
**Learning:** Standard Markdown header slugs often handle emojis inconsistently (e.g., stripping them, encoding them, or breaking the link entirely). This makes automatically generated Tables of Contents unreliable for headers like `## 💡 Recommendations`.
**Action:** Always add an explicit HTML anchor (e.g., `<a name='slug'></a>`) immediately before any header containing emojis or complex characters to ensure reliable internal linking across different Markdown renderers.
