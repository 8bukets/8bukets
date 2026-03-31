import os
import subprocess
from .base_agent import BaseAgent, Blackboard

class GitHubEvolutionAgent(BaseAgent):
    """Autonomously stages, commits, and pushes code changes based on system evolution."""
    def __init__(self):
        super().__init__("GitHubEvolutionAgent",
                         dependencies=["system_evolution"],
                         provides=["vcs_status"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        evolution = blackboard.get("system_evolution", {})
        if evolution.get("status") != "EVOLVED":
            self.logger.info("No system evolution detected. Skipping Git operations.")
            return {"vcs_status": "SKIPPED"}

        self.logger.info("System evolved. Performing autonomous Git operations...")

        try:
            # 1. Stage changes (Sanitized config, memory, and results)
            subprocess.run(["git", "add", "config/evolution_params.json", "config/owner_info.json", "data/", "results/", "links.json", "links.csv", "unique_links.txt"], check=True)

            # 2. Commit changes
            version = evolution.get("parameter_shifts", {}).get("current_version", "1.0")
            commit_msg = f"Autonomous System Evolution: Version {version}\n\nAutomated commit by GitHubEvolutionAgent."
            subprocess.run(["git", "commit", "-m", commit_msg], check=True)

            # 3. Push changes (if GITHUB_TOKEN is available)
            token = os.environ.get("GITHUB_TOKEN")
            if token:
                self.logger.info("GITHUB_TOKEN detected. Attempting to push...")
                # Note: This is a simplified push logic. In a real scenario, you'd handle remote URL properly.
                subprocess.run(["git", "push"], check=True)
                vcs_status = "COMMITTED_AND_PUSHED"
            else:
                self.logger.warning("GITHUB_TOKEN not found. Changes committed but not pushed.")
                vcs_status = "COMMITTED_LOCAL"

            return {"vcs_status": vcs_status}

        except subprocess.CalledProcessError as e:
            self.logger.error(f"Git operation failed: {e}")
            return {"vcs_status": "FAILED"}
        except Exception as e:
            self.logger.error(f"An unexpected error occurred during Git operations: {e}")
            return {"vcs_status": "ERROR"}
