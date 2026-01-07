import schedule
import time
import logging
import argparse
from main_orchestrator import run_orchestration

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("AutonomousRunner")

def job():
    logger.info("Executing scheduled daily orchestration job...")
    try:
        run_orchestration(save_report=True)
        logger.info("Daily job finished successfully.")
    except Exception as e:
        logger.error(f"Daily job failed: {e}")

def main():
    parser = argparse.ArgumentParser(description="Autonomous Agent Runner")
    parser.add_argument("--now", action="store_true", help="Run the job immediately once and exit")
    parser.add_argument("--interval", type=int, default=1, help="Interval in minutes for testing (default 24h normally)")

    args = parser.parse_args()

    if args.now:
        job()
        return

    # Schedule the job
    # For a real "every two weeks" scenario:
    schedule.every(2).weeks.do(job)
    logger.info("Scheduled job for every 2 weeks.")

    # For demonstration, we keep the process alive
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
