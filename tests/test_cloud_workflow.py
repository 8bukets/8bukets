import pytest
import asyncio
import os
from agents.cloud_workflow_agent import CloudWorkflowAgent
class Blackboard(dict):
    pass

@pytest.mark.asyncio
async def test_cloud_workflow_agent():
    bb = Blackboard()

    bb["vcs_status"] = {"status": "CLEAN"}
    bb["git_visualization_metrics"] = {"kraken_compatibility_score": 0.9}
    bb["gitlab_pipeline_metrics"] = {"pipeline_efficiency": "OPTIMIZED"}
    bb["container_status"] = {"runtime_stability": "VERIFIED"}

    agent = CloudWorkflowAgent()
    result = await agent.run([], bb)

    status = result.get("cloud_workflow_status", {})
    assert status["workflow_fluent"] is True
    assert status["availability_score"] == 1.0
    assert not status["active_decisions"]

@pytest.mark.asyncio
async def test_cloud_workflow_agent_degraded():
    bb = Blackboard()

    bb["vcs_status"] = {"status": "UNKNOWN"}
    bb["git_visualization_metrics"] = {"kraken_compatibility_score": 0.5}
    bb["gitlab_pipeline_metrics"] = {"pipeline_efficiency": "DEGRADED"}
    bb["container_status"] = {"runtime_stability": "DEGRADED"}

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
