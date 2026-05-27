import pytest
from agents.knowledge_agent import KnowledgeAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.creativity_agent import CreativityAgent
from agents.base_agent import Blackboard, BaseAgent
import os
import json

class MockAgent(BaseAgent):
    async def run(self, data, blackboard):
        return {"mock": "data"}

@pytest.mark.asyncio(loop_scope="function")
async def test_persona_and_memory_implementation():
    # Setup agent
    agent = MockAgent("TestAgent")

    # Verify Persona
    assert agent.persona["role"] == "TestAgent"
    assert "Professional" in agent.persona["personality"]

    # Verify Short-term Memory
    agent.update_agent_memory("context_key", "context_value", memory_type="short_term")
    assert agent.get_agent_memory("context_key", memory_type="short_term") == "context_value"

    # Verify Long-term Memory
    agent.update_agent_memory("long_key", "long_value", memory_type="long_term")
    assert agent.get_agent_memory("long_key", memory_type="long_term") == "long_value"

    # Verify Episodic Memory
    agent.update_agent_memory("episodic_event", "episodic_data", memory_type="episodic")
    episodes = agent.get_agent_memory(None, memory_type="episodic")
    assert len(episodes) > 0
    assert episodes[-1]["event"] == "episodic_event"

    # Verify Consensus Memory (via Blackboard)
    blackboard = Blackboard()
    await blackboard.update_consensus("shared_info", "shared_value")
    assert blackboard.get_consensus("shared_info") == "shared_value"

@pytest.mark.asyncio(loop_scope="function")
async def test_backward_compatibility():
    agent = MockAgent("TargetingAgent")
    # Existing data in data/memory.json: "TargetingAgent": {"last_primary_persona": "AdTech Professional"}
    val = agent.get_agent_memory("last_primary_persona")
    assert val == "AdTech Professional"

    # Update and check nested
    agent.update_agent_memory("new_key", "new_val")
    assert agent.get_agent_memory("new_key") == "new_val"
    assert agent.get_agent_memory("last_primary_persona") == "AdTech Professional"

@pytest.mark.asyncio(loop_scope="function")
async def test_knowledge_integration_flow():
    # Setup Blackboard
    blackboard = Blackboard()

    # 1. Test KnowledgeAgent
    k_agent = KnowledgeAgent()
    # Mock knowledge file if not exists or use the existing one
    if not os.path.exists("ai_agents_knowledge.json"):
        mock_data = {
            "what-is-an-ai-agent": {"content": "AI agents are software systems..."},
            "key-features-of-an-ai-agent": {"content": "Reasoning Acting Collaborating Self-refining Observing"},
            "challenges-with-using-ai-agents": {"content": "Empathy Ethical stakes Unpredictable"},
            "what-are-the-types-of-agents-in-ai": {"content": "Background Agents Interactive Partners"},
            "based-on-interaction": {"content": "Background Agents Interactive Partners"},
            "what-is-the-difference-between-ai-agents,-ai-assistants,-and-bots": {"content": "AI agents autonomously and proactively perform tasks..."},
            "benefits-of-using-ai-agents": {"content": "Simultaneous execution Realistic simulations Collaboration"},
            "google-cloud-and-ai-agents": {"content": "- ToolA Description\n- ToolB Description"},
            "customer-agents": {"content": "Customer context"},
            "employee-agents": {"content": "Employee context"},
            "creative-agents": {"content": "Creative context"},
            "data-agents": {"content": "Data context"},
            "code-agents": {"content": "Code context"},
            "security-agents": {"content": "Security context"},
            "deploy-ai-agents-for-scale-and-efficiency-with-cloud-run": {"content": "Cloud Run deployment"}
        }
        with open("ai_agents_knowledge.json", "w") as f:
            json.dump(mock_data, f)

    k_result = await k_agent.run([], blackboard)
    await blackboard.update(k_agent.name, k_result)

    # Update blackboard with taxonomy for IntelligenceAgent
    if "agent_taxonomy" in k_result:
        await blackboard.update(k_agent.name, {"agent_taxonomy": k_result["agent_taxonomy"]})

    assert "challenges" in k_result["ai_agents_definitions"]
    assert "deployment" in k_result["ai_agents_definitions"]
    assert any("Cloud Run" in bp for bp in k_result["agent_best_practices"])
    assert "customer" in k_result["agent_use_cases"]
    assert len(k_result["google_cloud_tools_list"]) > 0
    assert "agent_taxonomy" in k_result

    # 2. Test IntelligenceAgent
    # Needs analysis_stats and research_data
    await blackboard.update("MockAnalysis", {"analysis_stats": {"top_categories": {}}})
    await blackboard.update("MockResearch", {"research_data": {}})

    i_agent = IntelligenceAgent()
    i_result = await i_agent.run([], blackboard)
    await blackboard.update(i_agent.name, i_result)

    assert any("multi-agent collaboration" in insight for insight in i_result["intelligence_insights"])
    assert any("self-improvement" in insight for insight in i_result["intelligence_insights"])
    assert any("Taxonomy Alignment" in insight for insight in i_result["intelligence_insights"])
    assert any("Strategic Distinction" in insight for insight in i_result["intelligence_insights"])
    assert len(i_result["strategic_risk_assessment"]) > 0
    assert any("emotional intelligence" in risk for risk in i_result["strategic_risk_assessment"])
    assert len(i_result["strategic_outlook"]) > 0
    assert "Models" in i_result["categorized_knowledge"]

    # 3. Test CreativityAgent
    c_agent = CreativityAgent()
    c_result = await c_agent.run([], blackboard)

    assert any("Background Agents" in concept for concept in c_result["creative_concepts"])
    assert any("Interactive Partner" in concept for concept in c_result["creative_concepts"])
