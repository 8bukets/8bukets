import argparse
import time
import json
import os
import subprocess
import logging
from datetime import datetime

# Import Agents
from agents.health_check_agent import HealthCheckAgent
from agents.analysis_agent import AnalysisAgent
from agents.research_agent import ResearchAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.monetization_agent import MonetizationAgent
from agents.creativity_agent import CreativityAgent
from agents.content_agent import ContentAgent

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger("SystemOrchestrator")

def run_scraper():
    logger.info("Starting Scraper...")
    # Running scraper via subprocess to ensure clean state and async isolation
    # We limit to 5 pages for the daily run to keep it quick, or remove limit for full run

    # Check if scraper.py supports --limit (it does in current version)
    try:
        result = subprocess.run(
            ["python3", "scraper.py", "--limit", "5"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            logger.error(f"Scraper failed: {result.stderr}")
            return False
        logger.info("Scraper finished successfully.")
        return True
    except Exception as e:
        logger.error(f"Failed to execute scraper: {e}")
        return False

def load_data(filepath="links.json"):
    if not os.path.exists(filepath):
        logger.error(f"Data file {filepath} not found.")
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON data: {e}")
        return []

def generate_daily_report(context, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# Daily Autonomous Report: {datetime.now().strftime('%Y-%m-%d')}\n\n")

            f.write("## 1. Health Status\n")
            health = context.get("health_report", {})
            f.write(f"**Status:** {health.get('status', 'UNKNOWN')}\n")
            for check in health.get("checks", []):
                f.write(f"- {check}\n")

            f.write("\n## 2. Market Analysis\n")
            stats = context.get("analysis_stats", {})
            f.write(f"- **Total Posts Scraped:** {stats.get('total_posts')}\n")
            f.write("### Top Domains\n")
            for d, c in stats.get("top_domains", {}).items():
                f.write(f"- {d}: {c}\n")

            f.write("\n## 3. Intelligence & Research\n")
            for note in context.get("research_notes", []):
                f.write(f"- {note}\n")
            f.write("\n**Insights:**\n")
            for insight in context.get("intelligence_insights", []):
                f.write(f"- {insight}\n")

            f.write("\n## 4. Content Strategy\n")
            f.write("### Creative Angles\n")
            for angle in context.get("creative_angles", []):
                f.write(f"- {angle}\n")

            f.write("\n### Draft Content\n")
            f.write("```text\n")
            f.write(context.get("generated_content", ""))
            f.write("\n```\n")

        logger.info(f"Report generated at {filename}")
    except IOError as e:
        logger.error(f"Failed to write report: {e}")

def run_cycle():
    logger.info("=== Starting Daily Cycle ===")

    # 1. Scrape
    if not run_scraper():
        logger.error("Cycle aborted due to scraper failure.")
        return

    # 2. Load Data
    data = load_data()
    if not data:
        logger.warning("No data loaded. Skipping agent execution.")
        return

    # 3. Initialize Agents
    agents = [
        HealthCheckAgent(),
        AnalysisAgent(),
        ResearchAgent(),
        IntelligenceAgent(),
        MonetizationAgent(),
        CreativityAgent(),
        ContentAgent()
    ]

    context = {}

    # 4. Run Pipeline
    for agent in agents:
        try:
            result = agent.run(data, context)
            if result:
                context.update(result)
        except Exception as e:
            logger.error(f"Error in {agent.name}: {e}")

    # 5. Report
    report_file = f"results/DAILY_REPORT_{datetime.now().strftime('%Y-%m-%d')}.md"
    generate_daily_report(context, report_file)

    logger.info("=== Cycle Complete ===")

def main():
    parser = argparse.ArgumentParser(description="Autonomous Agent System")
    parser.add_argument("--loop", action="store_true", help="Run continuously every 24h")
    args = parser.parse_args()

    if args.loop:
        logger.info("System starting in LOOP mode.")
        try:
            while True:
                run_cycle()
                logger.info("Sleeping for 24 hours...")
                time.sleep(86400) # 24 hours
        except KeyboardInterrupt:
            logger.info("Loop interrupted by user.")
    else:
        run_cycle()

if __name__ == "__main__":
    main()
