## 2025-12-31 - [CLI Summary Box Layout]
**Learning:** Text truncation is critical for CLI summary boxes. Dynamic values like file paths can break the layout if they exceed the fixed width of the box. Using strict width calculations and truncation (e.g., `text[:35] + '...'`) ensures the visual integrity of the output.
**Action:** Always implement string width validation and truncation when designing fixed-width CLI UI elements.
