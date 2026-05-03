import pytest
import asyncio
from agents.google_models_research_agent import GoogleModelsResearchAgent
from agents.base_agent import Blackboard

@pytest.mark.asyncio
async def test_google_models_research_agent_run():
    agent = GoogleModelsResearchAgent()
    blackboard = Blackboard()

    # Run the agent (this will perform a real network request)
    result = await agent.run([], blackboard)

    assert "google_models_research_knowledge" in result
    knowledge = result["google_models_research_knowledge"]
    assert knowledge["source"] == "https://blog.google/innovation-and-ai/models-and-research/"
    assert isinstance(knowledge["articles"], list)

    # Check that we got some articles (assuming the blog is up)
    if knowledge["articles"]:
        article = knowledge["articles"][0]
        assert "title" in article
        assert "url" in article
        assert article["url"].startswith("https://blog.google")
