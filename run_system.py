import argparse
import time
import json
import os
import subprocess
import logging
import asyncio
from datetime import datetime

# Orchestrator
from agents.orchestrator import AgentOrchestrator

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
from agents.sigma_agent import SixSigmaAgent
from agents.swarm_agent import SwarmAgent
from agents.auth import AuthManager

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
            ["python3", "scraper.py", "--limit", "1"],
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
            f.write(f"# Six Belt Sigma SEO Autonomous Report: {datetime.now().strftime('%Y-%m-%d')}\n\n")

            sigma = context.get("sigma_performance_report", {})
            f.write(f"**Sigma Status:** {sigma.get('average_impact_score', 0):.2f} Impact Score | {sigma.get('total_swarm_optimizations', 0)} Swarm Optimizations\n")
            f.write(f"**Process Capability (Cpk):** {sigma.get('process_capability_cpk', 0)}\n\n")

            f.write("## 1. Sigma Belt Performance\n")
            for belt, status in sigma.get("belt_status", {}).items():
                f.write(f"- **{belt} BELT:** {status}\n")

            f.write("\n## 2. SEO Swarm Intelligence\n")
            f.write(f"Total Active Swarm Agents: 50\n")
            f.write("Recent Swarm Optimizations:\n")
            swarm_keys = [k for k in context.keys() if "SwarmAgent" in k][:5]
            for sk in swarm_keys:
                sdata = context[sk]
                f.write(f"- {sk}: {sdata.get('task')} -> {sdata.get('result')} (Impact: {sdata.get('impact_score', 0):.2f})\n")

            f.write("\n## 3. High-Level Research (Green Belt)\n")
            research = context.get("research_data", {})
            for trend in research.get("market_trends", []):
                f.write(f"- **Trend:** {trend}\n")

            f.write("\n## 4. Market Analysis & Intelligence\n")
            f.write(f"- **Total Posts Analyzed:** {context.get('analysis_stats', {}).get('total_posts')}\n")
            f.write("### AI Insights\n")
            for insight in context.get("intelligence_insights", []):
                f.write(f"- {insight}\n")

            f.write("\n## 5. Market Data Structural Telemetry\n")
            telemetry = context.get("telemetry_synthesis", {})
            f.write(f"- **Status:** {telemetry.get('status', 'N/A')}\n")
            f.write(f"- **Total Integrated Events:** {telemetry.get('total_events', 0)}\n")

            f.write("\n## 6. Peer Review & Collaboration Log\n")
            for review in context.get("peer_review_log", []):
                f.write(f"- {review}\n")

        logger.info(f"Report generated at {filename}")
    except IOError as e:
        logger.error(f"Failed to write report: {e}")

async def run_cycle(auth_token: str = None, skip_scraper: bool = False):
    logger.info("=== Starting Daily Six Belt Sigma SEO Cycle ===")

    if not AuthManager.verify_token(auth_token):
        logger.error("Authentication failed. Aborting cycle.")
        return

    if not skip_scraper:
        run_scraper()

    data = load_data()
    if not data:
        logger.warning("No data loaded. Skipping agent execution.")
        return

    # Base Intelligence Layer
    agents = [
        HealthCheckAgent(), RobotTxtAgent(), AnalysisAgent(),
        ResearchAgent(), IntelligenceAgent(), TargetingAgent(),
        CreativityAgent(), AdsAgent(), BidAgent(),
        MonetizationAgent(), ContentAgent(), AutonomousIntelligenceAgent(),
        TelemetryAgent(), SixSigmaAgent()
    ]

    # Add 50 Swarm Agents
    swarm_tasks = [
        "Keyword Density Optimization", "Backlink Analysis", "Meta Tag Alignment",
        "Page Speed Micro-Check", "ALT Text Validation", "Header Structure Audit",
        "Internal Link Mapping", "Mobile Responsiveness Probe", "Schema.org Validation",
        "Competitor SEO Gap Analysis"
    ]

    phases = ["DEFINE", "MEASURE", "ANALYZE", "IMPROVE", "CONTROL"]
    for i in range(50):
        phase = phases[i % len(phases)]
        agents.append(SwarmAgent(agent_id=i, phase=phase, tasks=swarm_tasks))

    orchestrator = AgentOrchestrator(agents)

    # 1. Primary Execution Cycle
    await orchestrator.execute_cycle(data)

    # 2. Peer Review Phase
    await orchestrator.run_peer_review()

    # 3. Final Synthesis
    context = orchestrator.blackboard.get_all()

    # 4. Report
    report_file = f"results/DAILY_REPORT_{datetime.now().strftime('%Y-%m-%d')}.md"
    generate_daily_report(context, report_file)

    logger.info("=== Cycle Complete ===")

async def main_async():
    parser = argparse.ArgumentParser(description="Six Belt Sigma SEO Autonomous System")
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
