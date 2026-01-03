import asyncio
import json
import os
import argparse
from datetime import datetime
from typing import List, Dict, Any

# Import Existing Agents
from agents.analysis_agent import AnalysisAgent
from agents.research_agent import ResearchAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.health_agent import HealthCheckAgent
from agents.monetization_agent import MonetizationAgent
from agents.content_agent import ContentAgent
from agents.creativity_agent import CreativityAgent

# Import New Agents
from agents.autonomous_intelligence_agent import AutonomousIntelligenceAgent
from agents.programmatic_ads_agent import ProgrammaticAdsAgent
from agents.market_simulation_agent import MarketSimulationAgent
from agents.cookie_agent import CookieAgent

# Import Scraper
from scraper import MarkPositionScraperAsync

AGENTS = [
    AnalysisAgent(),
    ResearchAgent(),
    IntelligenceAgent(),
    HealthCheckAgent(),
    MonetizationAgent(),
    ContentAgent(),
    CreativityAgent(),
    CookieAgent(),
    ProgrammaticAdsAgent()
]

# Special Agents (Run separately in the loop)
SIMULATION_AGENT = MarketSimulationAgent()
EVOLUTION_AGENT = AutonomousIntelligenceAgent()

DATA_FILE = "links.json"
DNA_FILE = "DNA.json"
RESULTS_DIR = "results"

def load_dna():
    if not os.path.exists(DNA_FILE):
        return {}
    with open(DNA_FILE, 'r') as f:
        return json.load(f)

def save_dna(dna):
    with open(DNA_FILE, 'w') as f:
        json.dump(dna, f, indent=4)

async def main():
    parser = argparse.ArgumentParser(description="Autonomous Agent System")
    parser.add_argument("--skip-scrape", action="store_true", help="Skip scraping and use existing data")
    args = parser.parse_args()

    # 0. Load DNA (Evolutionary Architecture)
    dna = load_dna()
    print(f"--- Loaded System DNA (IQ: {dna.get('system_iq', 'N/A')}) ---")

    # 1. Run Scraper (unless skipped)
    if not args.skip_scrape:
        print("--- Starting Scraper ---")
        scraper = MarkPositionScraperAsync(
            output_json=DATA_FILE,
            output_csv="links.csv",
            output_txt="unique_links.txt",
            concurrency=5
        )
        await scraper.scrape()
        print("--- Scraping Complete ---")
    else:
        print("--- Skipping Scraper ---")

    # 2. Load Data
    if not os.path.exists(DATA_FILE):
        print(f"Error: {DATA_FILE} not found. Cannot run agents.")
        return

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data: List[Dict[str, Any]] = json.load(f)

    print(f"Loaded {len(data)} records.")

    # 3. Run Standard Agents
    full_report = [f"# Daily Autonomous System Report - {datetime.now().strftime('%Y-%m-%d')}\n"]
    full_report.append(f"**Current System IQ:** {dna.get('system_iq', 'Unknown')}\n")

    agent_outputs = {}

    for agent in AGENTS:
        print(f"Running {agent.name}...")
        try:
            # Pass DNA to agents so they adapt
            results = agent.run(data, dna=dna)
            agent_outputs[agent.name] = results

            report_section = agent.format_report(results)
            full_report.append(report_section)
            full_report.append("\n---\n")
        except Exception as e:
            print(f"Error running {agent.name}: {e}")
            full_report.append(f"## {agent.name} Failed\nError: {str(e)}")

    # 4. Market Simulation (Feedback Loop)
    print("Running Market Simulation...")
    market_feedback = SIMULATION_AGENT.run(data, dna=dna, agent_outputs=agent_outputs)
    full_report.append(SIMULATION_AGENT.format_report(market_feedback))

    # 5. Evolution (Autonomous Intelligence)
    print("Running Autonomous Evolution...")
    evolution_result = EVOLUTION_AGENT.run(data, dna=dna, feedback=market_feedback)
    full_report.append(EVOLUTION_AGENT.format_report(evolution_result))

    # 6. Apply Evolution (Write to Disk)
    if evolution_result.get("new_dna"):
        save_dna(evolution_result["new_dna"])
        print("System DNA Updated.")

    # 7. Save Report
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)

    report_filename = f"{RESULTS_DIR}/daily_report_{datetime.now().strftime('%Y-%m-%d')}.md"
    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write("\n".join(full_report))

    print(f"\nReport generated successfully: {report_filename}")

if __name__ == "__main__":
    asyncio.run(main())
