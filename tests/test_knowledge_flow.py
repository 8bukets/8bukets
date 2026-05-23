import asyncio
import json
import os
import sys
import pytest

# Ensure agents can be imported
sys.path.append(os.getcwd())

from agents.knowledge_agent import KnowledgeAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.base_agent import Blackboard

@pytest.mark.asyncio
async def test_knowledge_flow():
    print("Testing Knowledge Flow...")

    # Setup
    blackboard = Blackboard()
    knowledge_agent = KnowledgeAgent()
    intelligence_agent = IntelligenceAgent()

    # 1. Run KnowledgeAgent
    knowledge_results = await knowledge_agent.run([], blackboard)
    await blackboard.update(knowledge_agent.name, knowledge_results)

    print("\nKnowledge Agent Definitions:")
    for key, value in knowledge_results['ai_agents_definitions'].items():
        if isinstance(value, str):
            print(f"- {key}: {value[:50]}...")
        else:
            print(f"- {key}: {type(value)}")

    print("\nExtracted Tools:")
    print(knowledge_results['google_cloud_tools_list'])

    # Assertions for KnowledgeAgent
    assert "ai_agent" in knowledge_results['ai_agents_definitions']
    assert len(knowledge_results['google_cloud_tools_list']) > 0

    # 2. Run IntelligenceAgent
    intelligence_results = await intelligence_agent.run([], blackboard)
    await blackboard.update(intelligence_agent.name, intelligence_results)

    print("\nIntelligence Insights:")
    for insight in intelligence_results['intelligence_insights']:
        print(f"- {insight}")

    # Assertions for IntelligenceAgent
    insights = intelligence_results['intelligence_insights']
    assert any("Ecosystem architecture aligns with ReAct framework" in i for i in insights)
    assert any("System utilizes multi-tiered memory architecture" in i for i in insights)
    assert any("Google Cloud AI Agent definitions" in i.replace(',', '') for i in insights)

    print("\nKnowledge flow test passed successfully!")

if __name__ == "__main__":
    asyncio.run(test_knowledge_flow())
