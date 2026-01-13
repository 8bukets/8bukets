import asyncio
import json
import logging
import os
import argparse
from datetime import datetime
from scraper import MarkPositionScraperAsync
from agents.robot_txt_agent import RobotTxtAgent
from agents.analysis_agent import AnalysisAgent
from agents.research_agent import ResearchAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.ads_agent import AdsAgent
from agents.bid_agent import BidAgent
from agents.content_agent import ContentAgent
from agents.health_agent import HealthCheckAgent
from agents.monetization_agent import MonetizationAgent
from agents.creativity_agent import CreativityAgent
from agents.iq_agent import IQAgent
from agents.antigravity_agent import AntigravityAgent

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

KB_FILE = "knowledge_base.json"

async def run_pipeline(skip_scrape=False, limit=2):
    # 0. Initialize Context and Knowledge Base
    shared_context = {}
    knowledge_base = {}

    if os.path.exists(KB_FILE):
        try:
            with open(KB_FILE, 'r', encoding='utf-8') as f:
                knowledge_base = json.load(f)
        except:
            logger.warning("Could not load Knowledge Base. Starting fresh.")

    # 1. Scrape (Autonomous Data Gathering)
    json_file = "links.json"
    if not skip_scrape:
        logger.info("Starting autonomous scraper...")
        scraper = MarkPositionScraperAsync(
            output_json=json_file,
            output_csv="links.csv",
            output_txt="unique_links.txt",
            max_pages=limit,
            concurrency=5
        )
        await scraper.scrape()
    else:
        logger.info("Skipping scrape, using existing data.")

    # 2. Load Data
    if not os.path.exists(json_file):
        logger.error("No data found. Exiting.")
        return

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 3. Initialize Agents in Dependency Order
    # Robot -> Scraper (Implicit) -> Analysis -> Intelligence -> Ads -> Research -> Bid -> Content -> Health -> Monetization -> Creativity -> IQ -> Antigravity
    agents = [
        RobotTxtAgent(),      # Checks rules first
        AnalysisAgent(),      # Basic stats
        IntelligenceAgent(),  # Finds keywords (needed by Bid)
        AdsAgent(),           # Finds segments (needed by Bid)
        ResearchAgent(),      # Checks headers (needs Robot permission)
        BidAgent(),           # Calculates bids (needs Keywords + Segments)
        ContentAgent(),       # Drafting
        HealthCheckAgent(),   # Maintenance
        MonetizationAgent(),  # Revenue
        CreativityAgent(),    # Ad Copy
        IQAgent(),            # Self-Learning (needs inputs from above)
        AntigravityAgent()    # Synthesis & Evolution (needs IQ)
    ]

    # 4. Execute Agents
    agent_results = {}
    logger.info("🚀 Starting Autonomous Agent Pipeline...")

    for agent in agents:
        logger.info(f"🤖 Running {agent.name}...")
        try:
            results = await agent.process(data, shared_context, knowledge_base)
            agent_results[agent.name] = {
                "results": results,
                "formatted": agent.format_report(results)
            }
        except Exception as e:
            logger.error(f"❌ Error in {agent.name}: {e}")
            agent_results[agent.name] = {
                "results": {},
                "formatted": f"### {agent.name} Failed\nError: {e}"
            }

    # 5. Generate Report
    report_lines = []
    report_lines.append(f"# Daily Autonomous Report: {datetime.now().strftime('%Y-%m-%d')}\n")

    # Executive Summary
    analysis_res = agent_results.get('Analysis Agent', {}).get('results', {})
    gravity_res = agent_results.get('Google Antigravity Agent', {}).get('results', {})

    total_posts = analysis_res.get('Total Posts', 'N/A')
    system_status = gravity_res.get('System Status', 'Unknown')
    strategy = gravity_res.get('Strategic Synthesis', 'Pending')

    report_lines.append("## 📊 Executive Summary\n")
    report_lines.append("| Metric | Value |")
    report_lines.append("| :--- | :--- |")
    report_lines.append(f"| **Total Posts** | {total_posts} |")
    report_lines.append(f"| **System Status** | {system_status} |")
    report_lines.append(f"| **Strategy** | {strategy} |")
    report_lines.append("\n---\n")
    report_lines.append("## 📝 Detailed Agent Reports\n")

    for agent in agents:
        data = agent_results.get(agent.name, {})
        content = data.get('formatted', '')

        # UX: Use collapsible details for cleaner reading
        report_lines.append(f"<details>\n<summary><strong>{agent.name}</strong></summary>\n\n")
        report_lines.append(content)
        report_lines.append("\n\n</details>\n")

    # 5. Save Report
    output_dir = "results"
    os.makedirs(output_dir, exist_ok=True)
    report_filename = f"{output_dir}/DAILY_REPORT_{datetime.now().strftime('%Y-%m-%d')}.md"

    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write("\n".join(report_lines))

    logger.info(f"Report generated successfully: {report_filename}")

    # 6. Save Knowledge Base (Evolution)
    try:
        with open(KB_FILE, 'w', encoding='utf-8') as f:
            json.dump(knowledge_base, f, indent=4)
        logger.info("Knowledge Base evolved and saved.")
    except Exception as e:
        logger.error(f"Failed to save Knowledge Base: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Autonomous Agent System")
    parser.add_argument("--skip-scrape", action="store_true", help="Skip scraping step")
    parser.add_argument("--limit", type=int, default=2, help="Limit scraper pages")
    args = parser.parse_args()

    asyncio.run(run_pipeline(skip_scrape=args.skip_scrape, limit=args.limit))
