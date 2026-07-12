import asyncio
from agents.chief_ai_officer import ChiefAIOfficerAgent
from agents.base_agent import Blackboard
import os

async def test_caio_phase_27_directives():
    print("Testing CAIO Phase 27 Directives...")

    # Setup: Create a mock AGENTS.md with Phase 27
    with open('AGENTS.md', 'w') as f:
        f.write("# Phase 27: Multi-Universal Resonance (MUR)\n")

    agent = ChiefAIOfficerAgent()
    blackboard = Blackboard()

    # Mock blackboard data
    blackboard["system_evolution"] = {"status": "OPTIMAL"}
    blackboard["cloud_workflow_status"] = "OPTIMAL"
    blackboard["market_intelligence"] = {"opportunity_score": 0.5}
    blackboard["resource_allocation"] = {"utilization": 0.5}

    result = await agent.run([], blackboard)

    directives = result.get("strategic_directives", [])

    expected_directives = [
        "ACTIVATE_PHASE_27_PROTOCOLS",
        "INITIALIZE_DNI_HOOKS",
        "ENFORCE_UNIVERSAL_CONSENSUS",
        "OPTIMIZE_ROI_TRACKING",
        "SCOUT_LINKEDIN_FOR_CAIO_OPENINGS",
        "AUDIT_COURSERA_AI_CERTIFICATIONS",
        "EVALUATE_UNIVERSITY_AI_PARTNERSHIPS",
        "MANDATE_DATA_READINESS_AUDIT"
    ]

    for directive in expected_directives:
        if directive not in directives:
             print(f"FAILED: Directive {directive} missing from CAIO output")
             exit(1)

    if result["ai_strategy_status"] != "OPTIMAL":
        print(f"FAILED: Expected strategy status OPTIMAL, got {result['ai_strategy_status']}")
        exit(1)

    print("PASSED: All Phase 27 directives verified.")

if __name__ == "__main__":
    asyncio.run(test_caio_phase_27_directives())
