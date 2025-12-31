import schedule
import time
import subprocess
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

def run_system_report():
    logger.info("Starting Bi-Weekly System Report Job...")
    try:
        # We run the run_system.py script as a subprocess to ensure clean state
        subprocess.run([sys.executable, "run_system.py"], check=True)
        logger.info("System Report Job Completed Successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"System Report Job Failed: {e}")

def main():
    logger.info("Scheduler started. Job scheduled every 2 weeks.")

    # Schedule the job to run every 2 weeks (14 days)
    # We can also start it immediately if desired, but typical scheduler behavior waits.
    # To run immediately on start:
    run_system_report()

    schedule.every(2).weeks.do(run_system_report)

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
