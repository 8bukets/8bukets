import time
import subprocess
import sys
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

def run_daily_job():
    logger.info("Scheduler: Starting daily job...")
    try:
        # Run the system
        subprocess.run([sys.executable, "run_system.py", "--limit", "2"], check=True)
        logger.info("Scheduler: Job finished successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Scheduler: Job failed with exit code {e.returncode}")

def main():
    logger.info("Starting Autonomous Agent Scheduler.")
    logger.info("Note: In a production environment, use 'cron' or 'systemd' timers.")
    logger.info("For demonstration, this script runs the job immediately and then waits.")

    # Run immediately once
    run_daily_job()

    # Loop for simulation (e.g., every 24 hours = 86400 seconds)
    # Uncomment the loop below for actual continuous execution
    # while True:
    #     logger.info("Waiting 24 hours for next run...")
    #     time.sleep(86400)
    #     run_daily_job()

if __name__ == "__main__":
    main()
