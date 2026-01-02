import asyncio
import json
import os
import argparse
import logging
import sys
from datetime import datetime
from typing import List, Dict, Any

from colors import Colors, ColoredFormatter

# Configure logging with colors
logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(ColoredFormatter())
logger.handlers = [] # Clear existing handlers
logger.addHandler(handler)

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

async def main():
    parser = argparse.ArgumentParser(description="Autonomous Agent System")
    parser.add_argument("--skip-scrape", action="store_true", help="Skip scraping and use existing data")
    args = parser.parse_args()

    # 1. Run Scraper (unless skipped)
    if not args.skip_scrape:
        logger.info(f"{Colors.HEADER}🚀 Starting Scraper process...{Colors.ENDC}")
        scraper = MarkPositionScraperAsync(
            output_json=DATA_FILE,
            output_csv="links.csv",
            output_txt="unique_links.txt",
            concurrency=5
        )
        await scraper.scrape()
        logger.info(f"{Colors.HEADER}✅ Scraping Complete{Colors.ENDC}")
    else:
        logger.info(f"{Colors.WARNING}⏭️  Skipping Scraper{Colors.ENDC}")

    # 2. Load Data
    if not os.path.exists(DATA_FILE):
        logger.error(f"❌ {DATA_FILE} not found. Cannot run agents.")
        return

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data: List[Dict[str, Any]] = json.load(f)

    # Re-applying green color (Colors.GREEN) after the reset to ensure consistency with INFO level
    logger.info(f"📂 Loaded {Colors.BOLD}{len(data)}{Colors.ENDC}{Colors.GREEN} records.")

    # 3. Run Agents
    full_report = [f"# Daily System Report - {datetime.now().strftime('%Y-%m-%d')}\n"]

    logger.info(f"{Colors.HEADER}🤖 Starting Agents...{Colors.ENDC}")

    for agent in AGENTS:
        # Re-applying green color after the agent name
        logger.info(f"⚡ Running {Colors.CYAN}{agent.name}{Colors.ENDC}{Colors.GREEN}...")
        try:
            results = agent.run(data)
            report_section = agent.format_report(results)
            full_report.append(report_section)
            full_report.append("\n---\n")
        except Exception as e:
            logger.error(f"❌ Error running {agent.name}: {e}")
            full_report.append(f"## {agent.name} Failed\nError: {str(e)}")

    # 4. Save Report
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)

    report_filename = f"{RESULTS_DIR}/daily_report_{datetime.now().strftime('%Y-%m-%d')}.md"
    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write("\n".join(full_report))

    # Re-applying green color after the filename
    logger.info(f"✨ Report generated successfully: {Colors.BOLD}{report_filename}{Colors.ENDC}")

if __name__ == "__main__":
    asyncio.run(main())
