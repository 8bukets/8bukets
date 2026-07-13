import sys
import os
import asyncio
import pytest

# Ensure project root is in the python path
sys.path.append(os.getcwd())

from agents.chief_ai_officer import ChiefAIOfficerAgent
from agents.base_agent import Blackboard

@pytest.mark.asyncio
async def test_caio_phase_27_recognition():
    """
    Verifies that the CAIO agent correctly recognizes Phase 27 status
    from AGENTS.md and issues the appropriate strategic directives.
    """
    agent = ChiefAIOfficerAgent()
    blackboard = Blackboard()

    # Setup blackboard with baseline telemetry
    blackboard["system_evolution"] = {"status": "STABLE", "technical_debt": []}
    blackboard["cloud_workflow_status"] = "OPTIMAL"
    blackboard["market_intelligence"] = {"opportunity_score": 0.9}
    blackboard["resource_allocation"] = {"utilization": 0.6, "roi_efficiency": 0.98}
    blackboard["container_status"] = {"engine": "Docker", "fullyOnline": True}

    # Ensure AGENTS.md has Phase 27
    with open('AGENTS.md', 'r') as f:
        content = f.read()
        assert "Phase 27: Multi-Universal Resonance (Current)" in content

    # Run the agent
    result = await agent.run([], blackboard)

    directives = result.get("strategic_directives", [])
    summary = result.get("executive_summary", "")

    # Verify Phase 27 specific directives
    assert "ACTIVATE_PHASE_27_PROTOCOLS" in directives
    assert "INITIALIZE_DNI_HOOKS" in directives
    assert "ENFORCE_UNIVERSAL_CONSENSUS" in directives

    # Verify summary reflects Phase 27
    assert "Phase 27 Operational Mode: ACTIVE" in summary
    assert "PHASE_27_MUR_DIRECTIVE_GENERATED" in summary

    print("\n✅ CAIO Phase 27 logic verified successfully.")

if __name__ == "__main__":
    asyncio.run(test_caio_phase_27_recognition())
