## 2026-01-27 - [Sequential Agent Bottleneck]
**Learning:** The `AgentOrchestrator` runs agents sequentially by default. `ResearcherAgent` and `CuriosityAgent` are IO-bound (network requests), causing significant delays. `AnalystAgent` and `MonetizationAgent` are fast but block downstream dependent agents.
**Action:** Use `ThreadPoolExecutor` to parallelize independent agents and carefully manage dependencies (Analyst -> Intelligence) to maximize concurrency. This pattern should be applied to future agent additions.
