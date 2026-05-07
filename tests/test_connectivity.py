import pytest
import aiohttp
from agents.research_agent import ResearchAgent
from agents.base_agent import Blackboard

@pytest.mark.asyncio
async def test_domain_connectivity():
    """Verify that the system can reach critical external domains."""
    domains = ["google.com", "markposition.wordpress.com"]
    async with aiohttp.ClientSession() as session:
        for domain in domains:
            url = f"https://{domain}"
            async with session.head(url, allow_redirects=True) as response:
                # Treat 429 as a success indicator for reachability (rate limiting)
                assert response.status < 400 or response.status == 429, f"Failed to reach {domain}, status: {response.status}"

@pytest.mark.asyncio
async def test_research_agent_real_connectivity():
    """Verify ResearchAgent performs real connectivity checks."""
    bb = Blackboard()
    await bb.update("AnalysisAgent", {
        "analysis_stats": {
            "top_domains": {"google.com": 1, "example.com": 1}
        }
    })

    agent = ResearchAgent()
    result = await agent.run([], bb)

    research_data = result.get("research_data", {})
    assert research_data["synchronization_status"] == "REAL_TIME_SYNC"

    investigations = research_data["external_investigations"]
    assert len(investigations) >= 2

    # Check for google.com result
    google_res = next((i for i in investigations if i["domain"] == "google.com"), None)
    assert google_res is not None
    assert google_res["status"] == "ACCESSIBLE"
    assert "http_code" in google_res
