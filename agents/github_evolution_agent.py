import os
import subprocess
from .base_agent import BaseAgent, Blackboard

class GitHubEvolutionAgent(BaseAgent):
    """Autonomously stages, commits, and pushes code changes based on system evolution."""
    def __init__(self):
        super().__init__("GitHubEvolutionAgent",
                         dependencies=["system_evolution", "evolution_strategy", "git_visualization_metrics", "container_status", "gitlab_pipeline_metrics"],
                         provides=["vcs_status"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        evolution = blackboard.get("system_evolution", {})
        strategy = blackboard.get("evolution_strategy", {})
        viz_metrics = blackboard.get("git_visualization_metrics", {})
        docker_status = blackboard.get("container_status", {})
        gitlab_metrics = blackboard.get("gitlab_pipeline_metrics", {})
        if evolution.get("status") != "EVOLVED":
            self.logger.info("No system evolution detected. Skipping Git operations.")
            return {"vcs_status": "SKIPPED"}

        self.logger.info("System evolved. Performing autonomous Git operations...")

        workflow_count = 0
        workflows_dir = ".github/workflows"
        if os.path.exists(workflows_dir) and os.path.isdir(workflows_dir):
            try:
                workflow_count = len([f for f in os.listdir(workflows_dir) if f.endswith('.yml') or f.endswith('.yaml')])
            except Exception as e:
                self.logger.warning(f"Could not count GitHub workflows: {e}")

        try:
            # 1. Stage changes (Sanitized config, memory, and results)
            subprocess.run(["git", "add", "config/evolution_params.json", "config/owner_info.json", "data/", "results/", "links.json", "links.csv", "unique_links.txt"], check=True)

            # Check for changes before committing
            status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout.strip()
            if not status:
                self.logger.info("No changes to commit. Skipping Git commit/push.")
                return {"vcs_status": "CLEAN", "workflow_count": workflow_count}

            # 2. Commit changes with collaborative insights
            version = evolution.get("parameter_shifts", {}).get("current_version", "1.0")
            commit_msg = (
                f"Autonomous System Evolution: Version {version}\n\n"
                f"Collaborative Evolution Metrics:\n"
                f"- GitKraken Visualization: {viz_metrics.get('kraken_compatibility_score', 0)*100}%\n"
                f"- Docker Stability: {docker_status.get('runtime_stability', 'N/A')}\n"
                f"- GitLab Pipeline: {gitlab_metrics.get('pipeline_efficiency', 'N/A')}\n"
                f"- Evolution Strategy: {strategy.get('optimization_priority', 'STANDARD')}\n\n"
                f"Automated commit by collaborative agent unit (Jules + GitHub + GitLab + GitKraken + Docker Cloud)."
            )
            subprocess.run(["git", "commit", "-m", commit_msg], check=True)

            # 3. Push changes (if GITHUB_TOKEN is available)
            token = os.environ.get("GITHUB_TOKEN")
            if token:
                self.logger.info("GITHUB_TOKEN detected. Pulling with rebase and attempting to push...")
                pull_result = subprocess.run(["git", "pull", "--rebase", "origin", "main"], check=False)
                if pull_result.returncode != 0:
                    self.logger.warning("Git pull rebase failed (likely merge conflict). Aborting rebase.")
                    subprocess.run(["git", "rebase", "--abort"], check=False)
                    vcs_status = "COMMITTED_LOCAL" # Prevent push from failing
                else:
                    # Note: This is a simplified push logic. In a real scenario, you'd handle remote URL properly.
                    try:
                        subprocess.run(["git", "push"], check=True)
                        vcs_status = "COMMITTED_AND_PUSHED"
                    except subprocess.CalledProcessError as e:
                        self.logger.error(f"Git push failed: {e}")
                        vcs_status = "COMMITTED_LOCAL"
            else:
                self.logger.warning("GITHUB_TOKEN not found. Changes committed but not pushed.")
                vcs_status = "COMMITTED_LOCAL"

            # Dynamic repository state validation before attempting to push
            # Automatically pull latest changes to prevent push failures when multiple agents are working
            if token:
                try:
                    self.logger.info("Synchronizing with remote to avoid conflicts...")
                    subprocess.run(["git", "pull", "--rebase", "origin", "main"], check=True)
                except subprocess.CalledProcessError as pull_e:
                    self.logger.warning(f"Failed to synchronize with remote: {pull_e}")

            return {"vcs_status": vcs_status, "workflow_count": workflow_count}

        except subprocess.CalledProcessError as e:
            self.logger.error(f"Git operation failed: {e}")
            return {"vcs_status": "FAILED", "workflow_count": workflow_count}
        except Exception as e:
            self.logger.error(f"An unexpected error occurred during Git operations: {e}")
            return {"vcs_status": "ERROR", "workflow_count": workflow_count}
