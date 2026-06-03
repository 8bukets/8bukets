import asyncio
import logging
import json
import os
from agents.chief_ai_officer import ChiefAIOfficerAgent
from agents.base_agent import Blackboard

logging.basicConfig(level=logging.INFO)

async def test_caio_roi_target():
    agent = ChiefAIOfficerAgent()
    blackboard = Blackboard()

    # Mock data with ROI below 95%
    blackboard["system_evolution"] = {"status": "STABLE"}
    blackboard["cloud_workflow_status"] = "OPTIMAL"
    blackboard["market_intelligence"] = {"opportunity_score": 0.5}
    blackboard["resource_allocation"] = {"utilization": 0.5, "roi_efficiency": 0.9}

    print("Running CAIO Agent with ROI efficiency 0.9 (below 95%)...")
    result = await agent.run([], blackboard)

    print("Directives:", result["strategic_directives"])

    # We need to make sure OPTIMIZE_ROI_TRACKING is in directives to trigger ROI check
    # It is added if AGENTS.md mentions Phase 12 or 13.
    assert "ENFORCE_AGGRESSIVE_ROI_OPTIMIZATION" in result["strategic_directives"]
    assert "REDUCE_NON_CRITICAL_COMPUTE" in result["strategic_directives"]

    print("Test passed!")

if __name__ == "__main__":
    asyncio.run(test_caio_roi_target())
