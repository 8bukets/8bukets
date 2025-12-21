import schedule
import time
import logging
import sys
from scraper import main as run_scraper
from google_checker import main as run_checker
from report_generator import ReportGenerator

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def job():
    logger.info("Starting scheduled job...")

    # 1. Run Scraper
    logger.info("Running scraper...")
    try:
        run_scraper()
    except Exception as e:
        logger.error(f"Scraper failed: {e}")

    # 2. Run Google Checker
    logger.info("Running Google SEO Checker...")
    try:
        # We call main, which relies on argparse defaults.
        # Ideally we'd refactor google_checker to have a run() method taking args,
        # but main() works if we don't need to change defaults dynamically.
        # It defaults to site:wishlist.design.blog and 10 results.
        run_checker()
    except Exception as e:
        # Google scraping often fails due to blocking, so log as warning mostly
        logger.warning(f"Google Checker failed (likely blocking): {e}")

    # 3. Generate Report
    logger.info("Generating report...")
    try:
        reporter = ReportGenerator()
        reporter.generate_daily_report()
    except Exception as e:
        logger.error(f"Report generation failed: {e}")

    logger.info("Job completed.")

def main():
    logger.info("Scheduler started. Running 24/7.")

    # Schedule the job to run every day at a specific time (e.g., 00:00)
    schedule.every().day.at("00:00").do(job)

    # Also run once immediately on startup for verification
    logger.info("Running initial job on startup...")
    job()

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
