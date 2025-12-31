import schedule
import time
import logging
import sys
from scraper import main as run_scraper
from agent_orchestrator import AgentOrchestrator

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

    # 1. Run Scraper (Data Collection)
    logger.info("Running scraper...")
    try:
        run_scraper()
    except Exception as e:
        logger.error(f"Scraper failed: {e}")

    # 2. Run Agents (Analysis, Research, Creation, Reporting)
    logger.info("Running Autonomous Agents...")
    try:
        orchestrator = AgentOrchestrator()
        orchestrator.run_agents()
    except Exception as e:
        logger.error(f"Agent Orchestrator failed: {e}")

    logger.info("Job completed.")

def main():
    logger.info("Scheduler started. Running 24/7.")

    # Schedule the job to run every 2 weeks (14 days) at a specific time
    schedule.every(14).days.at("00:00").do(job)

    # Also run once immediately on startup for verification
    logger.info("Running initial job on startup...")
    job()

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
