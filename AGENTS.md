# Agent Instructions: Markposition Scraper & Analytics

Welcome, Agent. This repository contains an autonomous ecosystem for scraping, analyzing, and generating content based on data from `https://markposition.wordpress.com/`.

## Architecture Overview

The system follows a modular, agent-based architecture with concurrent execution:
1.  **Scraper (`scraper.py`)**: Asynchronously fetches data from the target blog.
2.  **Analytics (`analytics.py`)**: Processes raw JSON data to generate statistics and a Markdown report.
3.  **Agents (`agents/`)**: Individual specialized agents that collaborate to synthesize intelligence, generate ads, and draft content.
4.  **Orchestrator (`run_system.py`)**: Manages the end-to-end cycle of scraping followed by agent execution.

## Agent Collaboration Flow

Agents execute in a pipeline where each agent can read from and contribute to a shared `context` dictionary.
- **HealthCheckAgent**: Validates the input data.
- **RobotTxtAgent**: Checks compliance with `robots.txt`.
- **AnalysisAgent**: Extracts basic stats.
- **Research/Intelligence Agents**: Synthesize deeper insights.
- **Targeting/Ads/Bid Agents**: Build marketing strategies.
- **ContentAgent**: Generates final content drafts.
- **BrowserTestAgent**: Performs automated UI verification using Playwright.

## Persistent Memory

Agents use a shared memory system located in `data/memory.json`.
- Use `self.get_agent_memory(key)` and `self.update_agent_memory(key, value)` to persist state across cycles.
- The `BaseAgent` class automatically handles directory creation for the memory file.

## Development Guidelines

- **Concurrent Execution**: The agent pipeline executes in stages. Independent agents within a stage run concurrently using `asyncio.gather`.
- **Asynchronous Execution**: All agents must implement an `async def run(self, data, context)` method and utilize the shared `self.session` for network I/O.
- **Testing**: Core utilities and agent interactions are tested in the `tests/` directory. Always run `pytest` before submitting changes.
- **Artifacts**: Execution results (JSON, CSV, reports) are ignored by Git. Do not commit these files.

## Command Reference

- Run tests: `python3 -m pytest tests/`
- Run full system: `python3 run_system.py`
- Scrape only: `python3 scraper.py --limit 5`
