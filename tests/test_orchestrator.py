import pytest
import asyncio
from markposition.agents.base_agent import Blackboard, BaseAgent
from markposition.agents.orchestrator import AgentOrchestrator

class MockAgent(BaseAgent):
    def __init__(self, name, deps=None, provides=None, result=None):
        super().__init__(name, dependencies=deps, provides=provides)
        self.mock_result = result or {}

    async def run(self, data, blackboard):
        return self.mock_result

@pytest.mark.asyncio(loop_scope="function")
async def test_blackboard_update():
    bb = Blackboard()
    await bb.update("AgentA", {"key": "value"})
    assert bb.get("key") == "value"
    assert len(bb.get_history()) == 1

@pytest.mark.asyncio(loop_scope="function")
async def test_orchestrator_execution():
    a1 = MockAgent("A1", provides=["data1"], result={"data1": 1})
    a2 = MockAgent("A2", deps=["data1"], provides=["data2"], result={"data2": 2})

    orchestrator = AgentOrchestrator([a1, a2])
    results = await orchestrator.execute_cycle([])

    assert results["data1"] == 1
    assert results["data2"] == 2

@pytest.mark.asyncio(loop_scope="function")
async def test_orchestrator_circular_dependency():
    a1 = MockAgent("A1", deps=["data2"], provides=["data1"])
    a2 = MockAgent("A2", deps=["data1"], provides=["data2"])

    orchestrator = AgentOrchestrator([a1, a2])
    with pytest.raises(RuntimeError, match="Unresolvable dependencies"):
        await orchestrator.execute_cycle([])
