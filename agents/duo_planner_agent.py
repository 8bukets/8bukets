import os
import json
import logging
from typing import Dict, Any, List, Optional
from .base_agent import BaseAgent, Blackboard

class DuoPlannerAgent(BaseAgent):
    """
    Duo Planner: GitLab Product Manager AI Agent

    This agent acts as a Product Manager embedded in GitLab, helping with
    Agile planning, prioritization, delivery tracking, and stakeholder communication.
    It reads instructions from agents/duo_planner_agent.md.
    """
    def __init__(self):
        super().__init__("DuoPlannerAgent",
                         dependencies=["gitlab_api"],
                         provides=["product_management_insights"])
        self.prompt_path = os.path.join(os.getcwd(), 'agents', 'duo_planner_agent.md')
        self.logger = logging.getLogger(self.name)

    def load_prompt(self) -> str:
        """Loads the system prompt defining the agent's behavior."""
        if os.path.exists(self.prompt_path):
            with open(self.prompt_path, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            self.logger.warning(f"Prompt file not found at {self.prompt_path}. Operating with default configuration.")
            return ""

    async def run(self, data: Any, blackboard: Blackboard) -> Dict[str, Any]:
        """
        Executes the product management workflow.

        Args:
            data: Incoming data, typically queries or context about GitLab work items.
            blackboard: Shared communication medium for agents.

        Returns:
            A dictionary containing the generated insights and recommended actions.
        """
        self.logger.info("🚀 [DuoPlannerAgent] Initiating Agile planning and delivery tracking...")

        system_prompt = self.load_prompt()

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(data)}
        ]

        response = await self.execute_llm_call(messages)

        try:
             results = json.loads(response)
        except json.JSONDecodeError:
             results = {"analysis": response}

        results["status"] = "success"

        self.logger.info("✅ [DuoPlannerAgent] Workflow complete.")
        return results
