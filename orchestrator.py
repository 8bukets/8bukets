import asyncio
import logging
import argparse
from agents.research_agent import ResearchAgent
from agents.analyze_agent import AnalyzeAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.monetization_agent import MonetizationAgent
from agents.creativity_agent import CreativityAgent
from agents.content_agent import ContentAgent
from agents.health_agent import HealthCheckAgent
from agents.compliance_agent import ComplianceAgent
from agents.ads_agent import AdsAgent
from agents.learning_agent import LearningAgent
from agents.antigravity_agent import AntigravityAgent
from agents.innovation_agent import InnovationAgent

from utils.log_formatter import setup_logging

# Configure logging
setup_logging()
logger = logging.getLogger("Orchestrator")

class Orchestrator:
    def __init__(self):
        self.agents = [
            ComplianceAgent(), # First check compliance
            ResearchAgent(),
            AnalyzeAgent(),
            IntelligenceAgent(),
            MonetizationAgent(),
            AdsAgent(), # New ads agent
            CreativityAgent(),
            AntigravityAgent(), # Fun/Innovation
            InnovationAgent(), # System evolution
            ContentAgent(),
            HealthCheckAgent(),
            LearningAgent() # Last to learn from the cycle
        ]
        self.context = {}

    async def run_once(self, limit=None):
        logger.info("Starting autonomous cycle...")

        # Load dynamic configuration from LearningAgent
        import json
        import os
        config = {}
        if os.path.exists("system_config.json"):
            try:
                with open("system_config.json", 'r') as f:
                    config = json.load(f)
                logger.info(f"Loaded autonomous config: {config}")
            except Exception as e:
                logger.warning(f"Failed to load system config: {e}")

        # Reset context or carry over state? Reset for now.
        self.context = {}

        # Priority: CLI override > Learned Config > Default
        self.context["limit"] = limit if limit is not None else config.get("limit", 5)
        self.context["concurrency"] = config.get("concurrency", 5)

        for agent in self.agents:
            try:
                await agent.run(self.context)
            except Exception as e:
                logger.error(f"Agent {agent.name} failed: {e}")

        logger.info("Cycle complete.")

    async def run_loop(self, interval, limit):
        while True:
            await self.run_once(limit)
            logger.info(f"Sleeping for {interval} seconds...")
            await asyncio.sleep(interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Autonomous Agent Orchestrator")
    parser.add_argument("--once", action="store_true", help="Run once and exit")
    parser.add_argument("--limit", type=int, default=5, help="Scrape limit")
    parser.add_argument("--interval", type=int, default=3600, help="Loop interval in seconds")

    args = parser.parse_args()

    orchestrator = Orchestrator()

    if args.once:
        asyncio.run(orchestrator.run_once(args.limit))
    else:
        try:
            asyncio.run(orchestrator.run_loop(args.interval, args.limit))
        except KeyboardInterrupt:
            logger.info("Orchestrator stopped by user.")
