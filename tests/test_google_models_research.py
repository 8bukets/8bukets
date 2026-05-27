import pytest
import asyncio
from aioresponses import aioresponses
from agents.google_models_research_agent import GoogleModelsResearchAgent
from agents.base_agent import Blackboard

@pytest.mark.asyncio
async def test_google_models_research_agent_run():
    agent = GoogleModelsResearchAgent()
    blackboard = Blackboard()

    url = "https://blog.google/innovation-and-ai/models-and-research/"
    mock_html = """
    <html>
        <body>
            <a href="/innovation-and-ai/models-and-research/test-article-1/">Test Article 1 Extra Long Title</a>
            <a href="https://blog.google/innovation-and-ai/models-and-research/test-article-2/">Test Article 2 Extra Long Title</a>
        </body>
    </html>
    """

    with aioresponses() as m:
        m.get(url, body=mock_html, status=200)

        # Run the agent
        result = await agent.run([], blackboard)

    assert "google_models_research_knowledge" in result
    knowledge = result["google_models_research_knowledge"]
    assert knowledge["source"] == url
    assert isinstance(knowledge["articles"], list)
    assert len(knowledge["articles"]) == 2

    urls = [a["url"] for a in knowledge["articles"]]
    assert "https://blog.google/innovation-and-ai/models-and-research/test-article-1/" in urls
    assert "https://blog.google/innovation-and-ai/models-and-research/test-article-2/" in urls
