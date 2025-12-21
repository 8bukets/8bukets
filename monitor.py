import time
import logging
import subprocess
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("monitor.log"),
        logging.StreamHandler()
    ]
)

def run_scraper(limit=1):
    logging.info("Starting Scraper (Limited to recent pages for daily improvement)...")
    try:
        # Run scraping for just 1 page to simulate a quick daily update check
        subprocess.run([sys.executable, "scrape_informatic.py", "-n", str(limit)], check=True)
        logging.info("Scraper finished successfully.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Scraper failed: {e}")
        return False

def run_analyzer():
    logging.info("Starting Intelligent Analyzer...")
    try:
        subprocess.run([sys.executable, "analyze_content.py"], check=True)
        logging.info("Analysis finished. Report generated.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Analyzer failed: {e}")
        return False

def daily_routine():
    logging.info(">>> BEGINNING DAILY IMPROVEMENT CYCLE <<<")

    if run_scraper(limit=2): # Fetch last 2 pages
        if run_analyzer():
            logging.info("Daily cycle complete. High value report ready.")
        else:
            logging.error("Analysis stage failed.")
    else:
        logging.error("Scraping stage failed.")

    logging.info(">>> CYCLE END <<<")

if __name__ == "__main__":
    # In a real 24/7 scenario, this would be a while True: loop with sleep(86400)
    # For this demonstration/task, we run it once immediately.
    daily_routine()
