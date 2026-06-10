import asyncio
import os
import json
import logging
from agents.chief_ai_officer import ChiefAIOfficerAgent
from agents.base_agent import Blackboard

# Configure logging to see CAIO output
logging.basicConfig(level=logging.INFO)

async def verify():
    print("🧪 [Verify] Testing ChiefAIOfficerAgent with Quantum Synergy knowledge...")

    agent = ChiefAIOfficerAgent()
    blackboard = Blackboard()

    # Mock data that would normally come from other agents
    blackboard["system_evolution"] = {"status": "OPTIMAL", "technical_debt": []}
    blackboard["cloud_workflow_status"] = "OPTIMAL"
    blackboard["market_intelligence"] = {"opportunity_score": 0.5, "trends": ""}
    blackboard["resource_allocation"] = {"utilization": 0.5, "roi_efficiency": 1.0}

    # Run the agent
    result = await agent.run([], blackboard)

    directives = result.get("strategic_directives", [])
    print(f"Issued directives: {directives}")

    if "ACTIVATE_QUANTUM_SYNERGY" in directives:
        print("✅ [Success] ACTIVATE_QUANTUM_SYNERGY directive correctly issued!")
    else:
        print("❌ [Failure] ACTIVATE_QUANTUM_SYNERGY directive missing.")
        # Print integrated knowledge for debugging
        knowledge = agent._get_integrated_knowledge()
        print(f"Debug Knowledge Sections count: {len(knowledge.get('typescript_sections', []))}")
        for k in knowledge.get('typescript_sections', []):
            content_match = any("quantum synergy" in str(s).lower() for s in k.get('sections', []))
            if "Quantum Synergy" in k.get('title', '') or content_match:
                print(f"Found match in: {k.get('title')}")
                print(f"Sections: {k.get('sections')}")

if __name__ == "__main__":
    os.environ['PYTHONPATH'] = os.getcwd()
    asyncio.run(verify())
