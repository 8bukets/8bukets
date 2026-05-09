from .base_agent import BaseAgent, Blackboard

class CloudWorkflowAgent(BaseAgent):
    """Multi-Cloud Orchestrator: Combines insights from GitHub, GitLab, GitKraken, and Docker Cloud."""
    def __init__(self):
        super().__init__("CloudWorkflowAgent",
                         dependencies=["vcs_status", "git_visualization_metrics", "gitlab_pipeline_metrics", "container_status"],
                         provides=["cloud_workflow_status"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        vcs_status = blackboard.get("vcs_status", "UNKNOWN")
        viz_metrics = blackboard.get("git_visualization_metrics", {})
        gitlab_metrics = blackboard.get("gitlab_pipeline_metrics", {})
        docker_status = blackboard.get("container_status", {})

        self.logger.info("Evaluating unified multi-cloud workflow status...")

        # Evaluate combined state
        is_fluent = (
            vcs_status in ["COMMITTED_AND_PUSHED", "COMMITTED_LOCAL", "CLEAN"] and
            viz_metrics.get("kraken_compatibility_score", 0) > 0.8 and
            gitlab_metrics.get("pipeline_efficiency") == "OPTIMIZED" and
            docker_status.get("runtime_stability") == "VERIFIED"
        )

        availability_score = 0.99 if is_fluent else 0.85

        active_decisions = []
        if docker_status.get("runtime_stability") != "VERIFIED":
            active_decisions.append("REBUILD_DOCKER")
        if gitlab_metrics.get("pipeline_efficiency") != "OPTIMIZED":
            active_decisions.append("OPTIMIZE_PIPELINE")
        if vcs_status not in ["COMMITTED_AND_PUSHED", "COMMITTED_LOCAL", "CLEAN"]:
            active_decisions.append("FORCE_GIT_SYNC")

        orchestration_mode = "RECOVERY_MODE" if active_decisions else "SYNCHRONIZED"

        cloud_workflow_status = {
            "workflow_fluent": is_fluent,
            "availability_score": availability_score,
            "orchestration": orchestration_mode,
            "active_decisions": active_decisions
        }

        self.logger.info(f"Multi-cloud workflow evaluated: Fluent={is_fluent}, Orchestration={orchestration_mode}, Decisions={active_decisions}")

        return {"cloud_workflow_status": cloud_workflow_status}
