## 2024-05-23 - [Initial Setup]
**Learning:** Bolt journal initialized.
**Action:** Always check for this file and log critical performance learnings.

## 2024-05-23 - [DOM Performance]
**Learning:** Live DOM filtering on 'input' event causes layout thrashing on every keystroke.
**Action:** Always debounce search/filter inputs (300ms) to batch DOM updates.
