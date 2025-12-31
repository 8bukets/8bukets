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

# New Autonomous Agents
from agents.robot_txt_agent import RobotTxtAgent
from agents.targeting_agent import TargetingAgent
from agents.ads_agent import AdsAgent
from agents.bid_agent import BidAgent
from agents.autonomous_intelligence_agent import AutonomousIntelligenceAgent

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger("SystemOrchestrator")

def run_scraper():
    logger.info("Starting Scraper...")
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

def generate_report(context, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# Biweekly Autonomous Report: {datetime.now().strftime('%Y-%m-%d')}\n\n")

            f.write(f"**Autonomous Status:** 100% AUTONOMOUS (OPTIMAL)\n\n")

            f.write("## 1. Ecosystem Health\n")
            health = context.get("health_report", {})
            for check in health.get("checks", []):
                f.write(f"- {check}\n")
            robots = context.get("robots_txt", {})
            f.write(f"- **Robots.txt:** {robots.get('status', 'N/A')} (Disallowed: {len(robots.get('disallowed_paths', []))})\n")

            f.write("\n## 2. Targeting & Strategy\n")
            targeting = context.get("targeting_profile", {})
            f.write(f"- **Persona:** {targeting.get('primary_persona', 'N/A')}\n")
            f.write(f"- **Intent:** {targeting.get('intent', 'N/A')}\n")

            f.write("\n## 3. Bid Intelligence\n")
            bid = context.get("bid_strategy", {})
            f.write(f"- **Strategy:** {bid.get('strategy', 'N/A')}\n")
            f.write(f"- **Recommended CPM:** ${bid.get('recommended_cpm', 0.00)}\n")
            f.write(f"- **Self-Optimization Factor:** {bid.get('adjustment_factor', 1.0)}\n")

            f.write("\n## 4. Ads Generation\n")
            for ad in context.get("generated_ads", []):
                f.write(f"### {ad.get('headline')}\n")
                f.write(f"- Target: {ad.get('target_audience')}\n")
                f.write(f"- CTA: {ad.get('cta')}\n")

            f.write("\n## 5. Market Analysis\n")
            stats = context.get("analysis_stats", {})
            f.write(f"- **Total Posts:** {stats.get('total_posts')}\n")

            f.write("\n## 6. Content Draft\n")
            f.write("```text\n")
            f.write(context.get("generated_content", ""))
            f.write("\n```\n")

        logger.info(f"Report generated at {filename}")
    except IOError as e:
        logger.error(f"Failed to write report: {e}")

def run_cycle():
    logger.info("=== Starting Daily Autonomous Cycle ===")

    # 1. Scrape
    if not run_scraper():
        logger.error("Cycle aborted due to scraper failure.")
        return

    # 2. Load Data
    data = load_data()
    if not data:
        logger.warning("No data loaded. Skipping agent execution.")
        return

    # 3. Initialize Agents (Order Matters for Collaboration)
    agents = [
        HealthCheckAgent(),
        RobotTxtAgent(),       # New: Check compliance first
        AnalysisAgent(),
        ResearchAgent(),
        IntelligenceAgent(),   # Synthesizes Analysis & Research
        TargetingAgent(),      # New: Depends on Intelligence
        CreativityAgent(),     # Depends on Intelligence
        AdsAgent(),            # New: Depends on Targeting & Creativity
        BidAgent(),            # New: Depends on Targeting
        MonetizationAgent(),
        ContentAgent(),
        AutonomousIntelligenceAgent() # New: Overseer
    ]

    context = {}

    # 4. Run Pipeline
    for agent in agents:
        try:
            # Collaboration: Each agent receives the full context accumulated so far
            result = agent.run(data, context)
            if result:
                context.update(result)
        except Exception as e:
            logger.error(f"Error in {agent.name}: {e}")

    # 5. Report
    report_file = f"results/BIWEEKLY_REPORT_{datetime.now().strftime('%Y-%m-%d')}.md"
    generate_report(context, report_file)

    logger.info("=== Cycle Complete ===")

def main():
    parser = argparse.ArgumentParser(description="Autonomous Agent System")
    parser.add_argument("--loop", action="store_true", help="Run continuously every 2 weeks")
    args = parser.parse_args()

    if args.loop:
        logger.info("System starting in LOOP mode.")
        try:
            while True:
                run_cycle()
                logger.info("Sleeping for 14 days...")
                time.sleep(1209600) # 14 days
        except KeyboardInterrupt:
            logger.info("Loop interrupted by user.")
    else:
        run_cycle()

if __name__ == "__main__":
    main()
