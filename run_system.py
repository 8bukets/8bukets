import asyncio
from agents.autonomous_intelligence_agent import AutonomousIntelligenceAgent

if __name__ == "__main__":
    agent = AutonomousIntelligenceAgent()
    asyncio.run(agent.run_pipeline())
