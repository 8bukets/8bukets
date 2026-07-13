import asyncio
import os
import logging
import pytest
from agents.chief_ai_officer import ChiefAIOfficerAgent
from agents.base_agent import Blackboard

# Configure logging
logging.basicConfig(level=logging.INFO)

@pytest.mark.asyncio
async def test_caio_phase_27_directives():
    print("🧪 [Test] Verifying Phase 27 directives issuance...")

    agent = ChiefAIOfficerAgent()
    blackboard = Blackboard()

    # Standard optimal state
    blackboard["system_evolution"] = {"status": "OPTIMAL", "technical_debt": []}
    blackboard["cloud_workflow_status"] = "OPTIMAL"
    blackboard["market_intelligence"] = {"opportunity_score": 0.5, "trends": ""}
    blackboard["resource_allocation"] = {"utilization": 0.5, "roi_efficiency": 1.0}

    # Run the agent
    result = await agent.run([], blackboard)
    directives = result.get("strategic_directives", [])

    print(f"Directives found: {directives}")

    # Phase 27 specific directives based on AGENTS.md and knowledge base
    expected_p27_directives = [
        "ACTIVATE_PHASE_27_PROTOCOLS",
        "INITIALIZE_DNI_HOOKS",
        "ENFORCE_UNIVERSAL_CONSENSUS",
        "OPTIMIZE_FOR_SINGULARITY_READINESS_PHASE_27",
        "ENFORCE_PHASE_27_RESONANCE_LATENCY",
        "MANDATE_SINGULARITY_AUDIT_4H"
    ]

    for directive in expected_p27_directives:
        assert directive in directives, f"Missing Phase 27 directive: {directive}"

    print("✅ [Test] All expected Phase 27 directives are present.")

if __name__ == "__main__":
    # If run directly, just execute the async function
    os.environ['PYTHONPATH'] = os.getcwd()
    asyncio.run(test_caio_phase_27_directives())
