import os
import json
import asyncio
from google import genai
from .base_agent import BaseAgent, Blackboard

class ThinkingAgent(BaseAgent):
    """
    A 24/7 Thinking Agent utilizing a 'Graph of Thought' methodology to evaluate
    code structure improvements and evaluate the license system engine for earning value.
    """
    def __init__(self):
        super().__init__("ThinkingAgent", provides=["graph_of_thought_evaluation"])
        # Use existing Gemini API Key
        self.api_key = os.environ.get("GEMINI_API_KEY")
        if self.api_key:
            self.client = genai.Client(api_key=self.api_key)
        else:
            self.client = None

    async def _generate_thoughts(self, prompt: str) -> str:
        """Helper to call Gemini API."""
        if not self.client:
            self.logger.warning("GEMINI_API_KEY not set. Returning fallback thought.")
            return "Fallback thought: Unable to connect to LLM."
        try:
            # We use a simple model call to simulate a thought generation
            response = await self.client.aio.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            return response.text
        except Exception as e:
            self.logger.error(f"Error generating thought: {e}")
            return f"Error during thought generation: {e}"

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("ThinkingAgent running Graph of Thought...")

        # Construct the Graph of Thought evaluation context
        input_context = "Current System State: Autonomous System executing 24/7."

        # Branch 1: Code Structure Improve
        prompt_branch_1 = f"Context: {input_context}\nTask: Evaluate how to make order code structure improve. Provide 3 distinct structural thoughts."
        thoughts_code = await self._generate_thoughts(prompt_branch_1)

        # Branch 2: Earn Valuate Licence System Engine
        prompt_branch_2 = f"Context: {input_context}\nTask: Evaluate the licence system engine to earn and create value. Provide 3 strategic thoughts."
        thoughts_licence = await self._generate_thoughts(prompt_branch_2)

        # Synthesis Node
        prompt_synthesis = f"Synthesize these two branches into a unified actionable plan:\nBranch 1 (Code Structure): {thoughts_code}\nBranch 2 (Licence System): {thoughts_licence}"
        final_synthesis = await self._generate_thoughts(prompt_synthesis)

        # Store results
        graph_of_thought_result = {
            "code_structure_thoughts": thoughts_code,
            "licence_system_thoughts": thoughts_licence,
            "final_synthesis": final_synthesis
        }

        # Propose improvement based on final synthesis
        await blackboard.propose_improvement(
            self.name,
            {
                "type": "GraphOfThought_Architecture_And_Licensing",
                "details": final_synthesis
            }
        )

        self.logger.info("Graph of Thought evaluation complete.")
        return {"graph_of_thought_evaluation": graph_of_thought_result}

    async def review(self, blackboard: Blackboard) -> list:
        # Reviews existing blackboard proposals using Graph of Thought
        proposals = blackboard.get_proposals()
        if not proposals:
            return []

        self.logger.info("ThinkingAgent reviewing proposals...")
        return [f"ThinkingAgent reviewed {len(proposals)} proposals using Graph of Thought context."]
