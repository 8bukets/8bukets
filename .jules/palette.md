## 2024-05-23 - CLI Visual Polish
**Learning:** Python's `logging` module works best with ANSI codes when using a custom `Formatter` attached to a `StreamHandler`, rather than `basicConfig`.
**Action:** Use `ColoredFormatter` pattern for all future CLI tools to provide instant visual feedback on success/failure.
