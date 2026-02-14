import asyncio
import time
import schedule
import logging
from agents.autonomous_intelligence_agent import AutonomousIntelligenceAgent

# Configure Scheduler Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("SystemScheduler")

def job():
    logger.info("⏰ Starting Daily Autonomous Pipeline Job...")
    agent = AutonomousIntelligenceAgent()
    try:
        asyncio.run(agent.run_pipeline())
        logger.info("✅ Daily Job Completed Successfully.")
    except Exception as e:
        logger.error(f"❌ Job Failed: {e}")

if __name__ == "__main__":
    logger.info("🚀 System initialized. Scheduling daily report at 09:00 AM...")

    # Schedule the job every day at 09:00
    schedule.every().day.at("09:00").do(job)

    # Also run once immediately on startup to ensure coverage
    logger.info("⚡ Running immediate startup job...")
    job()

    while True:
        schedule.run_pending()
        time.sleep(60)
