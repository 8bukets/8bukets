## 2024-05-22 - [Vanilla JS Debouncing]
**Learning:** In a vanilla JS environment without external libraries (lodash), utility functions like `debounce` must be manually implemented and carefully scoped to avoid polluting the global namespace or losing context (`this`).
**Action:** When working in this codebase, implement utilities as local helper functions within the relevant scope or a dedicated utilities module if reused. Ensure `this` context is preserved in callbacks.
