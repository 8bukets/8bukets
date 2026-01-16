import asyncio
import json
import os
import argparse
import sys
from datetime import datetime
from typing import List, Dict, Any

# Import Agents
from agents.analysis_agent import AnalysisAgent
from agents.research_agent import ResearchAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.health_agent import HealthCheckAgent
from agents.monetization_agent import MonetizationAgent
from agents.content_agent import ContentAgent
from agents.creativity_agent import CreativityAgent

# Import Scraper
from scraper import MarkPositionScraperAsync

AGENTS = [
    AnalysisAgent(),
    ResearchAgent(),
    IntelligenceAgent(),
    HealthCheckAgent(),
    MonetizationAgent(),
    ContentAgent(),
    CreativityAgent()
]

DATA_FILE = "links.json"
RESULTS_DIR = "results"

# --- UX Enhancements ---
class Style:
    # Only use colors if stdout is a TTY (terminal)
    USE_COLOR = sys.stdout.isatty()

    BLUE = '\033[94m' if USE_COLOR else ''
    CYAN = '\033[96m' if USE_COLOR else ''
    GREEN = '\033[92m' if USE_COLOR else ''
    YELLOW = '\033[93m' if USE_COLOR else ''
    RED = '\033[91m' if USE_COLOR else ''
    BOLD = '\033[1m' if USE_COLOR else ''
    RESET = '\033[0m' if USE_COLOR else ''

def log_step(msg: str):
    print(f"{Style.CYAN}⚙️  {msg}{Style.RESET}")

def log_start(msg: str):
    print(f"\n{Style.BOLD}{Style.BLUE}🚀 {msg}{Style.RESET}")

def log_success(msg: str):
    print(f"{Style.GREEN}✅ {msg}{Style.RESET}")

def log_error(msg: str):
    print(f"{Style.RED}❌ {msg}{Style.RESET}")

def log_info(msg: str):
    print(f"{Style.BLUE}ℹ️  {msg}{Style.RESET}")
# -----------------------

async def main():
    parser = argparse.ArgumentParser(description="Autonomous Agent System")
    parser.add_argument("--skip-scrape", action="store_true", help="Skip scraping and use existing data")
    args = parser.parse_args()

    # 1. Run Scraper (unless skipped)
    if not args.skip_scrape:
        log_start("Starting Scraper...")
        scraper = MarkPositionScraperAsync(
            output_json=DATA_FILE,
            output_csv="links.csv",
            output_txt="unique_links.txt",
            concurrency=5
        )
        await scraper.scrape()
        log_success("Scraping Complete")
    else:
        log_info("Skipping Scraper (using cached data)")

    # 2. Load Data
    if not os.path.exists(DATA_FILE):
        log_error(f"{DATA_FILE} not found. Cannot run agents.")
        return

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data: List[Dict[str, Any]] = json.load(f)

    log_success(f"Loaded {len(data)} records")

    # 3. Run Agents
    full_report = [f"# Daily System Report - {datetime.now().strftime('%Y-%m-%d')}\n"]

    log_start("Initializing Agent Swarm...")

    for agent in AGENTS:
        log_step(f"Running {agent.name}...")
        try:
            results = agent.run(data)
            report_section = agent.format_report(results)
            full_report.append(report_section)
            full_report.append("\n---\n")
        except Exception as e:
            log_error(f"Error running {agent.name}: {e}")
            full_report.append(f"## {agent.name} Failed\nError: {str(e)}")

    # 4. Save Report
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)

    report_filename = f"{RESULTS_DIR}/daily_report_{datetime.now().strftime('%Y-%m-%d')}.md"
    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write("\n".join(full_report))

    print() # Add newline
    log_success(f"Report generated successfully: {Style.BOLD}{report_filename}{Style.RESET}")

if __name__ == "__main__":
    asyncio.run(main())
