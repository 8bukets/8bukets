import asyncio
from agents.orchestrator import AutonomousOrchestrator

if __name__ == "__main__":
    orchestrator = AutonomousOrchestrator()
    asyncio.run(orchestrator.run_pipeline())
