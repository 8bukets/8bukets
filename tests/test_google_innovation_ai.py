import pytest
import asyncio
from aioresponses import aioresponses
from agents.google_innovation_ai_agent import GoogleInnovationAIAgent
from agents.base_agent import Blackboard

@pytest.mark.asyncio
async def test_google_innovation_ai_agent_run():
    agent = GoogleInnovationAIAgent()
    blackboard = Blackboard()

    url = "https://blog.google/innovation-and-ai/"
    mock_html = """
    <html>
        <body>
            <a href="/innovation-and-ai/test-article-1/">Test Article 1 Extra Long Title for Heuristic</a>
            <a href="https://blog.google/innovation-and-ai/test-article-2/">Test Article 2 Extra Long Title for Heuristic</a>
            <a href="/other-category/">Other Category</a>
            <a href="/innovation-and-ai/">Self Link</a>
        </body>
    </html>
    """

    with aioresponses() as m:
        m.get(url, body=mock_html, status=200)

        # Run the agent
        result = await agent.run([], blackboard)

    assert "google_innovation_ai_knowledge" in result
    knowledge = result["google_innovation_ai_knowledge"]
    assert knowledge["source"] == url
    assert isinstance(knowledge["articles"], list)
    assert len(knowledge["articles"]) == 2

    titles = [a["title"] for a in knowledge["articles"]]
    assert "Test Article 1 Extra Long Title for Heuristic" in titles
    assert "Test Article 2 Extra Long Title for Heuristic" in titles

    urls = [a["url"] for a in knowledge["articles"]]
    assert "https://blog.google/innovation-and-ai/test-article-1/" in urls
    assert "https://blog.google/innovation-and-ai/test-article-2/" in urls
