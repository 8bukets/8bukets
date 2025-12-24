import asyncio
import logging
import time
from datetime import datetime
from agents.health import HealthCheckAgent
from agents.research import ResearchAgent
from agents.analyze import AnalyzeAgent
from agents.intelligence import IntelligenceAgent
from agents.monetization import MonetizationAgent
from agents.creativity import CreativityAgent
from agents.content import ContentAgent

# Configure main logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("DailyTask")

async def run_daily_cycle():
    logger.info("Starting Daily Agent Cycle...")
    context = {}

    # 1. Health Check
    health_agent = HealthCheckAgent("https://markposition.wordpress.com/")
    context.update(await health_agent.run(context))

    # Stop if site is down? No, we might have old data or just want to report the failure.

    # 2. Research (Scraping)
    research_agent = ResearchAgent(limit=5) # Limit to 5 pages for demo/daily run
    context.update(await research_agent.run(context))

    # 3. Analyze
    analyze_agent = AnalyzeAgent()
    context.update(await analyze_agent.run(context))

    # 4. Intelligence
    intelligence_agent = IntelligenceAgent()
    context.update(await intelligence_agent.run(context))

    # 5. Monetization
    monetization_agent = MonetizationAgent()
    context.update(await monetization_agent.run(context))

    # 6. Creativity
    creativity_agent = CreativityAgent()
    context.update(await creativity_agent.run(context))

    # 7. Content (Reporting)
    content_agent = ContentAgent()
    context.update(await content_agent.run(context))

    logger.info("Daily Cycle Complete.")

async def main():
    while True:
        try:
            await run_daily_cycle()
        except Exception as e:
            logger.error(f"Error in daily cycle: {e}")

        # Calculate time until next run (e.g., 24 hours)
        # For demonstration, we just wait 24h
        logger.info("Sleeping for 24 hours...")
        await asyncio.sleep(24 * 3600)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Stopped by user.")
