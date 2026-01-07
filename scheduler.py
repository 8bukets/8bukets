"""
Scheduler script for running the scraper and agent orchestrator periodically.
"""

import logging
import sys
import time

import schedule

from agent_orchestrator import AgentOrchestrator
from scraper import main as run_scraper

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
    """Execute the scheduled tasks: Scraper and Agents."""
    logger.info("Starting scheduled job...")

    # 1. Run Scraper (Data Collection)
    logger.info("Running scraper...")
    try:
        run_scraper()
    except Exception as e:
        logger.error("Scraper failed: %s", e)

    # 2. Run Agents (Analysis, Research, Creation, Reporting)
    logger.info("Running Autonomous Agents...")
    try:
        orchestrator = AgentOrchestrator()
        orchestrator.run_agents()
    except Exception as e:
        logger.error("Agent Orchestrator failed: %s", e)

    logger.info("Job completed.")

def main():
    """Main entry point for the scheduler."""
    logger.info("Scheduler started. Running 24/7.")

    # Schedule the job to run every 2 weeks
    schedule.every(2).weeks.do(job)

    # Also run once immediately on startup for verification
    logger.info("Running initial job on startup...")
    job()

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
