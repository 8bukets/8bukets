## 2024-05-22 - CLI Visual Hierarchy
**Learning:** CLI tools often output dense blocks of white text, making it difficult for users to quickly scan for errors or success states. Adding simple ANSI colors and semantic emojis (e.g., ❌ for error, 💾 for save) drastically reduces cognitive load and improves perceived quality.
**Action:** Always check if a CLI tool has a `logging` configuration and propose a custom `Formatter` to inject visual hierarchy.
