## 2024-05-24 - [CLI Output UX]
**Learning:** Python's `len()` calculates character count, not visual width. Emojis like '✨' (sparkles) are often double-width in terminals, but `len()` counts them as 1 or 2 depending on encoding, leading to misaligned borders in CLI boxes if not padded manually.
**Action:** When creating CLI summary boxes with emojis, manually adjust padding or use a library like `wcwidth` (though we avoid deps). For this project, I'll manually pad +1 for known double-width emojis.
