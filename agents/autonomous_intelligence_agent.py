import os
import json
import logging
import asyncio
import sys
import time
from utils.ui import Colors, print_step, print_summary_box

# Import Agents (Refactored)
from agents.health_check_agent import HealthCheckAgent
from agents.analyze_agent import AnalyzeAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.research_agent import ResearchAgent
from agents.content_creation_agent import ContentCreationAgent
from agents.programmatic_ads_agent import ProgrammaticAdsAgent
from scraper import OracleNewsScraper

# Configure Orchestrator Logging
# Use sys.stdout to ensure chronological order with print statements
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("AutonomousIntelligenceAgent")

class AutonomousIntelligenceAgent:
    def __init__(self, output_dir="results"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    async def run_pipeline(self):
        start_time = time.time()
        logger.info("Starting Autonomous Pipeline...")
        print(Colors.style("\n🚀 INITIALIZING AUTONOMOUS AGENT SWARM...", Colors.BOLD + Colors.HEADER))

        # 1. Scrape Data (Simulating 'Intelligence Gathering')
        print_step(1, "Intelligence Gathering (Scraping)...")
        scraper = OracleNewsScraper(
            output_json="links.json",
            output_csv="links.csv",
            output_txt="unique_links.txt"
        )
        await scraper.scrape()

        # 2. Health Check
        print_step(2, "System Health Check...")
        health_agent = HealthCheckAgent()
        health_report = health_agent.check()
        self._save_json("health_report.json", health_report)

        if health_report['status'] != 'healthy':
            logger.error("System Unhealthy. Aborting pipeline.")
            print(Colors.style("\n❌ PIPELINE ABORTED: System Unhealthy", Colors.FAIL + Colors.BOLD))
            return

        # 3. Analysis & Intelligence
        print_step(3, "Analysis & Strategic Intelligence...")
        analyze_agent = AnalyzeAgent()
        intelligence_agent = IntelligenceAgent()

        analysis_data = analyze_agent.analyze()
        strategy = intelligence_agent.synthesize_strategy(analysis_data)

        self._save_json("analysis_data.json", analysis_data)
        self._save_json("strategic_brief.json", strategy)

        # 4. Research
        print_step(4, "Autonomous Research...")
        research_agent = ResearchAgent()
        trends = research_agent.identify_trends(analysis_data)
        self._save_json("trends_report.json", trends)

        # 5. Content Creation
        print_step(5, "Creative Content Generation...")
        content_agent = ContentCreationAgent()
        blog_post = content_agent.generate_content(trends, strategy)

        # Save Markdown
        with open(os.path.join(self.output_dir, "generated_blog_post.md"), 'w', encoding='utf-8') as f:
            f.write(blog_post)

        # 6. Monetization & Ads
        print_step(6, "Programmatic Advertising Strategy...")
        ads_agent = ProgrammaticAdsAgent()
        ad_strategy = ads_agent.generate_ad_strategy(trends)
        self._save_json("ad_campaign_strategy.json", ad_strategy)

        end_time = time.time()
        duration = f"{end_time - start_time:.2f}s"

        # Summary Box
        files_generated = len([f for f in os.listdir(self.output_dir) if os.path.isfile(os.path.join(self.output_dir, f))])

        stats = {
            "Total Time": duration,
            "Agents Run": "6",
            "Files Generated": str(files_generated),
            "Status": Colors.style("COMPLETED", Colors.GREEN + Colors.BOLD)
        }

        print_summary_box(stats)
        logger.info("Autonomous Pipeline Completed Successfully.")

    def _save_json(self, filename, data):
        path = os.path.join(self.output_dir, filename)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
