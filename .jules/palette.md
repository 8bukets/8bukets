## 2024-05-22 - CLI Visual Width Calculation
**Learning:** Python's `len()` counts characters, but emojis like ⏱️ (width 2) and 🚀 (width 2) have different character lengths (2 vs 1), requiring careful padding logic for table alignment.
**Action:** Use a helper function that detects specific emojis and adjusts padding calculation based on their visual width rather than string length.
