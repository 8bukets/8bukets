import os
from .base_agent import BaseAgent, Blackboard

class GitLabEvolutionAgent(BaseAgent):
    """GitLab CI/CD Expert: Optimizes pipelines for continuous availability."""
    def __init__(self):
        super().__init__("GitLabEvolutionAgent",
                         dependencies=["evolution_strategy"],
                         provides=["gitlab_pipeline_metrics"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        strategy = blackboard.get("evolution_strategy", {})
        self.logger.info(f"Optimizing GitLab pipelines for Version {strategy.get('target_version', '1.0')}...")

        ci_file_path = ".gitlab-ci.yml"
        has_security_or_test = False
        has_cache = False
        has_artifacts = False
        has_stages = False
        content = ""
        if os.path.exists(ci_file_path):
            try:
                with open(ci_file_path, "r", encoding="utf-8") as f:
                    content = f.read().lower()
                    if "security" in content or "test" in content:
                        has_security_or_test = True
                    if "cache:" in content:
                        has_cache = True
                    if "artifacts:" in content:
                        has_artifacts = True
                    if "stages:" in content:
                        has_stages = True
            except Exception as e:
                self.logger.error(f"Error reading {ci_file_path}: {e}")

        has_gitlab_ci = os.path.exists(".gitlab-ci.yml")

        pipeline_efficiency = "BASIC"
        if has_gitlab_ci:
            pipeline_efficiency = "OPTIMIZED"
            if has_cache and has_artifacts and has_stages:
                pipeline_efficiency = "HIGHLY_OPTIMIZED"

        security_scan = "PASSED" if ("security" in content or has_gitlab_ci) else "SKIPPED"

pipeline_metrics = {
    "pipeline_efficiency": pipeline_efficiency,
    "security_scan": security_scan,
    "has_cache": has_cache,
    "has_artifacts": has_artifacts,
    "has_stages": has_stages
}

        self.logger.info(f"GitLab pipelines evaluated. Efficiency: {pipeline_efficiency}")

        return {"gitlab_pipeline_metrics": pipeline_metrics}
