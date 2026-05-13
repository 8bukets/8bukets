import schedule
import time
import subprocess
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

def job():
    logger.info("Starting bi-weekly system run...")
    try:
        # Run run_system.py using subprocess to ensure a clean environment for each run
        result = subprocess.run([sys.executable, "run_system.py"], capture_output=True, text=True)
        if result.returncode == 0:
            logger.info("System run completed successfully.")
            logger.info(result.stdout)
        else:
            logger.error("System run failed.")
            logger.error(result.stderr)
    except Exception as e:
        logger.error(f"An error occurred while running the job: {e}")

def main():
    logger.info("Scheduler started. Task scheduled for every 2 weeks.")

    # Schedule the job every 2 weeks
    schedule.every(2).weeks.do(job)

    while True:
        schedule.run_pending()
        time.sleep(60) # Check every minute

if __name__ == "__main__":
    main()
