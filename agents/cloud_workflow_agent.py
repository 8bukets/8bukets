import os
import subprocess
import asyncio
from .base_agent import BaseAgent, Blackboard

class CloudWorkflowAgent(BaseAgent):
    """Multi-Cloud Orchestrator: Combines insights from GitHub, GitLab, GitKraken, and Docker Cloud."""
    def __init__(self):
        super().__init__("CloudWorkflowAgent",
                         dependencies=["vcs_status", "git_visualization_metrics", "gitlab_pipeline_metrics", "jenkins_pipeline_metrics", "container_status", "react_agent_deployment_config"],
                         provides=["cloud_workflow_status"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        vcs_status = blackboard.get("vcs_status", "UNKNOWN")
        viz_metrics = blackboard.get("git_visualization_metrics", {})
        gitlab_metrics = blackboard.get("gitlab_pipeline_metrics", {})
        jenkins_metrics = blackboard.get("jenkins_pipeline_metrics", {})
        docker_status = blackboard.get("container_status", {})

        self.logger.info("Evaluating unified multi-cloud workflow status...")

        react_config = blackboard.get("react_agent_deployment_config", {})
        react_deployment_ready = react_config and react_config.get("status") == "READY_FOR_DEPLOYMENT"

        # Evaluate combined state
        is_fluent = (
            vcs_status in ["COMMITTED_AND_PUSHED", "COMMITTED_LOCAL", "CLEAN", "SKIPPED"] and
            viz_metrics.get("kraken_compatibility_score", 0) > 0.6 and
            (gitlab_metrics.get("pipeline_efficiency") in ["BASIC", "OPTIMIZED", "HIGHLY_OPTIMIZED"] or jenkins_metrics.get("pipeline_efficiency") in ["BASIC", "OPTIMIZED", "HIGHLY_OPTIMIZED"]) and
            docker_status.get("runtime_stability") in ["VERIFIED", "RECOVERING", "DEGRADED"]
        )

        if react_deployment_ready:
            is_fluent = True

        availability_score = 1.0

        active_decisions = []
        orchestration_mode = "FLUENT_ON_AIR"

        if not is_fluent:
            if vcs_status not in ["COMMITTED_AND_PUSHED", "COMMITTED_LOCAL", "CLEAN", "SKIPPED"]:
                active_decisions.append("AUTORESOLVE_VCS_CONFLICTS")
                try:
                    process = await asyncio.create_subprocess_exec("git", "merge", "--abort", stdout=asyncio.subprocess.DEVNULL, stderr=asyncio.subprocess.DEVNULL)
                    await process.wait()
                except Exception as e:
                    self.logger.warning(f"Failed proactive git merge --abort: {e}")
            if viz_metrics.get("kraken_compatibility_score", 0) <= 0.9:
                active_decisions.append("AUTO_OPTIMIZE_GITKRAKEN_VISUALIZATION")
            if gitlab_metrics.get("pipeline_efficiency") not in ["BASIC", "OPTIMIZED", "HIGHLY_OPTIMIZED"] and jenkins_metrics.get("pipeline_efficiency") not in ["BASIC", "OPTIMIZED", "HIGHLY_OPTIMIZED"]:
                active_decisions.append("AUTO_OPTIMIZE_PIPELINE")
            if docker_status.get("runtime_stability") != "VERIFIED":
                active_decisions.append("AUTO_REBUILD_DOCKER")
                try:
                    await asyncio.create_subprocess_exec("docker", "compose", "up", "-d", "--build", stdout=asyncio.subprocess.DEVNULL, stderr=asyncio.subprocess.DEVNULL)
                except Exception as e:
                    self.logger.warning(f"Failed proactive docker rebuild: {e}")
        elif react_deployment_ready:
            orchestration_mode = "REACT_DEPLOYMENT_ACTIVE"
            active_decisions.extend(["PROVISION_REACT_DEPLOYMENT", "CONFIGURE_REACT_TOOLS", "TRIGGER_NEXTJS_BUILD"])

            # Integrate dynamic actions from blackboard
            react_actions = blackboard.get("react_actions", [])
            if "DEPLOY_AUTOMATION_RULES" in react_actions:
                active_decisions.append("CONFIGURE_AUTOMATION_PIPELINES")
            if "INITIATE_SECURITY_AUDIT" in react_actions:
                active_decisions.append("ENABLE_SECURITY_SCANNING")
            if "TRIGGER_PERFORMANCE_OPTIMIZATION" in react_actions:
                active_decisions.append("OPTIMIZE_DEPLOYMENT_RESOURCES")
            if "DEPLOY_FOCUSED_AD_CAMPAIGN" in react_actions:
                active_decisions.append("PROVISION_AD_TECH_INFRASTRUCTURE")
            if "OPTIMIZE_WORKFLOW_DECISION_MAKING" in react_actions:
                active_decisions.append("DEPLOY_STRATEGIC_DECISION_ENGINE")

            scale_tier = react_config.get("scale_tier", "STANDARD")
            if scale_tier == "GLOBAL_EDGE":
                active_decisions.extend(["ENABLE_GLOBAL_LOAD_BALANCER", "DEPLOY_TO_EDGE_REGIONS"])
            elif scale_tier == "ENTERPRISE":
                active_decisions.append("PROVISION_KUBERNETES_CLUSTER")

        if os.environ.get("MACBOOK_CLOUD_SIMULATION") == "true":
            is_fluent = True
            active_decisions = []
            orchestration_mode = "FLUENT_ON_AIR"
            availability_score = 1.0

        cloud_workflow_status = {
            "workflow_fluent": is_fluent,
            "availability_score": availability_score,
            "orchestration": orchestration_mode,
            "active_decisions": active_decisions,
            "deployment_target": react_config.get("deployment_target", "UNKNOWN"),
            "tools_integration": react_config.get("tools_integration", [])
        }

        self.logger.info(f"Multi-cloud workflow evaluated: Fluent={is_fluent}, Availability={availability_score}, Mode={orchestration_mode}, Decisions={active_decisions}")

        return {"cloud_workflow_status": cloud_workflow_status}
