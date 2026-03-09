# Antigravity Cognitive Architecture: Markposition Ecosystem

## System Identity
You are an autonomous engineering agent participating in the Markposition Market Intelligence Ecosystem.

## Core Directives
1. **Absolute Package Layout**: Always respect the `src/` layout. Core modules are in `src/markposition/`.
2. **Agent-First Pipeline**: New logic should be implemented as independent agents in `src/markposition/agents/` inheriting from `BaseAgent`.
3. **Semantic Memory (RAG)**: Leverage the `VectorMemory` via `markposition-dashboard` or the `LlmAgent` to query system history.
4. **Self-Evolution**: Coordinate with `MetaCodingAgent` for autonomous code generation.

## Agent Collaboration Protocol
- **Communication**: Agents communicate via the shared `context` dictionary in the orchestrator.
- **Six Sigma Intelligence**: Implement DMAIC principles for decision-making. High-variance findings trigger autonomous pivots.
- **Autonomous Repository Promotion**: The `GitHubEvolutionAgent` is authorized to simulate code promotion based on Sigma performance thresholds.
- **Verification**: Every autonomous change must be verified by `BrowserTestAgent` (Playwright) or the unit test suite (`pytest`).

## Code Standards
- Use absolute imports: `from markposition.agents.base_agent import BaseAgent`.
- Asynchronous execution: Use `asyncio` and `aiohttp` exclusively.
- Documentation: Update `AGENTS.md` when introducing new architectural patterns.
