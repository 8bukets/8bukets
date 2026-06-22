import pytest
import asyncio
import os
import json
from agents.knowledge_agent import KnowledgeAgent
from agents.base_agent import Blackboard, BaseAgent

class MockAgent(BaseAgent):
    async def run(self, data: list, blackboard: Blackboard):
        return {"mock": "data"}

@pytest.mark.asyncio(loop_scope="function")
async def test_knowledge_agent_loading():
    # Setup Blackboard
    blackboard = Blackboard()

    # Test KnowledgeAgent
    k_agent = KnowledgeAgent()

    # The file should already be updated by the script
    json_path = "data/knowledge/ai_agents_knowledge.json"
    assert os.path.exists(json_path)

    with open(json_path, "r", encoding="utf-8") as f:
        knowledge = json.load(f)

    assert "what-is-an-ai-agent" in knowledge
    assert "google-cloud-and-ai-agents" in knowledge

    k_result = await k_agent.run([], blackboard)

    assert "ai_agents_definitions" in k_result
    defs = k_result["ai_agents_definitions"]
    assert "AI agents are software systems" in defs["ai_agent"]
    assert "Reasoning" in defs["features"]
    assert "Cloud Run" in defs["deployment"]

    # Check use cases (they should come from the more detailed entries if available)
    assert "customer" in defs["use_cases"]
    assert "personalized customer experiences" in defs["use_cases"]["customer"]

    # Check tools list
    tools = k_result["google_cloud_tools_list"]
    assert any("Gemini" in t for t in tools)
    assert any("Cloud Run" in t for t in tools)

if __name__ == "__main__":
    pytest.main([__file__])
