import pytest
import asyncio
from agents.base_agent import Blackboard
from agents.collaboration_agent import CollaborationAgent

@pytest.mark.asyncio
async def test_collaboration_agent():
    bb = Blackboard()

    # Pre-populate blackboard with required data for CollaborationAgent
    await bb.update("SixSigmaChampion", {"sigma_performance_report": {"average_impact_score": 0.85}})
    await bb.update("ArchitectAgent", {"system_evolution": {"parameter_shifts": {"current_version": 1.18}}})

    agent = CollaborationAgent()
    result = await agent.run([], bb)

    context = result.get("antigravity_context", {})
    assert context["platform"] == "Antigravity"
    assert context["system_version"] == 1.18
    assert context["sigma_status"] == 0.85
    assert "keser.filip@gmail.com" in context["stakeholders"]
    assert "8bukets@gmail.com" in context["stakeholders"]
    assert context["status"] == "SYNCED"
    assert "Antigravity Mission" in context["mission_statement"]
    assert "Integration Rules" in context["integration_rules"]
