import asyncio
import argparse
import logging
import time
from datetime import datetime
from scraper import WordpressScraperAsync, DEFAULT_BASE_URL
from analytics import load_data, generate_report

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

async def run_cycle(url, json_file, csv_file, txt_file, limit, concurrency):
    logger.info("Starting scrape cycle...")
    scraper = WordpressScraperAsync(
        base_url=url,
        output_json=json_file,
        output_csv=csv_file,
        output_txt=txt_file,
        max_pages=limit,
        concurrency=concurrency
    )
    await scraper.scrape()
    logger.info("Scrape complete.")

    logger.info("Generating reports...")
    data = load_data(json_file)

    # Generate main report
    generate_report(data, "REPORT.md")

    # Generate dated report
    date_str = datetime.now().strftime('%Y-%m-%d')
    dated_report_file = f"REPORT_{date_str}.md"
    generate_report(data, dated_report_file)
    logger.info("Reports generated.")

async def main_loop(args):
    while True:
        try:
            await run_cycle(args.url, args.json, args.csv, args.txt, args.limit, args.concurrency)
        except Exception as e:
            logger.error(f"Error in cycle: {e}")

        logger.info(f"Sleeping for {args.interval} seconds...")
        await asyncio.sleep(args.interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Continuous Automation for Scraper and Analytics")
    parser.add_argument("--url", default=DEFAULT_BASE_URL, help="Base URL of the WordPress blog")
    parser.add_argument("--interval", type=int, default=1209600, help="Interval in seconds (default: 1209600 / 2 weeks)")
    parser.add_argument("--json", default="links.json", help="Output JSON filename")
    parser.add_argument("--csv", default="links.csv", help="Output CSV filename")
    parser.add_argument("--txt", default="unique_links.txt", help="Output TXT filename for unique links")
    parser.add_argument("--limit", type=int, help="Limit number of pages to scrape per cycle")
    parser.add_argument("--concurrency", type=int, default=5, help="Number of concurrent requests")

    args = parser.parse_args()

    try:
        asyncio.run(main_loop(args))
    except KeyboardInterrupt:
        logger.info("Automation stopped by user.")
