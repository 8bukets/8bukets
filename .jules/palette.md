## 2025-02-04 - Enhanced CLI Logging with Emojis and Colors
**Learning:** CLI tools are often verbose and hard to scan. Adding visual cues like emojis and colors based on context (not just log level) dramatically improves readability and user delight.
**Action:** Created `ux_utils.py` with `UXFormatter` to automatically inject emojis and colors into logs. Applied to all main scripts. Next time, consider a dedicated `CLI` class for even richer interactions.
