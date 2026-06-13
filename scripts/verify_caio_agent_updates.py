import asyncio
import sys
import os

# Add the project root to sys.path to allow importing agents
sys.path.append(os.getcwd())

from agents.chief_ai_officer import ChiefAIOfficerAgent
from agents.base_agent import Blackboard

async def test_caio_agent():
    print("🧪 [Test] Verifying ChiefAIOfficerAgent with updated knowledge...")

    agent = ChiefAIOfficerAgent()
    blackboard = Blackboard()

    # Initialize blackboard with minimal required data
    # Blackboard is a dict subclass, use dict assignment or update
    blackboard["system_evolution"] = {"status": "OPTIMAL", "technical_debt": []}
    blackboard["cloud_workflow_status"] = "OPTIMAL"
    blackboard["market_intelligence"] = {"opportunity_score": 0.5, "trends": "None"}
    blackboard["resource_allocation"] = {"utilization": 0.5, "roi_efficiency": 1.0}

    # Run the agent
    result = await agent.run([], blackboard)

    directives = result.get("strategic_directives", [])
    summary = result.get("executive_summary", "")

    print(f"Issued Directives: {directives}")
    print(f"Executive Summary: {summary}")

    # Verify specific directives triggered by the updated knowledge
    expected_directives = [
        "SCOUT_LINKEDIN_FOR_CAIO_OPENINGS",
        "AUDIT_COURSERA_AI_CERTIFICATIONS"
    ]

    missing = [d for d in expected_directives if d not in directives]

    if not missing:
        print("✅ [Test] All expected directives issued successfully.")
    else:
        print(f"❌ [Test] Missing expected directives: {missing}")
        sys.exit(1)

if __name__ == "__main__":
    # Configure logging to see agent output
    import logging
    logging.basicConfig(level=logging.INFO)
    asyncio.run(test_caio_agent())
