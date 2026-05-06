import pytest
import asyncio
import os
import json
from agents.knowledge_agent import KnowledgeAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.base_agent import Blackboard

@pytest.mark.asyncio
async def test_ai_agents_knowledge_flow():
    # 1. Setup Blackboard and Agents
    blackboard = Blackboard()
    k_agent = KnowledgeAgent()
    i_agent = IntelligenceAgent()

    # 2. Mock external knowledge
    await blackboard.update("MockInnovation", {
        "google_innovation_ai_knowledge": {
            "articles": [{"title": "Autonomous Agents in 2026", "url": "https://blog.google/agent-1"}]
        }
    })

    # 3. Run KnowledgeAgent (it reads from data/ai_agents_knowledge.json)
    # We ensure the file exists from our earlier scraper run
    assert os.path.exists("data/ai_agents_knowledge.json")

    k_result = await k_agent.run([], blackboard)
    await blackboard.update(k_agent.name, k_result)

    assert "ai_agent_knowledge" in k_result
    assert "all_definitions" in k_result["ai_agent_knowledge"]

    # 4. Run IntelligenceAgent
    # Mock other dependencies
    await blackboard.update("MockAnalysis", {"analysis_stats": {"top_categories": {}}})
    await blackboard.update("MockResearch", {"research_data": {"market_trends": [], "external_investigations": []}})
    await blackboard.update("MockEdge", {"google_edge_knowledge": {"sections": []}})
    await blackboard.update("MockResearchBlog", {"google_models_research_knowledge": {"articles": []}})

    i_result = await i_agent.run([], blackboard)

    assert "intelligence_insights" in i_result
    assert "strategic_risk_assessment" in i_result
    assert i_result["synchronization_level"] == "KNOWLEDGE_ALIGNED"

    insights = i_result["intelligence_insights"]
    assert any("AI Agent Knowledge Base Integrated" in insight for insight in insights)

if __name__ == "__main__":
    pytest.main([__file__])
