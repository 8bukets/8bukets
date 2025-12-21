import asyncio
import logging
import argparse
import time
import os
import shutil
from datetime import datetime, timedelta
from scraper import WebshopScraperAsync
from analytics import load_data, generate_report

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

def get_seconds_until_next_run(target_hour=6):
    """Calculates seconds until the next target_hour (e.g., 06:00 AM)."""
    now = datetime.now()
    target = now.replace(hour=target_hour, minute=0, second=0, microsecond=0)

    if now >= target:
        target += timedelta(days=1)

    seconds = (target - now).total_seconds()
    return seconds

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
    prev_json_file = "links_prev.json"

    logger.info(f"Starting daily job for {today}...")

    # 0. Backup previous data for comparison
    prev_data = None
    if os.path.exists(json_file):
        try:
            logger.info("Backing up current data...")
            shutil.copy(json_file, prev_json_file)
            prev_data = load_data(prev_json_file)
        except Exception as e:
            logger.warning(f"Failed to backup/load previous data: {e}")

    # 1. Run Scraper
    logger.info("Starting scraper...")
    try:
        scraper = WebshopScraperAsync(
            output_json=json_file,
            output_csv=csv_file,
            output_txt=txt_file,
            max_pages=max_pages,
            concurrency=5
        )
        asyncio.run(scraper.scrape())
    except Exception as e:
        logger.error(f"Scraper failed: {e}")
        # Continue to reporting even if scraper fails partially (to report old data)
        # or return if completely broken. For now, we continue.

    # 2. Generate Report
    logger.info("Generating analytics report...")
    try:
        data = load_data(json_file)
        if not data:
            logger.warning("No data found to report.")
            return

        generate_report(data, report_file, prev_data)
        logger.info(f"Job completed. Report saved to {report_file}")
    except Exception as e:
        logger.error(f"Analytics generation failed: {e}")

def main():
    parser = argparse.ArgumentParser(description="Daily Automation Task for Webshop Scraper")
    parser.add_argument("--loop", action="store_true", help="Run continuously every 24 hours")
    parser.add_argument("--limit", type=int, help="Limit number of pages to scrape per run")
    parser.add_argument("--hour", type=int, default=6, help="Hour of the day to run (0-23) in loop mode")
    args = parser.parse_args()

    if args.loop:
        logger.info(f"Starting in continuous mode (24/7). Scheduled for {args.hour}:00 daily.")

        # Run once immediately on startup? Or wait?
        # Typically "24/7" implies it runs now, then schedules next.
        # Let's run immediately for the first time.

        while True:
            try:
                run_job(max_pages=args.limit)
            except Exception as e:
                logger.critical(f"Critical job failure: {e}")

            # Calculate sleep time
            sleep_seconds = get_seconds_until_next_run(args.hour)
            next_run_time = (datetime.now() + timedelta(seconds=sleep_seconds)).strftime('%Y-%m-%d %H:%M:%S')

            logger.info(f"Sleeping for {sleep_seconds/3600:.1f} hours. Next run at {next_run_time}")
            time.sleep(sleep_seconds)
    else:
        run_job(max_pages=args.limit)

if __name__ == "__main__":
    main()
