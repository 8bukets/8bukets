
import asyncio
import logging
from agents.chief_ai_officer import ChiefAIOfficerAgent
from agents.base_agent import Blackboard

# Configure logging for the test
logging.basicConfig(level=logging.INFO)

async def test_caio_agent():
    agent = ChiefAIOfficerAgent()
    blackboard = Blackboard()

    # Mock data
    blackboard["system_evolution"] = {"status": "STABLE"}
    blackboard["cloud_workflow_status"] = "OPTIMAL"
    blackboard["market_intelligence"] = {"opportunity_score": 0.8}
    blackboard["resource_allocation"] = {"utilization": 0.9}

    print("Running CAIO Agent with mock data...")
    result = await agent.run([], blackboard)

    print("Result:", result)

    assert "strategic_directives" in result
    assert "LAUNCH_EXPLORATORY_AGENTS" in result["strategic_directives"]
    assert "INITIATE_CLOUD_BURSTING" in result["strategic_directives"]

    # Check for Phase 12 directives if AGENTS.md is at Phase 12
    with open('AGENTS.md', 'r') as f:
        agents_docs = f.read()
        if "Phase 12: Autonomous Super-Intelligence (Current)" in agents_docs or "Phase 13" in agents_docs:
            assert "ACTIVATE_SENTIENT_ORCHESTRATION" in result["strategic_directives"]
            assert "ESTABLISH_ETHICS_FRAMEWORK" in result["strategic_directives"]
            assert "OPTIMIZE_ROI_TRACKING" in result["strategic_directives"]

    # Check for Phase 13 integrated knowledge directives
    # Based on data/knowledge/system_knowledge.json which was updated during the cycle
    assert "ACTIVATE_PHASE_13_PROTOCOLS" in result["strategic_directives"]
    assert "DEPLOY_APAC_EDGE_NODES" in result["strategic_directives"]
    assert "DECIDE_BUILD_VS_BUY_STRATEGY" in result["strategic_directives"]

    # Verify Market Intelligence and Role Alignment integration in summary
    assert "Executive Role Alignment: Verified." in result["executive_summary"]
    assert "Market Intelligence Q3" in result["executive_summary"] or "demand for sovereign AI clusters" in result["executive_summary"]

    print("Test passed!")

if __name__ == "__main__":
    asyncio.run(test_caio_agent())
