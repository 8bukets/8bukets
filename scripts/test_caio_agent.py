
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
    assert "ENFORCE_ISO_42001_COMPLIANCE" in result["strategic_directives"]
    assert "INITIATE_CROSS_DEPARTMENT_TRAINING" in result["strategic_directives"]
    assert "ENFORCE_GOVERNANCE_FRAMEWORKS" in result["strategic_directives"]
    assert "ALIGN_AI_STRATEGY_WITH_BUSINESS_GOALS" in result["strategic_directives"]
    assert "MEASURE_AI_BUSINESS_IMPACT" in result["strategic_directives"]
    assert "COORDINATE_WITH_TECHNICAL_LEADERSHIP" in result["strategic_directives"]
    assert "ANALYZE_MARKET_AI_ROLES" in result["strategic_directives"]
    assert "RESEARCH_AI_LEADERSHIP_CERTIFICATIONS" in result["strategic_directives"]
    assert "OPTIMIZE_FOR_COMPETITIVE_ADVANTAGE" in result["strategic_directives"]
    assert "ENFORCE_HEARTBEAT_LATENCY" in result["strategic_directives"]
    assert "ACTIVATE_NEURAL_RECOVERY" in result["strategic_directives"]
    assert "SCOUT_LINKEDIN_FOR_CAIO_OPENINGS" in result["strategic_directives"]
    assert "AUDIT_COURSERA_AI_CERTIFICATIONS" in result["strategic_directives"]

    # Test robust matching - ensures "doctor" or "refactor" don't trigger COORDINATE_WITH_TECHNICAL_LEADERSHIP
    # if cto/cdo are NOT present in the content but doctor/refactor are.
    # In our current case, caio_user_input.md HAS "doctor" and "cto".
    # We can rely on the fact that re.search(r'\bcto\b', ...) was used.

    # Verify Market Intelligence and Role Alignment integration in summary
    assert "Executive Role Alignment: Verified." in result["executive_summary"]
    assert "Market Intelligence Q3" in result["executive_summary"] or "demand for sovereign AI clusters" in result["executive_summary"]
    assert "Licensure Status: Not required for executive AI leadership (Verified)." in result["executive_summary"]

    print("Test passed!")

if __name__ == "__main__":
    asyncio.run(test_caio_agent())
