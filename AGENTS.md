# Agent Instructions: Markposition Scraper & Analytics

Welcome, Agent. This repository contains an autonomous ecosystem for scraping, analyzing, and generating content based on data from `https://markposition.wordpress.com/`.

## Architecture Overview

The system follows a modular, agent-based architecture with concurrent execution:
1.  **Scraper**: Asynchronously fetches data from the target blog.
2.  **Agents (`src/markposition/agents/`)**: Specialized agents that collaborate to synthesize intelligence.
3.  **Intelligence Layer**: Uses FAISS and SentenceTransformers for semantic memory (RAG).
4.  **Orchestrator**: Manages the end-to-end cycle via the `markposition` command.

## Agent Collaboration Flow

Agents execute in a pipeline where each agent can read from and contribute to a shared `context` dictionary.
- **HealthCheckAgent**: Validates the input data.
- **RobotTxtAgent**: Checks compliance with `robots.txt`.
- **AnalysisAgent**: Extracts basic stats.
- **Research/Intelligence Agents**: Synthesize deeper insights.
- **Targeting/Ads/Bid Agents**: Build marketing strategies.
- **ContentAgent**: Generates final content drafts.
- **BrowserTestAgent**: Performs automated UI verification using Playwright.

## Persistent Memory (SQLite)

Agents use a shared SQLite database located in `data/memory.db`.
- Use `self.get_agent_memory(key)` and `self.update_agent_memory(key, value)` to persist state across cycles.
- The `BaseAgent` class uses SQLAlchemy for robust, concurrent-safe persistence.

## Development Guidelines

- **Dynamic Loading**: Agents are automatically discovered from the `agents/` directory. Simply create a new class inheriting from `BaseAgent`.
- **Stage Metadata**: Define `execution_stage` (int) in your agent class to control where it runs in the pipeline.
- **Concurrent Execution**: Independent agents within the same stage run concurrently using `asyncio.gather`.
- **Asynchronous Execution**: All agents must implement an `async def run(self, data, context)` method and utilize the shared `self.session` for network I/O.
- **Testing**: Core utilities and agent interactions are tested in the `tests/` directory. Always run `pytest` before submitting changes.
- **Artifacts**: Execution results (JSON, CSV, reports) are ignored by Git. Do not commit these files.

## Command Reference

- Run tests: `pytest`
- Run full system: `markposition`
- Run dashboard: `markposition-dashboard`
