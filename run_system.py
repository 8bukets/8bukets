import asyncio
import json
import logging
import os
import argparse
from datetime import datetime
from scraper import MarkPositionScraperAsync
from agents.autonomous_agent import AutonomousIntelligenceAgent

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

async def run_pipeline(skip_scrape=False, limit=2):
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

    # 3. Initialize Autonomous Intelligence
    ai_system = AutonomousIntelligenceAgent()

    # 4. Execute Autonomous Process
    report_content = await ai_system.run(data)

    # 5. Save Report
    output_dir = "results"
    os.makedirs(output_dir, exist_ok=True)
    report_filename = f"{output_dir}/DAILY_REPORT_{datetime.now().strftime('%Y-%m-%d')}.md"

    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write(report_content)

    logger.info(f"Report generated successfully: {report_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Autonomous Agent System")
    parser.add_argument("--skip-scrape", action="store_true", help="Skip scraping step")
    parser.add_argument("--limit", type=int, default=2, help="Limit scraper pages")
    args = parser.parse_args()

    asyncio.run(run_pipeline(skip_scrape=args.skip_scrape, limit=args.limit))
