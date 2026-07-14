import sys
import os
import asyncio
import logging

# Ensure root is in path for imports
sys.path.append(os.getcwd())

from agents.chief_ai_officer import ChiefAIOfficerAgent
from agents.base_agent import Blackboard

async def test_caio_phase_27():
    print("🧪 Testing CAIO Agent Phase 27 Compliance...")

    agent = ChiefAIOfficerAgent()
    blackboard = Blackboard()

    # Mock some data
    blackboard["system_evolution"] = {"status": "STABLE", "technical_debt": []}
    blackboard["cloud_workflow_status"] = "OPTIMAL"
    blackboard["market_intelligence"] = {"opportunity_score": 0.5}
    blackboard["resource_allocation"] = {"utilization": 0.4}

    # Run the agent
    result = await agent.run([], blackboard)

    directives = result.get("strategic_directives", [])
    print(f"📋 Issued Directives: {directives}")

    expected = [
        "ACTIVATE_PHASE_27_PROTOCOLS",
        "INITIALIZE_DNI_HOOKS",
        "ENFORCE_UNIVERSAL_CONSENSUS",
        "OPTIMIZE_FOR_SINGULARITY_READINESS_PHASE_27"
    ]

    for e in expected:
        if e in directives:
            print(f"✅ Directive '{e}' found.")
        else:
            print(f"❌ Directive '{e}' MISSING.")
            sys.exit(1)

    print("✨ CAIO Phase 27 Compliance Verified.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(test_caio_phase_27())
