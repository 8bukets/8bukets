import asyncio
import logging
from typing import List, Dict, Set
from agents.base_agent import BaseAgent, Blackboard

logger = logging.getLogger("AgentOrchestrator")

class AgentOrchestrator:
    def __init__(self, agents: List[BaseAgent]):
        self.agents = agents
        self.blackboard = Blackboard()

    def _resolve_execution_plan(self) -> List[List[BaseAgent]]:
        """Calculates tiers based on dependencies."""
        executed_provides: Set[str] = set()
        remaining_agents = list(self.agents)
        tiers = []

        while remaining_agents:
            current_tier = []
            for agent in remaining_agents[:]:
                # If all dependencies are met by previously executed agents' provides
                if all(dep in executed_provides for dep in agent.dependencies):
                    current_tier.append(agent)
                    remaining_agents.remove(agent)

            if not current_tier:
                # Circular dependency or missing provider
                unmet = [(a.name, [d for d in a.dependencies if d not in executed_provides]) for a in remaining_agents]
                raise RuntimeError(f"Unresolvable dependencies for agents: {unmet}")

            tiers.append(current_tier)
            for agent in current_tier:
                executed_provides.update(agent.provides)

        return tiers

    async def execute_cycle(self, data: list):
        logger.info("Starting Autonomous Execution Cycle...")
        tiers = self._resolve_execution_plan()

        for i, tier in enumerate(tiers):
            logger.info(f"Executing Tier {i+1}: {[a.name for a in tier]}")
            tasks = [self._run_agent(agent, data) for agent in tier]
            await asyncio.gather(*tasks)

        logger.info("Execution Cycle Complete.")
        return self.blackboard.get_all()

    async def _run_agent(self, agent: BaseAgent, data: list):
        try:
            result = await agent.run(data, self.blackboard)
            if result:
                await self.blackboard.update(agent.name, result)
        except Exception as e:
            logger.error(f"Error in agent {agent.name}: {e}", exc_info=True)

    async def run_peer_review(self):
        logger.info("Starting Peer Review Phase...")
        review_tasks = [agent.review(self.blackboard) for agent in self.agents]
        reviews = await asyncio.gather(*review_tasks)

        peer_review_log = []
        for agent, review_findings in zip(self.agents, reviews):
            if review_findings:
                logger.info(f"Review from {agent.name}: {review_findings}")
                peer_review_log.extend([f"[{agent.name}] {r}" for r in review_findings])

        await self.blackboard.update("Orchestrator", {"peer_review_log": peer_review_log})
