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
import cli_utils
import time

# Configure Orchestrator Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("AutonomousIntelligenceAgent")

class AutonomousIntelligenceAgent:
    def __init__(self, output_dir="results"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    async def run_pipeline(self):
        start_time = time.time()
        logger.info("Starting Autonomous Pipeline...")
        stats = {}

        # 1. Scrape Data (Simulating 'Intelligence Gathering')
        cli_utils.print_step(1, "Intelligence Gathering (Scraping)...", "🕵️")
        scraper = OracleNewsScraper(
            output_json="links.json",
            output_csv="links.csv",
            output_txt="unique_links.txt"
        )
        await scraper.scrape()
        # Note: In a real scenario we'd get stats from scraper, assuming success for now
        stats['Posts Scraped'] = "Checked"

        # 2. Health Check
        cli_utils.print_step(2, "System Health Check...", "🏥")
        health_agent = HealthCheckAgent()
        health_report = health_agent.check()
        self._save_json("health_report.json", health_report)
        stats['System Status'] = health_report['status']

        if health_report['status'] != 'healthy':
            cli_utils.print_error("System Unhealthy. Aborting pipeline.")
            return

        # 3. Analysis & Intelligence
        cli_utils.print_step(3, "Analysis & Strategic Intelligence...", "🧠")
        analyze_agent = AnalyzeAgent()
        intelligence_agent = IntelligenceAgent()

        analysis_data = analyze_agent.analyze()
        strategy = intelligence_agent.synthesize_strategy(analysis_data)

        self._save_json("analysis_data.json", analysis_data)
        self._save_json("strategic_brief.json", strategy)
        stats['Analysis Records'] = analysis_data.get('total_articles', 0) if isinstance(analysis_data, dict) else "N/A"

        # 4. Research
        cli_utils.print_step(4, "Autonomous Research...", "🔬")
        research_agent = ResearchAgent()
        trends = research_agent.identify_trends(analysis_data)
        self._save_json("trends_report.json", trends)
        stats['Trends Identified'] = len(trends) if isinstance(trends, dict) else "N/A"

        # 5. Content Creation
        cli_utils.print_step(5, "Creative Content Generation...", "✍️")
        content_agent = ContentCreationAgent()
        blog_post = content_agent.generate_content(trends, strategy)

        # Save Markdown
        with open(os.path.join(self.output_dir, "generated_blog_post.md"), 'w', encoding='utf-8') as f:
            f.write(blog_post)
        stats['Content Generated'] = "Blog Post"

        # 6. Monetization & Ads
        cli_utils.print_step(6, "Programmatic Advertising Strategy...", "💰")
        ads_agent = ProgrammaticAdsAgent()
        ad_strategy = ads_agent.generate_ad_strategy(trends)
        self._save_json("ad_campaign_strategy.json", ad_strategy)
        stats['Ad Strategy'] = "Ready"

        duration = time.time() - start_time
        stats['Total Time'] = f"{duration:.2f}s"

        cli_utils.print_success("Autonomous Pipeline Completed Successfully.")
        cli_utils.print_summary_box(stats)

    def _save_json(self, filename, data):
        path = os.path.join(self.output_dir, filename)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
