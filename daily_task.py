import asyncio
import logging
import argparse
import time
import os
from datetime import datetime
from scraper import WebshopScraperAsync
from analytics import load_data, generate_report

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

def run_job(max_pages=None):
    """Runs the scraper and generates a daily report."""
    today = datetime.now().strftime('%Y-%m-%d')
    report_dir = "reports"
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    report_file = os.path.join(report_dir, f"REPORT_{today}.md")
    json_file = "links.json"
    csv_file = "links.csv"
    txt_file = "unique_links.txt"

    logger.info(f"Starting daily job for {today}...")

    # 1. Run Scraper
    logger.info("Starting scraper...")
    scraper = WebshopScraperAsync(
        output_json=json_file,
        output_csv=csv_file,
        output_txt=txt_file,
        max_pages=max_pages,
        concurrency=5
    )
    try:
        asyncio.run(scraper.scrape())
    except Exception as e:
        logger.error(f"Scraper failed: {e}")
        return

    # 2. Generate Report
    logger.info("Generating analytics report...")
    try:
        data = load_data(json_file)
        generate_report(data, report_file)
        logger.info(f"Job completed. Report saved to {report_file}")
    except Exception as e:
        logger.error(f"Analytics generation failed: {e}")

def main():
    parser = argparse.ArgumentParser(description="Daily Automation Task for Webshop Scraper")
    parser.add_argument("--loop", action="store_true", help="Run continuously every 24 hours")
    parser.add_argument("--limit", type=int, help="Limit number of pages to scrape per run")
    args = parser.parse_args()

    if args.loop:
        logger.info("Starting in continuous mode (24/7)...")
        while True:
            run_job(max_pages=args.limit)

            # Calculate time until next run (e.g., next day at same time, or just sleep 24h)
            # For simplicity, sleep 24 hours
            logger.info("Sleeping for 24 hours...")
            time.sleep(86400)
    else:
        run_job(max_pages=args.limit)

if __name__ == "__main__":
    main()
