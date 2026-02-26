import pytest
import asyncio
from agents.health_check_agent import HealthCheckAgent
from agents.ads_agent import AdsAgent

@pytest.mark.asyncio
async def test_health_check_agent():
    agent = HealthCheckAgent()
    data = [
        {"title": "Test 1", "external_link": "http://a.com", "post_url": "http://a.com/1"},
        {"title": "Test 2", "external_link": "http://b.com", "post_url": "http://b.com/2"}
    ]
    context = {}
    result = await agent.run(data, context)

    assert "health_report" in result
    assert result["health_report"]["status"] == "PASS"
    assert "Data contains 2 records" in result["health_report"]["checks"][0]

@pytest.mark.asyncio
async def test_ads_agent():
    agent = AdsAgent()
    data = []
    context = {
        "targeting_profile": {"primary_persona": "Tester"},
        "creative_angles": ["Angle 1", "Deep Dive: Angle 2"]
    }
    result = await agent.run(data, context)

    assert "generated_ads" in result
    ads = result["generated_ads"]
    assert len(ads) == 2
    assert ads[0]["target_audience"] == "Tester"
    assert ads[0]["cta"] == "Get Started"
    assert ads[1]["cta"] == "Learn More"
