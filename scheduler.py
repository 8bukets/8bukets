import schedule
import time
import logging
import sys
from scraper import main as run_scraper
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

    # 2. Generate Report
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
    # For demonstration/testing, we can also run it every X minutes if needed.
    # Here we set it to run daily at midnight.
    schedule.every().day.at("00:00").do(job)

    # Also run once immediately on startup for verification
    logger.info("Running initial job on startup...")
    job()

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
