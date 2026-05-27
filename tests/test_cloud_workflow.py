import pytest
import asyncio
import os
from agents.base_agent import Blackboard
from agents.cloud_workflow_agent import CloudWorkflowAgent

@pytest.mark.asyncio
async def test_cloud_workflow_agent():
    bb = Blackboard()

    await bb.update("System", {"vcs_status": "CLEAN"})
    await bb.update("System", {"git_visualization_metrics": {"kraken_compatibility_score": 0.9}})
    await bb.update("System", {"gitlab_pipeline_metrics": {"pipeline_efficiency": "OPTIMIZED"}})
    await bb.update("System", {"container_status": {"runtime_stability": "VERIFIED"}})

    agent = CloudWorkflowAgent()
    result = await agent.run([], bb)

    status = result.get("cloud_workflow_status", {})
    assert status["workflow_fluent"] is True
    assert status["availability_score"] == 1.0
    assert not status["active_decisions"]

@pytest.mark.asyncio
async def test_cloud_workflow_agent_degraded():
    bb = Blackboard()

    await bb.update("System", {"vcs_status": "UNKNOWN"})
    await bb.update("System", {"git_visualization_metrics": {"kraken_compatibility_score": 0.5}})
    await bb.update("System", {"gitlab_pipeline_metrics": {"pipeline_efficiency": "DEGRADED"}})
    await bb.update("System", {"container_status": {"runtime_stability": "DEGRADED"}})

    agent = CloudWorkflowAgent()
    result = await agent.run([], bb)

    status = result.get("cloud_workflow_status", {})
    assert status["workflow_fluent"] is True
    assert status["availability_score"] < 1.0
    assert len(status["active_decisions"]) == 4
    assert "AUTORESOLVE_VCS_CONFLICTS" in status["active_decisions"]
    assert "AUTO_OPTIMIZE_GITKRAKEN_VISUALIZATION" in status["active_decisions"]
    assert "AUTO_OPTIMIZE_PIPELINE" in status["active_decisions"]
    assert "AUTO_REBUILD_DOCKER" in status["active_decisions"]
