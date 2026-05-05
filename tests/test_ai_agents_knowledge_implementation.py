import pytest
from agents.knowledge_agent import KnowledgeAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.creativity_agent import CreativityAgent
from agents.base_agent import Blackboard
import os
import json

@pytest.mark.asyncio(loop_scope="function")
async def test_knowledge_integration_flow():
    # Setup Blackboard
    blackboard = Blackboard()

    # 1. Test KnowledgeAgent
    k_agent = KnowledgeAgent()
    # Mock knowledge file if not exists or use the existing one
    if not os.path.exists("ai_agents_knowledge.json"):
        mock_data = {
            "key-features-of-an-ai-agent": {"content": "Reasoning Acting Collaborating Self-refining Observing"},
            "challenges-with-using-ai-agents": {"content": "Empathy Ethical stakes Unpredictable"},
            "what-are-the-types-of-agents-in-ai": {"content": "Background Agents Interactive Partners"}
        }
        with open("ai_agents_knowledge.json", "w") as f:
            json.dump(mock_data, f)

    k_result = await k_agent.run([], blackboard)
    await blackboard.update(k_agent.name, k_result)

    assert "challenges" in k_result["ai_agents_definitions"]
    assert "deployment" in k_result["ai_agents_definitions"]
    assert any("Cloud Run" in bp for bp in k_result["agent_best_practices"])

    # 2. Test IntelligenceAgent
    # Needs analysis_stats and research_data
    await blackboard.update("MockAnalysis", {"analysis_stats": {"top_categories": {}}})
    await blackboard.update("MockResearch", {"research_data": {}})

    i_agent = IntelligenceAgent()
    i_result = await i_agent.run([], blackboard)
    await blackboard.update(i_agent.name, i_result)

    assert any("multi-agent collaboration" in insight for insight in i_result["intelligence_insights"])
    assert any("self-improvement" in insight for insight in i_result["intelligence_insights"])
    assert len(i_result["strategic_risk_assessment"]) > 0
    assert any("emotional intelligence" in risk for risk in i_result["strategic_risk_assessment"])

    # 3. Test CreativityAgent
    c_agent = CreativityAgent()
    c_result = await c_agent.run([], blackboard)

    assert any("Background Agents" in concept for concept in c_result["creative_concepts"])
    assert any("Interactive Partner" in concept for concept in c_result["creative_concepts"])
