# Palette's Journal

## 2025-12-27 - CLI Visual Polish & Log Duplication
**Learning:** In Python CLI tools, duplicate logging often occurs when libraries add their own handlers without checking if the root logger is already configured. Also, standard white text logs are hard to scan.
**Action:** Use a centralized `ColorFormatter` with emojis for log levels to improve scannability. In library/agent classes, check `logging.getLogger().handlers` before adding a local handler to prevent double logging when orchestrated.
