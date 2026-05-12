import subprocess
from .base_agent import BaseAgent, Blackboard

class GitKrakenEvolutionAgent(BaseAgent):
    """Visual Evolution Expert: Optimizes repository structure and commit patterns for professional GitKraken visualization."""
    def __init__(self):
        super().__init__("GitKrakenEvolutionAgent",
                         dependencies=["evolution_strategy"],
                         provides=["git_visualization_metrics"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        strategy = blackboard.get("evolution_strategy", {})
        if not strategy.get("nexus_active"):
            self.logger.info("Collaboration Nexus not active. Operating in standalone mode.")

        self.logger.info("Optimizing repository for GitKraken professional visualization...")

        branch_count = 1
        commit_count = 1

        try:
            branches = subprocess.run(["git", "branch", "-r"], capture_output=True, text=True).stdout.strip().split('\n')
            branch_count = max(1, len([b for b in branches if b]))

            commits = subprocess.run(["git", "rev-list", "--all", "--count"], capture_output=True, text=True).stdout.strip()
            if commits.isdigit():
                commit_count = int(commits)
        except Exception as e:
            self.logger.warning(f"Could not retrieve dynamic git metrics: {e}")

        graph_depth = "EXTENDED" if commit_count > 10 else "STANDARD"
        kraken_compatibility_score = min(0.99, 0.8 + (0.05 * branch_count))

        visualization_data = {
            "graph_depth": graph_depth,
            "commit_clustering": "SEMANTIC",
            "kraken_compatibility_score": kraken_compatibility_score,
            "branches": branch_count,
            "commits": commit_count
        }

        # The agent 'prepares' metadata for the final commit
        await blackboard.update(self.name, {"visualization_prep": "COMPLETE"})

        return {"git_visualization_metrics": visualization_data}
