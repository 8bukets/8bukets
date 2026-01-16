import os
import json
import logging
import asyncio
import sys

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

class Style:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def print_step(emoji, title, description=""):
        if sys.stdout.isatty():
            print(f"\n{Style.HEADER}{Style.BOLD}{emoji}  {title}{Style.ENDC}")
            if description:
                print(f"{Style.OKCYAN}   {description}{Style.ENDC}")
        else:
            print(f"\n{emoji} {title}")
            if description:
                print(f"   {description}")

    @staticmethod
    def print_success(message):
        if sys.stdout.isatty():
            print(f"\n{Style.OKGREEN}{Style.BOLD}✨ {message} ✨{Style.ENDC}\n")
        else:
            print(f"\n✨ {message} ✨\n")

class AutonomousIntelligenceAgent:
    def __init__(self, output_dir="results"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    async def run_pipeline(self):
        logger.info("Starting Autonomous Pipeline...")

        # 1. Scrape Data (Simulating 'Intelligence Gathering')
        Style.print_step("🕵️", "Step 1: Intelligence Gathering", "Scraping latest data from Oracle News...")
        scraper = OracleNewsScraper(
            output_json="links.json",
            output_csv="links.csv",
            output_txt="unique_links.txt"
        )
        await scraper.scrape()

        # 2. Health Check
        Style.print_step("🏥", "Step 2: System Health Check", "Verifying system integrity and data quality...")
        health_agent = HealthCheckAgent()
        health_report = health_agent.check()
        self._save_json("health_report.json", health_report)

        if health_report['status'] != 'healthy':
            if sys.stdout.isatty():
                print(f"{Style.FAIL}❌ System Unhealthy. Aborting pipeline.{Style.ENDC}")
            logger.error("System Unhealthy. Aborting pipeline.")
            return

        # 3. Analysis & Intelligence
        Style.print_step("🧠", "Step 3: Analysis & Strategic Intelligence", "Synthesizing insights and formulating strategy...")
        analyze_agent = AnalyzeAgent()
        intelligence_agent = IntelligenceAgent()

        analysis_data = analyze_agent.analyze()
        strategy = intelligence_agent.synthesize_strategy(analysis_data)

        self._save_json("analysis_data.json", analysis_data)
        self._save_json("strategic_brief.json", strategy)

        # 4. Research
        Style.print_step("🔬", "Step 4: Autonomous Research", "Identifying market trends and opportunities...")
        research_agent = ResearchAgent()
        trends = research_agent.identify_trends(analysis_data)
        self._save_json("trends_report.json", trends)

        # 5. Content Creation
        Style.print_step("✍️", "Step 5: Creative Content Generation", "Drafting high-impact blog content...")
        content_agent = ContentCreationAgent()
        blog_post = content_agent.generate_content(trends, strategy)

        # Save Markdown
        with open(os.path.join(self.output_dir, "generated_blog_post.md"), 'w', encoding='utf-8') as f:
            f.write(blog_post)

        # 6. Monetization & Ads
        Style.print_step("📢", "Step 6: Programmatic Advertising Strategy", "Optimizing ad campaigns for maximum ROI...")
        ads_agent = ProgrammaticAdsAgent()
        ad_strategy = ads_agent.generate_ad_strategy(trends)
        self._save_json("ad_campaign_strategy.json", ad_strategy)

        Style.print_success("Autonomous Pipeline Completed Successfully")
        logger.info("Autonomous Pipeline Completed Successfully.")

    def _save_json(self, filename, data):
        path = os.path.join(self.output_dir, filename)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
