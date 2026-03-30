## 2026-01-21 - Data Layer vs Presentation Layer Sanitization
**Vulnerability:** Potential data corruption in JSON outputs caused by early sanitization.
**Learning:** Applying Markdown sanitization (escaping characters) to data-layer objects (like JSON responses in `MonetizationAgent`) corrupts the data for downstream programmatic consumers. Sanitization should be applied strictly at the presentation layer (e.g., when generating Markdown files in `ContentCreationAgent`).
**Prevention:** Verify where data is consumed before applying sanitization. Only sanitize when generating the final renderable artifact (HTML, Markdown), not intermediate data structures.
