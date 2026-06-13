import asyncio
import json
import sys
import os

# Ensure the project root is in the python path
sys.path.append(os.getcwd())

from agents.chief_ai_officer import ChiefAIOfficerAgent
from agents.base_agent import Blackboard

async def main():
    agent = ChiefAIOfficerAgent()
    blackboard = Blackboard()

    # In a real scenario, we would pull these from a database or telemetry service
    # For now, we use sensible defaults or env vars
    blackboard["system_evolution"] = {"status": "STABLE", "technical_debt": []}
    blackboard["cloud_workflow_status"] = os.getenv("CLOUD_STATUS", "OPTIMAL")
    blackboard["market_intelligence"] = {"opportunity_score": 0.85}
    blackboard["resource_allocation"] = {"utilization": 0.75}

    try:
        result = await agent.run([], blackboard)
        print(json.dumps(result))
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
