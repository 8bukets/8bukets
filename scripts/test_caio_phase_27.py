import asyncio
import pytest
import logging
import os
from agents.chief_ai_officer import ChiefAIOfficerAgent
from agents.base_agent import Blackboard

# Configure logging for the test
logging.basicConfig(level=logging.INFO)

@pytest.mark.asyncio
async def test_caio_agent_phase_27():
    agent = ChiefAIOfficerAgent()
    blackboard = Blackboard()

    # Mock data
    blackboard["system_evolution"] = {"status": "STABLE"}
    blackboard["cloud_workflow_status"] = "OPTIMAL"
    blackboard["market_intelligence"] = {"opportunity_score": 0.8}
    blackboard["resource_allocation"] = {"utilization": 0.9}

    print("Running CAIO Agent with Phase 27 metrics...")

    # Ensure AGENTS.md has Phase 27 Current
    with open('AGENTS.md', 'r') as f:
        agents_docs = f.read()

    assert "Phase 27: Multi-Universal Resonance (Current)" in agents_docs

    result = await agent.run([], blackboard)

    print("Result Strategic Directives:", result["strategic_directives"])

    assert "ACTIVATE_PHASE_27_PROTOCOLS" in result["strategic_directives"]
    assert "INITIALIZE_DNI_HOOKS" in result["strategic_directives"]
    assert "ENFORCE_UNIVERSAL_CONSENSUS" in result["strategic_directives"]
    assert "OPTIMIZE_ROI_TRACKING" in result["strategic_directives"]

    assert "Phase 27 Operational Mode: ACTIVE" in result["executive_summary"]

    print("Phase 27 logic test passed!")

if __name__ == "__main__":
    asyncio.run(test_caio_agent_phase_27())
