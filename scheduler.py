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

def run_biweekly_job():
    logger.info("Scheduler: Starting bi-weekly job...")
    try:
        # Run the system
        subprocess.run([sys.executable, "run_system.py", "--limit", "2"], check=True)
        logger.info("Scheduler: Job finished successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Scheduler: Job failed with exit code {e.returncode}")

def main():
    logger.info("Starting Autonomous Agent Scheduler.")
    logger.info("Note: In a production environment, use 'cron' or 'systemd' timers.")
    logger.info("This script runs the job immediately and then waits 14 days.")

    # Run immediately once
    run_biweekly_job()

    # Loop for simulation (every 14 days = 1,209,600 seconds)
    while True:
        logger.info("Waiting 14 days for next run...")
        time.sleep(1209600)
        run_biweekly_job()

if __name__ == "__main__":
    main()
