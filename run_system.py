import asyncio
import json
import logging
import os
import argparse
from datetime import datetime

# Import Scraper
from scraper import MarkPositionScraperAsync

# Import Agents
from agents.health_agent import HealthCheckAgent
from agents.analysis_agent import AnalysisAgent
from agents.monetization_agent import MonetizationAgent
from agents.research_agent import ResearchAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.creativity_agent import CreativityAgent
from agents.content_agent import ContentAgent

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger("SystemOrchestrator")

def run_scraper(limit=None):
    """Run the async scraper."""
    logger.info("Starting Scraper...")
    scraper = MarkPositionScraperAsync(
        output_json="links.json",
        output_csv="links.csv",
        output_txt="unique_links.txt",
        max_pages=limit,
        concurrency=5
    )
    asyncio.run(scraper.scrape())
    logger.info("Scraping completed.")

def load_data(filepath="links.json"):
    if not os.path.exists(filepath):
        logger.error(f"{filepath} not found.")
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_report(results, output_dir="results"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = f"{output_dir}/Daily_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# Autonomous System Daily Report - {datetime.now().strftime('%Y-%m-%d')}\n\n")

        # Health
        health = results.get('health', {})
        f.write(f"## 1. Health Status: {health.get('status', 'Unknown').upper()}\n")
        for check in health.get('checks', []):
            f.write(f"- {check}\n")

        # Analysis
        analysis = results.get('analysis', {})
        f.write("\n## 2. Analysis\n")
        f.write(f"- **Total Posts:** {analysis.get('total_posts')}\n")
        f.write(f"- **Date Range:** {analysis.get('date_range')}\n")
        f.write("### Top Domains\n")
        for d, c in analysis.get('top_domains', {}).items():
            f.write(f"- {d}: {c}\n")

        # Monetization
        money = results.get('monetization', {})
        f.write(f"\n## 3. Monetization Potential (Score: {money.get('total_value_score')})\n")
        for op in money.get('top_opportunities', []):
            f.write(f"- **{op['title']}** (Score: {op['score']}) - Keywords: {', '.join(op['keywords'])}\n")

        # Research
        res = results.get('research', {})
        f.write("\n## 4. Research Trends\n")
        f.write(f"{res.get('research_notes')}\n")
        f.write(f"**Keywords:** {', '.join(res.get('trending_keywords', []))}\n")

        # Intelligence
        intel = results.get('intelligence', {})
        f.write("\n## 5. Intelligence Brief\n")
        f.write(f"{intel.get('brief')}\n")
        f.write(f"**Action Item:** {intel.get('actionable_insight')}\n")

        # Creativity
        creative = results.get('creativity', {})
        f.write("\n## 6. Creative Hooks\n")
        for idea in creative.get('creative_hooks', []):
            f.write(f"- {idea}\n")

        # Content
        content = results.get('content', {})
        f.write("\n## 7. Content Draft\n")
        f.write(content.get('draft', ''))

    logger.info(f"Report saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Autonomous Agent System")
    parser.add_argument("--skip-scrape", action="store_true", help="Skip scraping and use existing data")
    parser.add_argument("--limit", type=int, default=2, help="Limit pages to scrape (default 2 for speed)")
    args = parser.parse_args()

    # 1. Run Scraper
    if not args.skip_scrape:
        run_scraper(limit=args.limit)

    # 2. Load Data
    data = load_data()
    if not data:
        logger.error("No data available to process. Exiting.")
        return

    results = {}

    # 3. Run Agents
    # Health Agent
    health_agent = HealthCheckAgent()
    results['health'] = health_agent.run()

    # Analysis Agent
    analysis_agent = AnalysisAgent()
    results['analysis'] = analysis_agent.run(data)

    # Monetization Agent
    monetization_agent = MonetizationAgent()
    results['monetization'] = monetization_agent.run(data)

    # Research Agent
    research_agent = ResearchAgent()
    results['research'] = research_agent.run(data)

    # Intelligence Agent (Depends on Analysis, Monetization, Research)
    intelligence_input = {
        "analysis": results['analysis'],
        "monetization": results['monetization'],
        "research": results['research']
    }
    intelligence_agent = IntelligenceAgent()
    results['intelligence'] = intelligence_agent.run(intelligence_input)

    # Creativity Agent (Depends on Research)
    creativity_input = {"research": results['research']}
    creativity_agent = CreativityAgent()
    results['creativity'] = creativity_agent.run(creativity_input)

    # Content Agent (Depends on Intelligence)
    content_input = {"intelligence": results['intelligence']}
    content_agent = ContentAgent()
    results['content'] = content_agent.run(content_input)

    # 4. Reporting
    save_report(results)

if __name__ == "__main__":
    main()
