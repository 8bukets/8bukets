import os
import json
import logging
import asyncio

# Import Agents (Refactored)
from agents.health_check_agent import HealthCheckAgent
from agents.analyze_agent import AnalyzeAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.research_agent import ResearchAgent
from agents.content_creation_agent import ContentCreationAgent
from agents.programmatic_ads_agent import ProgrammaticAdsAgent
from scraper import OracleNewsScraper
from colors import Colors, ColoredFormatter

# Configure Orchestrator Logging
handler = logging.StreamHandler()
handler.setFormatter(ColoredFormatter())
logging.basicConfig(level=logging.INFO, handlers=[handler], force=True)
logger = logging.getLogger("AutonomousIntelligenceAgent")

class AutonomousIntelligenceAgent:
    def __init__(self, output_dir="results"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    async def run_pipeline(self):
        logger.info(f"{Colors.BOLD}{Colors.HEADER}Starting Autonomous Pipeline...{Colors.RESET}")

        # 1. Scrape Data (Simulating 'Intelligence Gathering')
        logger.info(f"{Colors.CYAN}Step 1: Intelligence Gathering (Scraping)...{Colors.RESET}")
        scraper = OracleNewsScraper(
            output_json="links.json",
            output_csv="links.csv",
            output_txt="unique_links.txt"
        )
        await scraper.scrape()

        # 2. Health Check
        logger.info(f"{Colors.CYAN}Step 2: System Health Check...{Colors.RESET}")
        health_agent = HealthCheckAgent()
        health_report = health_agent.check()
        self._save_json("health_report.json", health_report)

        if health_report['status'] != 'healthy':
            logger.error("System Unhealthy. Aborting pipeline.")
            return

        # 3. Analysis & Intelligence
        logger.info(f"{Colors.CYAN}Step 3: Analysis & Strategic Intelligence...{Colors.RESET}")
        analyze_agent = AnalyzeAgent()
        intelligence_agent = IntelligenceAgent()

        analysis_data = analyze_agent.analyze()
        strategy = intelligence_agent.synthesize_strategy(analysis_data)

        self._save_json("analysis_data.json", analysis_data)
        self._save_json("strategic_brief.json", strategy)

        # 4. Research
        logger.info(f"{Colors.CYAN}Step 4: Autonomous Research...{Colors.RESET}")
        research_agent = ResearchAgent()
        trends = research_agent.identify_trends(analysis_data)
        self._save_json("trends_report.json", trends)

        # 5. Content Creation
        logger.info(f"{Colors.CYAN}Step 5: Creative Content Generation...{Colors.RESET}")
        content_agent = ContentCreationAgent()
        blog_post = content_agent.generate_content(trends, strategy)

        # Save Markdown
        with open(os.path.join(self.output_dir, "generated_blog_post.md"), 'w', encoding='utf-8') as f:
            f.write(blog_post)

        # 6. Monetization & Ads
        logger.info(f"{Colors.CYAN}Step 6: Programmatic Advertising Strategy...{Colors.RESET}")
        ads_agent = ProgrammaticAdsAgent()
        ad_strategy = ads_agent.generate_ad_strategy(trends)
        self._save_json("ad_campaign_strategy.json", ad_strategy)

        logger.info(f"{Colors.GREEN}{Colors.BOLD}✨ Autonomous Pipeline Completed Successfully.{Colors.RESET}")

    def _save_json(self, filename, data):
        path = os.path.join(self.output_dir, filename)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
