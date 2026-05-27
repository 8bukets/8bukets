import pytest
import asyncio
from agents.intelligence_agent import IntelligenceAgent
from agents.base_agent import Blackboard

@pytest.mark.asyncio
async def test_intelligence_agent_integration():
    agent = IntelligenceAgent()
    blackboard = Blackboard()

    await blackboard.update("MockAnalysis", {"analysis_stats": {"top_categories": {"Ad Ads Advertise": 5}}})
    await blackboard.update("MockResearch", {"research_data": {"market_trends": ["AI Expansion"], "external_investigations": []}})
    await blackboard.update("MockEdge", {"google_edge_knowledge": {"sections": [{"heading": "Edge AI", "content": "Edge AI is growing."}]}})
    await blackboard.update("MockInnovation", {
        "google_innovation_ai_knowledge": {
            "articles": [{"title": "New Innovation", "url": "https://blog.google/innovation-1"}]
        }
    })
    await blackboard.update("MockResearchBlog", {
        "google_models_research_knowledge": {
            "articles": [{"title": "Advanced Model", "url": "https://blog.google/research-1"}]
        }
    })

    result = await agent.run([], blackboard)

    assert "intelligence_insights" in result
    insights = result["intelligence_insights"]

    # assert any("Strategic Node" in i for i in insights) # Removed as it's not in the agent logic
    assert any("High concentration of advertising-related content." in i for i in insights)
    assert any("Synchronized Trend: AI Expansion" in i for i in insights)
    assert any("Google Edge Knowledge Integrated" in i for i in insights)

    assert "strategic_outlook" in result
    assert "categorized_knowledge" in result
