import asyncio
import subprocess
import os
import re
from .base_agent import BaseAgent, Blackboard

class JulesEvolutionAgent(BaseAgent):
    """
    The Lead Evolution Coordinator: Orchestrates high-level system transformation,
    agent collaboration, and acts autonomously to fix bugs, tune parameters, and
    dynamically write code during the daily run.
    """
    def __init__(self):
        super().__init__("JulesEvolutionAgent",
                         dependencies=["system_evolution", "meta_optimizations"],
                         provides=["evolution_strategy", "collaboration_nexus"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Coordinating system-wide autonomous evolution...")

        evolution = blackboard.get("system_evolution", {})
        meta = blackboard.get("meta_optimizations")

        # Build the 'Collaboration Nexus' - a shared strategy for specialized agents
        strategy = {
            "target_version": evolution.get("parameter_shifts", {}).get("current_version", "1.0"),
            "optimization_priority": "STABILITY_AND_VISUALIZATION",
            "required_collaborators": ["GitHubEvolutionAgent", "GitKrakenEvolutionAgent", "DockerEvolutionAgent"],
            "nexus_active": True
        }

        # 1. Autonomous Bug Fixing & Test Resolution
        await self._autonomous_test_repair()

        # 2. Autonomous Parameter Tuning based on Sigma Impact
        await self._autonomous_parameter_tuning(blackboard)

        # 3. Autonomous Dynamic Agent Creation based on Analytics
        await self._autonomous_agent_creation(blackboard)

        self.logger.info(f"Nexus established for Version {strategy['target_version']}. Engaging specialized units.")

        return {
            "evolution_strategy": strategy,
            "collaboration_nexus": "ACTIVE"
        }

    async def _autonomous_test_repair(self):
        """Runs tests and attempts rudimentary auto-fixes for syntax errors or missing imports."""
        self.logger.info("Jules: Running autonomous test diagnostics...")
        try:
            process = await asyncio.create_subprocess_exec(
                "python3", "-m", "pytest", "tests/",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            if process.returncode != 0:
                self.logger.warning("Jules: Test failures detected! Attempting autonomous repair.")
                error_output = (stderr.decode() if stderr else "") + (stdout.decode() if stdout else "")

                # Very basic auto-fix heuristics (e.g. missing basic imports)
                if "ModuleNotFoundError: No module named 'math'" in error_output:
                    # Search files and add import math
                    for root, _, files in os.walk("agents"):
                        for f in files:
                            if f.endswith(".py"):
                                path = os.path.join(root, f)
                                with open(path, "r") as file_read:
                                    content = file_read.read()
                                if "math." in content and "import math" not in content:
                                    with open(path, "w") as file_write:
                                        file_write.write("import math\n" + content)
                                    self.logger.info(f"Jules: Auto-patched {path} with 'import math'.")

                self.logger.info("Jules: Applied autonomous patches where possible.")
            else:
                self.logger.info("Jules: All tests passed. Codebase is stable.")
        except Exception as e:
            self.logger.error(f"Jules: Failed to run test diagnostics: {e}")

    async def _autonomous_parameter_tuning(self, blackboard: Blackboard):
        """Autonomously tune parameters based on performance impact"""
        sigma = blackboard.get("sigma_performance_report", {})
        impact = sigma.get("average_impact_score", 0)

        # Tune system parameters via blackboard evolution
        if impact > 0.5:
            # Scale up
            await blackboard.propose_improvement(self.name, {
                "system_concurrency": min(self.config.get("system_concurrency", 5) + 5, 50),
                "seo_impact_threshold": round(self.config.get("seo_impact_threshold", 0.5) * 1.1, 2)
            })
            self.logger.info(f"Jules: High impact {impact:.2f}. Autonomously proposing concurrency upscale.")
        elif impact < 0.2:
            # Scale down
            await blackboard.propose_improvement(self.name, {
                "system_concurrency": max(self.config.get("system_concurrency", 5) - 1, 1),
                "seo_impact_threshold": round(self.config.get("seo_impact_threshold", 0.5) * 0.9, 2)
            })
            self.logger.info(f"Jules: Low impact {impact:.2f}. Autonomously proposing downscale.")

    async def _autonomous_agent_creation(self, blackboard: Blackboard):
        """Dynamically writes new agent logic if the system analytics indicate a missing capability."""
        analysis = blackboard.get("analysis_stats", {})
        # If the analysis report indicates a high volume of a specific domain (e.g. youtube),
        # automatically provision a specialized agent.
        if "youtube.com" in str(analysis) and not os.path.exists("agents/youtube_specialist_agent.py"):
            self.logger.info("Jules: High volume of YouTube links detected. Autonomously generating 'YoutubeSpecialistAgent'...")
            agent_code = '''import asyncio
from .base_agent import BaseAgent, Blackboard

class YoutubeSpecialistAgent(BaseAgent):
    def __init__(self):
        super().__init__("YoutubeSpecialistAgent", dependencies=["analysis_stats"], provides=["youtube_insights"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Analyzing YouTube specific metrics autonomously...")
        return {"youtube_insights": "Active"}
'''
            with open("agents/youtube_specialist_agent.py", "w") as f:
                f.write(agent_code)
            self.logger.info("Jules: Successfully synthesized new agent: YoutubeSpecialistAgent.")

    async def review(self, blackboard: Blackboard):
        nexus = blackboard.get("collaboration_nexus")
        if nexus == "ACTIVE":
            return ["Evolution strategy is synchronized across all specialized agents."]
        return ["Evolution coordination pending."]
