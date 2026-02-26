import argparse
import asyncio
import aiohttp
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
from agents.browser_test_agent import BrowserTestAgent
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

def generate_daily_report(context, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# Daily Autonomous Report: {datetime.now().strftime('%Y-%m-%d')}\n\n")

            f.write(f"**Autonomous Status:** {context.get('autonomous_status', 'UNKNOWN')}\n\n")

            f.write("## 1. Ecosystem Health\n")
            health = context.get("health_report", {})
            for check in health.get("checks", []):
                f.write(f"- {check}\n")
            robots = context.get("robots_txt", {})
            f.write(f"- **Robots.txt:** {robots.get('status', 'N/A')} (Disallowed: {len(robots.get('disallowed_paths', []))})\n")

            browser = context.get("browser_test", {})
            f.write(f"- **Browser Check:** {browser.get('status', 'N/A')}\n")
            if browser.get("screenshot"):
                f.write(f"  - [View Screenshot](../{browser.get('screenshot')})\n")

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

async def run_cycle():
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

    context = {}

    async with aiohttp.ClientSession() as session:
        # 3. Stage-Based Concurrent Pipeline
        # Stage 1: Independent Foundation
        stage1 = [
            HealthCheckAgent(),
            RobotTxtAgent(),
            AnalysisAgent(),
            BrowserTestAgent()
        ]
        # Inject shared session
        for a in stage1: a.session = session

        logger.info(f"Executing Stage 1 ({len(stage1)} agents)...")
        results1 = await asyncio.gather(*[a.run(data, context) for a in stage1], return_exceptions=True)
    for res in results1:
        if isinstance(res, dict): context.update(res)
        elif isinstance(res, Exception): logger.error(f"Stage 1 error: {res}")

    # Stage 2: Research (Depends on Analysis)
    stage2 = [ResearchAgent()]
    for a in stage2: a.session = session
    logger.info(f"Executing Stage 2 ({len(stage2)} agents)...")
    results2 = await asyncio.gather(*[a.run(data, context) for a in stage2], return_exceptions=True)
    for res in results2:
        if isinstance(res, dict): context.update(res)
        elif isinstance(res, Exception): logger.error(f"Stage 2 error: {res}")

    # Stage 3: Intelligence (Depends on Research & Analysis)
    stage3 = [IntelligenceAgent()]
    for a in stage3: a.session = session
    logger.info(f"Executing Stage 3 ({len(stage3)} agents)...")
    results3 = await asyncio.gather(*[a.run(data, context) for a in stage3], return_exceptions=True)
    for res in results3:
        if isinstance(res, dict): context.update(res)
        elif isinstance(res, Exception): logger.error(f"Stage 3 error: {res}")

    # Stage 4: Strategy & Creativity (Depends on Intelligence)
    stage4 = [TargetingAgent(), CreativityAgent()]
    for a in stage4: a.session = session
    logger.info(f"Executing Stage 4 ({len(stage4)} agents)...")
    results4 = await asyncio.gather(*[a.run(data, context) for a in stage4], return_exceptions=True)
    for res in results4:
        if isinstance(res, dict): context.update(res)
        elif isinstance(res, Exception): logger.error(f"Stage 4 error: {res}")

    # Stage 5: Execution Assets (Depends on Targeting & Creativity)
    stage5 = [AdsAgent(), BidAgent(), MonetizationAgent(), ContentAgent()]
    for a in stage5: a.session = session
    logger.info(f"Executing Stage 5 ({len(stage5)} agents)...")
    results5 = await asyncio.gather(*[a.run(data, context) for a in stage5], return_exceptions=True)
    for res in results5:
        if isinstance(res, dict): context.update(res)
        elif isinstance(res, Exception): logger.error(f"Stage 5 error: {res}")

    # Stage 6: Oversight
    stage6 = [AutonomousIntelligenceAgent()]
    for a in stage6: a.session = session
    logger.info(f"Executing Stage 6 ({len(stage6)} agents)...")
    results6 = await asyncio.gather(*[a.run(data, context) for a in stage6], return_exceptions=True)
    for res in results6:
        if isinstance(res, dict): context.update(res)
        elif isinstance(res, Exception): logger.error(f"Stage 6 error: {res}")

    # 4. Report
    report_file = f"results/DAILY_REPORT_{datetime.now().strftime('%Y-%m-%d')}.md"
    generate_daily_report(context, report_file)

    logger.info("=== Cycle Complete ===")

async def main_async():
    parser = argparse.ArgumentParser(description="Autonomous Agent System")
    parser.add_argument("--loop", action="store_true", help="Run continuously every 24h")
    args = parser.parse_args()

    if args.loop:
        logger.info("System starting in LOOP mode.")
        try:
            while True:
                await run_cycle()
                logger.info("Sleeping for 24 hours...")
                await asyncio.sleep(86400) # 24 hours
        except KeyboardInterrupt:
            logger.info("Loop interrupted by user.")
    else:
        await run_cycle()

def main():
    asyncio.run(main_async())

if __name__ == "__main__":
    main()
