import argparse
import time
import json
import os
import subprocess
import logging
import asyncio
from datetime import datetime

# Orchestrator & Auth
from agents.orchestrator import AgentOrchestrator
from agents.auth import AuthManager

# Agents
from agents.health_check_agent import HealthCheckAgent
from agents.analysis_agent import AnalysisAgent
from agents.research_agent import ResearchAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.monetization_agent import MonetizationAgent
from agents.creativity_agent import CreativityAgent
from agents.content_agent import ContentAgent
from agents.robot_txt_agent import RobotTxtAgent
from agents.targeting_agent import TargetingAgent
from agents.ads_agent import AdsAgent
from agents.bid_agent import BidAgent
from agents.autonomous_intelligence_agent import AutonomousIntelligenceAgent
from agents.telemetry_agent import TelemetryAgent

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

def generate_daily_report(context, filename):
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# Daily Autonomous Report: {datetime.now().strftime('%Y-%m-%d')}\n\n")

            f.write(f"**Autonomous Status:** {context.get('autonomous_status', 'UNKNOWN')}\n")
            f.write(f"**Synchronization Level:** {context.get('synchronization_level', 'BASIC')}\n\n")

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

            f.write("\n## 3. High-Level Research Insights\n")
            research = context.get("research_data", {})
            for trend in research.get("market_trends", []):
                f.write(f"- **Trend:** {trend}\n")

            f.write("\n## 4. Bid Intelligence\n")
            bid = context.get("bid_strategy", {})
            f.write(f"- **Strategy:** {bid.get('strategy', 'N/A')}\n")
            f.write(f"- **Recommended CPM:** ${bid.get('recommended_cpm', 0.00)}\n")
            f.write(f"- **Self-Optimization Factor:** {bid.get('adjustment_factor', 1.0)}\n")

            f.write("\n## 5. Ads Generation\n")
            for ad in context.get("generated_ads", []):
                f.write(f"### {ad.get('headline')}\n")
                f.write(f"- Target: {ad.get('target_audience')}\n")
                f.write(f"- CTA: {ad.get('cta')}\n")

            f.write("\n## 6. Market Analysis & Intelligence\n")
            stats = context.get("analysis_stats", {})
            f.write(f"- **Total Posts:** {stats.get('total_posts')}\n")
            f.write("### AI Insights\n")
            for insight in context.get("intelligence_insights", []):
                f.write(f"- {insight}\n")

            f.write("\n## 7. Content Draft\n")
            f.write("```text\n")
            f.write(context.get("generated_content", ""))
            f.write("\n```\n")

            f.write("\n## 8. Market Data Structural Telemetry\n")
            telemetry = context.get("telemetry_synthesis", {})
            f.write(f"- **Status:** {telemetry.get('status', 'N/A')}\n")
            f.write(f"- **Total Integrated Events:** {telemetry.get('total_events', 0)}\n")
            for etype, count in telemetry.get("event_types", {}).items():
                f.write(f"  - {etype}: {count}\n")

            f.write("\n## 9. Peer Review & Collaboration Log\n")
            f.write(f"**Synchronization Status:** {research.get('synchronization_status', 'N/A')}\n\n")
            f.write("### Review Findings:\n")
            for review in context.get("peer_review_log", []):
                f.write(f"- {review}\n")

        logger.info(f"Report generated at {filename}")
    except IOError as e:
        logger.error(f"Failed to write report: {e}")

async def run_cycle(auth_token: str = None, skip_scraper: bool = False):
    logger.info("=== Starting Daily Synchronized Autonomous Cycle (DAG Mode) ===")

    if not AuthManager.verify_token(auth_token):
        logger.error("Authentication failed. Aborting cycle.")
        return

    if not skip_scraper:
        if not run_scraper():
            logger.error("Cycle aborted due to scraper failure.")
            return

    data = load_data()
    if not data:
        logger.warning("No data loaded. Skipping agent execution.")
        return

    agents = [
        HealthCheckAgent(),
        RobotTxtAgent(),
        AnalysisAgent(),
        ResearchAgent(),
        IntelligenceAgent(),
        TargetingAgent(),
        CreativityAgent(),
        AdsAgent(),
        BidAgent(),
        MonetizationAgent(),
        ContentAgent(),
        AutonomousIntelligenceAgent(),
        TelemetryAgent()
    ]

    orchestrator = AgentOrchestrator(agents)

    # 1. Primary Execution Cycle
    context = await orchestrator.execute_cycle(data)

    # 2. Peer Review Phase
    await orchestrator.run_peer_review()

    # Final Context with Reviews
    context = orchestrator.blackboard.get_all()

    # 3. Report
    report_file = f"results/DAILY_REPORT_{datetime.now().strftime('%Y-%m-%d')}.md"
    generate_daily_report(context, report_file)

    logger.info("=== Cycle Complete ===")

async def main_async():
    parser = argparse.ArgumentParser(description="Autonomous Agent System")
    parser.add_argument("--loop", action="store_true", help="Run continuously every 24h")
    parser.add_argument("--token", type=str, help="Authentication token", default=os.environ.get("SYSTEM_AUTH_TOKEN"))
    parser.add_argument("--skip-scraper", action="store_true", help="Skip the scraping phase and use existing data")
    args = parser.parse_args()

    if args.loop:
        logger.info("System starting in LOOP mode.")
        try:
            while True:
                await run_cycle(args.token, args.skip_scraper)
                logger.info("Sleeping for 24 hours...")
                await asyncio.sleep(86400)
        except asyncio.CancelledError:
            logger.info("Loop interrupted.")
    else:
        await run_cycle(args.token, args.skip_scraper)

if __name__ == "__main__":
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        pass
