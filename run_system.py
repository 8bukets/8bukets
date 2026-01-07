import asyncio
import logging
from agents.analyze_agent import AnalyzeAgent
from agents.research_agent import ResearchAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.content_agent import ContentAgent
from agents.health_agent import HealthAgent
from agents.monetization_agent import MonetizationAgent
from agents.creativity_agent import CreativityAgent
from agents.ad_agent import AdAgent

# Configure main logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SystemOrchestrator")

async def main():
    logger.info("🚀 Starting Autonomous Agent System...")

    # Shared State
    shared_state = {
        'new_data_available': False,
        'agents': {}
    }

    # Initialize Agents
    agents = [
        ResearchAgent(shared_state),
        AnalyzeAgent(shared_state),
        IntelligenceAgent(shared_state),
        ContentAgent(shared_state),
        HealthAgent(shared_state),
        MonetizationAgent(shared_state),
        CreativityAgent(shared_state),
        AdAgent(shared_state)
    ]

    # Register agents in shared state for direct messaging
    for agent in agents:
        shared_state['agents'][agent.name] = agent

    # Run agents
    tasks = [agent.run() for agent in agents]

    try:
        await asyncio.gather(*tasks)
    except KeyboardInterrupt:
        logger.info("🛑 System stopping...")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
