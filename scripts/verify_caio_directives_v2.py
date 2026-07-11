import asyncio
import os
import sys
import logging
from agents.chief_ai_officer import ChiefAIOfficerAgent
from agents.base_agent import Blackboard

# Configure logging
logging.basicConfig(level=logging.INFO)

async def verify_v2():
    print("🧪 [Verify] Testing ChiefAIOfficerAgent v2 logic...")

    agent = ChiefAIOfficerAgent()
    blackboard = Blackboard()

    # Mock data
    blackboard["system_evolution"] = {"status": "OPTIMAL", "technical_debt": []}
    blackboard["cloud_workflow_status"] = "OPTIMAL"
    blackboard["market_intelligence"] = {"opportunity_score": 0.5, "trends": ""}
    blackboard["resource_allocation"] = {"utilization": 0.5, "roi_efficiency": 1.0}

    # Run the agent
    result = await agent.run([], blackboard)

    directives = result.get("strategic_directives", [])
    print(f"Issued directives: {directives}")

    success = True

    # Test for MANDATE_DATA_READINESS_AUDIT (should be triggered by 'architecture' in CDO description)
    if "MANDATE_DATA_READINESS_AUDIT" in directives:
        print("✅ [Success] MANDATE_DATA_READINESS_AUDIT directive correctly issued!")
    else:
        print("❌ [Failure] MANDATE_DATA_READINESS_AUDIT directive missing.")
        success = False

    # Test for EVALUATE_UNIVERSITY_AI_PARTNERSHIPS (should be triggered by 'Stanford' in integrated knowledge)
    if "EVALUATE_UNIVERSITY_AI_PARTNERSHIPS" in directives:
        print("✅ [Success] EVALUATE_UNIVERSITY_AI_PARTNERSHIPS directive correctly issued!")
    else:
        print("❌ [Failure] EVALUATE_UNIVERSITY_AI_PARTNERSHIPS directive missing.")
        success = False

    # Test for SCOUT_LINKEDIN_FOR_CAIO_OPENINGS
    if "SCOUT_LINKEDIN_FOR_CAIO_OPENINGS" in directives:
         print("✅ [Success] SCOUT_LINKEDIN_FOR_CAIO_OPENINGS directive correctly issued!")
    else:
        print("❌ [Failure] SCOUT_LINKEDIN_FOR_CAIO_OPENINGS directive missing.")
        success = False

    if not success:
        sys.exit(1)

if __name__ == "__main__":
    os.environ['PYTHONPATH'] = os.getcwd()
    asyncio.run(verify_v2())
