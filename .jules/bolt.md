## 2026-01-08 - [Frontend Event Debouncing]
**Learning:** In vanilla JavaScript applications without a build step or external libraries like Lodash, manual implementation of utility functions like `debounce` is necessary. Simple DOM-based search filters can become performance bottlenecks if they trigger reflows on every keystroke.
**Action:** Always wrap high-frequency event listeners (input, scroll, resize) with a debounce or throttle function to prevent main thread blocking, even in simple applications.
