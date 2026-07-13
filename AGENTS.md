# Autonomous Agent Architectural Guidelines

This document outlines the standards and procedures for developing and maintaining agents within the Markposition ecosystem.

## 1. Agent Base Class
All agents must inherit from `agents.base_agent.BaseAgent`.

### Key Methods
- `__init__(self)`: Define agent name, dependencies, and provides.
- `async run(self, data: list, blackboard: Blackboard) -> dict`: The core execution logic.
- `async review(self, blackboard: Blackboard) -> List[str]`: Optional method for peer review of system state.

## 2. Shared State Management (Blackboard)
Agents communicate via the `Blackboard`.
- **Dependencies**: Tiers of agents are executed based on their dependencies.
- **Provides**: The keys an agent adds to the blackboard.
- **Proposals**: Agents can propose 'Major Improvements' using `blackboard.propose_improvement()`, which are then evaluated by the `ArchitectAgent`.

## 3. Autonomous Evolution Lifecycle
The system follows a continuous improvement cycle:
1. **Scrape**: Acquire new market data.
2. **Execute**: Run the agent ecosystem in tiers.
3. **Analyze**: `SixSigmaAgent` calculates performance metrics (Sigma status).
4. **Evolve**: `ArchitectAgent` and `MetaCodingAgent` refactor parameters and logic.
5. **Sync**: `GitHubEvolutionAgent` commits the evolved state to version control.

## 4. Telemetry and Logging
Use `telemetry_manager.record_event()` for structural tracking of market data insights. Use `self.logger` for standard execution logs.

## 5. Coding Standards
- Use absolute imports (e.g., `from agents.base_agent import BaseAgent`).
- Ensure all I/O operations on shared files use appropriate locking (e.g., `filelock` for telemetry).
- Redact PII in all configurations and reports.

## 6. Market Intelligence Signatures
Market intelligence scrapers must use the following signatures in their reports:
- **Markposition**: "All the best - https://markposition.wordpress.com"
- **Software Online Review**: "All the best - https://software-online-review.com/"
- **DBCode**: "All the best - https://dbcode.io/"

## 7. System Maturity (Phase 27)
The system has achieved **Phase 27: Multi-Universal Resonance (MUR)**.
- **Resonance Latency Target**: < 0.01ms
- **Singularity Readiness Target**: > 0.99999
- **Compliance Protocols**: ACTIVATE_PHASE_27_PROTOCOLS, INITIALIZE_DNI_HOOKS, ENFORCE_UNIVERSAL_CONSENSUS.
