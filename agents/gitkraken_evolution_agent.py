import asyncio
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

        self.logger.info("Evaluating repository structure for GitKraken professional visualization...")

        branch_count = 1
        try:
            process = await asyncio.create_subprocess_exec("git", "branch", "-a", stdout=asyncio.subprocess.PIPE)
            stdout, _ = await process.communicate()
            if process.returncode == 0:
                branches = [b for b in stdout.decode().split('\n') if b.strip()]
                branch_count = len(branches)
        except Exception as e:
            self.logger.error(f"Error checking git branches: {e}")

        # The more branches, the more complex the visual graph depth
        graph_depth = "EXTENDED" if branch_count > 3 else "STANDARD"
        kraken_score = min(0.99, 0.80 + (branch_count * 0.05))

        branch_count = 1
        commit_count = 1

        try:
            process1 = await asyncio.create_subprocess_exec("git", "branch", "-r", stdout=asyncio.subprocess.PIPE)
            stdout1, _ = await process1.communicate()
            branches_res = stdout1.decode().strip().split('\n')
            branch_count = max(1, len([b for b in branches_res if b]))

            process2 = await asyncio.create_subprocess_exec("git", "rev-list", "--all", "--count", stdout=asyncio.subprocess.PIPE)
            stdout2, _ = await process2.communicate()
            commits_res = stdout2.decode().strip()
            if commits_res.isdigit():
                commit_count = int(commits_res)
        except Exception as e:
            self.logger.warning(f"Could not retrieve dynamic git metrics: {e}")

        semantic_commits_detected = False
        try:
            process3 = await asyncio.create_subprocess_exec("git", "log", "--oneline", "-n", "20", stdout=asyncio.subprocess.PIPE)
            stdout3, _ = await process3.communicate()
            log_res = stdout3.decode().lower()
            if any(prefix in log_res for prefix in ["feat:", "fix:", "chore:", "docs:", "refactor:"]):
                semantic_commits_detected = True
        except Exception as e:
            self.logger.warning(f"Could not check for semantic commits: {e}")

        graph_depth = "EXTENDED" if commit_count > 10 else "STANDARD"

        base_score = 0.85 if semantic_commits_detected else 0.80
        kraken_compatibility_score = min(0.99, base_score + (0.05 * branch_count))

        visualization_data = {
            "graph_depth": graph_depth,
            "commit_clustering": "SEMANTIC" if semantic_commits_detected else "CHRONOLOGICAL",
            "kraken_compatibility_score": kraken_compatibility_score,
            "branches": branch_count,
            "commits": commit_count,
            "semantic_commits_detected": semantic_commits_detected
        }

        self.logger.info(f"GitKraken compatibility evaluated. Score: {visualization_data['kraken_compatibility_score']}")

        # The agent 'prepares' metadata for the final commit
        await blackboard.update(self.name, {"visualization_prep": "COMPLETE"})

        return {"git_visualization_metrics": visualization_data}
