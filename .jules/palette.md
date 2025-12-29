## 2025-12-29 - [CLI Visual Alignment]
**Learning:** Standard string length calculations in Python do not account for the visual width of ANSI codes or emojis. `len()` counts bytes/chars, but ANSI codes have 0 visual width, and emojis often have 2. This causes misalignment in CLI borders.
**Action:** When centering or aligning text with ANSI codes, calculate the "invisible length" (raw len - visual len) and add it to the target width in `center()` or `ljust()`. For emojis, consider using `wcwidth` library or assuming width 2 for safety.
