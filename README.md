# Autonomous Multi-Agent System

This project implements a fully autonomous, self-evolving multi-agent system designed for high-interest solution generation, programmatic advertising, and continuous self-improvement.

## Architecture

The system is built on a modular agent framework where each agent has a specific role. They communicate via a shared context ("The Mind") during each daily cycle.

### Core Agents
- **AnalysisAgent:** Analyzes market trends and internal performance.
- **ResearchAgent:** Conducts autonomous research on high-value topics.
- **IntelligenceAgent:** Synthesizes data and forms strategies (The "Brain").
- **CreativityAgent:** Generates innovative ideas and code snippets.
- **ContentAgent:** Physically writes generated code to disk (`generated_output/`).

### Advertising & Monetization Ecosystem
- **ProgrammaticAdsAgent:** Configures ad campaigns and bidding strategies.
- **AdsAgent:** Generates ad creatives.
- **MarketSimulationAgent:** Simulates market feedback (clicks, impressions) to close the learning loop.
- **MonetizationAgent:** Manages revenue streams (simulated AdSense).

### System Evolution ("DNA")
- **AutonomousIntelligenceAgent:** The "Self" that evolves the system. It modifies `data/dna.json` based on performance, increasing IQ and adjusting parameters like bid aggressiveness.
- **HealthCheckAgent:** Ensures system integrity.

## Usage

1. **Install Dependencies:**
   No external dependencies required (uses standard Python library).

2. **Run the System:**
   Execute the main orchestrator loop:
   ```bash
   python3 run_system.py
   ```

3. **Observe Evolution:**
   - Check the console logs for the "Daily Cycle" reports.
   - Watch `data/dna.json` to see the "IQ" and "Generation" increase over time.
   - Check `generated_output/` for the code files the system writes autonomously.

## Key Features
- **Evolutionary Architecture:** The system rewrites its own configuration (`dna.json`) to adapt to the market.
- **Physical Code Integration:** The agents write actual Python code files to disk.
- **Robots.txt & Cookie Compliance:** Simulates cooperative web protocols.
- **100% Autonomous Loop:** The system runs end-to-end without human intervention.
