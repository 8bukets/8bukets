import os
import json
import logging
import asyncio
from datetime import datetime

# Import Agents (Refactored)
from agents.health_check_agent import HealthCheckAgent
from agents.analyze_agent import AnalyzeAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.research_agent import ResearchAgent
from agents.content_creation_agent import ContentCreationAgent
from agents.programmatic_ads_agent import ProgrammaticAdsAgent
from scraper import OracleNewsScraper

# Configure Orchestrator Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("AutonomousIntelligenceAgent")

class AutonomousIntelligenceAgent:
    def __init__(self, output_dir="results"):
        # Create a daily timestamped subdirectory to organize reports
        date_str = datetime.now().strftime("%Y-%m-%d")
        self.output_dir = os.path.join(output_dir, date_str)

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    async def run_pipeline(self):
        logger.info("Starting Autonomous Pipeline...")

        # 1. Scrape Data (Simulating 'Intelligence Gathering')
        logger.info("Step 1: Intelligence Gathering (Scraping)...")

        # Save scraped data in the daily folder as well
        scraper = OracleNewsScraper(
            output_json=os.path.join(self.output_dir, "links.json"),
            output_csv=os.path.join(self.output_dir, "links.csv"),
            output_txt=os.path.join(self.output_dir, "unique_links.txt")
        )
        await scraper.scrape()

        # 2. Health Check
        logger.info("Step 2: System Health Check...")
        health_agent = HealthCheckAgent()
        health_report = health_agent.check()
        self._save_json("health_report.json", health_report)

        if health_report['status'] != 'healthy':
            logger.error("System Unhealthy. Aborting pipeline.")
            return

        # 3. Analysis & Intelligence
        logger.info("Step 3: Analysis & Strategic Intelligence...")
        analyze_agent = AnalyzeAgent()
        intelligence_agent = IntelligenceAgent()

        analysis_data = analyze_agent.analyze()
        strategy = intelligence_agent.synthesize_strategy(analysis_data)

        self._save_json("analysis_data.json", analysis_data)
        self._save_json("strategic_brief.json", strategy)

        # 4. Research
        logger.info("Step 4: Autonomous Research...")
        research_agent = ResearchAgent()
        trends = research_agent.identify_trends(analysis_data)
        self._save_json("trends_report.json", trends)

        # 5. Content Creation
        logger.info("Step 5: Creative Content Generation...")
        content_agent = ContentCreationAgent()
        blog_post = content_agent.generate_content(trends, strategy)

        # Save Markdown
        with open(os.path.join(self.output_dir, "generated_blog_post.md"), 'w', encoding='utf-8') as f:
            f.write(blog_post)

        # 6. Monetization & Ads
        logger.info("Step 6: Programmatic Advertising Strategy...")
        ads_agent = ProgrammaticAdsAgent()
        ad_strategy = ads_agent.generate_ad_strategy(trends)
        self._save_json("ad_campaign_strategy.json", ad_strategy)

        logger.info("Autonomous Pipeline Completed Successfully.")

    def _save_json(self, filename, data):
        path = os.path.join(self.output_dir, filename)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
