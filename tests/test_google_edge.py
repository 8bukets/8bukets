import pytest
import asyncio
from unittest.mock import patch, MagicMock
from agents.google_edge_agent import GoogleEdgeAgent
from agents.base_agent import Blackboard

class MockResponse:
    def __init__(self, text_data, status=200):
        self._text = text_data
        self.status = status

    async def text(self):
        return self._text

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        pass

class MockSession:
    def __init__(self, mock_response):
        self.mock_response = mock_response

    def get(self, url):
        return self.mock_response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        pass

@pytest.mark.asyncio
async def test_google_edge_agent_success():
    """Verify that the GoogleEdgeAgent successfully parses valid HTML."""
    html_content = """
    <html>
        <head><title>AI Edge - Google</title></head>
        <body>
            <h1>Deploying AI Models on Edge</h1>
            <p>This is a long enough paragraph about deploying models on edge devices. It needs to be over 20 characters.</p>
            <h2>Optimization Techniques</h2>
            <p>Another sufficiently long paragraph that describes quantization and pruning for edge deployments.</p>
            <p>Short</p> <!-- Should be ignored -->
        </body>
    </html>
    """

    mock_resp = MockResponse(html_content, 200)
    mock_session = MockSession(mock_resp)

    agent = GoogleEdgeAgent()
    bb = Blackboard()

    with patch('aiohttp.ClientSession', return_value=mock_session):
        result = await agent.run([], bb)

    assert "google_edge_knowledge" in result
    knowledge = result["google_edge_knowledge"]
    assert knowledge["title"] == "AI Edge - Google"
    assert len(knowledge["sections"]) == 2

    # Check first section
    assert knowledge["sections"][0]["heading"] == "Deploying AI Models on Edge"
    assert "This is a long enough paragraph" in knowledge["sections"][0]["content"]

    # Check second section
    assert knowledge["sections"][1]["heading"] == "Optimization Techniques"
    assert "Another sufficiently long paragraph" in knowledge["sections"][1]["content"]

@pytest.mark.asyncio
async def test_google_edge_agent_failure():
    """Verify that the GoogleEdgeAgent handles HTTP failures gracefully."""
    mock_resp = MockResponse("", 404)
    mock_session = MockSession(mock_resp)

    agent = GoogleEdgeAgent()
    bb = Blackboard()

    with patch('aiohttp.ClientSession', return_value=mock_session):
        result = await agent.run([], bb)

    # Even on failure, it returns the empty structure instead of crashing
    assert "google_edge_knowledge" in result
    knowledge = result["google_edge_knowledge"]
    assert knowledge["title"] == ""
    assert len(knowledge["sections"]) == 0
