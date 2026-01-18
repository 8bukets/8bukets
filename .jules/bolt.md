## 2025-10-26 - Frontend Search Performance
**Learning:** Frequent DOM updates on `input` events can cause layout thrashing and unresponsiveness.
**Action:** Always debounce input handlers that trigger DOM manipulation or expensive calculations.
