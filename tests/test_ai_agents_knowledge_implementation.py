import pytest
import asyncio
import os
import json
from agents.knowledge_agent import KnowledgeAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.creativity_agent import CreativityAgent
from agents.base_agent import Blackboard, BaseAgent

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
    # Set a specific value for the test to be independent of external state
    agent.update_agent_memory("test_compatibility_persona", "Compatibility Enthusiast")
    val = agent.get_agent_memory("test_compatibility_persona")
    assert val == "Compatibility Enthusiast"
    # Existing data in data/memory.json: "TargetingAgent": {"last_primary_persona": "General Tech Enthusiast"}
    agent.update_agent_memory("last_primary_persona", "General Tech Enthusiast")

    val = agent.get_agent_memory("last_primary_persona")
    assert val == "General Tech Enthusiast"

    # Update and check nested
    agent.update_agent_memory("new_key", "new_val")
    assert agent.get_agent_memory("new_key") == "new_val"
    assert agent.get_agent_memory("test_compatibility_persona") == "Compatibility Enthusiast"

@pytest.mark.asyncio(loop_scope="function")
async def test_ai_agents_knowledge_flow():
    # Setup Blackboard
    blackboard = Blackboard()

    # 1. Mock external knowledge
    await blackboard.update("MockInnovation", {
        "google_innovation_ai_knowledge": {
            "articles": [{"title": "Autonomous Agents in 2026", "url": "https://blog.google/agent-1"}]
        }
    })
    await blackboard.update("MockAnalysis", {"analysis_stats": {"top_categories": {}}})
    await blackboard.update("MockResearch", {"research_data": {"market_trends": [], "external_investigations": []}})
    await blackboard.update("MockEdge", {"google_edge_knowledge": {"sections": []}})
    await blackboard.update("MockResearchBlog", {"google_models_research_knowledge": {"articles": []}})

    # 2. Test KnowledgeAgent
    k_agent = KnowledgeAgent()
    
    # Mock knowledge file for test stability
    mock_kf = "data/ai_agents_knowledge.json"
    os.makedirs(os.path.dirname(mock_kf), exist_ok=True)
    mock_data = {
        "what-is-an-ai-agent": {"content": "AI agents are software systems..."},
        "key-features-of-an-ai-agent": {"content": "Reasoning Acting Collaborating Self-refining Observing Planning"},
        "challenges-with-using-ai-agents": {"content": "Empathy Ethical stakes Unpredictable"},
        "what-are-the-types-of-agents-in-ai": {"content": "Background Agents Interactive Partners"},
        "based-on-interaction": {"content": "Background Agents Interactive Partners"},
        "what-is-the-difference-between-ai-agents,-ai-assistants,-and-bots": {"content": "AI agents autonomously and proactively perform tasks..."},
        "key-differences": {"content": "Autonomy Learning Complexity"},
        "how-do-ai-agents-work": {"content": "- Persona: Consistent\n- Memory: Multi-tiered\n- Tools: External\n- Model: Brain"},
        "benefits-of-using-ai-agents": {"content": "Simultaneous execution Realistic simulations Collaboration"},
        "google-cloud-and-ai-agents": {"content": "- Gemini Enterprise Agent Platform\n- A2A Protocol"},
        "customer-agents": {"content": "Customer context"},
        "employee-agents": {"content": "Employee context"},
        "creative-agents": {"content": "Creative context"},
        "data-agents": {"content": "Data context"},
        "code-agents": {"content": "Code context"},
        "security-agents": {"content": "Security context"},
        "deploy-ai-agents-for-scale-and-efficiency-with-cloud-run": {"content": "Cloud Run deployment"}
    }
    with open(mock_kf, "w") as f:
        json.dump(mock_data, f)

    k_result = await k_agent.run([], blackboard)
    await blackboard.update(k_agent.name, k_result)

    assert "ai_agent_knowledge" in k_result
    assert "ai_agents_definitions" in k_result
    assert "challenges" in k_result["ai_agents_definitions"]
    assert "customer" in k_result["agent_use_cases"]

    # 3. Test IntelligenceAgent
    i_agent = IntelligenceAgent()
    i_result = await i_agent.run([], blackboard)
    await blackboard.update(i_agent.name, i_result)

    assert "intelligence_insights" in i_result
    assert any("AI Agent Knowledge Base Integrated" in insight for insight in i_result["intelligence_insights"])
    assert i_result["synchronization_level"] == "ADVANCED_COLABORATIVE"

    # 4. Test CreativityAgent
    c_agent = CreativityAgent()
    # Provide necessary concepts via mock if not already there
    await blackboard.update("MockKnowledge", {
        "agent_taxonomy": {
            "interactive_partners": "Assisting with tasks like customer service via direct conversation.",
            "background_processes": "Automating routine tasks and optimizing processes behind the scenes."
        }
    })
    c_result = await c_agent.run([], blackboard)
    assert any("Background Agents" in concept for concept in c_result["creative_concepts"])

if __name__ == "__main__":
    pytest.main([__file__])
