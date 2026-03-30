## 2025-05-27 - Avoid @import in CSS
**Learning:** Using `@import` in CSS files creates a sequential network request chain (HTML -> CSS -> @imported CSS), delaying resource loading and rendering.
**Action:** Always link CSS and fonts directly in the HTML `<head>` to allow parallel downloading.
